from django.shortcuts import render

# import REST framework(view sets)
from rest_framework import viewsets

# import TodoSerializer
from .serializers import TodoSerializer

# import Todo model 
from .models import Todo

# create class for the Todo model viewsets
class TodoView(viewsets.ModelViewSet):

	# create a serializer class and
	# assign it to TodoSerializer
	serializer_class = TodoSerializer

	# define a variable and assign it
	# the Todo list objects
	queryset = Todo.objects.all()

