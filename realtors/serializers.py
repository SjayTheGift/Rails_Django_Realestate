from rest_framework import serializers

from .models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    api_url = serializers.HyperlinkedIdentityField(
        view_name='realtor-detail',
        lookup_field='pk'
        )
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Realtor
        fields = ('api_url', 'url', 'id', 'name', 'photo', 'description', 'phone', 'email', 'top_seller', 'date_hired')
    
    def get_url(self, obj):
        return f'/realtor/{obj.id}/'
