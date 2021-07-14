from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('blog/',  include('blog.urls'), name='blog'),
]
