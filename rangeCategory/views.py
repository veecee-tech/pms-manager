from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rangeCategory.models import Category, Range
from .permissions import IsOwner
from .serializers import CategoryAPIViewSerializer, RangeAPIViewSerializer


# from rest_framework import status
# Create your views here.

class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategoryAPIViewSerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryAPIViewSerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"

    def get_queryset(self):
        return Category.objects.all()


class RangeAPIView(ListCreateAPIView):
    serializer_class = RangeAPIViewSerializer
    queryset = Range.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Range.objects.filter(user=self.request.user)


class RangeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RangeAPIViewSerializer
    queryset = Range.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"

    def get_queryset(self):
        return Range.objects.all()


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsOwner])
def numberOfRangeEtsCategory(request, *args, **kwargs):
    if request.method == 'GET':
        total = {
            'range': len(Range.objects.filter(user=request.user)),
            'range_category': len(Category.objects.filter(user=request.user))
        }
        # serializer = RangeAPIViewSerializer(total)

        return JsonResponse(total)
