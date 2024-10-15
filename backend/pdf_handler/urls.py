from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from pdf_handler.views import PDFDocumentViewSet
from .views import create_pdf_document, get_pdf_documents, get_pdf_document, update_pdf_document, delete_pdf_document

# router = DefaultRouter()
# router.register(r'pdfs', PDFDocumentViewSet)

urlpatterns = [
    # path('pdfs/', include(router.urls)),
    path('pdf-documents/', create_pdf_document, name='create_pdf_document'),
    path('pdf-documents/', get_pdf_documents, name='get_pdf_documents'),
    path('pdf-documents/<int:pk>/', get_pdf_document, name='get_pdf_document'),
    path('pdf-documents/<int:pk>/', update_pdf_document, name='update_pdf_document'),
    path('pdf-documents/<int:pk>/', delete_pdf_document, name='delete_pdf_document'),
]
