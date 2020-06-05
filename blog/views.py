from django.shortcuts import render,get_object_or_404,reverse
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')


class Home(ListView):
	model = Post
	template_name = 'blog/home.html' #default_name = 'blog/post_list.html'
	context_object_name = 'post_list' #default_name = 'object_list'
	ordering = '-created_on'
	paginate_by = 10
	
class DetailPost(DetailView):
	model = Post
	context_object_name = 'post' #default = obj
	template_name = 'blog/post_detail.html' #default = 'blog/post_detail.html'

class NewPost(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/post_create.html'  # default = 'blog/post_form.html'
	context_object_name = 'form' # default = form 

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class UpdatePost(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/post_create.html'  # default = 'blog/post_form.html'
	context_object_name = 'form' # default = form 

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else :
			return False

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)



class DeletePost(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	template_name = 'blog/post_delete.html' #default = 'blog/post_delete.html'
	pk = None
	success_url = '/' #reverse('blog:user_post',kwargs={'pk':pk})
	def test_func(self):
		post = self.get_object()
		pk = self.request.user.pk
		if self.request.user == post.author:
			return True
		else :
			return False


class UserPosts(ListView):
	model = Post
	context_object_name='post_list' #default = 'object'
	template_name = 'blog/user_post.html'
	ordering = '-created_on'
	paginate_by = 10
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		user = get_object_or_404(get_user_model(),pk=self.kwargs.get("pk"))
		context['author'] = user
		return context

	def get_queryset(self):
		user = get_object_or_404(get_user_model(),pk=self.kwargs.get("pk"))
		return Post.objects.filter(author = user)
