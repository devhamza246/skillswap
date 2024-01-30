from django.urls import path, re_path
from dashboards import views

# from dashboards.views import (
#     dashboard_view,
#     ProfileUpdateView,
#     NotificationListView,
#     NotificationDeleteView,
# )

app_name = "dashboards"

urlpatterns = [
    # The home page
    path("", views.index, name="home"),
    # Matches any html file
    re_path(r"^.*\.*", views.pages, name="pages"),
]
