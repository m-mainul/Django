
"""Serializers for th Blog App

Serializer Documentation
http://www.django-rest-framework.org/api-guide/serializers/
http://www.django-rest-framework.org/api-guide/fields/
http://www.django-rest-framework.org/api-guide/relations/
"""

from rest_framework.serializers import ModelSerializer

from .models import Post

from organizer.serializers import (
    StartupSerializer,
    TagSerializer,
)

class PostSerializer(ModelSerializer):
    """Serialize Post data"""

    tags = TagSerializer(many=True)
    startup = StartupSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"