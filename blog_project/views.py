from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request, category_slug=None):
    data = Post.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        data=Post.objects.filter(category= category)
    categories=Category.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'home.html', {'data' : data, 'category':categories})