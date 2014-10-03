from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost


def home(request):
    blog = BlogPost.objects.all()
    blog_posts = { "blogs" : blog }
    return render(request, 'main.html', blog_posts)