from rest_framework.views import APIView
from .models import *
from django.contrib.auth import authenticate
from .serializers import (GetAllUserSerializer, AddUserSerializer,
                          LoginTokenSerializer, TableSerializer, SerializerRole, SerializerDepartament,
                          SerializerCategory, SerializerStatus, SerializerMeals, SerializerOrder, SerializerGetOrder,
                          SerializerCheck
                          )
from rest_framework.response import Response
import jwt
from rest_framework import status

"""USER"""


class GetAddUser(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = GetAllUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = AddUserSerializer(data=request.data)

        if user.is_valid():
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id_object = request.data.get('id')
        user = User.objects.get(id=id_object)
        user.delete()
        return Response('deleted')

    def put(self, request):
        data = request.data
        user = User.objects.get(id=data['id'])
        serializer = AddUserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('error')


class LoginUserClass(APIView):

    def get(self, request, login, password):
        password = password.strip()
        user = authenticate(login=login, password=password)
        if user:
            serializer = LoginTokenSerializer(user)
            return Response(serializer.data)
        else:
            return Response('error')


class ChangePassword(APIView):
    def get(self, request):
        token = request.data.get('token')
        token = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
        user = User.objects.get(id=token['id'])
        oldpassword = request.data.get('oldpassword')
        newpass = request.data.get('newpassword')
        if user.check_password(oldpassword):
            user.set_password(newpass)
            user.save()
            return Response('')
        else:
            return Response('old password is incorrect')


"""meals"""


class ApiMelas(APIView):

    def get(self, request):
        meals = Meal.objects.all()
        serializer = SerializerMeals(meals, many=True)
        return Response(serializer.data)

    def post(self, request):
        meals = SerializerMeals(data=request.data)

        if meals.is_valid():
            meals.save()
            return Response('created')
        else:
            return Response('error')

    def delete(self, request):
        id_object = request.data.get('id')
        meals = Meal.objects.get(id=id_object)
        meals.delete()
        return Response('deleted')

    def put(self, request):
        data = request.data
        meals = Meal.objects.get(id=data['id'])
        serializer = SerializerMeals(meals, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('error')


class MealsByCategory(APIView):
    def get(self, request, id_object):
        category = Category.objects.get(id=id_object)
        meals = category.meal_set.all()
        serializer = SerializerMeals(meals, many=True)
        return Response(serializer.data)


"""API Tables"""


class ApiTables(APIView):

    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

    def post(self, request):
        table = TableSerializer(data=request.data)

        if table.is_valid():
            table.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id_object = request.data.get('id')
        table = Table.objects.get(id=id_object)
        table.delete()
        return Response('deleted')


"""Api Roles"""


class ApiRoles(APIView):

    def get(self, request):
        tables = Role.objects.all()
        serializer = SerializerRole(tables, many=True)
        return Response(serializer.data)

    def post(self, request):
        role = SerializerRole(data=request.data)

        if role.is_valid():
            role.save()
            return Response('created')
        else:
            return Response('error')

    def delete(self, request):
        id_object = request.data.get('id')
        role = Role.objects.get(id=id_object)
        role.delete()
        return Response('deleted')


"""Api Departament"""


class ApiDepartament(APIView):

    def get(self, request):
        department = Department.objects.all()
        serializer = SerializerDepartament(department, many=True)
        return Response(serializer.data)

    def post(self, request):
        dep = SerializerDepartament(data=request.data)

        if dep.is_valid():
            dep.save()
            return Response('created')
        else:
            return Response('error')

    def delete(self, request):
        id_object = request.data.get('id')
        dep = Department.objects.get(id=id_object)
        dep.delete()
        return Response('deleted')


"""Api Category"""


class ApiCategory(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = SerializerCategory(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        category = SerializerCategory(data=request.data)

        if category.is_valid():
            category.save()
            return Response('created')
        else:
            return Response('error')

    def delete(self, request):
        id_object = request.data.get('id')
        category = Category.objects.get(id=id_object)
        category.delete()
        return Response('deleted')


class CategoriesByDepartment(APIView):
    def get(self, request, id_object):
        departament = Department.objects.get(id=id_object)
        categories = departament.category_set.all()
        serializer = SerializerCategory(categories, many=True)
        return Response(serializer.data)


"""Api Status"""


class ApiStatus(APIView):

    def get(self, request):
        status = Status.objects.all()
        serializer = SerializerStatus(status, many=True)
        return Response(serializer.data)

    def post(self, request):
        status = SerializerStatus(data=request.data)

        if status.is_valid():
            status.save()
            return Response('created')
        else:
            return Response('error')

    def delete(self, request):
        id_object = request.data.get('id')
        status = Status.objects.get(id=id_object)
        status.delete()
        return Response('deleted')


"""Api Order"""


class OrderClass(APIView):
    def post(self, request):
        order = SerializerOrder(data=request.data)

        if order.is_valid():
            order.save()
            return Response('created')
        else:
            return Response('error')

    def get(self, request):
        order = Order.objects.all()
        serializer = SerializerGetOrder(order, many=True)
        return Response(serializer.data)

    def delete(self, request):
        id_object = request.data.get('id')
        order = Order.objects.get(id=id_object)
        order.delete()
        return Response('deleted')


"""Check"""


class Chek(APIView):
    def get(self, request):
        check = Check.objects.all()
        serializer = SerializerCheck(check, many=True)
        return Response(serializer.data)

    def post(self, request):
        id = request.data.get('orderid')
        order = Order.objects.get(id=id)
        check = Check.objects.create(orderid=order)
        serializer = SerializerCheck(check)
        return Response(serializer.data)

    def delete(self, request):
        id_object = request.data.get('id')
        check = Check.objects.get(id=id_object)
        check.delete()
        return Response('deleted')
