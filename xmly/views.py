from django.shortcuts import render
from .xmlyss import *

# Create your views here.
def search(request):
    context = {}
    return render(request,'xmly/search.html',context)

def search_result(request):
    search_name = request.GET['search_name']
    content = Xmly(search_name).search_content()
    context = {'content':content}
    #print(context)
    return render(request,'xmly/result.html',context)
def album(request,ab_id):
    content = Xmly().album(ab_id)
    context = {'content':content}
    print(context)
    return render(request,'xmly/album.html',context)
def zhubo(request,zhubo_id):
    content = Xmly().zhubo(zhubo_id)
    context = {'content':content}
    return render(request, 'xmly/zhubo.html', context)
def zb_album(request,zb_album_id):
    content = Xmly().album(zb_album_id)
    context = {'content': content,'xiao':'xiao'}
    return render(request, 'xmly/album.html', context)



