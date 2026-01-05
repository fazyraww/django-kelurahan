from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router ini untuk ViewSet (otomatis buat endpoint list, detail, dll)
router = DefaultRouter()
router.register(r'warga-vset', views.WargaViewSet, basename='warga-vset')

urlpatterns = [
    path('', views.WargaListView.as_view(), name='warga-list'),
    path('tambah/', views.WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', views.WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', views.WargaUpdateView.as_view(), name='warga-edit'), 
    path('<int:pk>/hapus/', views.WargaDeleteView.as_view(), name='warga-hapus'),
    
    path('pengaduan/', views.PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', views.PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', views.PengaduanUpdateView.as_view(), name='pengaduan-edit'),   
    path('pengaduan/<int:pk>/hapus/', views.PengaduanDeleteView.as_view(), name='pengaduan-hapus'), 
    path('api/warga/', views.WargaListAPIView.as_view(), name='api-warga-list'),
    path('api/aduan/', views.PengaduanListAPIView.as_view(), name='api-aduan-list'),
    path('api/', include(router.urls)),
]