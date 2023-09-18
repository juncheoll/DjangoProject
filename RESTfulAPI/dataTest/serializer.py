from rest_framework import serializers
from .models import Users

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["name", "address", "phone_number", "job_position", "age", "dateTimeOfPosting"]