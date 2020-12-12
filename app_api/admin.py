from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Meal)
admin.site.register(OrderMeal)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Check)

