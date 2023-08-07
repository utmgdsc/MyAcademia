from django.urls import path, include
from .views import TestDegreeExplorerView
urlpatterns = [
    path('testDegreeExplorer/', TestDegreeExplorerView.as_view(), name='testDegreeExplorer') # custom endpoint for testing the degree explorer
]