
from django.contrib import admin 
from django.urls import path
from MySql_CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"), # localhost:8000
    path('insert/',views.insert),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]