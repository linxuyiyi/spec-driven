"""Backend application serializers."""

from rest_framework import serializers
from .models import Bulletin


class BulletinSerializer(serializers.ModelSerializer):
    """系统公告序列化器。"""
    
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Bulletin
        fields = [
            'id', 'title', 'content', 'status', 'priority',
            'author', 'published_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'author', 'published_at', 'created_at', 'updated_at']
    
    def validate_title(self, value: str) -> str:
        """验证标题不为空。"""
        if not value or not value.strip():
            raise serializers.ValidationError("标题不能为空")
        return value
    
    def validate_content(self, value: str) -> str:
        """验证内容不为空。"""
        if not value or not value.strip():
            raise serializers.ValidationError("内容不能为空")
        return value
    
    def validate_status(self, value: str) -> str:
        """验证状态选项。"""
        valid_statuses = ['DRAFT', 'PUBLISHED', 'ARCHIVED']
        if value not in valid_statuses:
            raise serializers.ValidationError(f"无效的状态，必须是 {valid_statuses} 之一")
        return value
    
    def validate_priority(self, value: str) -> str:
        """验证优先级选项。"""
        valid_priorities = ['LOW', 'NORMAL', 'HIGH', 'URGENT']
        if value not in valid_priorities:
            raise serializers.ValidationError(f"无效的优先级，必须是 {valid_priorities} 之一")
        return value
