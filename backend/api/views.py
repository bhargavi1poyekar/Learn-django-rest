from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response

from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

def api_home(request, *args, **kwargs):

    # request=> Django HTTP (not python requests)
    body=request.body  # byte string of JSON data
    
    print(request.GET) # gives url params
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    print(data)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    return JsonResponse(data)

def api_model(request):
    if request.method!='GET':
        return HttpResponse(json.dumps("POST not allowed"))
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        # data["id"]=model_data.id
        # data["title"]=model_data.title
        # data["content"]=model_data.content
        # data["price"]=model_data.price

        data=model_to_dict(model_data)
        # data=model_to_dict(model_data, fields=['id','title','price']) # specific fields
        # Serialization=> Model data=> python dict=> to JSON => to client
    
    # json_data=json.dumps(data)
    #JsonResponse accepts dictionary, while HttpResponse requires String 
    # return HttpResponse(json_data, headers={'content-type':"application/json"})
    return JsonResponse(data)

@api_view(["GET"]) # decorator and get post states the permission for these requests
def api_rest(request):

    '''
    Django Rest Framework : Api-view
    '''

    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        # data=model_to_dict(model_data, fields=['id','title','price','sale_price'])
        data=ProductSerializer(instance).data
    return Response(data)


@api_view(["POST"])
def api_post(request):
    '''
    Django Rest Framework : Api-view
    '''
    
    serializer=ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        # data=serializer.data
        # instance=serializer.save() # saves object into table

        return Response(serializer.data)
    return Response({"invalid":"no title"}, status=405)