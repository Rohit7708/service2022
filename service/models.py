from sre_constants import CATEGORY
from django.db import models
import uuid


# Create your models here.
class Customer(models.Model):
    CATEGORY = (
        ('Cook', 'Cook'),
        ('Full-time Maid', 'Full-time Maid'),
        ('part-time Maid', 'part-time Maid'),
        ('Gardner', 'Gardner'),
    )
    Districts=(
            ("Ariyalur","Ariyalur"),
            ("Chennai","Chennai"),
            ("Coimbatore","Coimbatore"),
            ("Cuddalore","Cuddalore"),
            ("Dharmapuri","Dharmapuri"),
            ("Dindigul","Dindigul"),
            ("Erode","Erode"),
            ("Kanchipuram","Kanchipuram"),
            ("Kanyakumari","Kanyakumari"),
            ("Karur","Karur"),
            ("Krishnagiri","Krishnagiri"),
            ("Madurai","Madurai"),
            ("Nagapattinam","Nagapattinam"),
            ("Namakkal","Namakkal"),
            ("Nilgiris","Nilgiris"),
            ("Perambalur","Perambalur"),
            ("Pudukkottai","Pudukkotai"),
            ("Ramanathapuram","Ramanathapuram"),
            ("Salem","Salem"),
            ("Sivaganga","Sivaganga"),
            ("Thanjavur","Thanjavur"),
            ("Theni","Theni"),
            ("Thoothukudi (Tuticorin)","Thoothukudi (Tuticorin)"),
            ("Tiruchirappalli","Tiruchirappalli"),
            ("Tirunelveli","Tirunelveli"),
            ("Tiruppur","Tiruppur"),
            ("Tiruvallur","Tiruvallur"),
            ("Tiruvannamalai","Tiruvannamalai"),
            ("Tiruvarur","Tiruvarur"),
            ("Vellore","Vellore"),
            ("Viluppuram","Viluppuram"),
            ("Virudhunagar","Virudhunagar"),

    )    
    username = models.CharField(max_length=200, null=True)
    password1 = models.CharField(max_length=200, null=True)
    password2 = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    otp=models.CharField(max_length=200,null=True,blank=True)
    cust_uid=models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200,null=True)
    Domestic=models.CharField(max_length=200,null=True,choices=CATEGORY)
    city=models.CharField(max_length=200,null=True,choices=Districts)
    address=models.CharField(max_length=200,null=True)

    pincode=models.CharField(max_length=200,null=True)




    def __str__(self):
        return self.username

