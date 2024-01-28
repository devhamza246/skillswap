"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ckeditor_uploader import views as ckeditor_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboards.urls")),
    path("community/", include("community.urls")),
    path("feedback/", include("feedback.urls")),
    path("matching/", include("matching.urls")),
    path("messaging/", include("messaging.urls")),
    path("profiles/", include("profiles.urls")),
    path("progress_tracking/", include("progress_tracking.urls")),
    path("scheduling/", include("scheduling.urls")),
    path("accounts/", include("allauth.urls")),
    path(
        "ckeditor/upload/",
        login_required(ckeditor_views.upload),
        name="ckeditor_upload",
    ),
    path(
        "ckeditor/browse/",
        never_cache(login_required(ckeditor_views.browse)),
        name="ckeditor_browse",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
