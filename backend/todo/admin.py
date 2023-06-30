from django.contrib import admin

# import Todo
from .models import Todo

# create class for admin-model
class TodoAdmin(admin.ModelAdmin):

	# add the fields
	list_display = ("title","description","completed")

# register .model class and admin-model class
# using the register() method(w/ admin.site class)
admin.site.register(Todo,TodoAdmin)

