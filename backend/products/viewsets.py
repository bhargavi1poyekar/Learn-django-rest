from rest_framework import viewsets

from .models import Product

from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get-> list-> queryset
    get -> retreive-> detail instance
    post-> create
    put-> update
    patch-> partila instance
    delete-> destroy
    '''
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    lookup_field='pk'