from django.shortcuts import render,HttpResponse
import os
import openai
def imagegen(b):
        openai.api_key = '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' # your api key
        openai.Model.list()
        c=openai.Image.create(
            prompt=b,
            n=2,
            size="1024x1024")
        return c.data

def index(request):
    url1=str()
    url2=str()
    check = False
    valid = str()
    if request.method == "POST":
        b = request.POST['topic']
        print(b)
        try:
            c = imagegen(b)
            c1 = dict(c[0])
            c2 = dict(c[1])
            url1 = c1['url']
            url2 = c2['url']
            print(url2)
            check = True
        except:
            valid = "Can't display your request for Safety Reason"
    else:
        print("passed")
        pass
    return render(request,"index.html",{'url1':url1,'url2':url2,'check':check,'valid':valid})
