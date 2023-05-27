from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def navbar(request):
    posts = Post.objects.all()
    is_owner = False

    if request.user.is_authenticated:
        is_owner = posts.filter(author=request.user).exists()

    context = {
        'is_owner': is_owner,
        'posts': posts,
    }

    return render(request, 'navbar.html', context)


def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'Posts/post_pages.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'Posts/posts.html', context)

def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'Posts/form_post.html', context)

def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {'post': post}

    return render(request, 'delete_template.html', context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    update = 1

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance= post)
        form.save()
        return redirect('home')
            
    context = {'form': form, 'update': update}

    return render(request, 'Posts/form_post.html', context)
 
def contacto(request):
    return render(request, "contacto.html")
