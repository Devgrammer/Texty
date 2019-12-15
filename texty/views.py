# #I have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return  HttpResponse("hello Abhinav")

# def about(request):
#     return  HttpResponse('''<b>Hey Its a Test</b> <br> <a href="https://www.google.com">Hello</a>''') 
    
# def home(request):
#     return HttpResponse("Hey It's your home..")

def index(request):
    return render(request, 'index.html')
    #  return HttpResponse("Home")
 

def analyze(request):
    htext = request.POST.get('text','default' )
    print(htext)
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('capital','off')
    print(removepunc)
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~''' 
        analyzed = "" 
        for char in htext:
            if char not in punctuations:
                analyzed = analyzed + char 

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed }

        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in htext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose':'Changed to Uppercase    ', 'analyzed_text': analyzed }

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

def removepunc(request):
    return HttpResponse("Remove Punctuation")