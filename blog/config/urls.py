"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog.views import blog_list, blog_detail, blog_create, blog_update, blog_delete
from member.views import sign_up, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", blog_list, name="blog_list"),
    path("<int:pk>/", blog_detail, name="blog_detail"),
    path("create/", blog_create, name="blog_create"),
    path("<int:pk>/update/", blog_update, name="blog_update"),
    path("<int:pk>/delete/", blog_delete, name="blog_delete"),

    # auth
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", sign_up, name="sign_up"),
    path("login/", login, name="login"),
]
