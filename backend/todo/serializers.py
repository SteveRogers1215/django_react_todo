# import REST framework(serializers)
from rest_framework import serializers

# import Todo model
from .models import Todo

# create serializer class
class TodoSerializer(serializers.ModelSerializer):

	# create meta class
	class Meta:
		model = Todo
		fields = ('id', 'title','description','completed')
