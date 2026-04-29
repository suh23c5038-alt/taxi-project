from django.urls import path
from . import views

urlpatterns = [
    # الصفحة الرئيسية لعرض الرحلات
    path("", views.index, name="index"),
    
    # صفحة تفاصيل الرحلة
    path("<int:route_id>", views.route, name="route"),
    
    # صفحة التسجيل
    path("register", views.register, name="register"),
    
    # روابط عمليات الحجز
    path("<int:route_id>/book", views.book, name="book"),
    path("<int:route_id>/unbook", views.unbook, name="unbook"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:route_id>", views.route, name="route"),
    path("register", views.register, name="register"),
    path("<int:route_id>/book", views.book, name="book"),
    path("<int:route_id>/unbook", views.unbook, name="unbook"),
    path("my_trips", views.my_trips, name="my_trips"), 
]