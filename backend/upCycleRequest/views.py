from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import UpCycleRequest
from .serializers import UpCycleRequestSerializer


# Create your views here.


class UpCycleRequestListCreateView(ListCreateAPIView):
    queryset = UpCycleRequest.objects.all()
    serializer_class = UpCycleRequestSerializer


class UpCycleRequestRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = UpCycleRequest.objects.all()
    serializer_class = UpCycleRequestSerializer
    lookup_url_kwarg = 'id'
