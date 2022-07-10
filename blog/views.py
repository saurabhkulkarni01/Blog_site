from django.shortcuts import render, get_object_or_404
from .models import Post, sample_no
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

class SearchView(ListView):
    model = sample_no
    template_name = 'blog/home.html'
    context_object_name='posts'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = sample_no.objects.filter(Model_Code=query)
          result = postresult
          
       else:
           result = None
       return result

def home(request):
    context={
        'posts':sample_no.objects.all()
    }
    print(context)
    return render(request, 'blog/home.html',context)


class PostListView(ListView):
    model=sample_no
    template_name= 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name='posts'
    paginate_by = 5

    


class UserPostListView(ListView):
    model=Post
    template_name= 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by = 5    

    def get_queryset(self):
        user= get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=sample_no

class PostCreateView(LoginRequiredMixin,CreateView):
    model=sample_no 
    fields =['Sample_No','Model_Code','Sub_Category','Curr_Location','Curr_Assignee','STPI']

    def form_valid(self,form):
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=sample_no  
    fields =['Sample_No','Model_Code','Sub_Category','Curr_Location','Curr_Assignee','STPI']

    def form_valid(self,form):
        return super().form_valid(form)    

    def test_func(self):    
        post=self.get_object()
        if post:
            return True
        return False    
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=sample_no
    success_url='/'

    def test_func(self):    
        post=self.get_object()
        if post:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})