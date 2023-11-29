from django.shortcuts import render,redirect
from myapp.models import categorysave,productsave
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from website.models import Profile,cart,delivaryuser,contsave,customerreview,codsave,razorpaydb


# Create your views here.
def indexrender(request):
    total_users = User.objects.count()
    total_pur_cod = codsave.objects.count()
    total_pur_rez = razorpaydb.objects.count()
    total_purchased = total_pur_cod+total_pur_rez
    return render(request,"index.html",{"total_users":total_users,"total_purchased":total_purchased})
def categoryform(request):
    return render(request,"categoryfill.html")
def categorystore(request):
    if request.method=="POST":
        name=request.POST.get('categoryname')
        description=request.POST.get('description')
        image=request.FILES['image']
        obj=categorysave(categoryname=name,description=description,categoryimage=image)
        obj.save()
        messages.success(request,"Data Saved Successfully")

    return redirect(categoryform)
def categorydisplay(request):
    data=categorysave.objects.all()
    return render(request,"categorydisplay.html",{"key":data})
def displayeditcategory(request,dataid):
    data=categorysave.objects.get(id=dataid)
    return render(request,"displayeditcategory.html",{"keye":data})
def categoryeditsave(request,dataid):
    if request.method=="POST":
        catename=request.POST.get('categoryname')
        des=request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            categorysave.objects.filter(id=dataid).update(categoryname=catename,categoryimage=file,description=des)

        except MultiValueDictKeyError:
            categorysave.objects.filter(id=dataid).update(categoryname=catename,description=des)
        messages.success(request, "Data Edited Successfully")

    return redirect(categorydisplay)
def deletecategory(request,dataid):
    fs=categorysave.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")

    return redirect(categorydisplay)
def productfill(request):
    data=categorysave.objects.all()
    return render(request,"productform.html",{"keye":data})
def prosave(request):
    if request.method=="POST":
        catname=request.POST.get('catename')
        proname=request.POST.get('productname')
        qunt=request.POST.get('quantity')
        price=request.POST.get('price')
        image=request.FILES['image']
        des=request.POST.get('description')
        obj=productsave(procategoryname=catname,productname=proname,proquantity=qunt,proprice=price,productimage=image, prodescription=des)
        obj.save()
        messages.success(request,"Data Saved Successfully")

        return redirect(productfill)

def productsaveshow(request):
    prodata=productsave.objects.all()
    return render(request,"productdisplay.html",{"key":prodata})
def productedit(request,dataid):
    db=categorysave.objects.all()
    data=productsave.objects.get(id=dataid)
    return render(request,"productedit.html",{"key":data,"kaya":db})
def producteditsave(request,dataid):
    if request.method == "POST":
        catname = request.POST.get('catename')
        proname = request.POST.get('productname')
        qunt = request.POST.get('quantity')
        price = request.POST.get('price')
        des = request.POST.get('description')
        try:
            image = request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
            productsave.objects.filter(id=dataid).update(procategoryname=catname,productname=proname,proquantity=qunt,proprice=price,productimage=file, prodescription=des)
        except MultiValueDictKeyError:
            productsave.objects.filter(id=dataid).update(procategoryname=catname,productname=proname,proquantity=qunt,proprice=price, prodescription=des)
        messages.success(request, "Data Edited Successfully")

    return redirect(productsaveshow)
def productdelete(request,dataid):
    data=productsave.objects.filter(id=dataid)
    data.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(productsaveshow)
def loginadmin(request):
    return render(request,"adminpass.html")
def loginathutication(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexrender)
            else:
                return redirect(loginadmin)
        return redirect(loginadmin)
def logoutadmin(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginadmin)


def newly_arrived_products(request):
    newly_arrived = productsave.objects.order_by('-created_date')[:10]  # Retrieve 10 most recent products
    return render(request, 'newly_arrived_products.html', {'newly_arrived': newly_arrived})



def profiledispaly(request):
    pro=Profile.objects.all()
    return render(request,"profiledis.html",{"keye":pro})
def deleteprofile(request,dataid):
    fs=Profile.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(profiledispaly)
def cartdispaly(request):
    pro=cart.objects.all()
    return render(request,"cartdis.html",{"keye":pro})
def cartdelete(request,dataid):
    fs=cart.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(cartdispaly)
def deliverydispaly(request):
    pro=delivaryuser.objects.all()
    return render(request,"deliverydis.html",{"keye":pro})
def editdelivery(request,dataid):
    data=delivaryuser.objects.get(id=dataid)
    return render(request,"editdelivery.html",{"keye":data})
def deliveryeditsave(request,dataid):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        mobilenumber = request.POST.get('mobilenumber')
        landmark = request.POST.get('landmark')
        twon_or_city = request.POST.get('twon_or_city')
        delivaryuser.objects.filter(id=dataid).update(fullname=fullname,mobilenumber=mobilenumber,landmark=landmark,twon_or_city=twon_or_city)
        messages.success(request, "Data Edited  Succssfully")

    return redirect(deliverydispaly)
def deletedeliveryuser(request,dataid):
    fs=delivaryuser.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(deliverydispaly)
def contactdispaly(request):
    pro=contsave.objects.all()
    return render(request,"contactdisplay.html",{"keye":pro})
def deletecontact(request,dataid):
    fs=contsave.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(contactdispaly)
def customerdispaly(request):
    pro=customerreview.objects.all()
    return render(request,"customerreview.html",{"keye":pro})
def deletecutomerreview(request,dataid):
    fs=customerreview.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(customerdispaly)
def coddispaly(request):
    pro=codsave.objects.all()
    return render(request,"codsave.html",{"keye":pro})
def deletecoddispaly(request,dataid):
    fs=codsave.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(customerdispaly)
def razorpaydisplay(request):
    pro=razorpaydb.objects.all()
    return render(request,"razorpaydis.html",{"keye":pro})
def deleterazorpay(request,dataid):
    fs=razorpaydb.objects.filter(id=dataid)
    fs.delete()
    messages.warning(request, "Data Deletd  Succssfully")
    return redirect(razorpaydisplay)




