class Employee(models.Model):


    LI=(
        ('Male','Male'),
        ('Female','Female')
    )
    CATEGORY=(
        ('Cook', 'Cook'),
        ('Full-time Maid', 'Full-time Maid'),
        ('part-time Maid', 'part-time Maid'),
        ('Gardner', 'Gardner'),
        ('Driver','Driver'),
        ('Electrician','Electrician'),
        ('Plumber','plumber'), 
    )
    # Districts=(
    #     ("Ariyalur","Ariyalur"),
    #     ("Chennai","Chennai"),
    #     ("Coimbatore","Coimbatore"),
    #     ("Cuddalore","Cuddalore"),
    #     ("Dharmapuri","Dharmapuri"),
    #     ("Dindigul","Dindigul"),
    #     ("Erode","Erode"),
    #     ("Kanchipuram","Kanchipuram"),
    #     ("Kanyakumari","Kanyakumari"),
    #     ("Karur","Karur"),
    #     ("Krishnagiri","Krishnagiri"),
    #     ("Madurai","Madurai"),
    #     ("Nagapattinam","Nagapattinam"),
    #         ("Namakkal","Namakkal"),
    #         ("Nilgiris","Nilgiris"),
    #         ("Perambalur","Perambalur"),
    #         ("Pudukkottai","Pudukkotai"),
    #         ("Ramanathapuram","Ramanathapuram"),
    #         ("Salem","Salem"),
    #         ("Sivaganga","Sivaganga"),
    #         ("Thanjavur","Thanjavur"),
    #         ("Theni","Theni"),
    #         ("Thoothukudi (Tuticorin)","Thoothukudi (Tuticorin)"),
    #         ("Tiruchirappalli","Tiruchirappalli"),
    #         ("Tirunelveli","Tirunelveli"),
    #         ("Tiruppur","Tiruppur"),
    #         ("Tiruvallur","Tiruvallur"),
    #         ("Tiruvannamalai","Tiruvannamalai"),
    #         ("Tiruvarur","Tiruvarur"),
    #         ("Vellore","Vellore"),
    #         ("Viluppuram","Viluppuram"),
    #         ("Virudhunagar","Virudhunagar"),

    # )
    name=models.CharField(max_length=200,null=True,blank=True)
    gender=models.CharField(max_length=200,null=True,choices=LI,blank=True)
    dob=models.CharField(max_length=200,null=True,blank=True)
    permanent_add=models.CharField(max_length=200,null=True,blank=True)
    present_add=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=200,null=True,blank=True)
    pincode=models.CharField(max_length=200,null=True,blank=True)
    aadhar=models.CharField(max_length=200,null=True,blank=True)
    profession=models.CharField(max_length=200,null=True,choices=CATEGORY,blank=True)
    Exp=models.CharField(max_length=200,null=True,blank=True)
    aadhar_photo=models.ImageField(null=True,blank=True)
    other_photo=models.ImageField(null=True,blank=True)
    username = models.CharField(max_length=200, null=True,blank=True)
    password1 = models.CharField(max_length=200, null=True,blank=True)
    password2 = models.CharField(max_length=200, null=True,blank=True)
    email = models.CharField(max_length=200, null=True,blank=True)
    phone = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    otp=models.CharField(max_length=200,null=True,blank=True)
    uid=models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.username




class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    CATEGORY = (
        ('Cook', 'Cook'),
        ('Full-time Maid', 'Full-time Maid'),
        ('part-time Maid', 'part-time Maid'),
        ('Gardner', 'Gardner'),
    )
    # Districts=(
    #         ("Ariyalur","Ariyalur"),
    #         ("Chennai","Chennai"),
    #         ("Coimbatore","Coimbatore"),
    #         ("Cuddalore","Cuddalore"),
    #         ("Dharmapuri","Dharmapuri"),
    #         ("Dindigul","Dindigul"),
    #         ("Erode","Erode"),
    #         ("Kanchipuram","Kanchipuram"),
    #         ("Kanyakumari","Kanyakumari"),
    #         ("Karur","Karur"),
    #         ("Krishnagiri","Krishnagiri"),
    #         ("Madurai","Madurai"),
    #         ("Nagapattinam","Nagapattinam"),
    #         ("Namakkal","Namakkal"),
    #         ("Nilgiris","Nilgiris"),
    #         ("Perambalur","Perambalur"),
    #         ("Pudukkottai","Pudukkotai"),
    #         ("Ramanathapuram","Ramanathapuram"),
    #         ("Salem","Salem"),
    #         ("Sivaganga","Sivaganga"),
    #         ("Thanjavur","Thanjavur"),
    #         ("Theni","Theni"),
    #         ("Thoothukudi (Tuticorin)","Thoothukudi (Tuticorin)"),
    #         ("Tiruchirappalli","Tiruchirappalli"),
    #         ("Tirunelveli","Tirunelveli"),
    #         ("Tiruppur","Tiruppur"),
    #         ("Tiruvallur","Tiruvallur"),
    #         ("Tiruvannamalai","Tiruvannamalai"),
    #         ("Tiruvarur","Tiruvarur"),
    #         ("Vellore","Vellore"),
    #         ("Viluppuram","Viluppuram"),
    #         ("Virudhunagar","Virudhunagar"),

    # )
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    uid = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    ord_uid=models.UUIDField(default=uuid.uuid4)
    Domestic=models.CharField(max_length=200,null=True,blank=True,choices=CATEGORY)
    city=models.CharField(max_length=200,null=True)
    pincode=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS,default='Pending')
    cust_uid = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    
  
    
    
    





