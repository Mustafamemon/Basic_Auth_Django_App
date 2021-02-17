from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import logout

from django.views import View

from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .tokens import account_activation_token
from .models import User

import datetime
import dateutil.parser
import os

from io import BytesIO
from django.template.loader import get_template

from django.views.generic import View

def LoginRequired(request):
    return JsonResponse({'status':401,'message':'Please Login'},status=401)


def PasswordResetDoneView(request):
    return JsonResponse({'status':200,'message':"success"})


def Activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        password = getattr(user,'password') 
        print(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Activation link is Valid!')
        # return redirect('https://tms-student.tk/')
    else:
        return HttpResponse('Activation link is invalid!')


def GetCsrf(request):
    return JsonResponse({'csrfToken': get_token(request)}) 


def LogoutView(request,*args, **kwargs):
    logout(request,*args, **kwargs)
    return JsonResponse({'status':200,'message':'Successfully logout!'})


#CHANGE_PASSWORD
@method_decorator(login_required(None, login_url='/user-auth/login-required'),name='dispatch')
class ChangePassword(View):
    def post(self,request):
        form = PasswordChangeForm(request.user, request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print(user)
            update_session_auth_hash(request, user)  # Important!
            return JsonResponse({"status": 200, 'message':'Successfull Chnaged !'})
        else:
            error_list = list(form.errors.values())[0]
            error_string = ' '.join([' '.join(x for x in error_list)])
            return JsonResponse({"status": 400, 'message':error_string})
