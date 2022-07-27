from .models import Category, Things
from .serializers import CategorySerializer, ThingsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def things_list(request):
    if request.method == "GET":
        things = Things.objects.all()
        serializer = ThingsSerializer(things, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ThingsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, response=201)
        return JsonResponse(serializer.errors, response=400)

@csrf_exempt
def things_detail(request, pk):

    try:
        thing = Things.objects.get(pk=pk)
    except Things.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ThingsSerializer(thing)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser.parse(request)
        serializer = ThingsSerializer(thing, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        thing.delete()
        return HttpResponse(status=204)
    
def category_list(request, cat):
    try:
        category = Category.objects.get(name=cat.lower())
        things = Things.objects.all().filter(category=category.id)
    except (Things.DoesNotExist, Category.DoesNotExist):
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ThingsSerializer(things, many=True)
        return JsonResponse(serializer.data, safe=False)