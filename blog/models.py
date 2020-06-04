from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
User = get_user_model()


# Create your models here.
# TODO TAGS ....
class Tag(models.Model):
	tag_name = models.CharField(max_length=20)

	def __str__(self):
		return self.tag_name

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now=True)
	#tags = models.ManyToManyField(Tag)

	def get_absolute_url (self):
		return reverse('blog:detail',kwargs={"pk":self.pk})

	def __str__(self):
		return self.title

class Comment(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return f"comment on {self.post}"


