from django.db import models
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, unique=True)
	image = models.ImageField(upload_to='blog/')
	text = models.TextField()
	draft = models.BooleanField("Черновик", default=False)
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args[str(self.id)])
