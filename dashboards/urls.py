from django.urls import path, re_path
from dashboards import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "dashboards"

urlpatterns = [
    # The home page
    path("", views.index, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Match any html file (this should come last)
urlpatterns += [re_path(r"^.*\.*", views.pages, name="pages")]
