from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from home.models import Product
from home.models import Productone
from home.models import Categories
from home.models import Color
from home.models import Brand
from home.models import Filter_Price
from home.models import Tag
from home.models import Contact
from home.models import Checkout
from home.models import OrderItem
from datetime import datetime
from django.contrib.auth.models import User
from home.models import Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import razorpay
from home.models import Commingsoon
from django.views.decorators.csrf import csrf_exempt
from home.models import Shoptwocolum
from home.models import Tagsss
import logging

logger = logging.getLogger(__name__)
# Create your views here.

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRECT))



def home(request):
    HttpResponse("Welcome to Home Page")
    product = Product.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    tag  = Tag.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID)
    else:
        product = Product.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        product = Product.objects.filter(tag=TAGID)
    else:
        product = Product.objects.filter(status="Publish")
    context = {
        'product': product,
        'categories': categories,
        'tag': tag,
    }
    return render(request , 'home.html' , context)
def base(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'base.html')
def productleftside(request):
    HttpResponse("WelCome to Home Page")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    tag  = Tag.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        productone = Productone.objects.filter(categories=CATID)
    else:
        productone = Productone.objects.filter(status="Publish")

    COLID = request.GET.get('color')
    if COLID:
        productone = Productone.objects.filter(color=COLID)
    else:
        productone = Productone.objects.filter(status="Publish")
    
    PRICID = request.GET.get('filter_price')
    if PRICID:
        productone = Productone.objects.filter(filter_price=PRICID)
    else:
        productone = Productone.objects.filter(status="Publish")
        
    BRAID = request.GET.get('brand')
    if BRAID:
        productone = Productone.objects.filter(brand=BRAID)
    else:
        productone = Productone.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        productone = Productone.objects.filter(tag=TAGID)
    else:
        productone = Productone.objects.filter(status="Publish")

    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
        'tag':tag,
    }
    return render(request, 'productleftside.html',context)


def phone(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'phone.html')
def watch(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'watch.html')
def headphone(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'headphone.html')
def computer(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'computer.html')
def electronic(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'electronic.html')
def sunglasses(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'sunglasses.html')
def leather(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'leather.html')
def smasung(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'smasung.html')
def fossial(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'fossial.html')
def sony(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'sony.html')
def lakmeeto(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'lakmeeto.html')
def Beautifill(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'Beautifill.html')
def made(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'made.html')
def pecifico(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'pecifico.html')
def xlovgtire(request):
    HttpResponse("WelCome to Home Page")
    return render(request, 'xlovgtire.html')


def productleftsidetwo(request):
    HttpResponse("WelCome to Home Page")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    tag  = Tag.objects.all()


    CATID = request.GET.get('categories')
    if CATID:
        productone = Productone.objects.filter(categories=CATID)
    else:
        productone = Productone.objects.filter(status="Publish")

    COLID = request.GET.get('color')
    if COLID:
        productone = Productone.objects.filter(color=COLID)
    else:
        productone = Productone.objects.filter(status="Publish")
    
    PRICID = request.GET.get('filter_price')
    if PRICID:
        productone = Productone.objects.filter(filter_price=PRICID)
    else:
        productone = Productone.objects.filter(status="Publish")
        
    BRAID = request.GET.get('brand')
    if BRAID:
        productone = Productone.objects.filter(brand=BRAID)
    else:
        productone = Productone.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        productone = Productone.objects.filter(tag=TAGID)
    else:
        productone = Productone.objects.filter(status="Publish")


    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
        'tag':tag,
    }
    return render(request, 'productleftsidetwo.html',context)
def productleftsidethree(request):
    HttpResponse("WelCome to Home Page")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
    }
    return render(request, 'productleftsidethree.html',context)
def productleftsidenext(request):
    HttpResponse("WelCome to Home Page")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
    }
    return render(request, 'productleftsidenext.html',context)
def search(request):
    HttpResponse("WelCome to Home Page")
    quary = request.GET.get('quary')
    productone = Productone.objects.filter(name__icontains = quary)

    context = {
        # 'quary' : quary,
        'productone' : productone,
    }
    return render(request, 'search.html' , context)


def about(request):
    HttpResponse("Welcome to the about  Page")
    return render(request , 'about.html')

def indextwo(request):
    HttpResponse("Welcome to the indextwo page")
    product = Product.objects.all()

    context = {
        'product':product,
    }
    return render(request , 'indextwo.html', context)


