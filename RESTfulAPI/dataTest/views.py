from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from .serializer import userSerializer

from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserEditForm

@csrf_exempt
def user_list(request):
    query_set = Users.objects.all()
    context = {'users': query_set}
    return render(request, 'dataTest/user_list.html', context)
    
def user_select(request, pk):
    user = get_object_or_404(Users, pk=pk)
    
    object = Users.objects.get(pk=pk)
    if request.method == "GET":
        context = {'user': user}
        return render(request, 'dataTest/user_detail.html', context)
    
    elif request.method == "DELETE":
        object.delete()
        return HttpResponse(status=204)
   

def user_edit(request, pk):
    user = get_object_or_404(Users, pk=pk)
    
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        
    context = {'user': user, 'form' : form}
    return render(request, 'dataTest/user_edit.html', context)


def user_create(request):
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # 사용자 추가 후 목록 페이지로 리디렉션
    else:
        form = UserEditForm()
    
    context = {'form': form}
    return render(request, 'dataTest/user_create.html', context)
