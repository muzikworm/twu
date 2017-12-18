from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from task.serializers import UserSerializer, GroupSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

from .models import User

def view_user(request):
    posts = User.objects.order_by('name')
    return render(request, 'task/usertable.html', {'user':posts})
from django.shortcuts import redirect

from .forms import AddUserForm

def new_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            name = cleaned_data['name']
            email = cleaned_data['email']
            dob = cleaned_data['dob']
            aadhar = cleaned_data['aadhar']
            area = cleaned_data['area']
            amount = cleaned_data['amount']

            print('here')
            print(name+email+dob+aadhar)
            return redirect('users')
    else:
        form = AddUserForm()
    return render(request, 'task/adduser.html', {'form': AddUserForm},context_instance=RequestContext(request))
