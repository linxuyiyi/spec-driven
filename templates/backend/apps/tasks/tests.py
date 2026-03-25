import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task


@pytest.mark.django_db
class TaskModelTest:
    def test_create_task(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            priority=2
        )
        assert task.title == 'Test Task'
        assert task.status == 'pending'
        assert task.priority == 2
    
    def test_task_default_values(self):
        task = Task.objects.create(title='Simple Task')
        assert task.status == 'pending'
        assert task.priority == 1
        assert task.description == ''
    
    def test_task_str(self):
        task = Task.objects.create(title='My Task')
        assert str(task) == 'My Task'


@pytest.mark.django_db
class TaskAPITest(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='Test',
            priority=2
        )
        self.list_url = reverse('task-list')
        self.detail_url = reverse('task-detail', kwargs={'pk': self.task.pk})
    
    def test_list_tasks(self):
        response = self.client.get(self.list_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['title'] == 'Test Task'
    
    def test_create_task(self):
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'priority': 3
        }
        response = self.client.post(self.list_url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Task.objects.count() == 2
        assert Task.objects.get(pk=response.data['id']).title == 'New Task'
    
    def test_retrieve_task(self):
        response = self.client.get(self.detail_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Test Task'
    
    def test_update_task(self):
        data = {'title': 'Updated Task'}
        response = self.client.put(self.detail_url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.task.refresh_from_db()
        assert self.task.title == 'Updated Task'
    
    def test_partial_update_task(self):
        data = {'status': 'completed'}
        response = self.client.patch(self.detail_url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.task.refresh_from_db()
        assert self.task.status == 'completed'
    
    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Task.objects.count() == 0
    
    def test_filter_by_status(self):
        Task.objects.create(title='Completed Task', status='completed')
        response = self.client.get(self.list_url + '?status=pending')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
    
    def test_filter_by_priority(self):
        response = self.client.get(self.list_url + '?priority=2')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
    
    def test_search_tasks(self):
        response = self.client.get(self.list_url + '?search=Test')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
