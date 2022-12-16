from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from Model.config import BertClassifier,x,predict_issue



def detail(request):
        # MODEL = settings.GLOBAL_MODEL
        # MODEL.eval()
        # text = ['pitch is low.','Display got a scratch','gave me damage box']
        # for t in text:  
        #         print(predict_issue(MODEL,t))
        return JsonResponse({'foo':x})