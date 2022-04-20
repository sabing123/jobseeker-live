import csv

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .models import *

from .form import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse

from django.db.models import Count

from django.templatetags.static import static


# Create your views here.

# login and register

def error404(request):
    context = {}
    return render(request, 'findingJob/404.html', context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = form.cleaned_data.get('groups')
            for g in group:
                print(g.name)
                g.user_set.add(user)
                user.save()

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'findingJob/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('jobPost')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'findingJob/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    countingCat = jobdetail.objects.values('jobcategory', 'jobcategory__name', 'jobcategory__category_logo').annotate(
        Count('jobcategory'))

    jobSearch = jobdetail.objects.all()

    page = Paginator(jobSearch, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {'page': page, 'countingCat': countingCat}
    return render(request, 'findingJob/home.html', context)


def jobList(request):


    jobListinaprt = jobdetail.objects.filter(type='Part Time')
    jobListinfull = jobdetail.objects.filter(type='Full Time')
    context = {'jobListinfull': jobListinfull, 'jobListinaprt': jobListinaprt,}
    return render(request, 'findingJob/job-list.html', context)


def jobDetail(request, jobid):
    jobinfo = jobdetail.objects.filter(id=jobid)
    context = {'jobinfo': jobinfo[0]}
    return render(request, 'findingJob/job-detail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def jobPost(request):
    formset = JobdetailForm()

    if request.method == "POST":
        formset = JobdetailForm(request.POST or None, request.FILES or None)

        if formset.is_valid():
            obj = formset.save(commit=False)
            obj.user = request.user
            obj.save()
            formset = JobdetailForm()

            # post_jobForm = post_jobForm.save(commit=False)
            # post_jobForm.user = request.user
            # post_jobForm.save()

            messages.success(request, 'Successfully! Posted Job.')

            return redirect('/jobPost')
        else:
            # messages.error(request, 'Invalid form submission.')
            messages.error(request, formset.non_field_errors())

    context = {'formset': formset}
    return render(request, 'findingJob/job-posting.html', context)


@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def jobpostedListedperuser(request):
    postedjob = request.user.jobdetail_set.all()
    context = {'postedjob': postedjob}
    return render(request, 'findingJob/jobpostedListedperuser.html', context)


@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def deletejobDetail(request, pk):
    delete_jobDetail = jobdetail.objects.get(id=pk)
    print(delete_jobDetail)
    if request.method == "POST":
        delete_jobDetail.delete()
        return redirect('/jobpostedListedperuser')

    context = {'item': delete_jobDetail}

    return render(request, 'findingJob/jobpostedListedperuser.html', context)


@login_required(login_url='login')
@allowed_users(allowed_role=['admin'])
def updatejobDetail(request, pk):
    job = jobdetail.objects.get(id=pk)
    formset = JobdetailForm(instance=job)

    if request.method == 'POST':
        formset = JobdetailForm(request.POST or None, request.FILES or None, instance=job)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Successfully! Updated Job Details.')

            return redirect('/jobpostedListedperuser')

    context = {'formset': formset}
    return render(request, 'findingJob/job-posting.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
        name: {}
        New Message: {}
        
        From: {}
        '''.format(data['name'], data['message'], data['email'])

        email = EmailMessage(data['subject'], message, '', ['gsabin696@gmail.com'])

        email.send()
        messages.success(request, 'Thank you submitting the form. we will be in touch soon')
        return redirect('contact')

    return render(request, 'findingJob/contact.html')


def about(request):
    context = {}
    return render(request, 'findingJob/about.html', context)

def termandcondition(request):
    context = {}
    return render(request, 'findingJob/termandcondition.html', context)

def PrivacyPolicy(request):
    context = {}
    return render(request, 'findingJob/PrivacyPolicy.html', context)

def Cookies(request):
    context = {}
    return render(request, 'findingJob/cookies.html', context)
