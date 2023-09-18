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
    
    elif request.method == "PUT":
        update_data = JSONParser().parse(request)
        serializer = userSerializer(object, data= update_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        object.delete()
        return HttpResponse(status=204)
    
    elif request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            context = {'user': user, 'form' : form}
            return render(request, 'dataTest/user_edit.html', context)
   

def user_edit(request, pk):
    user = get_object_or_404(Users, pk=pk)
    
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        
    context = {'user': user, 'form' : form}
    return render(request, 'dataTest/user_edit.html', context)
