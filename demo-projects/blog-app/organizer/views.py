"""Views for Organizer App"""
# from django.shortcuts import (
#     get_object_or_404,
#     redirect,
#     render,
# )
from django.shortcuts import get_object_or_404
# from django.urls import reverse
from django.urls import reverse_lazy
# from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# from django.views.generic import DetailView, ListView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    # RetrieveUpdateAPIView
    RetrieveUpdateDestroyAPIView
)
from .forms import TagForm
from .models import NewsLink, Startup, Tag
# from .serializers import NewsLinkSerializer
# from rest_framework.response import Response
# from rest_framework.status import (
#     HTTP_200_OK,
#     HTTP_400_BAD_REQUEST,
# )
# from rest_framework.status import (
#     HTTP_201_CREATED,
#     HTTP_400_BAD_REQUEST
# )
# from rest_framework.response import Response
# from rest_framework.status import HTTP_204_NO_CONTENT

from .models import NewsLink, Startup, Tag
from .serializers import (
    NewsLinkSerializer,
    StartupSerializer,
    TagSerializer
)


class TagList(ListView):
    """Display a list of Tags"""

    queryset = Tag.objects.all()
    template_name = "tag/list.html"

class TagDetail(DetailView):
    """Display a single Tag"""

    queryset = Tag.objects.all()
    template_name = "tag/detail.html"

# class TagCreate(View):
class TagCreate(CreateView):
    """Create new Tags via HTML form"""

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": False}

    # def get(self, request):
    #     """Display an HTML form"""
    #     context = {"form": TagForm(), "update": False}
    #     return render(request, "tag/form.html", context)

    # def post(self, request):
    #     """Handle Form submission: save Tag"""
    #     tform = TagForm(request.POST)
    #     if tform.is_valid():
    #         tag = tform.save()
    #         return redirect(tag.get_absolute_url())
    #     # invalid data; show form with errors
    #     context = {"form": tform, "update": False}
    #     return render(request, "tag/form.html", context)

# class TagUpdate(View):
class TagUpdate(UpdateView):
    """Update a Tag via HTML form"""

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": True}

    # def get(self, request, slug):
    #     """Display an HTML form with pre-filled data"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     context = {
    #         "tag": tag,
    #         "form": TagForm(instance=tag),
    #         "update": True,
    #     }
    #     return render(request, "tag/form.html", context)

    # def post(self, request, slug):
    #     """Handle Form submission: save Tag"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     tform = TagForm(request.POST, instance=tag)
    #     if tform.is_valid():
    #         tag = tform.save()
    #         return redirect(tag.get_absolute_url())
    #     # invalid data; show form with errors
    #     context = {
    #         "tag": tag,
    #         "form": tform,
    #         "update": True,
    #     }
    #     return render(request, "tag/form.html", context)

# class TagDelete(View):
class TagDelete(DeleteView):
    """Confirm and delete a Tag via HTML Form"""

    model = Tag
    template_name = "tag/confirm_delete.html"
    success_url = reverse_lazy("tag_list")

    # def get(self, request, slug):
    #     """Display an HTML form to confirm removal"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     return render(
    #         request, "tag/confirm_delete.html", {"tag": tag}
    #     )

    # def post(self, request, slug):
    #     """Delete Tag"""
    #     tag = get_object_or_404(Tag, slug=slug)
    #     tag.delete()
    #     return redirect(reversed("tag_list"))

class StartupList(ListView):
    """Display a list of Startups"""

    queryset = Startup.objects.all()
    template_name = "startup/list.html"

class StartupDetail(DetailView):
    """Display a single Startup"""

    queryset = Startup.objects.all()
    template_name = "startup/detail.html"

# class TagApiDetail(RetrieveAPIView):
class TagApiDetail(RetrieveUpdateDestroyAPIView):
    """Return JSON for single Tag object"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"

    # def put(self, request, slug):
    #     """Update existing Tag upon PUT
    #
    #     All Tag fields are expected.
    #     """
    #     # tag = get_object_or_404(Tag, slug=slug)
    #     tag = self.get_object()
    #     # s_tag = TagSerializer(
    #     s_tag = self.serializer_class(
    #         tag,
    #         data=request.data,
    #         context={"request": request}
    #     )
    #     if s_tag.is_valid():
    #         s_tag.save()
    #         return Response(s_tag.data, status=HTTP_200_OK)
    #     return Response(
    #         s_tag.errors, status=HTTP_400_BAD_REQUEST
    #     )

    # def patch(self, request, slug):
    #     """Update existing Tag upon PATCH"""
    #     tag = self.get_object()
    #     s_tag = self.serializer_class(
    #         tag,
    #         data=request.data,
    #         partial=True,
    #         context={"request": request}
    #     )
    #     if s_tag.is_valid():
    #         s_tag.save()
    #         return Response(s_tag.data, status=HTTP_200_OK)
    #     return Response(
    #         s_tag.errors, status=HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, slug):
    #     """DELETE the Tag with specified slug"""
    #     tag = self.get_object()
    #     tag.delete()
    #     return Response(status=HTTP_204_NO_CONTENT)


# class TagApiList(ListAPIView):
class TagApiList(ListCreateAPIView):
    """Return JSON for multiple Tag objects"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # def post(self, request):
    #     """Create new Tag upon POST"""
    #     s_tag = self.serializer_class(
    #         data=request.data, context={"request": request}
    #     )
    #     if s_tag.is_valid():
    #         s_tag.save()
    #         return Response(
    #             s_tag.data, status=HTTP_201_CREATED
    #         )
    #     return Response(
    #         s_tag.errors, status=HTTP_400_BAD_REQUEST
    #     )

class StartupAPIDetail(RetrieveAPIView):
    """Handle GET HTTP method"""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_field = "slug"

class StartupAPIList(ListAPIView):
    """Return JSON for multiple Startup objects"""

    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

class NewsLinkAPIDetail(RetrieveAPIView):
    """Return JSON for single NewsLink object"""

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer

    def get_object(self):
        """Override DRF's generic method

        http://www.cdrf.co/3.7/rest_framework.generics/ListAPIView.html#get_object
        """

        startup_slug = self.kwargs.get("startup_slug")
        newslink_slug = self.kwargs.get("newslink_slug")

        queryset = self.filter_queryset(self.get_queryset())

        newslink = get_object_or_404(
            queryset,
            slug=newslink_slug,
            startup__slug=startup_slug,
         )

        self.check_object_permissions(
            self.request, newslink
        )
        return newslink

class NewsLinkAPIList(ListAPIView):
    """Return JSON for multiple NewsLink objects"""

    queryset = NewsLink.objects.all()
    serializer_class = NewsLinkSerializer
