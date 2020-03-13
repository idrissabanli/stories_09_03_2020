from django.shortcuts import render
import datetime

# Create your views here.
def index(request):

    return render(request , 'index.html' )

    # mystring = 'Teymur'
    # birthdate = datetime.datetime.now()
    # html = "<h1>Nebiyev</h1>"
    # a = [75,2,3,4,5,6]

    # context = {
    #     'name': mystring,
    #     'birthdate': birthdate,
    #     'html': html,
    #     'array': a,
    # }

    mypost = [
        {
            'title': 'Tasty & Delicious Foods1',
            'category': 'Dessert',
            'date': datetime.date(2017,3,3),
            'image': 'https://realfood.tesco.com/media/images/RFO-1400x919-classic-chocolate-mousse-69ef9c9c-5bfb-4750-80e1-31aafbd80821-0-1400x919.jpg'
        }, 
        {
            'title': 'Tasty & Delicious Foods2',
            'category': 'Dessert',
            'date': datetime.date(2017,3,3),
            'image': 'https://realfood.tesco.com/media/images/RFO-1400x919-classic-chocolate-mousse-69ef9c9c-5bfb-4750-80e1-31aafbd80821-0-1400x919.jpg'
        }, 
        {
            'title': 'Tasty & Delicious Foods3',
            'category': 'Dessert',
            'date': datetime.date(2017,3,3),
            'image': 'https://realfood.tesco.com/media/images/RFO-1400x919-classic-chocolate-mousse-69ef9c9c-5bfb-4750-80e1-31aafbd80821-0-1400x919.jpg'
        }, 
        {
            'title': 'Tasty & Delicious Foods4',
            'category': 'Dessert',
            'date': datetime.date(2017,3,3),
            'image': 'https://realfood.tesco.com/media/images/RFO-1400x919-classic-chocolate-mousse-69ef9c9c-5bfb-4750-80e1-31aafbd80821-0-1400x919.jpg'
        },
    ]

    context = {
        'posts': mypost
    }
    return render(request , 'index.html', context)


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