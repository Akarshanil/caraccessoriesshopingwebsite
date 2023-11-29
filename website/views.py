from myapp.models import categorysave,productsave
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm,ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
import uuid
from .models import Profile,contsave,customerreview,codsave,razorpaydb
from django.core.exceptions import ObjectDoesNotExist
from .helpers import send_forget_password_mail
from django.http import JsonResponse
from django.core import serializers
from .models import cart,delivaryuser
# Create your views here.
def indexweb(request):
    cat=customerreview.objects.order_by('-id')
    premiumproduct=productsave.objects.order_by('-proprice')[:2]
    newly_arrived = productsave.objects.order_by('-created_date')[:10]  # Retrieve 10 most recent products
    data=categorysave.objects.all()
    return render(request,"indexweb.html",{"key":data,"kaya":newly_arrived,"pre":premiumproduct,"cat":cat})

def productdisplay(request,catg):
    kyyy=categorysave.objects.all()
    cate=catg
    data=productsave.objects.filter(procategoryname=catg)
    return render(request,"productpage.html",{"key":data,"cat":kyyy,"cate":cate})
def singlepro(request,dataid):
    cat=categorysave.objects.all()
    obj=productsave.objects.get(id=dataid)
    return render(request,"singleproduct.html",{"key":obj,'cat':cat})
