"""
URL configuration for lms_backend project.

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
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

SchemaView = get_schema_view(
    openapi.Info(
        title="LMS API",
        default_version="v1",
        description="This API details the necessary endpoints.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("", RedirectView.as_view(url="redoc/", permanent=False)),
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        SchemaView.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "swagger.json/",
        SchemaView.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]

admin.site.site_header = "LMS ADMIN"
admin.site.site_title = "LMS Admin Portal"
admin.site.index_title = "LMS Admin Portal"
