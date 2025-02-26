from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from login_system.models import UserProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer

# Create your views here.
def home(request):
    return render(request, 'login.html', {})


# Create api for user profile
@api_view(['GET'])
def search_users(request):
    query = request.GET.get('query', '')
    # if query:
    #     users = User.objects.filter(username_icontains=query)
        
    # else:
    users = UserProfile.objects.all()
        
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
    

