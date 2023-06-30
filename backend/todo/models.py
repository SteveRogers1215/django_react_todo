from django.db import models

class Todo(models.Model):
	title=models.CharField(max_length=150)
	description=models.CharField(max_length=500)
	completed=models.BooleanField(default=False)

	#stringify class
	def __str__(self):

		#return the title
		return self.title

