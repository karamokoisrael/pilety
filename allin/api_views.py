from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from allin.models import (Expense, FullCargo, FullContainer, Invoice,
                          LooseCargo, LooseContainer, Product)
from allin.serializers import (FullCargoSerializer, FullContainerSerializer,
                               LooseCargoSerializer, LooseContainerSerializer,
                               ProductSerializer)


class RecentProductAPIView(APIView):
    def get(self, request, format=None):
        # Retrieve the most recent products
        recent_products = Product.objects.all().order_by('-recieved')[:10] 

        # Serialize the data
        serializer = ProductSerializer(recent_products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
