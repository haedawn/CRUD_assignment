from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog, Comment
from .forms import BlogForm

def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog)
    return render(request,'detail.html',{'blog':blog, 'comments':comments})

def new(request):
    return render(request,'new.html')
    
def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.save()
    return redirect('detail',new_blog.id)
    #return render(request, 'detail.html', {'blog':new_blog})

# def create(request):
#     form = BlogForm(request, POST)

#     if form.is_vaild():
#         new_blog = form.save(commit=False)
#         new_blog.save()
#         return redirect('detail', new_blog.id)
    
#     return render(request, 'new.html')

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})

def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title =request.POST["title"]
    old_blog.content =request.POST["content"]
    old_blog.save()
    return redirect('detail', old_blog.id)

# def update(request, blog_id):
#     old_blog= get_object_or_404(Blog, pk=blog_id)
#     form = BlogForm(request.POST, instance=old_blog)

    # if form.is_valid():
    #     new_blog=form.save(commit=False)
    #     new_blog.save()
    # return redirect('detail', old_blog.id)
    
    # return render(request, 'new.html', {'old_blog':old_blog})

def delete(request, blog_id):
    delete_blog =get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')

# def comment_create(request, blog_id):
#         global comment
    
#         content=request.POST.get('content')
#         comment=comment()
#         comment.blog_id = blog_id
#         comment.content = content
#         comment.save()

#         return redirect('blogs:detail',blog_id)


def create_comment(request, blog_id):
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.blog = get_object_or_404(Blog, pk=blog_id)
    comment.save()
    return redirect('detail', blog_id)