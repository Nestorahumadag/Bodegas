from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserRegisterForm
from django.views.generic import DetailView, TemplateView
from .models import Noticia,TipoBodega, Like
import uuid

class IndexView(View):
    def get(self, request):
        noticias = Noticia.objects.all().order_by('-fecha_publicacion')
        noticias_con_likes = []

        for noticia in noticias:
            ha_dado_like = False
            if request.user.is_authenticated:
                ha_dado_like = noticia.likes.filter(usuario=request.user).exists()
            noticias_con_likes.append({
                'noticia': noticia,
                'ha_dado_like': ha_dado_like
            })

        return render(request, 'index.html', {'noticias_con_likes': noticias_con_likes})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'logout.html')
    
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después de un registro exitoso
        return render(request, 'register.html', {'form': form})
    
from django.views.generic import DetailView
from .models import Noticia, Like

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia_detail.html'
    context_object_name = 'noticia'
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Verificar si el usuario está autenticado antes de comprobar el like
        if user.is_authenticated:
            context['ha_dado_like'] = Like.objects.filter(usuario=user, noticia=self.object).exists()
        else:
            context['ha_dado_like'] = False  # No ha dado like si no está autenticado

        return context


class CotizarView(View):
    def get(self, request):
        tipos_bodega = TipoBodega.objects.all()  # Obtenemos todos los tipos de bodegas
        print(tipos_bodega)  # Esto debería imprimir los tipos de bodega en la consola del servidor
        return render(request, 'cotizar.html', {'tipos_bodega': tipos_bodega})

class AgregarBodegaView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado

        tipo_bodega_id = request.POST.get('tipo_bodega')
        tipo_bodega = get_object_or_404(TipoBodega, id=tipo_bodega_id)
        
        # Obtener o inicializar la lista de bodegas en la sesión
        carrito = request.session.get('carrito', [])
        
        # Corregir el carrito existente asegurando que todos los elementos tengan un UUID
        for item in carrito:
            if 'uuid' not in item:
                item['uuid'] = str(uuid.uuid4())

        # Añadir la bodega seleccionada al carrito con un ID único
        carrito.append({
            'uuid': str(uuid.uuid4()),  # Genera un ID único para cada bodega en el carrito
            'id': tipo_bodega.id,
            'tipo': tipo_bodega.tipo,
            'metros_cuadrados': tipo_bodega.metros_cuadrados,
            'precio_mensual': tipo_bodega.precio_mensual,
        })
        
        # Guardar el carrito actualizado en la sesión
        request.session['carrito'] = carrito
        
        return redirect('cotizacion_resultado')

class EliminarBodegaView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado
        
        # Obtener el UUID de la bodega que se quiere eliminar
        bodega_uuid = request.POST.get('bodega_uuid')
        
        # Obtener el carrito de la sesión
        carrito = request.session.get('carrito', [])
        
        # Imprimir para depuración
        print("Carrito antes de eliminar:", carrito)
        print("UUID para eliminar:", bodega_uuid)
        
        # Filtrar el carrito para eliminar la bodega específica por su UUID
        nuevo_carrito = [item for item in carrito if item.get('uuid') != bodega_uuid]
        
        # Comprobar si algo cambió en el carrito
        if len(carrito) == len(nuevo_carrito):
            print("No se encontró el UUID en el carrito.")
        else:
            print("Elemento eliminado del carrito.")
        
        # Guardar el carrito actualizado en la sesión
        request.session['carrito'] = nuevo_carrito
        
        return redirect('cotizacion_resultado')

class CotizacionResultadoView(View):
    def get(self, request, *args, **kwargs):
        carrito = request.session.get('carrito', [])
        total_precio = sum(item['precio_mensual'] for item in carrito)
        return render(request, 'cotizacion_resultado.html', {'carrito': carrito, 'total_precio': total_precio})
    
class LikeView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirige al login si el usuario no está autenticado

        noticia_id = request.POST.get('noticia_id')
        print(f"Received noticia_id: {noticia_id}")  # Depuración

        if not noticia_id:
            return redirect('index')  # Redirige a index si noticia_id está vacío

        noticia = get_object_or_404(Noticia, id=noticia_id)

        # Manejo del like
        like, created = Like.objects.get_or_create(usuario=request.user, noticia=noticia)
        if not created:
            like.delete()  # Si ya existe un like, se elimina (unlike)

        # Redirigir de nuevo a la página desde donde se envió la solicitud
        next_url = request.POST.get('next', 'index')
        if next_url == 'noticia_detail':
            return redirect('noticia_detail', pk=noticia.id)
        return redirect(next_url)
