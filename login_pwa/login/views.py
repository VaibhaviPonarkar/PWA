from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from webpush import send_user_notification
from .models import stock
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def base(request):
	return render(request=request, template_name="base.html")

def sign_up(request):
    form = UserCreationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('user_login')

    return render(request=request, template_name="sign_up.html", context={"form":form})


def user_login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            payload = {"head": "Welcome!", "body": "Hello World"}
            send_user_notification(user=user, payload=payload, ttl=1000)
            login(request, user)
            return render(request=request, template_name="home.html", context={"form":form})

        else:
            return render(request=request, template_name="login.html", context={"form":form})

    return render(request=request, template_name="login.html", context={"form":form})


def git_view(request):
    return render(request=request, template_name="githud.html")


def push_view(request):

    return render(request=request, template_name="push.html")


def stock_view(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['quantity']:
            post = stock()
            post.item = request.POST['name']
            post.qnt = request.POST['quantity']
            post.save()
                
            return render(request, 'stock_inster.html')  

    else:
        return render(request, 'stock_inster.html')


def stock_fetch(request):
    data = stock.objects.values()
 
    #post_list = serializers.serialize('json', list(data))

    return JsonResponse({'result': list(data)})


def stock_disp(request):
    return render(request, "stock_fetch.html")


def stock_update(request):
    if request.POST['item'] and request.POST['quantity']:
        stock.objects.filter(id=request.POST['item']).update(qnt=request.POST['quantity'])
        return render(request, 'stock_update.html')
    return render(request, 'stock_update.html')
