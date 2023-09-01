from django.contrib import messages
from django.shortcuts import render, redirect
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyAJrtFpUhBv-3qlAu4TnJh8968_LpW6THs",
    "authDomain": "secondproject-f9874.firebaseapp.com",
    "databaseURL": "https://secondproject-f9874-default-rtdb.firebaseio.com",
    "projectId": "secondproject-f9874",
    "storageBucket": "secondproject-f9874.appspot.com",
    "messagingSenderId": "472768847903",
    "appId": "1:472768847903:web:2c7fef46f39df8f0a6f52a",
    "measurementId": "G-VH38JMQGXJ"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    try:
        if request.method == "POST":
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['confirm_password']
            if password1 != password2:
                messages.error(request, 'password does not match')
                return redirect('signup')
            user = auth.create_user_with_email_and_password(email, password1)
            user = auth.sign_in_with_email_and_password(email, password1)
            messages.success(request, 'Registration Successful!')
            return redirect('profile')
    except Exception as e:
        print(e)
        q = 'Insert something wrong'
        messages.error(request, q)
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            messages.success(request, "Successfully Logged In")
            return redirect("profile")
        except Exception as e:
            print(e)
            messages.error(request, "Invalid Credentials.")
            redirect('signin')
    return render(request, 'signin.html')


def reset_password(request):
    if request.method == "POST":
        email = request.POST['email']
        auth.send_password_reset_email(email)
    return render(request, 'reset_password.html')


def profile(request):
    user = auth.current_user
    print(1, user)
    return render(request, 'profile.html', {'user': user})


def logout(request):
    auth.current_user = None
    return redirect('index')
