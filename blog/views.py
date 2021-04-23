
from django.views.generic import ListView

from .models import Post



class BlogListView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    template_name = 'home_page.html'
