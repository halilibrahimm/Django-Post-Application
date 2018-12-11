from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
import django
from post.models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.utils.text import slugify #küçük harfe çevirecek
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #sayfalara postları dağıtmak için
from django.db.models import Q #tüm parametrelere göre arama yapmak için








# Create your views here.
def post_index(request):
    postList=Post.objects.all()
    
    query=request.GET.get('q')
    if query:
        postList=postList.filter( # arama yapıyoruz tüm parametreler için
            Q(title__icontains=query) |
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
            ).distinct()
         



     #sayfalara postları dağıtmak için

    paginator = Paginator(postList, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
     #sayfalara postları dağıtmak için

   




    return render(request,'post/index.html',{'posts':posts})


def post_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)


    form=CommentForm(request.POST or None) #yorum için.Request.files yok çünkü yorumlarda dosya gönderilmez.
    if form.is_valid():
       comment= form.save(commit=False)#veritabanına kayıt eder
       comment.post=post#hangi posta yorum yazılacağı post nesnesi eşitlenerek belirtiliyor
       comment=form.save()
       return HttpResponseRedirect(post.get_absolute_url())#işlem bitince yönlendirmek isteiğimiz adres


    context={
        'post':post,
        'form':form,#yukarıdaki form nesnesi içerik olarak gönderiliyor
        }
    return render(request,'post/detail.html',context)

def post_create(request):
    if not request.user.is_authenticated():
        return Http404()
    form=PostForm(request.POST or None, request.FILES or None) 
    if form.is_valid():
       post= form.save(commit=False)#veritabanına kayıt eder
       post.user=request.user
       post=form.save()
       messages.success(request,'BAŞARILI')
       return HttpResponseRedirect(post.get_absolute_url())
       
    context={
        'form':form,}
    return render(request,'post/form.html',context)
    

def post_update(request,slug):
    if not request.user.is_authenticated():#yetkisiz kullanıcı giremez
        return Http404()
    post=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        post=form.save()
        messages.success(request,'BAŞARILI')
        return HttpResponseRedirect(post.get_absolute_url())
    context={
        'form':form,}
    
    return render(request,'post/form.html',context)
    

def post_delete(request,slug):
    if not request.user.is_authenticated():
        return Http404()
    post=get_object_or_404(Post,slug=slug)
    post.delete()
    return redirect('post:index')
