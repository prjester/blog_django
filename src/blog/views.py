from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list( request ):
    object_list = Post.published.all()
    panigator = Paginator( object_list, 3 )
    page = request.GET.get('page')
    try:
        posts = panigator.page(page)
    except PageNotAnInteger:
        posts = panigator.page(1)
    except EmptyPage:
        posts = panigator.page(panigator.num_pages)

    return render( request, 'blog/post/list.html', {'page': page, 'posts': posts } )

def post_detail( request, year, month, day, post ): 
    post = get_object_or_404( Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day )

    return render( request, 'blog/post/detail.html', {'post': post } )