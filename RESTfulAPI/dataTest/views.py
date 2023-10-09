from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Menu

from django.shortcuts import render, get_object_or_404, redirect
from .forms import MenuForm

@csrf_exempt
def menu_list(request):
    query_set = Menu.objects.all()
    context = {'menus': query_set}
    return render(request, 'dataTest/menu_list.html', context)
    
def menu_select(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    
    object = Menu.objects.get(pk=pk)
    if request.method == "GET":
        context = {'menu': menu}
        return render(request, 'dataTest/menu_detail.html', context)
    
    elif request.method == "DELETE":
        object.delete()
        return HttpResponse(status=204)
   

def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
        
    context = {'menu': menu, 'form' : form}
    return render(request, 'dataTest/menu_edit.html', context)


def menu_create(request):
    form = MenuForm()
    
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')  # 사용자 추가 후 목록 페이지로 리디렉션
    
    context = {'form': form}
    return render(request, 'dataTest/menu_create.html', context)
