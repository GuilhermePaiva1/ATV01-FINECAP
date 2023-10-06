from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("core.urls", namespace="core")),
    path("", include("stands.urls", namespace="stands")),
    path("", include("main.urls", namespace="reservas")),
]
