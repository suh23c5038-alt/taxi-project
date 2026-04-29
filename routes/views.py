from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Station, Route

# 1. الصفحة الرئيسية: عرض جميع الرحلات
def index(request):
    return render(request, "routes/index.html", {
        "routes": Route.objects.all()
    })

# 2. صفحة تفاصيل الرحلة
def route(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
    return render(request, "routes/route.html", {
        "route": route,
        "passengers": route.passengers.all(),
        # التحقق إذا كان المستخدم الحالي قد حجز بالفعل
        "is_booked": route.passengers.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    })

# 3. صفحة تسجيل مستخدم جديد
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# 4. عملية الحجز
@login_required
def book(request, route_id):
    if request.method == "POST":
        route = get_object_or_404(Route, pk=route_id)
        route.passengers.add(request.user)
        return redirect("route", route_id=route.id)
    return redirect("index")

# 5. عملية إلغاء الحجز
@login_required
def unbook(request, route_id):
    if request.method == "POST":
        route = get_object_or_404(Route, pk=route_id)
        route.passengers.remove(request.user)
        return redirect("route", route_id=route.id)
    return redirect("index")

# 6. صفحة رحلاتي (الميزة الجديدة)
@login_required
def my_trips(request):
    # جلب الرحلات التي حجز فيها المستخدم الحالي
    user_routes = request.user.routes.all()
    return render(request, "routes/my_trips.html", {
        "routes": user_routes
    })
@login_required
def my_trips(request):
    # جلب الرحلات التي حجز فيها المستخدم الحالي
    user_routes = request.user.routes.all()
    return render(request, "routes/my_trips.html", {
        "routes": user_routes
    })