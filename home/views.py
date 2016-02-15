from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
# Create your views here.
#-*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
import datetime

def hello(request):
	return HttpResponse('Здравствуй, Мир')

def main(request):
	return HttpResponse('This is main page')
def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	return render_to_response('hours_ahead.html',{'hour_offset': offset, 'next_time':dt})
