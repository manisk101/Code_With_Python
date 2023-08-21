from django.shortcuts import render
def index(request):

    return render(request,'index.html',)
def counter(request):
    word = request.POST['word']
    amount_of_word = len(word.split())

    return render(request,"counter.html",{'amount':amount_of_word})

# Create your views here.
