from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *

def hello(request):
    post_list = Post.objects.all()
    return render(request,'index.html',{"post_list":post_list})
def add_post(request):
    if request.method=='POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = AddForm()
    return render(request,'form.html',{"form":form})
def edit_post(request,id):
    if request.method=='POST':
        form = AddForm(request.POST,instance=Post.objects.get(id=id))
        if form.is_valid():
            form.save()
        return redirect('/')
    form = AddForm(instance=Post.objects.get(id=id))
    return render(request,'form.html',{"form":form})
def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')
