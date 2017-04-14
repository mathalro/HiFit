from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


def home(request):
	return render(request, 'base.html',{})


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return redirect("/")
		else:
			messages.warning(request, "Usuário e/ou senha incorretos. ")
			return redirect('/login')

	return render(request, 'login.html',{})


def logout(request):
	auth_logout(request)
	return redirect('/login')
