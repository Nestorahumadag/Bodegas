from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, LoginView, LogoutView, NoticiaDetailView, CotizarView, AgregarBodegaView, LikeView, RegisterView, CotizacionResultadoView, EliminarBodegaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('cotizar/', CotizarView.as_view(), name='cotizar'),
    path('agregar_bodega/', AgregarBodegaView.as_view(), name='agregar_bodega'),
    path('like/', LikeView.as_view(), name='like'),
    path('cotizacion_resultado/', CotizacionResultadoView.as_view(), name='cotizacion_resultado'),
    path('eliminar_bodega/', EliminarBodegaView.as_view(), name='eliminar_bodega'),
     path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('like/', LikeView.as_view(), name='like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)