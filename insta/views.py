from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index (request):
    if request.method == 'POST':
        return redirect('home')

    else:   
        return render(request,'index.html')

def home(request):

    return render(request,'home.html')

def followers(request):

    return render(request,'followers.html')