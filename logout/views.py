# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import logout

def logout_view(request):
        logout(request)
        return render_to_response("logout.html",{})
