from rest_framework.generics import ListAPIView
from tag.models import Tag
from tag.serializers import TagSerializer


class TagListView(ListAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()
