from django.shortcuts import render, redirect
from apps.user.models import User
import bcrypt

def index(request):
    return render(request, 'reg_login.html')

def register(request):
    if request.method == "POST":
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        this_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        
        request.session['userid'] = this_user.id
        
        print(this_user)
        print('user is registered and logged in')
        return redirect('movie/')


def login(request):
    if request.method == "POST":
        email = request.POST['email']

        user = User.objects.filter(email = email).first()
        
        if user and bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['userid'] = user.id
            print('user has logged in')
            return redirect('movie/')
    return redirect('/')





def logout(request):
    user_id = request.session.pop('userid', None)
    print('user is logged out') # user is no longer in session
    return redirect('/')