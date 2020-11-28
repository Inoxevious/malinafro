from django.db import models
from decimal import Decimal
from account.models import *
class Category(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    short_name = models.CharField(null=True ,blank=True,max_length=70)
    long_name = models.CharField(null=True ,blank=True,max_length=70)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    mobile_image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    description = models.TextField(null=True ,blank=True)
    def __str__(self):
        return self.short_name

class SubCategory(models.Model):
    main_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    short_name = models.CharField(null=True ,blank=True,max_length=70)
    long_name = models.CharField(null=True ,blank=True,max_length=70)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    description = models.TextField(null=True ,blank=True)
    def __str__(self):
        return self.short_name

class SalesCategorie(models.Model):
    short_name = models.CharField(null=True ,blank=True,max_length=70)
    long_name = models.CharField(null=True ,blank=True,max_length=70)
    description = models.TextField(null=True ,blank=True)
    def __str__(self):
        return self.short_name

class ProductMaterialMainColor(models.Model):
    name = models.CharField(max_length=191)
    isAvailable = models.BooleanField(default=False, null=True ,blank=True)
    def __str__(self):
        return self.name
class MenuItems(models.Model):
    just_in = 'just_in'
    summer_look = 'summer_look'
    lovers_show_off = 'lovers_show_off'
    ambitious_personalities = "ambitious_personalities"
    ambitious_kidz = 'ambitious_kidz'
    fashion_blog = 'fashion_blog'
    COLLECTION_CHOICES = [
        (just_in,'just_in'),
        (summer_look,'summer_look'),
        (lovers_show_off,'lovers_show_off'),
        (ambitious_personalities,'ambitious_personalities'),
        (ambitious_kidz,'ambitious_kidz'),
        (fashion_blog,'fashion_blog'),
    ]
    short_name = models.CharField(null=True ,blank=True,max_length=70)
    nav_tag = models.CharField(null=True ,blank=True,max_length=70)
    collecion_category = models.CharField(null=True ,blank=True,max_length=50, choices=COLLECTION_CHOICES, default = just_in)
    def __str__(self):
        return self.short_name

class Product(models.Model):
    just_in = 'just_in'
    summer_look = 'summer_look'
    lovers_show_off = 'lovers_show_off'
    ambitious_personalities = "ambitious_personalities"
    ambitious_kidz = 'ambitious_kidz'
    fashion_blog = 'fashion_blog'
    ORDER_STATUS_CHOICES = [
        (just_in,'just_in'),
        (summer_look,'summer_look'),
        (lovers_show_off,'lovers_show_off'),
        (ambitious_personalities,'ambitious_personalities'),
        (ambitious_kidz,'ambitious_kidz'),
        (fashion_blog,'fashion_blog'),
    ]
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity =models.IntegerField(null=True ,blank=True)
    slug = models.SlugField(null=True ,blank=True)
    long_name = models.CharField(null=True ,blank=True,max_length=70)
    major_colors = models.ManyToManyField(ProductMaterialMainColor, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True ,blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True ,blank=True)
    sales_category = models.ForeignKey(SalesCategorie, on_delete=models.CASCADE, null=True ,blank=True)    
    collecion_category = models.CharField(null=True ,blank=True,max_length=50, choices=ORDER_STATUS_CHOICES, default = just_in)
    first_image = models.ImageField(upload_to='products_images/', blank=True)
    second_image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image2 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image3 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    size1_model_image = models.ImageField(upload_to="media/models/products/%Y/%m/%d",null=True, blank=True)
    size2_model_image = models.ImageField(upload_to="media/models/products/%Y/%m/%d",null=True, blank=True)
    size3_model_image = models.ImageField(upload_to="media/models/products/%Y/%m/%d",null=True, blank=True)
    size4_model_image = models.ImageField(upload_to="media/models/products/%Y/%m/%d",null=True, blank=True)
    description = models.TextField(null=True ,blank=True)
    stock_date = models.DateTimeField(null=True ,blank=True)
    restoke_date = models.DateTimeField(null=True ,blank=True)
    isAvailable = models.BooleanField(default=False, null=True ,blank=True)
    def __str__(self):
        return self.name


class DepartmentAdverts(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True ,blank=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title = models.CharField(max_length=50,null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class ProductAdverts(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title = models.CharField(max_length=50,null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title


class Collection_Banner(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,null=True ,blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title = models.CharField(max_length=50,null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image2 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image3 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image4 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image5 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image6 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image7 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class MainMenuAds(models.Model):
    just_in = 'just_in'
    summer_look = 'summer_look'
    lovers_show_off = 'lovers_show_off'
    ambitious_personalities = "ambitious_personalities"
    ambitious_kidz = 'ambitious_kidz'
    fashion_blog = 'fashion_blog'
    ORDER_STATUS_CHOICES = [
        (just_in,'just_in'),
        (summer_look,'summer_look'),
        (lovers_show_off,'lovers_show_off'),
        (ambitious_personalities,'ambitious_personalities'),
        (ambitious_kidz,'ambitious_kidz'),
        (fashion_blog,'fashion_blog'),
    ]
    title = models.CharField(max_length=50,null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    category = models.CharField(null=True ,blank=True,max_length=50, choices=ORDER_STATUS_CHOICES, default = just_in)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    size= models.CharField(max_length=50,null=True ,blank=True)
    color= models.CharField(max_length=50,null=True ,blank=True)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price


class Order(models.Model):
    unattended = 'unattended'
    waiting_payment = 'waiting_payment'
    in_progress = 'in_progress'
    completed = "completed"
    recieved = 'recieved'
    in_transit = 'in_transit'
    ORDER_STATUS_CHOICES = [
        (unattended,'unattended'),
        (waiting_payment,'High'),
        (in_progress,'in_progress'),
        (completed,'completed'),
        (recieved,'recieved'),
        (in_transit,'in_transit'),
    ]
    name = models.CharField(max_length=191)
    email = models.EmailField()
    phone = models.CharField(max_length=191,null=True ,blank=True)
    city = models.CharField(max_length=191, null=True ,blank=True)
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(null=True ,blank=True,max_length=20, choices=ORDER_STATUS_CHOICES, default = unattended)
    requested = models.BooleanField(default=False)
    shippig_cost = models.CharField(max_length=191, null=True ,blank=True)

    def __str__(self):
        return "{}:{}".format(self.id, self.email)

    def total_cost(self):
        cart_cost = Decimal(sum([ li.cost() for li in self.lineitem_set.all() ] ))
        shipping_cost = Decimal(self.shippig_cost)
        return shipping_cost + cart_cost 

    # def get_total_cost(self):
    #     return Decimal(sum(item.get_cost() for item in self.items.all()))

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    size= models.CharField(max_length=50,null=True ,blank=True)
    color= models.CharField(max_length=50,null=True ,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def cost(self):
        return self.price * self.quantity

class PaynowPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cellphone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100)
    paynow_reference = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=500, blank=True)
    init_status = models.CharField(max_length=10, blank=True)
    poll_url = models.CharField(max_length=500)
    browser_url = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10)
    paid = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username + ' - $' + str(self.amount) + ' - ' + self.status       