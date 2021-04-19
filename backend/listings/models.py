from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

class Listing(models.Model):
  class SaleType(models.TextChoices):
    FOR_SALE= 'For Sale'
    FOR_RENT = 'For rent'

  class HomeType(models.TextChoices):
    HOUSE= 'House'
    CONDO = 'Condo'
    TOWNHOUSE = 'Townhouse'

  realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
  slug = models.CharField(max_length= 200, unique =True)
  title = models.CharField(max_length= 200)
  address = models.CharField(max_length= 200)
  city = models.CharField(max_length= 200)
  state = models.CharField(max_length= 200)
  zipcode = models.CharField(max_length= 200)
  address = models.TextField(blank= True)
  sale_type = models.CharField(max_length=50, choices= SaleType.choices, default= SaleType.FOR_SALE)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places = 1)
  home_type = models.CharField(max_length=50, choices = HomeType.choices, default = HomeType.HOUSE)
  sqft = models.IntegerField()
  open_house= models.BooleanField(default=False)
  photo_main = models.ImageField(upload_to= 'photos/%Y/%m%/d')
  photo_1 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_2 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_3 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_4 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_5 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_6 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_7 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_8 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_9 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_10 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_11 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_12 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_13 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_14 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_15 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_16 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_17 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  photo_20 = models.ImageField(upload_to= 'photos/%Y/%m%/d', black=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=now, blank=True)


  def __str__(self):
    return self.title



