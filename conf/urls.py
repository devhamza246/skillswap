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
from rest_framework import routers
from ckeditor_uploader import views as ckeditor_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from accounts.urls import router as accounts_router
from matching.urls import router as matching_router
from scheduling.urls import router as scheduling_router
from feedback.urls import router as feedback_router

router = routers.DefaultRouter()
router.registry.extend(accounts_router.registry)
router.registry.extend(matching_router.registry)
router.registry.extend(scheduling_router.registry)
router.registry.extend(feedback_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("community/", include("community.urls")),
    path("feedback/", include("feedback.urls")),
    path("matching/", include("matching.urls")),
    path("messaging/", include("messaging.urls")),
    path("progress_tracking/", include("progress_tracking.urls")),
    path("scheduling/", include("scheduling.urls")),
    path("", include("accounts.urls")),
    path("", include("dashboards.urls")),
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
]
