from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user,allowed_users,admin_only
from accounts.models import *
from .forms import *
from .models import *
from .filters import *
# Create your views here.

def home_page(request):
    context={}
    return render(request,'accounts/home_page.html',context)

def about_us(request):
    context={}
    return render(request,'accounts/about_us.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def profile_user(request):
    user=request.user.customer
    form=CustomerForm(instance=user)

    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'accounts/profile.html',context)


@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/accounts')
        else:
            messages.info(request,'Username/Password is Incorrect')
    context={}
    return render(request,'accounts/login_page.html',context)

@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Registration for ' +username+ ' Success')
            return redirect('/login')
    context={'form':form}
    return render(request,'accounts/register_page.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer','admin'])
def user_page(request):
    orders=request.user.customer.orders_set.all()

    total_orders=orders.count()
    orders_delevired=orders.filter(status='Delivered').count()
    orders_pending=orders.filter(status='Pending').count()

    print('ORDERS',orders)
    context={'orders':orders,'total_orders':total_orders,"orders_pending":orders_pending,'orders_delevired':orders_delevired}
    return render(request,'accounts/user_page.html',context)







@login_required(login_url='login')
@admin_only
def dashboard(request):
    orders=Orders.objects.all()
    customer=Customer.objects.all()
    total_orders=orders.count()
    orders_delevired=orders.filter(status='Delivered').count()
    orders_pending=orders.filter(status='Pending').count()
    context={'customer':customer,'orders':orders,'total_orders':total_orders,"orders_pending":orders_pending,'orders_delevired':orders_delevired}
    return render(request,'accounts/dashboard.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request,pk):
    customer=Customer.objects.get(id=pk)

    orders=customer.orders_set.all()
    total_order=orders.count()

    myFilter=OrdersFilter(request.GET,queryset=orders)

    orders=myFilter.qs

    context={'orders':orders,'customer':customer,'total_order':total_order,'myFilter':myFilter}
    return render(request,'accounts/customers.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request):
    forms=Orderform()
    if request.method=='POST':
        # print('posting data',request.POST)
        forms=Orderform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/accounts')

    context={'forms':forms}
    return render(request,'accounts/new_order.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request,pk):
    order=Orders.objects.get(id=pk)
    forms=Orderform(instance=order)
    if request.method=='POST':
        forms=Orderform(request.POST,instance=order)
        if forms.is_valid():
            forms.save()
            return redirect('/accounts')
    context={'forms':forms,'order':order}
    return render(request,'accounts/update_order.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request,pk):
    order=Orders.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/accounts')
    context={'item':order}
    return render(request,'accounts/delete.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_product(request):
    forms=ProductForm()
    if request.method=="POST":
        forms=ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/accounts/products')
    context={'forms':forms}
    return render(request,'accounts/add_products.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_product(request,pk):
    product=Product.objects.get(id=pk)
    forms=ProductForm(instance=product)
    if request.method=='POST':
        forms=ProductForm(request.POST,instance=product)
        if forms.is_valid():
            forms.save()
            return redirect('/accounts/products')
    context={'forms':forms,'product':product}
    return render(request,'accounts/add_products.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_product(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=='POST':
        product.delete()
        return redirect('/accounts/products')
    context={'item':product}
    return render(request,'accounts/delete_product.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def new_customers(request):
    forms=CustomerForm()
    if request.method=='POST':
        # print('posting data',request.POST)
        forms=CustomerForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/accounts')

    context={'forms':forms}
    return render(request,'accounts/new_customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_customer(request,pk):
    cust=Customer.objects.get(id=pk)
    if request.method=='POST':
        cust.delete()
        return redirect('/accounts')
    context={'item':cust}
    return render(request,'accounts/delete_customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_customer(request,pk):
    cust=Customer.objects.get(id=pk)
    forms=CustomerForm(instance=cust)
    if request.method=='POST':
        forms=CustomerForm(request.POST,instance=cust)
        if forms.is_valid():
            forms.save()
            return redirect('/accounts')
    context={'forms':forms,'cust':cust}
    return render(request,'accounts/update_customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def multiple_order(request,pk):
    cust=Customer.objects.get(id=pk)
    OrderFormSet=inlineformset_factory(Customer,Orders,fields=('product','status'),extra=10)
    formset=OrderFormSet(queryset=Orders.objects.none(),instance=cust)
    if request.method=='POST':
        formset=OrderFormSet(request.POST,instance=cust)
        if formset.is_valid():
            formset.save()
            return redirect('/accounts/customer/%s'%(cust.id))
    context={'formset':formset,'cust':cust}
    return render(request,'accounts/multiple_order.html',context)
