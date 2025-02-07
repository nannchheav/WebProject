from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True) 
    categoryImage =  models.ImageField(upload_to ='images/')
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):
           return self.categoryName
    
class tblProducts(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_ratting = models.CharField(max_length=200, null=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Change to DecimalField
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Change to DecimalField
    description = RichTextUploadingField(null=True)
    productImage = models.ImageField(upload_to='Productimages/')
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):         
        return self.productName
    
class tblSocialMedia(models.Model):
    socialMediaName = models.CharField(max_length=200, null=True)
    socialMediaURL = models.CharField(max_length=200, null=True)
    socialMediaImage = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.socialMediaName

class tblTopMenu(models.Model):
    topMenuName = models.CharField(max_length=200, null=True)
    topMenuImage = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.topMenuName

class tblSubTopMenu(models.Model):
    subTopMenuName = models.CharField(max_length=200, null=True)
    subTopMenuImage = models.ImageField(upload_to="SubTopMenu")
    TopMenuID = models.ForeignKey(tblTopMenu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.subTopMenuName}'  

class TblBlogType (models.Model):
    BlogTypeName = models. CharField (max_length=200, null=True)

    def __str__(self):
        return f'{self.id} {self.BlogTypeName}'

class TblBlog(models. Model):
    BlogName = models. CharField(max_length=200, null=True)
    BlogDescription = models. CharField(max_length=200, null=True)
    BlogDate = models. DateTimeField(auto_now_add=True, null=True)
    BlogURL = models. CharField(max_length=200, null=True)
    BlogImage =  models.ImageField(upload_to ='images/')


    def __str__(self):
        return f'{self.id} {self.BlogName}'
    
class tblSlides(models.Model):
    slideName = models.CharField(max_length=200, null=True)
    slideImage = models.ImageField(upload_to ='images/',null=True)
    slideDescription = models.CharField(max_length=200, null=True)
    smallslideDescription = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.slideName}'
    
class tblProductDetail(models.Model):
    productDetailName = models.CharField(max_length=200, null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    productID = models.ForeignKey(tblProducts, on_delete=models.CASCADE, null=True)
    productSize =  RichTextUploadingField(null=True)
    productColor = RichTextUploadingField(null=True)
    def __str__(self):
        return f'{self.productDetailName}'
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} - User: {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(tblProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.productName} in Cart {self.cart.id}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    
    def __str__(self):
        return f'Order {self.id} - User: {self.user.username}'

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    
    def __str__(self):
        return f'Payment {self.id} - Order: {self.order.id}'


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


class tblFooter(models.Model):
    footerName = models.CharField(max_length=200, null=True)
    logo = models.ImageField(upload_to="logoImg")
    SpanContact = models.CharField(max_length=200, null=True)
    Contact = models.CharField(max_length=200, null=True)
    SpanLocation = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.footerName
    
class tblBanner(models.Model):
    bannerName = models.CharField(max_length=200, null=True)
    img1 = models.ImageField(upload_to="logoImg")
    img2 = models.ImageField(upload_to="logoImg")
    img3 = models.ImageField(upload_to="logoImg")
    img4 = models.ImageField(upload_to="logoImg")
    text1 = models.CharField(max_length=200, null=True)
    text2 = models.CharField(max_length=200, null=True)
    span1 = models.CharField(max_length=200, null=True)
    span2 = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.bannerName


