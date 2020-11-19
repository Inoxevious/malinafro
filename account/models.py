from django.db import models
from django.contrib.auth.models import User


class UserClass(models.Model): 
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=70)
    user_group = models.ForeignKey(UserClass, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
class AccountUser(models.Model):
    role = models.CharField(null=True ,blank=True,max_length=70)
    category = models.CharField(null=True ,blank=True,max_length=70)
    age = models.IntegerField(null=True ,blank=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    address =models.TextField(null=True ,blank=True)
    date_birth =models.DateField(null=True ,blank=True)
    phone =models.CharField(null=True ,blank=True,max_length=70)
    id_number =models.CharField(null=True ,blank=True,max_length=20)
    gender =models.CharField(null=True ,blank=True,max_length=20)
    education_level =models.CharField(null=True ,blank=True,max_length=70)
    marital_status =models.CharField(null=True ,blank=True,max_length=20)
    number_dependants =models.IntegerField(null=True ,blank=True)
    total_worth =models.IntegerField(null=True ,blank=True)
    profile_pic = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    bio = models.TextField(null=True ,blank=True)
    

    def __str__(self):
        return self.user.username


class About_us(models.Model):
    tag_text =models.CharField(max_length=50,null=True ,blank=True)
    image1 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image2 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image3 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    image4 = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    statement =models.TextField(null=True ,blank=True)
    statement2 =models.TextField(null=True ,blank=True)
    statement3 =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.tag_text

class Department(models.Model):
    name = models.CharField(null=True ,blank=True,max_length=20)
    head = models.OneToOneField(AccountUser, on_delete = models.CASCADE)
    mission =models.TextField(null=True ,blank=True)
    vision =models.TextField(null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    def __str__(self):
        return self.name

class Executive(models.Model):
    profile = models.OneToOneField(AccountUser, on_delete = models.CASCADE)
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    appointment_date = models.DateTimeField()
    valid_till_date = models.DateTimeField()
    def __str__(self):
        return self.profile.user.username

class NoticeBoard(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class Articles(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    author = models.ForeignKey(AccountUser, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    summary =models.CharField(max_length=100,null=True ,blank=True)
    paragraph =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isHomeArticle = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title