def contact(request):
    HttpResponse("Welcome to the Contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

        contact = Contact(name = name , email = email , subject = subject , message = message)
        contact.save()
        messages.success(request, "Thank You!")
        

        # subject = subject
        # message = message
        # email_from = settings.EMAIL_HOST_USER
        # # try:
        # send_mail(subject, message, email_from, ["awaiskhanbhutta322@gmail.com"])
        # return redirect('home')
        # except:
        # return redirect('contact.html')

        # subject = request.POST.get("subject", "")
        # subject = request.POST.get("subject", "")
        # from_email = request.POST.get("from_email", "")
        # try:
        #     send_mail(subject, subject, from_email, ["awaisqamar321@gmail.com"])
        #     return redirect('home.html')
        # except BadHeaderError:
        #     return redirect('contact.html')
        # return HttpResponse("Make sure all fields are entered and valid.")




        
    return render(request , 'contact.html')
def singleproduct(request  , id):
    HttpResponse("Welcome to the Single page product")
    # product = Product.objects.filter(id = id).first()
    

    # context = {
    #     'product' : product,
    # }

    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }

    return render(request , 'singleproduct.html' , context)

def singleproductone(request  , id):
    HttpResponse("Welcome to the Single page product")
    # shopcolum = Shoptwocolum.objects.filter(id = id).first()
    

    # context = {
    #     'shopcolum' : shopcolum,
    # }

    product = get_object_or_404(Shoptwocolum, id=id)
    context = {
        'product': product,
    }

    return render(request , 'singleproductone.html' , context)
def myaccout(request):
    HttpResponse("Welcome to the Single page product")
    return render(request , 'myaccout.html')
def loginuser(request):
    HttpResponse("Welcome to the Single page product")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('home.html')
        else:
            return redirect('register.html')


    return render(request , 'login.html')
def register(request):
    HttpResponse("Welcome to the Single page product")
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("repeatpassword")
        
        sign = Signup(username=username , first_name = first_name , last_name = last_name , email = email , password =  password , repeatpassword = repeatpassword )
        sign.save()

        if User.objects.filter(username = username).exists():
            error_message = 'Username already taken. Please choose a different username.'
            return render(request , 'register.html' ,{'error_message' : error_message})
        
        if password != repeatpassword:
            return HttpResponse("Your Password and confirm password are not the same!")
        
        else:
            myuser = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        myuser.save()
        return redirect('login.html')
    return render(request ,'register.html')

def logoutuser(request):
    logout(request)
    return redirect('home.html')
    return render(request , 'logout.html')

def errorpages(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'errorpages.html')

def ordertracker(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'ordertracker.html')

def faqpage(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'faqpage.html')
def commingsoon(request):
    HttpResponse("Welcome to the Error Pages")
    if request.method == "POST":
        email = request.POST.get('email')

        commingsoon = Commingsoon(email = email)
        commingsoon.save()
    return render(request , 'commingsoon.html')

# def cart(request):
#     HttpResponse("Welcome to the Error Pages")
#     if request.user.is_anonymous:
#         return redirect('login.html')
#     return render(request , 'cart.html')



def comparepage(request):
    HttpResponse("Welcome to the Error Pages")
    product = Product.objects.filter(status = "Publish")
    categories = Categories.objects.all() 
    tag  = Tag.objects.all()
    color = Color.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID)
    else:
        product = Product.objects.filter(status="Publish")
    
    COLID = request.GET.get('color')
    if COLID:
        product = Product.objects.filter(color = COLID)
    else:
        product = Product.objects.filter(status = "Publish")
    TAGID = request.GET.get('tag')
    if TAGID:
        product = Product.objects.filter(tag=TAGID)
    else:
        product = Product.objects.filter(status="Publish")
    context = {
        'product': product,
        'categories': categories,
        'tag': tag,
        'color': color,
    }
    return render(request , 'comparepage.html' , context)

def wishlistpage(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'wishlistpage.html')

def emptycartpage(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'emptycartpage.html')



def bloglist(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'bloglist.html')

def bloggrid(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'bloggrid.html')
def singleblog(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'singleblog.html')
def bloggridleftside(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'bloggridleftside.html')
def bloggridrightside(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'bloggridrightside.html')
def bloglistleftside(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'bloglistleftside.html')
def bloglistrightside(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'bloglistrightside.html')
def singleblogleftside(request):
    HttpResponse("Welcome to the Error Pages")
    return render(request , 'singleblogleftside.html')
def singleblogrightside(request):
    HttpResponse("Welcome to the singleblogrightside")
    return render(request , 'singleblogrightside.html')


