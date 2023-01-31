from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from api.mixins import (StaffEditorPermissionMixin,UserQuerySetMixin)
from api.permissions import IsStaffEditorPermission

'''
Class Based Views- Easier to write and understand
'''

class ProductCreateAPIView(
    StaffEditorPermissionMixin,
    generics.CreateAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        if content==None:
            content=title
        serializer.save(content=content)
    
    

product_create_view=ProductCreateAPIView.as_view()


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    # authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content==None:
            content=title
        serializer.save(user=self.request.user,content=content)
    

    '''
    Alternative Mixin-> UserQuerySetMixin
    '''
    # def get_queryset(self, *args, **kwargs):
    #     qs=super().get_queryset(*args, **kwargs)
    #     request=self.request
    #     user=request.user
    #     print(f'user={user}')
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)

product_list_create_view=ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]


    #Prduct.objects.get(pk='abc')

product_detail_view=ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

    lookup_field='pk'

    def perform_update(self,serializer):
        
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
            # Not required to save again

product_update_view=ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]


    #Prduct.objects.get(pk='abc')
    def perform_destroy(self,instance):
        
        # instance
        super().perform_destroy(instance)

product_delete_view=ProductDestroyAPIView.as_view()

'''
Class based view (all together)
'''

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk' # required for Retrieve Model Mixin


    def get(self, request, *args, **kwargs):
        # print(args, kwargs) pk is present in kwargs
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs) # the list method from mixins
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self,serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content==None:
            content='No content'
        serializer.save(content=content)

product_mixin_view=ProductMixinView.as_view()


'''
Not required'''
class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

product_list_view=ProductListAPIView.as_view()
'''
-----
'''


'''
Function Based Views
'''
# create, retrieve(detail), list view all together - but generics is better

@api_view(['GET','POST']) 
def product_alt_view(request,pk=None, *args, **kwargs):
   
    method=request.method
    # 'PUT' => update and 'DESTROY'=> delete
    if method=='GET':
        if pk is not None:
            #detail
            # queryset=Product.objects.filter(pk=pk)
            # if not queryset.exists():
            #     raise HTTP404
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj, many=False).data

            return Response(data)
        
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)

    if method=='POST':
        serializer=ProductSerializer(data=request.data)
    
        if serializer.is_valid(raise_exception=True):
            # data=serializer.data
            # instance=serializer.save() # saves object into table
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content')
            if content==None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"no title"}, status=405)

