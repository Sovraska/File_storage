from rest_framework.generics import CreateAPIView, ListAPIView

from .models import File
from .serializers import FileSerializer


class FileCreateView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
