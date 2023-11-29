from django.urls import path
from myapp import views



urlpatterns =[
    path('indexrender/',views.indexrender,name="indexrender"),
    path('categoryform/', views.categoryform, name="categoryform"),
    path('categorystore/', views.categorystore, name="categorystore"),
    path('categorydisplay/',views.categorydisplay,name="categorydisplay"),
    path('displayeditcategory/<int:dataid>/',views.displayeditcategory, name="displayeditcategory"),
    path('categoryeditsave/<int:dataid>/',views.categoryeditsave,name="categoryeditsave"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),
    path('productfill/', views.productfill, name="productfill"),
    path('prosave/', views.prosave, name="prosave"),
    path('productsaveshow/',views.productsaveshow, name="productsaveshow"),
    path('productedit/<int:dataid>/', views.productedit, name="productedit"),
    path('producteditsave/<int:dataid>/', views.producteditsave, name="producteditsave"),
    path('productdelete/<int:dataid>/', views.productdelete, name="productdelete"),
    path('loginadmin/',views.loginadmin,name="loginadmin"),
    path('loginathutication/', views.loginathutication, name="loginathutication"),
    path('logoutadmin/', views.logoutadmin, name="logoutadmin"),
    path('newly_arrived_products/', views.newly_arrived_products, name="newly_arrived_products"),
    path('profiledispaly/', views.profiledispaly, name="profiledispaly"),
    path('deleteprofile/<int:dataid>/', views.deleteprofile, name="deleteprofile"),
    path('cartdispaly/', views.cartdispaly, name="cartdispaly"),
    path('cartdelete/<int:dataid>/', views.cartdelete, name="cartdelete"),
    path('deliverydispaly/', views.deliverydispaly, name="deliverydispaly"),
    path('editdelivery/<int:dataid>/', views.editdelivery, name="editdelivery"),
    path('deliveryeditsave/<int:dataid>/', views.deliveryeditsave, name="deliveryeditsave"),
    path('deletedeliveryuser/<int:dataid>/', views.deletedeliveryuser, name="deletedeliveryuser"),
    path('contactdispaly/', views.contactdispaly, name="contactdispaly"),
    path('deletecontact/<int:dataid>/', views.deletecontact, name="deletecontact"),
    path('customerdispaly/', views.customerdispaly, name="customerdispaly"),
    path('deletecutomerreview/<int:dataid>/', views.deletecutomerreview, name="deletecutomerreview"),
    path('coddispaly/', views.coddispaly, name="coddispaly"),
    path('deletecoddispaly/<int:dataid>/', views.deletecoddispaly, name="deletecoddispaly"),
    path('razorpaydisplay/', views.razorpaydisplay, name="razorpaydisplay"),
    path('deleterazorpay/<int:dataid>/', views.deleterazorpay, name="deleterazorpay"),

]