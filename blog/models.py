from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
User = get_user_model()


# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now=True)
	#tags = models.ManyToManyField(Tag)

	def get_absolute_url (self):
		return reverse('blog:detail',kwargs={"pk":self.pk,"author":self.author.first_name})

	def __str__(self):
		return self.title


