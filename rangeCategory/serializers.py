from rest_framework import serializers
from .models import Category
# from django.utils import timezone

class CategoryAPIViewSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(max_length=255)
    # description = serializers.CharField(max_length=255, write_only=True)
    # date_added = serializers.DateField(default=timezone.now, read_only=True)
    # date_added = serializers.DateField(read_only=True)
    class Meta:
        model = Category
        fields = ['id','category_name', 'description', 'date_added']
        