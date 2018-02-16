# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Placeholder to later display all the list of blogs via HttpResponse"
	return HttpResponse(response)

def new(request):
	response = "Placeholder to display new form to create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def display(request, id):
	response = "placeholder to display blog " + id
	return HttpResponse(response)

def edit(request, id):
	response = "placeholder to edit blog " + id
	return HttpResponse(response)

def delete(request, id):
	response = "placeholder to delete blog " + id
	return HttpResponse(response)		
# Create your views here.
