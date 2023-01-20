from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Forests

# Create your views here.
def users(req):
    u = User.objects.all()
    data = dict()
    for u in User.objects.all():
        data[u.username] ={
            # 'id':u.id,
            'username':u.username,
            'email':u.email,
        }
    return JsonResponse(data)

def all_forest(req):
    forest = Forests.objects.all()
    
    return render(req,'api/showforest.html',{'forest':forest})


