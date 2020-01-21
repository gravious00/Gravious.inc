from django.shortcuts import render
from django.utils import timezone
from .models import resident , federal, visitor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import residentSerializer, fedralSerializer , visitorSerializer

def post_list(request):
	#resident = resident.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'app/post_list.html', {'resident': resident.objects.all})

@api_view(['GET', 'POST'])
def resident_list(request):
	if request.method == 'GET':
		obj = resident.objects.all()
		print (obj)
		serializer = residentSerializer(obj,many=True)
		print (type(serializer.data))
		return Response(serializer.data)
		
	elif request.method == 'POST':
		serializer = residentSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data , status = status.HTTP_201_CREATED)
		return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def federal_list(request):
	if request.method == 'GET':
		obj = federal.objects.all()
		print (obj)
		serializer = fedralSerializer(obj,many=True)
		print (type(serializer.data))
		return Response(serializer.data)
		
	elif request.method == 'POST':
		serializer = fedralSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data , status = status.HTTP_201_CREATED)
		return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def visitor_list(request):
	if request.method == 'GET':
		obj = visitor.objects.all()
		print (obj)
		serializer = visitorSerializer(obj,many=True)
		print (type(serializer.data))
		return Response(serializer.data)
		
	elif request.method == 'POST':
		serializer = visitorSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data , status = status.HTTP_201_CREATED)
		return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)