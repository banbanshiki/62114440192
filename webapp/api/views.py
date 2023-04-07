from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from rest_framework import generics
from .serializers import UserSerializer
from .serializers import ForestSerializer
from .models import Forest
from rest_framework.decorators import api_view
from .models import TentData,ZipoData,JacketData,MapData,CookData,LEDData,SleepData,EqipanoData,BackData,BootData,KnifeData
from .models import BookfoData,SLData,ToiletData,PortalData,CookingData,FirstaidData
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.middleware.csrf import get_token
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_superuser:
#             login(request, user)
#             next_page = request.GET.get('next')
#             if next_page:
#                 return redirect(next_page)
#             return redirect(reverse('admin:index'))
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'admin/login.html', {'form': AuthenticationForm()})

# @csrf_exempt
# def get_csrf_token(request):
#     token = get_token(request)
#     response = JsonResponse({'csrftoken': token})
#     response['X-CSRFToken'] = token
#     return response

def users(request):
    u = User.objects.all()
    data = dict()
    for u in User.objects.all():
        data[u.username] ={
            # 'id':u.id,
            'username':u.username,
            'email':u.email,
        }
    return JsonResponse(data)

@api_view(['POST'])
def tent_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        TentData.objects.create(type=type, content=content)
    return Response({'status': 'tent_save_success'})

@api_view(['POST'])
def zipo_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        ZipoData.objects.create(type=type, content=content)
    return Response({'status': 'zipo_save_success'})

@api_view(['POST'])
def jacket_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        JacketData.objects.create(type=type, content=content)
    return Response({'status': 'jacket_save_success'})

@api_view(['POST'])
def map_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        MapData.objects.create(type=type, content=content)
    return Response({'status': 'map_save_success'})

@api_view(['POST'])
def cook_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        CookData.objects.create(type=type, content=content)
    return Response({'status': 'cook_save_success'})

@api_view(['POST'])
def LED_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        LEDData.objects.create(type=type, content=content)
    return Response({'status': 'LED_save_success'})

@api_view(['POST'])
def sleep_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        SleepData.objects.create(type=type, content=content)
    return Response({'status': 'sleep_save_success'})

@api_view(['POST'])
def eqipano_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        EqipanoData.objects.create(type=type, content=content)
    return Response({'status': 'eqipano_save_success'})

@api_view(['POST'])
def back_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        BackData.objects.create(type=type, content=content)
    return Response({'status': 'back_save_success'})

@api_view(['POST'])
def boot_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        BootData.objects.create(type=type, content=content)
    return Response({'status': 'boot_save_success'})

@api_view(['POST'])
def knife_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        KnifeData.objects.create(type=type, content=content)
    return Response({'status': 'knife_save_success'})

@api_view(['POST'])
def bookfo_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        BookfoData.objects.create(type=type, content=content)
    return Response({'status': 'bookfo_save_success'})

@api_view(['POST'])
def sl_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        SLData.objects.create(type=type, content=content)
    return Response({'status': 'sl_save_success'})

@api_view(['POST'])
def toilet_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        ToiletData.objects.create(type=type, content=content)
    return Response({'status': 'toilet_save_success'})

@api_view(['POST'])
def portal_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        PortalData.objects.create(type=type, content=content)
    return Response({'status': 'portal_save_success'})

@api_view(['POST'])
def cooking_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        CookingData.objects.create(type=type, content=content)
    return Response({'status': 'cooking_save_success'})

@api_view(['POST'])
def firstaid_data(request):
    data = request.data.get('data')
    for item in data:
        type = item['type']
        content = item['content']
        FirstaidData.objects.create(type=type, content=content)
    return Response({'status': 'firstaid_save_success'})


@ensure_csrf_cookie
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrftoken': token})


class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            user = User.objects.create_user(username=username, password=password , email=email)
            print(user)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                data = serializer.data
                data['token'] = token.key
                headers = {
                    'Authorization': f'Token {token.key}'
                }
                    
                return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
       

class UserLogin(APIView):
    def post(self, request, format='json'):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                data = {
                    "message": "Login successful",
                    "loggedIn": True,
                    "user": {"id": user.id, "username": user.username},
                    'token': token.key
                }
                return Response(data , status=status.HTTP_200_OK)
            else:
                return Response({"message": "User is not active"})
        else:
            return Response({"message": "Login failed User"})
       

           
class UserLogout(APIView):
    def post(self, request, format='json'):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)   

class ForestList(generics.ListCreateAPIView):
    queryset = Forest.objects.all()
    serializer_class = ForestSerializer        

class DiaryEntryList(generics.ListCreateAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return DiaryEntry.objects.filter(user=user)

class DiaryEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer
    permission_classes = [IsAuthenticated]

