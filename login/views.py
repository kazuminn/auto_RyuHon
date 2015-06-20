# -*- coding: utf-8 -*-
# Create your views here.

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
#from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import Context, Template

def register(request):
    return render_to_response('register.html', {"koto":"登録画面"},
            context_instance=RequestContext(request))

def delete(request):
    return render_to_response('deletion.html', {"koto":"アカウント削除画面"},
            context_instance=RequestContext(request))



from django.template import Context, loader
import re



from django.contrib.auth.models import User

def create_user(request):
    user_id = request.POST['user_id'] #ユーザー任意の名前
    last_name = request.POST['last_name'] #password
    email = request.POST['email']  #学籍番号
    first_name = request.POST['first_name'] #repassword

    pattern = r"^e[0-9][0-9][0-9][0-9][0-9][0-9]$"
    if(user_id != ""):
	    if(None != re.match(pattern , email)):
		if(last_name != "" and first_name != "" and last_name == first_name):
	                        new_user = User.objects.create_user(user_id , email, last_name) 
				new_user.first_name = first_name
	                        new_user.save()
	                        s = Context({"kotoba":"登録ありがとうございました。"}) 


    				i = str(new_user.id)
				h = str(user_id)

				d =   h + '様　このメール本文を貼り付けて同じメールアドレスで返信してください' + i
				send_mail('django_test', d, 'e145702@ie.u-ryukyu.ac.jp', [email + '@eve.u-ryukyu.ac.jp'], fail_silently=False) ;
    				
				return render_to_response('thank.html',s,context_instance=RequestContext(request))
 		else:
			s = Context({"kotoba":"PassWordが一致しない、または、入力されていません。"})	
    			return render_to_response('register.html',s,context_instance=RequestContext(request))
	    else:
	        s = Context({"kotoba":"exxxxxxフォーマットの学籍番号を入力してください"})
    		return render_to_response('register.html',s,context_instance=RequestContext(request))
    else:
   	s = Context({"kotoba":"学績番号が未記入です。"})
    	return render_to_response('register.html',s,context_instance=RequestContext(request))




def deletion(request):
    user_id = request.POST['user_id']
    last_name = request.POST['last_name']

    try:
	di = User.objects.filter(username__exact=user_id)[0]	
	if(last_name != di.first_name):
		raise Exception('spam', 'eggs')
        di.delete()		
	s = Context({"kotoba":"アカウントを削除しました。"})
    except Exception as ints:
	s = Context({"kotoba":"passwordと学績番号が一致しません。"})
		

    return render_to_response('thank.html',s,context_instance=RequestContext(request))



