# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from base.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def all_books(request, id=-1):
    if request.method == 'GET':
        if id == -1:
            return Response(BookSerializer(Book.objects.all(), many=True) .data)
        else:
            return Response(BookSerializer(Book.objects.get(id=id), many=False). data)
    elif request.method == 'POST':
        tsk_serializer = BookSerializer(data=request.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("book added succefuly")
    elif request.method == 'DELETE':
        try:
            temp_task=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_task.delete()
        return Response ("deleted succefuly")
    elif request.method =='PUT':
        try:
            temp_task=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("Book not found")
       
        ser = BookSerializer(data=request.data)
        old_task = Book.objects.get(id=id)
        res = ser.update(old_task, request.data)
        return Response("done")
