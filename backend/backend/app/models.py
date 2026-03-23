"""Backend application models."""

from django.conf import settings
from django.db import models


class Bulletin(models.Model):
    """系统公告模型。"""
    
    STATUS_CHOICES = [
        ('DRAFT', '草稿'),
        ('PUBLISHED', '已发布'),
        ('ARCHIVED', '已归档'),
    ]
    
    PRIORITY_CHOICES = [
        ('LOW', '低'),
        ('NORMAL', '普通'),
        ('HIGH', '高'),
        ('URGENT', '紧急'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='NORMAL')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'bulletin'
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['status', 'published_at']),
            models.Index(fields=['priority', 'status']),
        ]
    
    def __str__(self) -> str:
        return self.title
    
    def publish(self):
        """发布公告，设置发布时间。"""
        self.status = 'PUBLISHED'
        from django.utils import timezone
        self.published_at = timezone.now()
        self.save()
