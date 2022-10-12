from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from .models import video_content,Eat_better
from django.db.models import Q
from .custom_form import loginform,signupform
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request,'index.html')
# def videos(request):
#     return render(request,'Services.html')

def Signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context={}
        context['sign_up_form']=signupform()
        context['login_form']=loginform()
        return render(request,'Signup.html',context)

@login_required(login_url='Login_signup')
def play(request, video_id):
    fetch_video=video_content.objects.filter(video_id=video_id)
    summary=fetch_video.values_list('video_summary')
    summary=summary[0][0].split('%')
    playing={'video_data':fetch_video,'summary':summary}
    return render(request,'play.html',playing)

@login_required(login_url='Login_signup')
def view_recipe(request,recipe_id):
    fetch_recpie=Eat_better.objects.filter(recipe_id=recipe_id)
    ingredient=fetch_recpie.values_list('recipe_ingredients')
    prep_steps=fetch_recpie.values_list('recipe_steps')
    ingredientlist=ingredient[0][0].split(',')
    prep_steps=prep_steps[0][0].split(',')
    recipe_data={'fetch_recpie':fetch_recpie,'ingredientlist':ingredientlist,'prep_steps':prep_steps}
    return render(request,'Recipe.html',recipe_data)


def Eatbetter(request):
    recipe_data=Eat_better.objects.all()
    # category_names=Eat_better.objects.order_by().values_list('video_category').distinct()
    # category_names=category_names.values_list()
    context={'recipe_data': recipe_data}
    return render(request, 'Eatbetter.html',context)



def videos(request):
    v_data=video_content.objects.all()
    category_names=video_content.objects.order_by().values_list('video_category').distinct()
    category_names=category_names.values_list()
    context={'v_data': v_data,'cat_name':category_names,'lenght':range(len(category_names))}
    return render(request, 'Services.html',context)

def about(request):
    return render(request,'about.html')


####Filter Request

def filter_video(request):
    if request.method=='POST':
        filter=request.POST.get("filter")
        search=request.POST.get("search_input")
        if search=="" or search is None:
            if filter is None or filter=="None":
                v_data=video_content.objects.all()
            # v_data=video_content.objects.filter(Q(video_category=filter)| Q(video_category__contains=search)|Q(video_title__contains=search)|Q(w_equipment__contains=search))
                context={'v_data': v_data,'search_value':'Search..','filtervalue':"All"}
                return render(request, 'Services.html',context)
            else:
                v_data=video_content.objects.filter(video_category__contains=filter)
                context={'v_data': v_data,'search_value':'Search..','filtervalue':filter}
                return render(request, 'Services.html',context)
        else:
            if filter is None or filter=="None":
                v_data=video_content.objects.filter(Q(video_category__contains=search)|Q(video_title__contains=search)|Q(w_equipment__contains=search))
                context={'v_data': v_data,'search_value':search,'filtervalue':filter}
                return render(request, 'Services.html',context)
            else:
                v_data=video_content.objects.filter(Q(video_category__contains=filter),Q(video_category__contains=search)|Q(video_title__contains=search)|Q(w_equipment__contains=search))
                context={'v_data': v_data,'search_value':search,'filtervalue':filter}
                return render(request, 'Services.html',context)
        
####Register User
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context={'reload':True}
        if request.method=="POST":
            sign_up_form=signupform(request.POST)
            if sign_up_form.is_valid(): # All validation rules pass
                sign_up_form.save()
                user=sign_up_form.cleaned_data.get('username')
                messages.success(request,"User Created with username"+ user)
                return redirect('Login_signup')
            else:
                context['sign_up_form']=sign_up_form
        else:
            sign_up_form=signupform()
            context['sign_up_form']=sign_up_form
        return render(request,'Signup.html',context)


#####User Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context={}
        if request.method=='POST':
            login_form=loginform(request=request, data=request.POST)
            if login_form.is_valid():
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
            else:
                context['login_form']=login_form
        else:
            login_form=loginform()
            context['login_form']=login_form
        return render(request,'Signup.html',context)


##  Logout
def user_logout(request):
    logout(request)
    return redirect('Login_signup')


def filter_recipe(request):
    if request.method=='POST':
        filter=request.POST.get("filter")
        search=request.POST.get("search_input")
        if search=="" or search is None:
            if filter is None or filter=="None":
                recipe_data=Eat_better.objects.all()
                context={'recipe_data': recipe_data,'search_value':'Search..','filtervalue':filter}
                return render(request, 'Eatbetter.html',context) 
            else:
                recipe_data=Eat_better.objects.filter(recipe_category__contains=filter) 
                context={'recipe_data': recipe_data,'search_value':search,'filtervalue':filter}
                return render(request, 'Eatbetter.html',context) 
        else:
            if filter is None or filter=="None":
                recipe_data=Eat_better.objects.filter(Q(recipe_category__contains=search)|Q(recipe_title__contains=search)|Q(recipe_ingredients__contains=search))
                context={'recipe_data': recipe_data,'search_value':search,'filtervalue':filter}
                return render(request, 'Eatbetter.html',context) 
            else:
                recipe_data=Eat_better.objects.filter(Q(recipe_category__contains=filter),Q(recipe_category__contains=search)|Q(recipe_title__contains=search)|Q(recipe_ingredients__contains=search))
                context={'recipe_data': recipe_data,'search_value':search,'filtervalue':filter}
                return render(request, 'Eatbetter.html',context) 
