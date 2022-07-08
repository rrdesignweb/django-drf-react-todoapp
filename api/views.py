from django.shortcuts import render, HttpResponseRedirect, Http404
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
def index(request):
    return render(request, 'build/index.html')

@csrf_exempt #anti forgery token
def TodosHandler(request):
    if request.method == 'GET':
        items = Todo.objects.all()
        serializer = TodoSerializer(items, many = True)
        return JsonResponse(serializer.data, safe = False)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data = data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def TodoHandler(request, pk):
    try: 
        todo = Todo.objects.get(id = pk)
    except Todo.DoesNotExist:
        raise Http404('Not found')
 
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)
 
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo,data = data)
 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)
 
    if request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status = 204)