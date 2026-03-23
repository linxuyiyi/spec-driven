"""Backend application viewsets."""

from rest_framework import viewsets, status, decorators, permissions
from rest_framework.response import Response
from django.utils import timezone

from .models import Bulletin
from .serializers import BulletinSerializer


class BulletinPermission(permissions.BasePermission):
    """公告权限类。"""
    
    def has_permission(self, request, view):
        # 允许匿名用户查看已发布的公告
        if view.action in ['list', 'retrieve']:
            return True
        # 其他操作需要认证
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # 允许匿名用户查看已发布的公告
        if view.action == 'retrieve' and obj.status == 'PUBLISHED':
            return True
        # 写操作需要是作者或管理员
        if request.user and request.user.is_authenticated:
            return (
                obj.author == request.user or
                request.user.is_staff
            )
        return False


class BulletinViewSet(viewsets.ModelViewSet):
    """系统公告视图集。"""
    
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = [BulletinPermission]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'content']
    ordering_fields = ['published_at', 'created_at', 'priority']
    
    def get_queryset(self):
        """获取查询集。"""
        queryset = super().get_queryset()
        
        # 匿名用户只能看已发布的
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(status='PUBLISHED')
        
        return queryset
    
    def perform_create(self, serializer):
        """创建时设置作者。"""
        serializer.save(author=self.request.user)
    
    @decorators.action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """发布公告。"""
        bulletin = self.get_object()
        bulletin.publish()
        serializer = self.get_serializer(bulletin)
        return Response(serializer.data)