# def login(req):
#     return render(req,'login.html')
#
class WebLogin(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'login.html'  # Replace with your custom HTML form template path
    success_url = reverse_lazy('log')  # Redirect to login page upon successful registration

    def form_valid(self, form):
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the form data to the database
            return super().form_valid(form)  # Call the parent class's form_valid() method
        return self.form_invalid(form)  # If the form data is not valid, call form_invalid() method
def loginweb(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['username'] = username
            return redirect(indexweb)
        else:
            return redirect('log')
    return redirect('log')
def change_password(request,token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forget_password_token=token).first()
        context = {"user_id":profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('password1')
            confirm_password = request.POST.get('password1')
            user_id = request.POST.get('user_id')
            print(user_id)
            if user_id is None:
                messages.success(request,'no user id fond.')
                return redirect(change_password,token)
            if new_password != confirm_password:
                messages.success(request,'both should be equal')
                return redirect(change_password,token)
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('log')
    except Exception as e:
        print(e)
    return render(request,"changepassword.html",context)
def forgetpassweb(request):
    return render(request,"Forgotpas.html")

def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user_obj = User.objects.filter(username=username).first()

        if not user_obj:
            return redirect('log')

        token = str(uuid.uuid4())

        try:
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
        except ObjectDoesNotExist:
            # If no profile exists, create one and set the forget_password_token
            profile_obj = Profile.objects.create(user=user_obj, forget_password_token=token)
            send_forget_password_mail(user_obj.email, token)

        return redirect('log')

    return redirect(forgetpassweb)
def searchpage(request):
    if request.method=="POST":
        searchterm=request.POST.get("search")
        if searchterm is None:
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=productsave.objects.filter(productname=searchterm).first()

            if product:
                return redirect(singlepro,product.id)
            else:
                messages.error(request,"No Product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))
def productlistajax(request):
    product_names = productsave.objects.values_list('productname', flat=True)
    productlist = list(product_names)

    return JsonResponse(productlist, safe=False)

def filter_by_price(request):
    min_price = int(request.GET.get('min_price', 0))
    max_price = int(request.GET.get('max_price', 1000))
    catg= (request.GET.get('catg'))

    filtered_products = productsave.objects.filter(proprice__range=(min_price, max_price),procategoryname=catg).order_by('-proprice')
    serialized_products = serializers.serialize('json', filtered_products)

    return JsonResponse({'filtered_products': serialized_products}, safe=False)
def addtcart(request):
    cat=categorysave.objects.all()
    car =cart.objects.filter(user=request.user)
    return render(request,"addtocart.html",{"car":car,"cat":cat})
def procartdetailes(request,productid):
    product=get_object_or_404(productsave,id=productid)

    if request.method=="POST":
        p=int(request.POST.get('totalprice'))
        qunt=int(request.POST.get('quantity', 1))
        price=request.POST.get('total_price')
        try:
            price = int(price)
        except ValueError:
            print("ValueError: Could not convert 'price' to an integer")
            price = p  # Handle the case where total_price is not a valid integer

        cart_item, created = cart.objects.get_or_create(user=request.user, product=product)
        if created:
            cart_item.quantity = qunt
            cart_item.total_price=price

        else:
            cart_item.quantity += qunt
            cart_item.total_price +=price
        cart_item.save()

        return redirect('addtcart')  # Redirect to the cart page
    return redirect(singlepro, productid)
def delcart(request,delcartid):
    remcart=cart.objects.filter(id=delcartid)
    remcart.delete()
    return redirect(addtcart)
def checkout(request,cartid):
    cat=categorysave.objects.all()
    chectcart=cart.objects.filter(id=cartid)

    return render(request,"checkout.html",{'chectcart':chectcart,'cat':cat})
def savecheckdetailes(request,productid,cartid):
    product=get_object_or_404(productsave,id=productid)
    user=request.user
    cat=categorysave.objects.all()
    chectcart = cart.objects.filter(id=cartid)  # Fetch the cart items

    if request.method=="POST":
        fullname=request.POST.get('name')
        mobilenumber=request.POST.get('mobilenumber')
        address=request.POST.get('Address')
        request.session['mobilenumber'] = mobilenumber
        request.session['fullname'] = fullname
        request.session['Address'] = address
        address=request.POST.get('Address')
        town=request.POST.get('twon')
        obj=delivaryuser(user=user,product=product,fullname=fullname,mobilenumber=mobilenumber,landmark=address,twon_or_city=town)
        obj.save()
        form_submitted = True  # Set the flag to True
        messages.success(request, "Now Please Proceed The Payement")
        return render(request, "checkout.html", {'chectcart': chectcart, 'cat': cat, 'form_submitted': form_submitted})


def contactweb(request):
    cat=categorysave.objects.all()
    return  render(request,"contact.html",{"cat":cat})
class savecontact(CreateView):
    model = contsave
    form_class = ContactForm  # Use the appropriate form class here
    template_name = 'contact.html'  # Replace with your custom HTML form template path
    success_url = reverse_lazy('contactweb')  # Redirect to login page upon successful registration

    def form_valid(self, form):
        # You can add custom logic here before saving the form
        messages.success(self.request, 'data is saved')
        return super().form_valid(form)
def customerreviewsave(request):
    if request.method == "POST":
        n=request.POST.get('Name')
        discription=request.POST.get('Message')
        obj=customerreview(name=n,discription=discription)
        obj.save()
        messages.success(request, 'Saved')
        return redirect(indexweb)
def aboutpage(request):
    ct=categorysave.objects.all()
    cat=customerreview.objects.order_by('-id')
    return render(request,"about.html",{"cat":cat,"ct":ct})
def paymentrun(request):
    return render(request,"payment.html")
def cashondelivery(request,productid,desired_fullname,cartid):
    threshold_score = 5
    product = delivaryuser.objects.filter(product=productid,fullname=desired_fullname).first()
    codsave.objects.create(deluser=product, mode_of_payment='COD')
    cod_order = codsave.objects.filter(deluser=product)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
    print(cod_order)
    product_instance = cod_order.first().deluser.product
    print(product_instance)
    product_instance.popularity_score=+1
    product_instance.save()
    trending_products = productsave.objects.filter(popularity_score__gte=threshold_score)
    trending_products.update(is_trending=True)
    print(cod_order)
    messages.success(request,"Order is successfull")
    return redirect(checkout,cartid)

def razropaycheck(request,cartid):
        try:
            cart_item = cart.objects.get(id=cartid)
            totalprice = cart_item.total_price
            return JsonResponse({'totalprice': totalprice})
        except cart.DoesNotExist:
            return JsonResponse({'error': 'Cart not found'}, status=404)
def razorpaysave(request,productid,fullname,carid):             #fullname=user
    threshold_score = 5
    product = delivaryuser.objects.filter(product=productid,user=fullname).order_by('-id').first()
    modepayment=request.POST.get('payment_mode')
    paymentid=request.POST.get('payment_id')
    razorpaydb.objects.create(deluserrazorpay=product, mode_of_paymentrazorpay=modepayment,paymentid=paymentid)
    cod_order = razorpaydb.objects.filter(deluserrazorpay=product)
    print("llllll")
    print(cod_order)
    product_instance = cod_order.first().deluserrazorpay.product
    print(product_instance)
    product_instance.popularity_score = +1
    product_instance.save()
    trending_products = productsave.objects.filter(popularity_score__gte=threshold_score)
    trending_products.update(is_trending=True)
    print(cod_order)
    return JsonResponse({'status': 'Payment and order are successful'}, status=200)






















