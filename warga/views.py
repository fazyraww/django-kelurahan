from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Warga, Pengaduan
from .serializers import WargaSerializer, PengaduanSerializer
from .forms import WargaForm, PengaduanForm

# --- TAMPILAN WEB (HTML) ---
# Tidak ada perubahan besar di sini, sudah benar.
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html' # Pastikan template ini ada

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'  
    context_object_name = 'object_list' 

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list') 

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'  
    success_url = reverse_lazy('pengaduan-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' 
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')


# --- API VIEWS (JSON) ---

# Menggunakan ListCreateAPIView supaya di /api/warga/ muncul form POST (tambah data)
class WargaListAPIView(ListCreateAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [AllowAny] # Supaya bisa diakses tanpa login saat testing

# Menggunakan RetrieveUpdateDestroyAPIView supaya bisa GET detail, PUT (edit), & DELETE via API
class WargaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [AllowAny]

class PengaduanListAPIView(ListCreateAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
    permission_classes = [AllowAny]

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer
    permission_classes = [AllowAny] # Set ke IsAuthenticated jika ingin wajib login
    
# ViewSet tetap dipertahankan jika kamu ingin fitur pencarian/filter yang canggih
class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticated] # Khusus ini wajib login
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']