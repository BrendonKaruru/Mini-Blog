from django.shortcuts import render, redirect
from . models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def blog (request):
    blogs = Blog.objects.all()

    # for blog in blogs:
    #     print(blog.title)
    context = {'blogs' : blogs}

    return render(request, 'blog.html', context)

def contact (request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def createBlog (request):


    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        cover = request.FILES.get('cover')


        blog = Blog(title = title, body = body , cover = cover)
        blog.save()
        return redirect('blog')
    return render(request, 'createBlog.html')

@login_required(login_url='login')
def updateBlog (request, pk):
    blog = Blog.objects.get(id = pk)

    context =  { 'blog' : blog}

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        cover = request.FILES.get('cover')

        blog.title  = title
        blog.body = body
        blog.cover = cover
        blog.save()
        return redirect('blog')
    return render(request, 'updateBlog.html' , context)

def bloginfo(request, pk):
    blog = Blog.objects.get(id = pk)
    context = {'blog' : blog }
    return render(request, 'bloginfo.html' , context)

def deleteblog(request, pk):
    blog = Blog.objects.get(id = pk)
    context = {'blog' : blog }

    if request.method == 'POST':
         blog.delete()

         messages.success(request, 'Blog successfully deleted.')
         return redirect('blog')
    else:
         messages.error(request, 'Blog cannot delete')
   
    return render(request , 'deleteblog.html' , context)

def loginuser (request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is not None:

            login(request, user)

            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('blog')
        else:
            messages.error(request,'Invalid Username or Password')
        

    return render(request, 'login.html')

def logout_user (request):

    logout(request)

    return redirect('login')


