from .import views
from django.urls import path

urlpatterns = [
    
    path("",views.home,name="home"),
    path('upload/', views.upload_images, name='upload_images'),
    path('scanne_page/', views.scanner_page, name='scanner_page'),
    path('scan_single_document/', views.scan_single_document, name='scan_single_document'),
    path('scan_multiple_documents/', views.scan_multiple_documents, name='scan_multiple_documents'),
]


