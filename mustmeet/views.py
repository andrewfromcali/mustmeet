from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from google.appengine.ext import db

import facebook.djangofb as facebook

@facebook.require_login()
def main(request):
  list = request.facebook.users.getInfo(request.facebook.friends.get(), ['name','pic_square'])
  return render_to_response('main/main.html', {'list': list})
