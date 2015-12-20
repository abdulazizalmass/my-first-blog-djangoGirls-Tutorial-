from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

#author is a link to anther model 
#modles.Model means that the post, name of our Django model knows 
#it should be saved in django sqlit3 database
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

#publish(self) is a method
#def is the function method
	def publish(self):
		self.published_date = timezone.now()
		self.save()
#methods returning post title 
		def __str__(self):
			return self.title
