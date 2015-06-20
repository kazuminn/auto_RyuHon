# -*- coding: utf-8 -*-


# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context, Template

def home(request): 
    s = Context({"koto":"学籍番号とPassWordを登録するだけ"})
    return render_to_response("home.html",s)


def rule(request):
    return render_to_response("rule.html",{})
