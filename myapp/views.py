from django.shortcuts import render, redirect
from .models import Product, Customer,Cart, OrderPlaced
from django.views import View
from .forms import CustomerRegistrationForm ,CustomerAddressForm
from django.contrib import messages
from django.db.models import Q 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def home(request):
    bottoms_wear = Product.objects.filter(category="BT")
    Tops_wear = Product.objects.filter(category="TW")
    print(bottoms_wear)
    return render(request,'myapp/home.html',{'BottomsWear':bottoms_wear,'TopsWear':Tops_wear})


class ProductView(View):
   def get(self,request,pk):
       product=Product.objects.get(id=pk)
       return render(request,'myapp/producdetail.html',{'product':product})
   

def Mobile(request, data=None):
    if data == None:
        mobiles=Product.objects.filter(category='M')
        print(mobiles)
    elif data == 'Redmi' or data=="Samsung":
        mobiles=Product.objects.filter(category='M').filter(Brand=data)
        print(mobiles)
    return render(request,"myapp/mobiles.html",{'mobiles':mobiles})


class CustomerRegistration(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'myapp/registration.html',{'form':form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !! Registered Successfully...')
            form.save()
        return render(request,'myapp/registration.html',{'form':form})
        

@method_decorator(login_required,name='dispatch')
class Profileview(View):
    def get(self,request):
        form=CustomerAddressForm()
        return render(request,'myapp/profile.html',{'form':form,'active':'btn-primary'})
    
    def post(self,request):
        form=CustomerAddressForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            reg=Customer(user=usr,name=name,locality=locality,city=city,zipcode=zipcode,state=state)    
            reg.save()
            messages.success(request,'Congratulations !! saved Successfully...')
        return render(request,'myapp/profile.html',{'form':form,'active':'btn-primary'})


def Address(request):
    my_address=Customer.objects.filter(user=request.user)
    return render(request,'myapp/address.html',{'address':my_address,'active':'btn-primary'})

@login_required
def addtocart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required
def ShowCart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        totalamount=0.0
        shipping_amount=70
        prices=[p for p in Cart.objects.all()]
        for p in prices:
            tempamount=p.product.discounted_price * p.quantity 
            amount+=tempamount
            totalamount+=amount
        totalamount=amount + shipping_amount
        return render(request,'myapp/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
    

def pluscart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)   &  Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        totalamount=0.0
        shipping_amount=70
        prices=[p for p in Cart.objects.all() if p.user == request.user]
        for p in prices:
            tempamount=p.product.discounted_price * p.quantity 
            amount+=tempamount
            totalamount+=amount

        totalamount=amount + shipping_amount

        data= {
            'quantity':c.quantity,
            'amount' : amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    

def minuscart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)   &  Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        totalamount=0.0
        shipping_amount=70
        prices=[p for p in Cart.objects.all() if p.user == request.user]
        for p in prices:
            tempamount=p.product.discounted_price * p.quantity 
            amount+=tempamount
            totalamount+=amount

        totalamount=amount + shipping_amount

        data= {
            'quantity':c.quantity,
            'amount' : amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    

def removecart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)   &  Q(user=request.user))
        c.delete()
        amount=0.0
        totalamount=0.0
        shipping_amount=70
        prices=[p for p in Cart.objects.all() if p.user == request.user]
        for p in prices:
            tempamount=p.product.discounted_price * p.quantity 
            amount+=tempamount
            totalamount+=amount

        totalamount=amount + shipping_amount

        data= {
            'quantity':c.quantity,
            'amount' : amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    
@login_required
def checkout(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_item=Cart.objects.filter(user=user)
    amount=0.0
    totalamount=0.0
    shipping_amount=70
    prices=[p for p in Cart.objects.all() if p.user == user]
    for p in prices:
        tempamount=p.product.discounted_price * p.quantity 
        amount+=tempamount
        totalamount+=amount
    totalamount=amount + shipping_amount
    return render(request,'myapp/checkout.html',{'add':add,'totalamount':totalamount,'cart':cart_item})

@login_required
def payment(request):
   user=request.user
   custid=request.GET.get('custid')
   print(custid)
   customer=Customer.objects.get(id=custid)
   cart=Cart.objects.filter(user=user)
   for c in cart:
       OrderPlaced(user=user,customer=customer, product=c.product, quantity=c.quantity ).save()
       c.delete()
   return redirect("orders")