@login_required(login_url="login.html")
def cart_add(request, id):
    # cart = Cart(request)
    # product = Product.objects.get(id=id)
    # product = get_object_or_404(Product, id=id)
    # cart.add(product=product)
    # return redirect('home.html')

    cart = Cart(request)
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        logger.error(f'Product with id {id} does not exist.')
        return HttpResponse("Product not found", status=404)
    
    cart.add(product=product)
    return redirect('home.html')


@login_required(login_url="login.html")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_details")


@login_required(login_url="login.html")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_details")


@login_required(login_url="login.html")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_details")


@login_required(login_url="login.html")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_details')


@login_required(login_url="login.html")
def cart_details(request):
    return render(request, 'cart/cart_details.html')

@login_required(login_url="login.html")
def checkout(request):
    if request.method == 'GET':
        try:
            payment = client.order.create({
                "amount": 50000,  # amount in the smallest currency unit
                "currency": "INR",
                "payment_capture": 1  # automatic capture
            })
            order_id = payment['id']
            context = {
                'order_id': order_id,
                'payment': payment,
            }
            return render(request, 'cart/checkout.html', context)
        except razorpay.errors.BadRequestError as e:
            return HttpResponse(f"BadRequestError: {e}", status=400)
        except razorpay.errors.ServerError as e:
            return HttpResponse(f"ServerError: {e}", status=500)
        except Exception as e:
            return HttpResponse(f"Error: {e}", status=500)
@login_required(login_url="login.html")
def placeorder(request):
    HttpResponse("Welcome to the Error Pages")
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid) 
        cart = request.session.get('cart') 
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        order_id = request.POST.get('order_id')
        payment = request.POST.get('payment')
        amount = request.POST.get('amount')

        context = {
                'order_id' : order_id,
        }

        

        placeorder = Checkout(user = user , firstname = firstname , lastname = lastname , country = country , 
                              address =  address , city = city , state = state , postcode = postcode ,
                              phone = phone , email = email , message = message , payment_id = order_id ,
                              amount = amount ,date = datetime.today())
        placeorder.save()

        for i in cart:
            a = (int(cart[i]['price']))
            c = cart[i]['quantity']

            total = a * c

            Item = OrderItem(
                oredr = placeorder,
                product = cart[i]['name'],
                image =  cart[i]['image'],
                quantity =  cart[i]['quantity'],
                price =  cart[i]['price'],
                total = total
            )
            Item.save()

        
    return render(request , 'cart/placeorder.html' , context)


@csrf_exempt
@login_required(login_url="login.html")
def thankupage(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, value in a.items():
            if key == 'razorpay_order_id':
                order_id = value
                break
        user = OrderItem.objects.filter(razorpay_order_id=order_id).first()

        if user:
            user.paid = True
            user.save()
    return render(request, 'cart/thankupage.html')
    # if request.method == "POST":
    #     a = request.POST
    #     order_id = ""
    #     for key, value in a.items():
    #         if key == 'razorpay_order_id':
    #             order_id = value
    #             break
    #     user = OrderItem.objects.filter(payment = order_id).first()

    #     user.paid = True
    #     user.save()

        

def shoppage(request):
    HttpResponse("Welcome to the shoppage")
    return render(request , 'shoppage.html')

def shop3colum(request):
    HttpResponse("Welcome to the shoppage")
    product = Shoptwocolum.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    tages  = Tagsss.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        product = Shoptwocolum.objects.filter(categories=CATID)
    else:
        product = Shoptwocolum.objects.filter(status="Publish")

    TAGID = request.GET.get('tages')
    if TAGID:
        product = Shoptwocolum.objects.filter(tages=TAGID)
    else:
        product = Shoptwocolum.objects.filter(status="Publish")
    context = {
        'product': product,
        'categories': categories,
        'tages': tages,
    }
    return render(request , 'shop3colum.html' , context)

def shopfourcolum(request):
    HttpResponse("Welcome to the shoppage")
    product = Shoptwocolum.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    tages  = Tagsss.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        product = Shoptwocolum.objects.filter(categories=CATID)
    else:
        product = Shoptwocolum.objects.filter(status="Publish")

    TAGID = request.GET.get('tages')
    if TAGID:
        product = Shoptwocolum.objects.filter(tages=TAGID)
    else:
        product = Shoptwocolum.objects.filter(status="Publish")
    context = {
        'product': product,
        'categories': categories,
        'tages': tages,
    }
    return render(request , 'shopfourcolum.html' , context)

def shopleftside(request):
    HttpResponse("Welcome to the shoppage")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    tag  = Tag.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        productone = Productone.objects.filter(categories=CATID)
    else:
        productone = Productone.objects.filter(status="Publish")

    COLID = request.GET.get('color')
    if COLID:
        productone = Productone.objects.filter(color=COLID)
    else:
        productone = Productone.objects.filter(status="Publish")
    
    PRICID = request.GET.get('filter_price')
    if PRICID:
        productone = Productone.objects.filter(filter_price=PRICID)
    else:
        productone = Productone.objects.filter(status="Publish")
        
    BRAID = request.GET.get('brand')
    if BRAID:
        productone = Productone.objects.filter(brand=BRAID)
    else:
        productone = Productone.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        productone = Productone.objects.filter(tag=TAGID)
    else:
        productone = Productone.objects.filter(status="Publish")

    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
        'tag':tag,
    }
    return render(request , 'shopleftside.html' , context)

