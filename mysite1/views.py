# This is created by me --> Twoha
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # get the chechbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # analyze the text with select checkbox
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Total Characters ', 'analyzed_text': analyzed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error,please selected any opearation and try again!!")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# def removepunc(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # analyze the text
#     return HttpResponse('Remove punc <br> <a href="/">Back To Home</a>')

# def capfirst(request):
#     return HttpResponse('capitalize first <br> <a href="/">Back To Home</a>')

# def newlineremove(request):
#     return HttpResponse('newline remove <br> <a href="/">Back To Home</a>')

# def spaceremove(request):
#     return HttpResponse('space remover <br> <a href="/">Back To Home</a>')

# def charcount(request):
#     return HttpResponse('character count <br> <a href="/">Back To Home</a>')
