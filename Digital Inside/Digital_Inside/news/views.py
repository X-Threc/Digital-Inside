from django.shortcuts import render, redirect
from .models import Post, Comments
from .forms import PostForm, CommentForm, UserRegisterForm, UserLoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login,logout
# Create your views here.


def news_home(request):
    news = Post.objects.order_by('-date_post')
    return render(request, 'news/news_home.html', {'news': news})


def NewsDetailsView(request, pk):
    post = get_object_or_404(Post,pk=pk)
    comment = Comments.objects.filter(post=post)
    if request.method=="POST":
        form= CommentForm(request.POST)
        if form.is_valid():
            comm=form.save(commit=False)
            comm.commentator =request.user
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(request, 'news/details_view.html', {'arcticle': post, "form":form, 'comment':comment})


def create(request):
    error=''
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posted = form.save(commit=False)
            posted.author = request.user
            posted.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = PostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,'Вы успешно зарегистрировались')
            return redirect('news_home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request,'news/register.html',{'form':form})


def user_login(request):
    if request.method =='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('news_home')
    else:
        form = UserLoginForm()
    return render(request,'news/login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')
