from django.shortcuts import render
from .forms import UserForm, BillForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Bill


# Create your views here.
def index(request):
    if request.user.is_authenticated and request.user.is_active:
        return HttpResponseRedirect('bills/general')
    errors = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('bills/general')
            else:
                errors = 'User %s is not active' % username
        else:
            errors = 'Incorrect username/password'
    return render(request, 'bills/index.html', {'errors': errors})


def register(request):
    registered = False
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        form = UserForm()
    return render(request, 'bills/register.html', {'form': form, 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def general(request):
    bills = Bill.objects.filter(user=request.user).order_by('fecha').order_by('insercion')
    for i, bill in enumerate(bills):
        bills[i].metodo = Bill.metodo_choices[bill.metodo]
        bills[i].fechahora = bill.fechahora.strftime('%Y-%m-%d %H:%M:%S')
        bills[i].insercion = bill.insercion.strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'bills/general.html', {'bills': bills})


@login_required
def add_bill(request):
    if request.method == 'POST':
        form = BillForm(data=request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            setattr(bill, 'user', request.user)
            bill.save()
            return HttpResponseRedirect(reverse('bills:general'))
    else:
        form = BillForm()
    return render(request, 'bills/add_bill.html', {'form': form, 'edit': False})


@login_required
def edit_bill(request, bill_id):
    if request.method == 'POST':
        form = BillForm(data=request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            setattr(bill, 'id', bill_id)
            setattr(bill, 'user', request.user)
            bill.save()
            return HttpResponseRedirect(reverse('bills:general'))
    else:
        bill_data = Bill.objects.filter(id=bill_id)[0]
        form = BillForm(instance=bill_data)
    return render(request, 'bills/add_bill.html', {'form': form, 'edit': True})


@login_required
def delete_bill(request, bill_id):
    if request.method == 'GET':
        bill_to_delete = Bill.objects.filter(id=bill_id)[0]
        bill_to_delete.delete()
        return JsonResponse({'is_deleted': True})
    else:
        return JsonResponse({'is_deleted': False})
