from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.db.models import Q
from datetime import datetime

from realtors.models import Realtor

import string
import random


# class ListingQuerySet(models.QuerySet):
#     def is_public(self):
#         return self.filter(is_public=True)
    
#     def search(self, query):
#         lookup = Q(province__icontains=query)
#         return self.filter(lookup)


# class ListingManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return ListingQuerySet(self.model, using=self._db)

#     def search(self, query):
#         return self.get_queryset().is_public().search(query)


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    
    class HomeType(models.TextChoices):
        HOUSE = 'House'
        APARTMENTS = 'Apartments'
        TOWNHOUSE = 'Townhouse'
        VACANT_LAND = 'Vacant Land'

    class Provinces(models.TextChoices):
        EASTERN_CAPE = 'Eastern Cape'
        FREE_STATE = 'Free State'
        GAUTENG = 'Gauteng'
        KWAZULU_NATAL = 'KwaZulu-Natal'
        LIMPOPO = 'Limpopo'
        MPUMALANGA = 'Mpumalanga'
        NORTHERN_CAPE = 'Northern Cape'
        NORTHWEST = 'North West'
        WESTERN_CAPE = 'Western Cape'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, related_name='realtor')
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=50, choices=Provinces.choices, default=Provinces.EASTERN_CAPE)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_19 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_20 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    # objects = ListingManager()

    def __str__(self):
        return self.title
    
    def rand_slug(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.rand_slug() + "-" + self.title)
        super(Listing, self).save(*args, **kwargs)


class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.listing.title} - {self.image}'
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
        