def shoprightside(request):
    HttpResponse("Welcome to the shoppage")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    tag  = Tag.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        productone = Productone.objects.filter(categories=CATID)
    else:
        productone = Productone.objects.filter(status="Publish")

    COLID = request.GET.get('color')
    if COLID:
        productone = Productone.objects.filter(color=COLID)
    else:
        productone = Productone.objects.filter(status="Publish")
    
    PRICID = request.GET.get('filter_price')
    if PRICID:
        productone = Productone.objects.filter(filter_price=PRICID)
    else:
        productone = Productone.objects.filter(status="Publish")
        
    BRAID = request.GET.get('brand')
    if BRAID:
        productone = Productone.objects.filter(brand=BRAID)
    else:
        productone = Productone.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        productone = Productone.objects.filter(tag=TAGID)
    else:
        productone = Productone.objects.filter(status="Publish")

    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
        'tag':tag,
    }
    return render(request , 'shoprightside.html' ,context)

def shoplistleftside(request):
    HttpResponse("Welcome to the shoppage")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    tag  = Tag.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        productone = Productone.objects.filter(categories=CATID)
    else:
        productone = Productone.objects.filter(status="Publish")

    COLID = request.GET.get('color')
    if COLID:
        productone = Productone.objects.filter(color=COLID)
    else:
        productone = Productone.objects.filter(status="Publish")
    
    PRICID = request.GET.get('filter_price')
    if PRICID:
        productone = Productone.objects.filter(filter_price=PRICID)
    else:
        productone = Productone.objects.filter(status="Publish")
        
    BRAID = request.GET.get('brand')
    if BRAID:
        productone = Productone.objects.filter(brand=BRAID)
    else:
        productone = Productone.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        productone = Productone.objects.filter(tag=TAGID)
    else:
        productone = Productone.objects.filter(status="Publish")

    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
        'tag':tag,
    }
    return render(request , 'shoplistleftside.html' , context)

def shoplistrightside(request):
    HttpResponse("Welcome to the shoppage")
    productone = Productone.objects.filter(status = "Publish")
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    tag  = Tag.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        productone = Productone.objects.filter(categories=CATID)
    else:
        productone = Productone.objects.filter(status="Publish")

    COLID = request.GET.get('color')
    if COLID:
        productone = Productone.objects.filter(color=COLID)
    else:
        productone = Productone.objects.filter(status="Publish")
    
    PRICID = request.GET.get('filter_price')
    if PRICID:
        productone = Productone.objects.filter(filter_price=PRICID)
    else:
        productone = Productone.objects.filter(status="Publish")
        
    BRAID = request.GET.get('brand')
    if BRAID:
        productone = Productone.objects.filter(brand=BRAID)
    else:
        productone = Productone.objects.filter(status="Publish")

    TAGID = request.GET.get('tag')
    if TAGID:
        productone = Productone.objects.filter(tag=TAGID)
    else:
        productone = Productone.objects.filter(status="Publish")

    context = {
        'productone' : productone,
        'categories': categories,
        'filter_price': filter_price,
        'color':color,
        'brand':brand,
        'tag':tag,
    }
    return render(request , 'shoplistrightside.html', context)

def productgroup(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productgroup.html', context)

def productsingle(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productsingle.html' , context)

def Productvariable(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'Productvariable.html', context)

def productaffiliate(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productaffiliate.html',context)

def producttav2(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'producttav2.html' , context)

def producttav3(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'producttav3.html' , context)

def productslider(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productslider.html' , context)

def productgalleryleft(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productgalleryleft.html' , context)

def productgalleryright(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productgalleryright.html' , context)

def productstickyleft(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productstickyleft.html' , context)

def productstickyright(request):
    HttpResponse("Welcome to the shoppage")
    product = Product.objects.filter().first()
    

    context = {
        'product' : product,
    }
    return render(request , 'productstickyright.html' , context)











