from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

# class ProductInlineSerializer(serializers.Serializer):
#     url=serializers.HyperlinkedIdentityField(
#         view_name='product-detail',
#         lookup_field='pk',
#         read_only=True
#     )
#     title=serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    # user=UserPublicSerializer(read_only=True)
    owner=UserPublicSerializer(source='user',read_only=True)

    # related_products=ProductInlineSerializer(source='user.product_set.all()', read_only=True, many=True)

    # my_user_data=serializers.SerializerMethodField(read_only=True)
    # my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    # email=serializers.EmailField(write_only=True)
    title=serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name=serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model=Product
        fields=[
            # 'user',
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            # 'my_discount',
            # 'my_user_data',
            # 'related_products',
        ]

    # def get_my_user_data(self,obj):
    #     return {
    #         "username":obj.user.username
    #     }

    ######################################
    # for a field which is not an attribute of model, but is taken as input

    # def create(self, validated_data):
    #     email=validated_data.pop('email')
    #     obj=super().create(validated_data)
    #     return obj

    # def update(self,instance, validated_data):
    #     email=validated_data.pop('email')
    #     obj=super().update(instance, validated_data)
    #     return obj
    ############################################

    # '''
    # Custom validation
    # '''
    # def validate_title(self,value):
    #     request=self.context.get('request')
    #     user=request.user
    #     qs=Product.objects.filter(user=user,title__iexact=value) # iexact makes it case insensitive.
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    # '''
    # -----------
    # '''
    
    def get_edit_url(self, obj):
        # return f'/api/products/{obj.pk}'
        request=self.context.get('request')
        if request is None:
            return None
        return reverse("product-update",kwargs={"pk":obj.id},request=request)

    # def get_my_discount(self,obj):
    #     # try:
    #     #     return obj.get_discount()
    #     # except:
    #     #     return None

    #     if not hasattr(obj,'id'):
    #         return None
    #     if not isinstance(obj,Product):
    #         return None
    #     return obj.get_discount()