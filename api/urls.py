from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('blog-list/',views.blogList,name="blog-list"),
    path('blog-details/<str:pk>',views.blogDetails,name="blog-details"),
    path('blog-create/',views.createBlog,name="blog-create"),
    path('blog-update/<str:pk>',views.updateBlog,name="blog-update"),
    path('blog-delete/<str:pk>',views.deleteBlog,name="blog-delete"),
]