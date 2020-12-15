from rest_framework import serializers
from .models import *

"""serializers User"""


class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "name", "surname", "login", "email", "roleid", "date_joined", "phone", 'password']


class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "surname", "login", "email", "roleid", "phone", 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['roleid', 'token']


"""serializers Table"""


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


"""Serializer Role"""


class SerializerRole(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


"""Serializer Departament"""


class SerializerDepartament(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


"""Serializer Category"""


class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


"""Serializer Status"""


class SerializerStatus(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


"""Serializer Meal"""


class SerializerMeals(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


"""Serializer Order and Meals"""


class SerializerPostOrderMeal(serializers.ModelSerializer):
    class Meta:
        model = OrderMeal
        fields = ('meal', 'count')


class SerializerGetOrderMeal(serializers.ModelSerializer):
    class Meta:
        model = OrderMeal
        fields = ('id', 'name', 'count', 'total', 'price')


class SerializerOrder(serializers.ModelSerializer):
    ordermeal = SerializerPostOrderMeal(many=True)

    class Meta:
        model = Order
        fields = ('tableid', 'ordermeal', 'waiterid')

    def create(self, validated_data):
        meals_data = validated_data.pop('ordermeal')
        print(validated_data)
        order = Order.objects.create(**validated_data)
        for a in meals_data:
            order.ordermeal.create(**a)
        return order


class SerializerGetOrder(serializers.ModelSerializer):
    ordermeal = SerializerGetOrderMeal(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'tableid', 'waiterid', 'table_name', 'date', 'ordermeal')


"""Check"""


class SerializerCheck(serializers.ModelSerializer):
    meals = SerializerGetOrderMeal(many=True, read_only=True)

    class Meta:
        model = Check
        fields = ('id', 'orderid', 'date', 'total', 'meals')
