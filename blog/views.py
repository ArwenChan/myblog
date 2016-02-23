from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Tags
import urllib.request
import json
# Create your views here.


def IndexView(request):
    try:
        blogs = Blog.objects.all()[:10]
        tags = Tags.objects.all()
    except Blog.DoesNotExist:
        raise Http404("Error: can not get blog list or tag list")
    return render(request, 'blog/index.html', {'blogs': blogs, 'tags': tags})


def Category(request, category):
    blogs = Blog.objects.filter(blog_type=category)[:10]
    tags = Tags.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs, 'tags': tags})


def Query_Blog(request):
    if request.is_ajax():
        query = request.GET.get('query')
        blogs = Blog.objects.filter(name__contains=query)[:10]
        return render(request, 'blog/list-content.html', {'blogs': blogs})


def Tag_ajax(request):
    if request.is_ajax():
        tagname = request.GET.get('tag')
        blog_type = request.GET.get('blog_type')
        tag = Tags.objects.get(name=tagname)
        if(blog_type):
            blogs = tag.blog_set.filter(blog_type=blog_type)[:10]
        else:
            blogs = tag.blog_set.all()[:10]
        return render(request, 'blog/list-content.html', {'blogs': blogs})


def More_ajax(request):
    if request.is_ajax():
        tagname = request.GET.get('tag')
        num = int(request.GET.get('blogs_number'))
        blog_type = request.GET.get('blog_type')
        query = request.GET.get('query')
        no_more = False
        if tagname:
            tag = Tags.objects.get(name=tagname)
            blog_query = tag.blog_set
        else:
            blog_query = Blog.objects
        if blog_type:
            blog_query = blog_query.filter(blog_type=blog_type)
        if query:
            blog_query = blog_query.filter(name__contains=query)
        all_num = blog_query.count()
        if(all_num > num):
            blogs = blog_query.all()[:num]
        else:
            blogs = blog_query.all()
            no_more = True

        return render(request, 'blog/list-content.html', {'blogs': blogs, 'nomore': no_more})


def Blog_content(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.reads = blog.reads + 1
    try:
        url = "http://api.duoshuo.com/threads/counts.json?short_name=arwen&threads=" + str(blog.id)
        data = urllib.request.urlopen(url, timeout=0.5).read()
        sdata = data.decode('utf-8')
        print(sdata)
        values = json.loads(sdata)
        blog.comments = values['response'][str(blog.id)]['comments']
    except Exception as e:
        print(e)
    blog.save()
    return render(request, 'blog/content.html', {'blog': blog})


def Add_like(request):
    if request.is_ajax():
        blog_id = int(request.GET.get('blog_id'))
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.likes = blog.likes + 1
        blog.save()
        return HttpResponse('success')
