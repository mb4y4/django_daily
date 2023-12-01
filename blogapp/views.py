from django.shortcuts import get_object_or_404, redirect, render

from myapp.models import Post
from .forms import EditPostForm, PostForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def post_list(request):
    posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)

            post.save()

            form = PostForm()

            return redirect('/post_list')
        
    else:
        form = PostForm()

    return render(request, "post_form.html", {'form': form})


def edit_post(request, slug):

    post = get_object_or_404(Post, slug=slug)

    form = EditPostForm(instance=post)
    if request.method ==  "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('/post_list', slug=post.slug )
    else:
        form = EditPostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post':post} )
