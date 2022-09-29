from django.shortcuts import render

# Create your views here.

#!indexView
def indexView(request):
    return render(request,'index.html',context={'text':'Hello World'})