"""Tests for Bulletin model, serializer, and viewset."""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from app.models import Bulletin

User = get_user_model()


@pytest.fixture
def api_client():
    """Create API client."""
    return APIClient()


@pytest.fixture
def user():
    """Create test user."""
    return User.objects.create_user(
        username='testuser',
        password='testpass123'
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """Create authenticated API client."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def bulletin_data():
    """Sample bulletin data."""
    return {
        'title': '测试公告',
        'content': '这是测试公告的内容',
        'status': 'DRAFT',
        'priority': 'NORMAL'
    }


@pytest.fixture
def sample_bulletin(user, bulletin_data):
    """Create sample bulletin."""
    return Bulletin.objects.create(
        title=bulletin_data['title'],
        content=bulletin_data['content'],
        status=bulletin_data['status'],
        priority=bulletin_data['priority'],
        author=user
    )


# ==================== Model Tests ====================

class TestBulletinModel:
    """Test Bulletin model."""
    
    def test_bulletin_creation(self, user, bulletin_data):
        """Test creating bulletin successfully."""
        bulletin = Bulletin.objects.create(
            title=bulletin_data['title'],
            content=bulletin_data['content'],
            status=bulletin_data['status'],
            priority=bulletin_data['priority'],
            author=user
        )
        
        assert bulletin.id is not None
        assert bulletin.title == bulletin_data['title']
        assert bulletin.content == bulletin_data['content']
        assert bulletin.status == 'DRAFT'
        assert bulletin.priority == 'NORMAL'
        assert bulletin.author == user
    
    def test_bulletin_str(self, sample_bulletin):
        """Test bulletin string representation."""
        assert str(sample_bulletin) == sample_bulletin.title
    
    def test_default_status(self, user):
        """Test default status is DRAFT."""
        bulletin = Bulletin.objects.create(
            title='Test',
            content='Content',
            author=user
        )
        assert bulletin.status == 'DRAFT'
    
    def test_default_priority(self, user):
        """Test default priority is NORMAL."""
        bulletin = Bulletin.objects.create(
            title='Test',
            content='Content',
            author=user
        )
        assert bulletin.priority == 'NORMAL'
    
    def test_published_at_auto_set(self, user, authenticated_client):
        """Test published_at is set when publishing."""
        bulletin = Bulletin.objects.create(
            title='Test',
            content='Content',
            status='DRAFT',
            author=user
        )
        
        # Publish the bulletin
        response = authenticated_client.post(
            f'/api/bulletins/{bulletin.id}/publish/'
        )
        
        assert response.status_code == status.HTTP_200_OK
        bulletin.refresh_from_db()
        assert bulletin.published_at is not None


# ==================== Serializer Tests ====================

class TestBulletinSerializer:
    """Test BulletinSerializer."""
    
    def test_serializer_valid(self, sample_bulletin):
        """Test serialization with valid data."""
        from app.serializers import BulletinSerializer
        
        serializer = BulletinSerializer(instance=sample_bulletin)
        data = serializer.data
        
        assert 'id' in data
        assert 'title' in data
        assert 'content' in data
        assert 'status' in data
        assert 'priority' in data
        assert data['title'] == sample_bulletin.title
    
    def test_serializer_required_fields(self):
        """Test required fields validation."""
        from app.serializers import BulletinSerializer
        
        serializer = BulletinSerializer(data={})
        assert not serializer.is_valid()
        assert 'title' in serializer.errors
        assert 'content' in serializer.errors
    
    def test_serializer_status_choices(self, user):
        """Test status choices validation."""
        from app.serializers import BulletinSerializer
        
        data = {
            'title': 'Test',
            'content': 'Content',
            'status': 'INVALID_STATUS',
            'author': user
        }
        serializer = BulletinSerializer(data=data)
        assert not serializer.is_valid()
        assert 'status' in serializer.errors


# ==================== ViewSet Tests ====================

class TestBulletinViewSet:
    """Test BulletinViewSet."""
    
    def test_list_bulletins(self, authenticated_client, sample_bulletin):
        """Test listing bulletins."""
        response = authenticated_client.get('/api/bulletins/')
        
        assert response.status_code == status.HTTP_200_OK
        assert 'count' in response.data
        assert 'results' in response.data
        assert len(response.data['results']) >= 1
    
    def test_create_bulletin(self, authenticated_client, bulletin_data):
        """Test creating bulletin."""
        response = authenticated_client.post('/api/bulletins/', bulletin_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == bulletin_data['title']
        assert response.data['status'] == 'DRAFT'
    
    def test_get_bulletin_detail(self, authenticated_client, sample_bulletin):
        """Test getting bulletin detail."""
        response = authenticated_client.get(f'/api/bulletins/{sample_bulletin.id}/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == sample_bulletin.id
        assert response.data['title'] == sample_bulletin.title
    
    def test_update_bulletin(self, authenticated_client, sample_bulletin):
        """Test updating bulletin."""
        update_data = {'title': '更新后的标题'}
        response = authenticated_client.patch(
            f'/api/bulletins/{sample_bulletin.id}/',
            update_data
        )
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == '更新后的标题'
    
    def test_delete_bulletin(self, authenticated_client, sample_bulletin):
        """Test deleting bulletin."""
        response = authenticated_client.delete(
            f'/api/bulletins/{sample_bulletin.id}/'
        )
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Bulletin.objects.filter(id=sample_bulletin.id).exists() is False
    
    def test_publish_bulletin(self, authenticated_client, sample_bulletin):
        """Test publishing bulletin."""
        response = authenticated_client.post(
            f'/api/bulletins/{sample_bulletin.id}/publish/'
        )
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] == 'PUBLISHED'
        assert response.data['published_at'] is not None
    
    def test_filter_by_status(self, authenticated_client, user):
        """Test filtering bulletins by status."""
        Bulletin.objects.create(
            title='Draft Bulletin',
            content='Content',
            status='DRAFT',
            author=user
        )
        Bulletin.objects.create(
            title='Published Bulletin',
            content='Content',
            status='PUBLISHED',
            author=user
        )
        
        response = authenticated_client.get('/api/bulletins/?status=DRAFT')
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['title'] == 'Draft Bulletin'
    
    def test_search_by_title(self, authenticated_client, sample_bulletin):
        """Test searching bulletins by title."""
        response = authenticated_client.get('/api/bulletins/?search=测试')
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) >= 1
        assert '测试' in response.data['results'][0]['title']


# ==================== Permission Tests ====================

class TestBulletinPermissions:
    """Test bulletin permissions."""
    
    def test_unauthenticated_list(self, api_client):
        """Test unauthenticated users can list published bulletins."""
        response = api_client.get('/api/bulletins/')
        
        # Allow unauthenticated list for published bulletins
        assert response.status_code == status.HTTP_200_OK
    
    def test_unauthenticated_create(self, api_client, bulletin_data):
        """Test unauthenticated users cannot create bulletins."""
        response = api_client.post('/api/bulletins/', bulletin_data)
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_unauthenticated_delete(self, api_client, sample_bulletin):
        """Test unauthenticated users cannot delete bulletins."""
        response = api_client.delete(f'/api/bulletins/{sample_bulletin.id}/')
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
