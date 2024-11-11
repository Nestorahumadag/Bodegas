# Proyecto Bodegas

Este archivo contiene las instrucciones necesarias para configurar y ejecutar el proyecto "Bodegas", 
así como información sobre las dependencias y los usuarios de prueba.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrese de tener instaladas las siguientes herramientas:

- Python 3.11.7 (o superior)
- Django 5.1
- PostgreSQL
- Virtualenv (recomendado)

## Instalación

1. **Extraer el contenido del archivo ZIP**:

   Extraiga el contenido del archivo ZIP en una carpeta de su elección.

2. **Crear y activar un entorno virtual:**
    
    Entorno virtual hecho en mkvirtualenv, llamado (examenfinal)

3.-**Instalar dependencias**

    Se adjunta el archivo de requerimientos para su instalacion
    - requerimientos.txt




# Datos de Usuarios
    **Superusuario
        Nombre de usuario: admin
        Correo electrónico: admin@admin.cl
        Contraseña: admin
    
    **Usuarios de Prueba
    ================================

    Nombre de usuario: Nestor

    Correo electrónico: ne.ahumada53@gmail.com

    Contraseña: praxis2024

    =================================

    Nombre de usuario: Eduardo

    Correo electrónico: ne.ahumada53@gmail.com

    Contraseña: praxis2024

    =================================

    Nombre de usuario: Fran

    Correo electrónico: fran@fran.cl

    Contraseña: praxis2024

 **Carpeta de Medios: Las imágenes de las noticias se almacenan en la carpeta noticias/

**Usuario y contraseña base de datos
 DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bodegasdb',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}