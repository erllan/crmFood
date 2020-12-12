from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.GetAddUser.as_view()),
    path('meals/', views.ApiMelas.as_view()),
    path('mealsByCategory/<int:id_object>', views.MealsByCategory.as_view()),
    path('login/<login>/<password>', views.LoginUserClass.as_view()),
    path('tables/', views.ApiTables.as_view()),
    path('roles/', views.ApiRoles.as_view()),
    path('departments/', views.ApiDepartament.as_view()),
    path('mealCategories/', views.ApiCategory.as_view()),
    path('categoriesByDepartment/<int:id_object>', views.CategoriesByDepartment.as_view()),
    path('statuses/', views.ApiStatus.as_view()),
    path('orders/', views.OrderClass.as_view()),
    path('check/', views.Chek.as_view()),
    path('changePassword/', views.ChangePassword.as_view()),
]
