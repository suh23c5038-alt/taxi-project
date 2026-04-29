from django.urls import path
from . import views

urlpatterns = [
    # رابط الصفحة الرئيسية (قائمة الرحلات)
    path("", views.index, name="index"),
    # رابط صفحة تفاصيل الرحلة (باستخدام رقم الرحلة id)
    path("<int:route_id>", views.route, name="route"),
    # رابط تسجيل المستخدمين الجدد
    path("register", views.register, name="register"),
    # رابط عملية الحجز
    path("<int:route_id>/book", views.book, name="book"),
    # رابط عملية إلغاء الحجز
    path("<int:route_id>/unbook", views.unbook, name="unbook"),
]