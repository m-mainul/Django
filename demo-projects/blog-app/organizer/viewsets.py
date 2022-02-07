"""Viewsets for the Organizer App"""
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    # HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST
)
# from rest_framework.viewsets import ViewSet

from rest_framework.viewsets import ModelViewSet

from .models import Startup, Tag
from .serializers import StartupSerializer, TagSerializer

# class TagViewSet(ViewSet):
class TagViewSet(ModelViewSet):
    """A set of views for the Tag model"""

    lookup_field = "slug"
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # def list(self, request):
    #     """List Tag objects"""
    #     tag_list = Tag.objects.all()
    #     s_tag = TagSerializer(
    #         tag_list,
    #         many=True,
    #         context={"request": request},
    #     )
    #     return Response(s_tag.data)
    #
    # def retrieve(selfs, request, slug):
    #     """Display a single Tag object"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     s_tag = TagSerializer(
    #         tag, context={"request": request}
    #     )
    #     return Response(s_tag.data)
    #
    # def create(self, request):
    #     """Create a new Tag object"""
    #     s_tag = TagSerializer(
    #         data=request.data, context={"request": request}
    #     )
    #     if s_tag.is_valid():
    #         s_tag.save()
    #     return Response(s_tag.data, status=HTTP_201_CREATED)
    #
    # def update(self, request, slug):
    #     """Update an existing Tag object"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     s_tag = TagSerializer(
    #         tag,
    #         data=request.data,
    #         context={"request": request},
    #     )
    #     if s_tag.is_valid():
    #         s_tag.save()
    #         return Response(s_tag.data)
    #     return Response(
    #         s_tag.errors, status=HTTP_400_BAD_REQUEST
    #     )
    #
    # def partial_update(self, request, slug):
    #     """Update a Tag object partially"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     s_tag = TagSerializer(
    #         tag,
    #         data=request.data,
    #         partial=True,
    #         context={"request": request},
    #     )
    #     if s_tag.is_valid():
    #         s_tag.save()
    #         return Response(s_tag.data)
    #     return Response(
    #         s_tag.errors, status=HTTP_400_BAD_REQUEST
    #     )
    #
    # def delete(self, request, slug):
    #     """Delete a Tag object"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     tag.delete()
    #     return Response(status=HTTP_204_NO_CONTENT)

class StartupViewSet(ModelViewSet):
    """A set of views for the Startup model"""

    lookup_field = "slug"
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

    @action(detail=True, methods=["HEAD", "GET", "POST"])
    def tags(self, request, slug=None):
        """Relate a POSTed Tag to Startup in URI"""
        startup = self.get_object()
        if request.method in ("HEAD", "GET"):
            s_tag = TagSerializer(
                startup.tags,
                many=True,
                context={"request": request},
            )
            return Response(s_tag.data)
        tag_slug = request.data.get("slug")
        if not tag_slug:
            return Response(
                "Slug of Tag must be specified",
                status=HTTP_400_BAD_REQUEST,
            )
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        startup.tags.add(tag)
        return Response(status=HTTP_204_NO_CONTENT)