from django.contrib import admin
from home.models import Color
from home.models import Categories
from home.models import Brand
from home.models import Filter_Price
from home.models import Product
from home.models import Productone
from home.models import Images
from home.models import Tag
from home.models import Imagess
from home.models import Tags
from home.models import Contact
from home.models import Signup
from home.models import Checkout
from home.models import OrderItem
from home.models import Commingsoon
from home.models import Shoptwocolum
from home.models import Imagessss
from home.models import Tagsss
# Register your models here.
class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerinline]

admin.site.register(Checkout , OrderAdmin)
admin.site.register(OrderItem)

class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag

class Productadmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline , TagTublerinline] 


class ImageTublerinline(admin.TabularInline):
    model = Imagess

class TagsTublerinline(admin.TabularInline):
    model = Tags

class Productadminone(admin.ModelAdmin):
    inlines = [ImageTublerinline , TagsTublerinline] 



class ImagesssTublerinline(admin.TabularInline):
    model = Imagessss
class TagsssTublerinline(admin.TabularInline):
    model = Tagsss

class Shopadmintwo(admin.ModelAdmin):
    inlines = [ImagesssTublerinline , TagsssTublerinline]


admin.site.register(Color)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Filter_Price)
admin.site.register(Product , Productadmin)
admin.site.register(Productone , Productadminone)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Imagess)
admin.site.register(Tags)
admin.site.register(Contact)
admin.site.register(Commingsoon)
admin.site.register(Signup)

admin.site.register(Shoptwocolum , Shopadmintwo)
admin.site.register(Imagessss)
admin.site.register(Tagsss)
