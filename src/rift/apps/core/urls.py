from django.urls import path

from .views import register_students

app_name = "core"

urlpatterns = [
    path("", register_students, name="register_students"),
]
