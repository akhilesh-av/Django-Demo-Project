from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Old Method: 
@login_required(login_url='login/')
def create(request):
    frm = MovieForm()
    if request.POST:
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        year = request.POST.get('year')
        poster = request.POST.get('poster')
        movie_obj = MovieInfo(title=title,summary=summary,year=year,poster=poster)
        movie_obj.save()
    return render(request,"create.html",{ 'frm' : frm })



# def create(request):
#     if request.POST:
#         frm = MovieForm(request.POST)
#         if frm.is_valid():
#             frm.save()
#         else:
#             frm=MovieForm()    
#     return render(request,"create.html",{ 'frm' : frm })


@login_required(login_url='login/')
def list(request):
    print(request.COOKIES)
    visit = int(request.COOKIES.get('visits',0))
    visit +=1
    movie_data=MovieInfo.objects.all()
    
    response =render(request,"list.html",{'movies': movie_data})
    response.set_cookie('visit',visit)

    return response

@login_required(login_url='login/')
def edit(request,pk):
    edit_instance =MovieInfo.objects.get(pk=pk)
    if request.POST:
        edit_instance.title = request.POST.get('title')
        edit_instance.summary = request.POST.get('summary')
        edit_instance.year = request.POST.get('year')
        edit_instance.poster = request.POST.get('poster')
        edit_instance.save()
    frm = MovieForm(instance=edit_instance)
    return render(request,"create.html",{ 'frm' : frm })
@login_required(login_url='login/')
def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_data=MovieInfo.objects.all()
    
    return render(request,"list.html",{'movies': movie_data})


def test(request):
    movie_data=MovieInfo.objects.all()
    return render(request,"index.html",{'movies': movie_data})
    
