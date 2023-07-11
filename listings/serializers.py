from rest_framework import serializers
from .models import Listing, Contact, Photo


class RealtorSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    photo = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)


class ListingSerializer(serializers.ModelSerializer):
    link_url = serializers.HyperlinkedIdentityField(
        view_name='listing-detail',
        lookup_field='pk' )

    # url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Listing
        fields = ('id', 'title', 'address', 'city', 'province', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main' ,'link_url' )

    # def get_url(self, obj):
    #     return f'/realtor/{obj.pk}/'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class listingDetailSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    # realtor = RealtorSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = ('id', 'title', 'address', 'city', 'province', 'price', 'zipcode', 'description',
                'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'realtor', 'list_date', 'is_published', 'photos')
        lookup_field = 'pk'
    


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        
