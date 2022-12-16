from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from Model.config import BertClassifier,x


def detail(request):
        settings.GLOBAL_MODEL.eval()
        return JsonResponse({'foo':x})