#Keshav made file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def analyse(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlinerm=request.GET.get('newlinerm','off')
    charcount=request.GET.get('charcount','off')
    spacerm=request.GET.get('spacerm','off')
    punctuations='''!()-{}#[];'":@$%^&*.,_~`/'''
    analyzed=''
    count=0
    if removepunc=='on':
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
                

    elif fullcaps=='on':
        analyzed=djtext.upper()
        params={'purpose':'Capitalised your data','analyzed_text':analyzed}       

    elif newlinerm=='on':
        for char in djtext:
            if char!=' ':
                analyzed=analyzed+char
        params={'purpose':'Removed new lines','analyzed_text':analyzed}
        
    elif charcount=='on':
        for i in range(0,len(djtext)):
            if djtext[i]!=' ':
                count=count+1
                analyzed=count
        params={'purpose':'Number of characters','analyzed_text':analyzed}
        
                
    elif spacerm=='on':
        for char in djtext:
            if char!='':
                analyzed=analyzed+char
        params={'purpose':'Removed extra spaces','analyzed_text':analyzed}
            # elif removepunc=='on' and fullcaps=='on':
    #     for char in djtext:
    #         if char not in punctuations:
    #             cha=cha+char
    #             analyzed=cha.upper
    else:
        analyzed=djtext
        params={'purpose':'No task selected',"analyzed_text":analyzed}
    return render(request,'analyze2.html',params)
