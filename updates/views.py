# Create your views here.

from django.views.generic import View
from restapi.mixins import JsonResponseMixin
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update





#def detail_view(request):
#	return render() # return JSON data  -> useful when working with javascript as frontend




def json_example_view(request):
	data = {
		'count' : 100,
		'content': "some content"
	}
	return JsonResponseMixin(data)

class JSONCBV(View):
	def get(self, request, *args ,**kwargs):
		data = {
			'count' : 200,
			'content' : "some more content"
		}
		return JsonResponse(data)


class JSONCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
			'count' : 300,
			'content' : "some more content"
		}
		json_data = json.dumps(data)
		return HttpResponse(json_data, content_type = 'application/json')

class SerializedView(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=1)
		data = {
			"user": obj.user.username,
			"content": obj.content
		}
		return self.render_to_json_response(data)


class SerializedListView(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		qs = Update.objects.all()
		data = serialize("json", qs, fields = ('user', 'content'))
		return HttpResponse(data, content_type = 'application/json')

class SerializedManagerView(View):
	def get(self,request, *args, **kwargs):
		qs = Update.objects.all()
		json_data = qs.serialize()
		return HttpResponse(json_data, content_type='application/json')
