from django.urls import path, re_path
from dashboards import views

# from dashboards.views import (
#     dashboard_view,
#     ProfileUpdateView,
#     NotificationListView,
#     NotificationDeleteView,
# )

app_name = "dashboards"

# urlpatterns = [
#     path("profile/<int:pk>/", ProfileUpdateView.as_view(), name="user_profile"),
#     path("", view=dashboard_view, name="dashboard"),
#     path(
#         "notification-list/", NotificationListView.as_view(), name="notification_list"
#     ),
#     path(
#         "notification-delete/<int:pk>/",
#         NotificationDeleteView.as_view(),
#         name="notification_delete",
#     ),
# ]

urlpatterns = [
    # The home page
    path("", views.index, name="home"),
    # Matches any html file
    re_path(r"^.*\.*", views.pages, name="pages"),
]
