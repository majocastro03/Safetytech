"""safetytech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Modulos.Tablas.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from Modulos.Front.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('', landing),
    path('conocenos/', conocenos),
    path('contacto/', Contacto),
    path('contactar/', contactar),
    #------------------------------------------
    path('usuario/', nuevoUsuario),
    path('empleado/', agregaEmpleado, name="empleado"),
    path('bitacora/', agregaBitacora),
    path('instalacion/', agregaInstalacion),
    #----------------------------------------------
    path('lempleado/', ListadosEmpleado, name="lempleado"),
    path("modificarempleado/", modificar_empleado, name="modificar_empleado"),
    path("elimempelado/", eliminar_empleado),
    #---------------------------------------------
    path('linsta/', ListadosInstalacion),
    path("modificarinsta/", modificar_instalacion, name="modificar_instalacion"),
    path("eliminsta/", eliminar_instalacion),
    #---------------------------------------------
    path('lbitacora/', ListadosBitacora),
    path("modificarbitacora/", modificar_Bitacora, name="modificar_Bitacora"),
    path("elimbitacora/", eliminar_Bitacora),
    #---------------------------------------------
    path('lusu/', ListadoUsuario),
    path("modificarusu/", modificar_Usuario, name="modificar_Usuario"),
    path("elimusu/", eliminar_Usuario),
    #---------------------------------
    path("searchusu/", buscarUsuario, name="searchusu"),
    path("searchbit/", buscarBitacora, name="searchbit"),
    path("searchemp/", buscarEmpleado, name="searchemp"),
    path("searchins/", buscarInstalacion, name="searchins"),
#---------------------------------
    path('descargar_pdfe/', vista_pdfEM, name='descargar_pdfe'), 
    path('descargar_pdfin/', vista_pdfIN, name='descargar_pdfin'),
    path('descargar_pdfbi/', vista_pdfBI, name='descargar_pdfbi'),

    #-----------------------------------------
    path('pdf/', process_pdf, name='pdf'),
    #------------------------------------
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),

    #-----------------
    path('calendario', calen, name='index'), 
    path('all_events/', all_events, name='all_events'), 
    path('add_event/', add_event, name='add_event'), 
    path('update/', update, name='update'),
    path('remove/', remove, name='remove'),

    #-------------------------
    path("perfil", cuenta),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
