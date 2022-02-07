"""Serializers for the Organizer App

Serializer Documentation
http://www.django-rest-framework.org/api-guide/serializers/
http://www.django-rest-framework.org/api-guide/fields/
http://www.django-rest-framework.org/api-guide/relations/
"""
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedRelatedField
)

from .models import NewsLink, Startup, Tag

class TagSerializer(HyperlinkedModelSerializer):
    """Serialize Tag data"""

    class Meta:
        model = Tag
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-tag-detail"
            } 
        }

class StartupSerializer(HyperlinkedModelSerializer):
    """Serialize Startup data"""

    # tags = TagSerializer(many=True)
    # tags = TagSerializer(many=True, read_only=True)
    # tags = TagSerializer(many=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Startup
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "api-startup-detail",
            }
        }

    # def create(self, validated_data):
    #     """Create Startup and associated Tags"""
    #     tag_data_list = validated_data.pop("tags")
    #     startup = Startup.objects.create(**validated_data)
    #     # the code below, where we relate bulk-create objects,
    #     # works only in databases that returns PK after bulk insert,
    #     # which at the time of writing is only PostgreSQL
    #     tag_list = Tag.objects.bulk_create(
    #         [Tag(**tag_data) for tag_data in tag_data_list]
    #     )
    #     startup.tags.add(*tag_list)
    #     return startup

class NewsLinkSerializer(ModelSerializer):
    """Serialize NewsLink data"""

    url = SerializerMethodField()
    # startup = StartupSerializer()
    startup = HyperlinkedRelatedField(
        queryset=Startup.objects.all(),
        lookup_field="slug",
        view_name="api-startup-detail",
    )

    class Meta:
        model = NewsLink
        # fields = "__all__"
        exclude = ("id",)

    def get_url(self, newslink):
        """Build full URL for NewsLink API detail"""
        return reverse(
            "api-newslink-detail",
            kwargs=dict(
                startup_slug=newslink.startup.slug,
                newslink_slug=newslink.slug,
            ),
            request=self.context["request"],
        )

