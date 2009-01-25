from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from google.appengine.ext import db

import facebook.djangofb as facebook

@facebook.require_login()
def main(request):
  response = fbsession.users_getInfo(:uids => fbsession.friends_get.uid_list, 
                                       :fields => [:name, :pic_square])
  @list = response.user_list
  name = request.facebook.users.getInfo([request.facebook.uid], ['first_name'])[0]['first_name']
  return render_to_response('main/main.html', {'name': name})
