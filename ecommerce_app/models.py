from django.db import models
from decimal import Decimal
from account.models import *
class Category(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    short_name = models.CharField(null=True ,blank=True,max_length=70)
    long_name = models.CharField(null=True ,blank=True,max_length=70)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
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
class Product(models.Model):
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity =models.IntegerField(null=True ,blank=True)
    slug = models.SlugField(null=True ,blank=True)
    long_name = models.CharField(null=True ,blank=True,max_length=70)
    major_color = models.CharField(null=True ,blank=True,max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True ,blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True ,blank=True)
    image = models.ImageField(upload_to='products_images/', blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
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




class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price


class Order(models.Model):
    name = models.CharField(max_length=191)
    email = models.EmailField()
    phone = models.CharField(max_length=191,null=True ,blank=True)
    city = models.CharField(max_length=191, null=True ,blank=True)
    address = models.CharField(max_length=191)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
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
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def cost(self):
        return self.price * self.quantity