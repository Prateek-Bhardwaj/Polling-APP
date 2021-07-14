from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Poll, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    polls = Poll.objects.all().order_by('-id')
    content = {'polls':polls}
    return render(request, 'home.html', content)

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        user = request.user
        question = request.POST.get('question')
        option_one = request.POST.get('option1')
        option_two = request.POST.get('option2')
        poll = Poll(user=user, question=question,option_one=option_one, option_two=option_two)
        poll.save()
        return redirect('home')
    return render(request, 'create.html')

@login_required(login_url='login')
def results(request, id):
    poll = Poll.objects.get(id=id)
    content = {'poll':poll}
    return render(request, 'results.html', content)

@login_required(login_url='login')
def vote(request, id):
    polls = Poll.objects.get(id=id)
    # polls.delete()
    if request.method == 'POST':
        option = request.POST.get('poll')
        if option == 'option1':
            polls.option_one_count +=1
        elif option ==  'option2':
            polls.option_two_count +=1
        else:
            return HttpResponse(400, 'Invalid Choice')
        polls.save()
        return redirect('results', polls.id)
    content = {'polls':polls}
    return render(request, 'vote.html', content)
@login_required(login_url='login')
def delete(request, id):
    poll = Poll.objects.get(id=id)
    poll.delete()
    return redirect('profile')

@login_required(login_url='login')
def profile(request):
    user = request.user
    polls = Poll.objects.filter(user=user)
    print(polls)
    content={'polls':polls}
    return render(request, 'profile.html', content)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            form.save()
            return redirect('login')
        else:
            print('error')
    context = {'form':form, 'messages':messages}
    return render(request, 'registration.html', context)

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Cridentials')

    return render(request, 'login.html')

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')