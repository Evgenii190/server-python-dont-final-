from rest_framework import serializers
from .models import Characteristic, Project, ProjectCategory, ProjectCharacteristic

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ('id', 'title', 'slug')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectCharacteristicSerializer(serializers.ModelSerializer):
    params = serializers.CharField(source='characteristic')

    class Meta:
        model = ProjectCharacteristic
        fields = ['id', 'project', 'option', 'params']
