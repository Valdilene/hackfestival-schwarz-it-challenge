from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


class ListCreateItemView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        # Get all items and order by 'expiresAt'
        items = Item.objects.all().order_by('expiresAt')

        # Serialize the data
        serializer = ItemSerializer(items, many=True)

        # Return the serialized data as JSON
        return Response({'items': serializer.data})


class RetrieveUpdateDeleteItemView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_url_kwarg = 'id'



# class ItemListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         # Get all items and order by 'expiresAt'
#         items = Item.objects.all().order_by('expiresAt')
#
#         # Serialize the data
#         serializer = ItemSerializer(items, many=True)
#
#         # Return the serialized data as JSON
#         return Response({'items': serializer.data})

# from .models import Item
# from .serializers import ItemSerializer