from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import SignupForm
# , ProfileForm
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from .token import make_token
from .models import Profile
import hashlib

def register(request):
	# karbar dokme sabt nam ra click karde ast
	if 'requestcode' in request.POST:
		if User.objects.filter(email=request.POST['email']).exists():
			messages.error(request, 'قبلا کاربری با این ایمیل ثبت نام \
			کرده است. اگر اون شخص شمایید از قسمت %s رمز ورود خود را \
			بازیابی کنید.' % '<a href="#">بازیابی پسورد</a>')
			return redirect('register')

		if not User.objects.filter(username=request.POST['username']).exists():
			email = request.POST['email']
			username = request.POST['username']
			password = request.POST['password']
			password2 = request.POST['password2']
			if password == password2:
				password = make_password(request.POST['password'])
				password2 = None
				user = User(
	            email=email, username=username, password=password)
				user.is_active = False
				user.save()
				token = make_token(username, email)
				userid = User.objects.get(email=request.POST['email']).id
				messages.success(request, "<a href=\"{}?token={}&id={}\">\
				لینک رو به رو</a>".format(request.build_absolute_uri\
				('/register/'), token, userid))
				return redirect('register')
			else:
				messages.success(request, "پسوردهای وارد شده با هم برابر نیست.")
				return redirect('register')

		else:
			messages.error(request, "یوزرنیم وارد شده تکراری می باشد. \
			لطفا یکی دیگه انتخاب کنید.")
			return redirect('register')

	# karbar email ersal shode ra click karde ast
	elif 'token' in request.GET and 'id' in request.GET:
		code = request.GET['token']
		userid = request.GET['id']
		thisuser = get_object_or_404(User, id=userid)
		token = make_token(thisuser.username, thisuser.email)
		if code == token and thisuser.is_active == False:
			thisuser.is_active = True
			thisuser.save()
			messages.success(request, 'ثبت نام شما با موفقیت انجام شد.')
			Profile.objects.get_or_create(user=request.user)
		elif code == token and thisuser.is_active == True:
			messages.warning(request, 'از این توکن قبلا استفاده شده است!\
			اگر پسورد خود را گم کرده اید از قسمت %s استفاده کنید.\
			' % '<a href="#">بازیابی پسورد</a>')
		else:
			messages.error(request, 'متاسفانه مشکلی پیش آمده است. لطفا \
			دوباره امتحان کنید.')
		auth_login(request, thisuser)
		return redirect('register')

	# karbar avalin bar ast be safhe register amade ast
	else:
		return render(request, 'register.html', {})
