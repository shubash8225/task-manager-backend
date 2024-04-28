from rest_framework import serializers
from .models import Tasks, Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ['user']

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'