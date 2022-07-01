from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from random import randrange

def home(request):
	if request.user.is_authenticated:
		return redirect("uwelcome")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		ur = authenticate(username=un, password=pw)
		if ur is not None:
			login(request, ur)
			return redirect("uwelcome")
		else:
			return render(request, "home.html", {"msg": "Invalid Login"})
	else:
		return render(request, "home.html")


def usignup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		try:
			ur = User.objects.get(username=un)
			return render(request, "signup.html", {"msg":"User already exists"})
		except User.DoesNotExist:
			text = "0123456789"
			pw = ""
			for i in range(4):
				pw = pw + text[randrange(len(text))]
			print(pw)
			ur = User.objects.create_user(username=un, password=pw)
			ur.save()
			send_mail("Password", "ur pw is " + str(pw), "abcd26june@gmail.com", [str(un)])
			return redirect("home")
	else:
		return render(request, "signup.html")	
	
def urnpassword(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			un = request.POST.get("un")
			try:
				ur = User.objects.get(username=un)
				text = "0123456789"
				pw = ""
				for i in range(4):
					pw = pw + text[randrange(len(text))]
				print(pw)
				ur.set_password(pw)
				ur.save()
				send_mail("Password", "ur new pw is" + str(pw), "abcd26june22@gmail.com", [str(un)])
				return redirect("home")
			except User.DoesNotExist:
				return render(request, "rnpassword.html", {"msg":"User does not exist"})
		else:
			return render(request, "rnpassword.html")
	else:
		return redirect("home")

def uwelcome(request):
	if request.user.is_authenticated:
		return render(request, "welcome.html")
	else:
		return redirect("home")
	

def ulogout(request):
	logout(request)
	return redirect("home")
