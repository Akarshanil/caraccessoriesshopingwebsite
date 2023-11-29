from django.urls import path
from website import views
from website.views import WebLogin,savecontact



urlpatterns=[
    path('indexweb/',views.indexweb,name="indexweb"),
    path('customerreview/', views.customerreview, name="customerreview"),
    path('productdisplay/<catg>/', views.productdisplay, name="productdisplay"),
    path('singlepro/<int:dataid>/', views.singlepro, name="singlepro"),
    # path('login/', views.login, name="login"),
    path('WebLogin/', WebLogin.as_view(), name="log"),
    path('loginweb/', views.loginweb, name="loginweb"),
    path('forgetpassweb/', views.forgetpassweb, name="forgetpassweb"),
    path('forgotpaa/', views.forgotpassword, name="forgotpassword"),
    path('change_password/<token>/', views.change_password, name="change_password"),
    path('searchpage/', views.searchpage, name="searchpage"),
    path('product-list', views.productlistajax, name="productlistajax"),
    path('filter_by_price/', views.filter_by_price, name='filter_by_price'),
    path('addtcart/', views.addtcart, name="addtcart"),
    path('procartdetailes/<int:productid>/', views.procartdetailes, name="procartdetailes"),
    path('delcart/<int:delcartid>/', views.delcart, name="delcart"),
    path('checkout/<int:cartid>/', views.checkout, name="checkout"),
    path('savecheckdetailes/<int:productid>/<int:cartid>/', views.savecheckdetailes, name="savecheckdetailes"),
    path('contactweb/', views.contactweb, name="contactweb"),
    path('savecontact/', savecontact.as_view(), name="savecontact"),
    path('customerreviewsave/', views.customerreviewsave, name="customerreviewsave"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    # path('paymentrun/', views.paymentrun, name="paymentrun"),
    path('cashondelivery/<int:productid>/<desired_fullname>/<int:cartid>/', views.cashondelivery, name="cashondelivery"),
    path('proceed-to-pay/<int:cartid>/', views.razropaycheck, name="razropaycheck"),
    path('razorpaysave/<int:productid>/<str:fullname>/<int:carid>/', views.razorpaysave,name="razorpaysave"),

]