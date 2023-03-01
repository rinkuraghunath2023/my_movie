from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import my_movie
from .forms import movieform
# Create your views here.
def index(request):
    movie=my_movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request,'index.html',context)
def detail (request,movie_id):
    movie = my_movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method == "POST":
        name=request.POST.get('name')
        about = request.POST.get('about')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=my_movie(name=name,about=about,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=my_movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=my_movie.objects.get(id=id)
        movie.delete()

        return redirect('/')
    return render(request,'delete.html')