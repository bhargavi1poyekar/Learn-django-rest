from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    #Prduct.objects.get(pk='abc')

# product_detail_view=ProductDetailAPIView.as_view()
