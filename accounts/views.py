from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import jobs, taken
from .forms import ContactForm
import datetime
# Create your views here.


def jp(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            if date < datetime.date.today():
                messages.info(request, "Minimum date is tomorrow")
                return redirect('jp')
        role = request.POST['jr']
        location = request.POST['loc']
        duration = request.POST['dur']
        count = request.POST['cou']
        pay = request.POST['pay']
        job = jobs(role=role, date=date, location=location, count=int(count), duration=int(duration), pay=int(pay), farmer=request.user.username)
        job.save()
        return render(request, 'flogin.html')
    else:
        return render(request, 'job.html', {'form': form})


def jps(request):
    take = taken.objects.all()
    name = request.user.username
    return render(request, 'jps.html', {'take': take, 'name1': name})


def aj(request):
    form = ContactForm()
    alljobs = jobs.objects.all()
    date = datetime.date.today()
    if request.method == 'POST':
        id1 = request.POST['ji']
        role = request.POST['jr']
        farmer = request.POST['pb']
        cno = request.POST['cno']
        name = request.user.first_name+' '+request.user.last_name
        form = ContactForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            alltaken = taken.objects.all()
            for x in alltaken:
                if date == x.date and name == x.name:
                    messages.info(request, "You already have a job on this day")
                    return redirect('aj')
        take = taken(job_id=id1, date=date, role=role, name=name, cno=cno, farmer=farmer)
        take.save()
        job = jobs.objects.get(id=id1)
        job.count -= 1
        job.save()
        return render(request, 'elogin.html')
    else:
        return render(request, 'applyjob.html', {'alljobs': alljobs, 'date': date, 'form': form})


def ajs(request):
    name = request.user.first_name + ' ' + request.user.last_name
    take = taken.objects.all()
    alljobs = jobs.objects.all()
    return render(request, 'appliedjobs.html', {'alljobs': alljobs, 'take': take, 'name1':name})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_staff == True:
                return render(request, 'flogin.html')
            else:
                return render(request, 'elogin.html')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if 'ch1' in request.POST:
            f = True
        else:
            f = False
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name, is_staff=f )
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

