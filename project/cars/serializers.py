from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import Car, Owner

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    brand = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    price = serializers.IntegerField(validators=[MinValueValidator(0)])
    fuel_type = serializers.ChoiceField(

        choices=[
            ('petrol', 'Benzin'),
            ('diesel', 'Dizel'),
            ('electric', 'Elektro'),
            ('hybrid', 'Gibrid'),
        ]
    )
    mileage = serializers.IntegerField(validators=[MinValueValidator(0)])

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class OwnerSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(validators=[MinValueValidator(0)])
    phone_number = serializers.CharField(max_length=100)
    car_id = serializers.IntegerField()

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance