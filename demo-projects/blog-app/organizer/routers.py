"""URL Paths and Routers for Organizer App"""
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    NewsLinkAPIDetail,
    NewsLinkAPIList,
	# StartupAPIDetail,
	# StartupAPIList,
	# TagApiDetail,
	# TagApiList
)
from .viewsets import StartupViewSet, TagViewSet

api_router = SimpleRouter()
api_router.register("tag", TagViewSet, basename="api-tag")
api_router.register("startup", StartupViewSet, basename="api-startup")
api_routes = api_router.urls

# tag_create_list = TagViewSet.as_view(
#     {"get": "list", "post": "create"}
# )
# tag_retrieve_update_delete = TagViewSet.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "delete"
#     }
# )

urlpatterns = api_routes + [
    # path("tag/", TagApiList.as_view(), name="api-tag-list"),
    # path("tag/", tag_create_list, name="api-tag-list"),
    # path(
    #     "tag/<str:slug>/",
    #     TagApiDetail.as_view(),
    #     name="api-tag-detail"
    # ),
    # path(
    #     "tag/<str:slug>/",
    #     tag_retrieve_update_delete,
    #     name="api-tag-detail"
    # ),
    # path(
    # 	"startup/",
    # 	StartupAPIList.as_view(),
    # 	name="api-startup-list",
    # ),
    # path(
    # 	"startup/<str:slug>/",
    # 	StartupAPIDetail.as_view(),
    # 	name="api-startup-detail",
    # ),
    path(
        "newslink/",
        NewsLinkAPIList.as_view(),
        name="api-newslink-list",
    ),
    path(
        "newslink/<str:startup_slug>/<str:newslink_slug>/",
        NewsLinkAPIDetail.as_view(),
        name="api-newslink-detail",
    ),
]