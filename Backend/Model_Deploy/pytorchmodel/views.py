from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from Model.config import BertClassifier,predict_issue
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        MODEL = settings.GLOBAL_MODEL
        MODEL.eval()
        return Response(predict_issue(MODEL,request.data['complaint']), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        import json
        f = open(r"C:\Users\Saeem\Desktop\GitHub\Machine Learning Check\deploy\Model-Deploy\Backend\Model_Deploy\Model\non_iid.json")
        data = json.load(f)
        f.close()
        return Response(data, status=status.HTTP_200_OK)
    
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt 
def detail(request):
        print(request.POST.get("name"))
        # MODEL = settings.GLOBAL_MODEL
        # MODEL.eval()
        # text = ['pitch is low.','Display got a scratch','gave me damage box']
        # for t in text:  
        #         print(predict_issue(MODEL,t))
        return JsonResponse({'name':"Saeem",'Age':10,"Gender":"Male"})