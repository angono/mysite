from django.shortcuts import render, get_object_or_404
from .models import *  #here we import our models


# A function to display all information.
def post_list_view(request):
    all_post = PhotoModel.objects.all() #All posts

    context ={
        'all_post':all_post,
    }
    return render(request, 'blog/post_list.html', context)


# A function to display details of each post.
def post_detail_view(request, ids):
    post_ids = get_object_or_404(PhotoModel, id=ids) #Detail of each post

    context ={
        'post_ids':post_ids,
    }
    return render(request, 'blog/post_detail.html', context)










