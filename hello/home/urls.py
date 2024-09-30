from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home , name = 'home.html'),
    path('home.html', views.home , name = 'home.html'),
    path('base.html', views.base , name = 'base.html'),
    path('productleftside.html', views.productleftside , name = 'productleftside.html'),
    path('phone.html', views.phone , name = 'phone.html'),
    path('watch.html', views.watch , name = 'watch.html'),
    path('headphone.html', views.headphone , name = 'headphone.html'),
    path('computer.html', views.computer , name = 'computer.html'),
    path('electronic.html', views.electronic , name = 'electronic.html'),
    path('sunglasses.html', views.sunglasses , name = 'sunglasses.html'),
    path('leather.html', views.leather , name = 'leather.html'),
    path('smasung.html', views.smasung , name = 'smasung.html'),
    path('fossial.html', views.fossial , name = 'fossial.html'),
    path('sony.html', views.sony , name = 'sony.html'),
    path('lakmeeto.html', views.lakmeeto , name = 'lakmeeto.html'),
    path('Beautifill.html', views.Beautifill , name = 'Beautifill.html'),
    path('made.html', views.made , name = 'made.html'),
    path('pecifico.html', views.pecifico , name = 'pecifico.html'),
    path('xlovgtire.html', views.xlovgtire , name = 'xlovgtire.html'),
    path('productleftsidetwo.html', views.productleftsidetwo , name = 'productleftsidetwo.html'),
    path('productleftsidethree.html', views.productleftsidethree , name = 'productleftsidethree.html'),
    path('productleftsidenext.html', views.productleftsidenext , name = 'productleftsidenext.html'),
    path('search.html', views.search , name = 'search.html'),
    path('about.html' , views.about , name ='about.html'),
    path('indextwo.html' , views.indextwo , name = 'indextwo.html'),
    path('contact.html' , views.contact , name = 'contact.html'),
    path('products/<str:id>' , views.singleproduct , name = 'singleproduct.html'),
    path('myaccout.html' , views.myaccout , name = 'myaccout.html'),
    path('login.html' , views.loginuser , name = 'login.html'),
    path('register.html' , views.register , name = 'register.html'),
    path('logout.html' , views.logoutuser , name = 'logout.html'),
    path('errorpages.html' , views.errorpages , name = 'errorpages.html'),

    path('ordertracker.html' , views.ordertracker , name = 'ordertracker.html'),
    path('faqpage.html' , views.faqpage , name = 'faqpage.html'),
    path('commingsoon.html' , views.commingsoon , name = 'commingsoon.html'),
    # path('cart.html' , views.cart , name = 'cart.html'),
    path('comparepage.html' , views.comparepage , name = 'comparepage.html'),
    path('wishlistpage.html' , views.wishlistpage , name = 'wishlistpage.html'),
    path('emptycartpage.html' , views.emptycartpage , name = 'emptycartpage.html'),

    path('bloglist.html' , views.bloglist , name = 'bloglist.html'),
    path('bloggrid.html' , views.bloggrid , name = 'bloggrid.html'),
    path('singleblog.html' , views.singleblog , name = 'singleblog.html'),
    path('bloggridleftside.html' , views.bloggridleftside , name = 'bloggridleftside.html'),
    path('bloggridrightside.html' , views.bloggridrightside , name = 'bloggridrightside.html'),
    path('bloglistleftside.html' , views.bloglistleftside , name = 'bloglistleftside.html'),
    path('bloglistrightside.html' , views.bloglistrightside , name = 'bloglistrightside.html'),
    path('singleblogleftside.html' , views.singleblogleftside , name = 'singleblogleftside.html'),
    path('singleblogrightside.html' , views.singleblogrightside , name = 'singleblogrightside.html'),
    path('shoppage.html' , views.shoppage , name = 'shoppage.html'),


    #Cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-details/',views.cart_details,name='cart_details'),

    path('cart/checkout/' , views.checkout , name = 'checkout.html'),
    path('cart/placeorder/' , views.placeorder , name = 'placeorder.html'),
    path('thankupage.html' , views.thankupage , name = 'thankupage.html'),


    path('shop3colum.html' , views.shop3colum , name = 'shop3colum.html'),
    path('shopfourcolum.html' , views.shopfourcolum , name = 'shopfourcolum.html'),
    path('shopleftside.html' , views.shopleftside , name = 'shopleftside.html'),
    path('shoprightside.html' , views.shoprightside , name = 'shoprightside.html'),
    path('shoplistleftside.html' , views.shoplistleftside , name = 'shoplistleftside.html'),
    path('shoplistrightside.html' , views.shoplistrightside , name = 'shoplistrightside.html'),
    path('productgroup.html' , views.productgroup , name = 'productgroup.html'),
    path('productsingle.html' , views.productsingle , name = 'productsingle.html'),
    path('Productvariable.html' , views.Productvariable , name = 'Productvariable.html'),
    path('productaffiliate.html' , views.productaffiliate , name = 'productaffiliate.html'),
    path('producttav2.html' , views.producttav2 , name = 'producttav2.html'),
    path('producttav3.html' , views.producttav3 , name = 'producttav3.html'),
    path('productslider.html' , views.productslider , name = 'productslider.html'),
    path('productgalleryleft.html' , views.productgalleryleft , name = 'productgalleryleft.html'),
    path('productgalleryright.html' , views.productgalleryright , name = 'productgalleryright.html'),
    path('productstickyleft.html' , views.productstickyleft , name = 'productstickyleft.html'),
    path('productstickyright.html' , views.productstickyright , name = 'productstickyright.html'),

    path('productss/<int:id>' , views.singleproductone , name = 'singleproductone'),

    

    
    





]



