from django.urls import path
from version.apps import VersionConfig
from version.views import VersionListView, VersionDetailView, VersionCreateView, VersionUpdateView

app_name = VersionConfig.name

urlpatterns = [
    path('', VersionListView.as_view(), name='version_list'),
    path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('create/', VersionCreateView.as_view(), name='version_create'),
    path('update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
]
