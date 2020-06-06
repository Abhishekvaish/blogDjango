from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

	# www.mysite.com/
	path('', views.index,name='index'),

	# www.mysite.com/home
	path('home/', views.Home.as_view(),name='home'),

	# www.mysite.com/post/22/author?=name
	path('post/<int:pk>/author?=<str:author>/', views.DetailPost.as_view(),name='detail'),

	# www.mysite.com/new_post/
	path('new_post/', views.NewPost.as_view(),name='new_post'),

	# www.mysite.com/post/2?=delete/
	path('post/<int:pk>?=delete', views.DeletePost.as_view(),name='delete'),

	# www.mysite.com/post/2?=edit/
	path('post/<int:pk>?=edit', views.UpdatePost.as_view(),name='edit'),

	# www.mysite.com/home
	path('post/u<int:pk>/<str:name>/profile',views.UserPosts.as_view(),name='user_post'),
	
]