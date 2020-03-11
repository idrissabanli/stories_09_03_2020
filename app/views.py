from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request , 'index.html' )

def about(request):
    return render(request , 'about.html' )

def contact(request):
    return render(request , 'contact.html' )
    
def create_story(request):
    return render(request, 'create_story.html' )

def recipes(request):
    return render(request, 'recipes.html')

def single(request):
    return render(request, 'single.html')

def stories(request):
    return render(request,'stories.html')           

def user_profile(request):
    return render(request,'user-profile.html')    

def email_subscribers(request):
    return render(request,'email-subscribers.html')    