from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
from django.urls import reverse
from django.shortcuts import get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm,FormPost,PostForm
from django.contrib.auth.models import Group
from django.contrib import messages
# Create your views here.


    
    
class PostDetail(generic.DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'blog/postDetail.html'
    def get_queryset(self):
       qs = super().get_queryset()
       return qs.filter(pk= self.kwargs['pk'])
    
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username= username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('blog:general-page')
        else:
            messages.error(request,'username or password invalid')
            return redirect('blog:login')
            
        
    return render(request,'blog/login_register.html',{'page':page})

def logoutUser(request):
    logout(request)
    return redirect('blog:login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.save()
            
            user = authenticate(request,username=user.username,email=user.email,password=request.POST["password1"])
            
            if user is not None:
                login(request,user)
                return redirect('blog:general-page')
            else:
                messages.error(request,'invalid username or password')
                return redirect('blog:register')
    context ={'form':form,'page':page}
    return render(request,'blog/login_register.html',context)


def createPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = FormPost(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                subtitle = form.cleaned_data['subtitle']
                content = form.cleaned_data['content']
               
                pst = Post(title=title,subtitle=subtitle,content=content,)
                pst.save()
                return redirect('blog:dashboard')
        else:
            form = FormPost()
            return render(request,'blog/postFunc.html',{'form':form})
            

    page = 'login'
    return redirect('blog:login')
    
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('-created_on')
        
        user = request.user
        full_name = user.username
        context = {'posts': posts,'full_name':full_name}
        return render(request,'blog/dashboard.html',context)
    else:
        return HttpResponseRedirect(reverse('blog:login'))
    
def updatePost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = FormPost(request.POST,instance = pi)
            if form.is_valid():
                form.save()
                return redirect('blog:dashboard')
        else:
            pi = Post.objects.get(pk=id)
            form = FormPost(instance=pi)
            return render(request,'blog/updatePost.html',{'form':form})
            
        return render(request,'blog/updatePost.html',{'form':form})

    return HttpResponseRedirect('blog:login')
    
def deletePost(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return redirect('blog:dashboard')
        
    
    return redirect('blog:login')
def generalPage(request):
    post = Post.objects.all()[:5]
    return render(request,'blog/generalPage.html',{'post_list':post})