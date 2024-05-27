from django.shortcuts import render, redirect, get_object_or_404

from django.core.mail import send_mail

from django.contrib import messages

import re

from django.conf import settings

from django.http import HttpResponse

from .forms import *

from .models import *

from django.db.models import Q

from django.http import JsonResponse

from .utils import *

from django.http import FileResponse

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login

from PyPDF2 import PdfReader

from reportlab.lib.pagesizes import letter

from reportlab.pdfgen import canvas

from reportlab.platypus import Paragraph, SimpleDocTemplate

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Create your views here.

#PDF



@login_required

def vista_pdfEM(request):

    # Llama a la función generar_pdf

    pdf = generar_pdfEM(request)

    return HttpResponse(pdf, content_type='application/pdf')

@login_required

def vista_pdfIN(request):

    # Llama a la función generar_pdf

    pdf = generar_pdfIN(request)

    return HttpResponse(pdf, content_type='application/pdf')

@login_required

def vista_pdfBI(request):

    # Llama a la función generar_pdf

    pdf = generar_pdfBI(request)

    return HttpResponse(pdf, content_type='application/pdf')






#----------------------------------------

@login_required

def ListadosEmpleado(request):

	empleado=Empleado.objects.all()

	return render(request, "lEmpleado.html",{"empleado":empleado})


@login_required

def buscarEmpleado(request):

	busqueda=request.GET.get("buscar")

	empleado=Empleado.objects.all()

	if busqueda:

		empleado = Empleado.objects.filter(

			Q(codEmpleado__icontains = busqueda) |

			Q(Identificacion__icontains = busqueda) | #or (o)

			Q(nombre__icontains = busqueda) |

			Q(email__icontains = busqueda) |

			Q(cargo__icontains = busqueda)	|

			Q(fecha_registro__icontains = busqueda) |

			Q(codadmin = busqueda) 
			).distinct()


	return render(request, "lEmpleado.html", {"empleado":empleado})


@login_required

def modificar_empleado(request):   


	empleadoo=get_object_or_404(Empleado, codEmpleado=request.GET['codEmpleado'])#busca un elemento


	data={

		'form':EmpleadoForm(instance=empleadoo)

	}


	if request.method=='POST':

		formulario=EmpleadoForm(data=request.POST, instance=empleadoo, files=request.FILES)

		if formulario.is_valid():

			formulario.save()

			messages.success(request, "Modificado Correctamente")

			data["mensaje"]="Archivo Modificado"

		else:

			data["form"]=formulario

			data["mensaje"]="El archivo no existe"

		data["form"]=formulario

	return render(request, 'modificar.html', data) 


@login_required

def eliminar_empleado(request):

	empleado = get_object_or_404(Empleado, codEmpleado=request.GET['codEmpleado'])
	empleado.delete()

	messages.success(request, "Eliminado Correctamente")

	return redirect(to="../lempleado")


#------------------------------------------------------------------------------------------------


@login_required

def ListadosInstalacion(request):

	instala=Instalacion.objects.all()

	return render(request, "lInstala.html",{"instala":instala})


@login_required

def buscarInstalacion(request):

	busqueda=request.GET.get("buscar")

	instala=Instalacion.objects.all()

	if busqueda:

		instala = Instalacion.objects.filter(

			Q(codInstalacion__icontains = busqueda) | #or (o)

			Q(nombre__icontains = busqueda) |

			Q(fecha_instalacion__icontains = busqueda)
			).distinct()


	return render(request, "lInstala.html", {"instala":instala})


@login_required

def modificar_instalacion(request):   


	instalaa=get_object_or_404(Instalacion, codInstalacion=request.GET['codInstalacion'])#busca un elemento


	data={

		'form':InstalacionForm(instance=instalaa)

	}


	if request.method=='POST':

		formulario=InstalacionForm(data=request.POST, instance=instalaa, files=request.FILES)

		if formulario.is_valid():

			formulario.save()

			messages.success(request, "Modificado Correctamente")

			data["mensaje"]="Archivo Modificado"

		else:

			data["form"]=formulario

			data["mensaje"]="El archivo no existe"

		data["form"]=formulario

	return render(request, 'modificar.html', data) 


@login_required

def eliminar_instalacion(request):

	instala = get_object_or_404(Instalacion, codInstalacion=request.GET['codInstalacion'])
	instala.delete()

	messages.success(request, "Eliminado Correctamente")

	return redirect(to="../linsta")

#------------------------------------------------------------------------------------------------

@login_required

def ListadosBitacora(request):

	bitacora=Bitacora.objects.all()

	return render(request, "lBitacora.html",{"bitacora":bitacora})


@login_required

def buscarBitacora(request):

	busqueda=request.GET.get("buscar")

	bitacora=Bitacora.objects.all()

	if busqueda:

		bitacora = Bitacora.objects.filter(

			Q(codBitacora__icontains = busqueda) | #or (o)

			Q(nombre__icontains = busqueda) |

			Q(estado__icontains = busqueda) |

			Q(cantidad__icontains = busqueda) |

			Q(observaciones__icontains = busqueda) |

			Q(ubicacion__icontains = busqueda) |

			Q(nivel_riesgo__icontains = busqueda) |

			Q(fecha_registro__icontains = busqueda) |

			Q(codInstalacion = busqueda) 
			).distinct()


	return render(request, "lBitacora.html", {"bitacora":bitacora})


@login_required

def modificar_Bitacora(request):   


	bitacoraa=get_object_or_404(Bitacora, codBitacora=request.GET['codBitacora'])#busca un elemento


	data={

		'form':BitacoraForm(instance=bitacoraa)

	}


	if request.method=='POST':

		formulario=BitacoraForm(data=request.POST, instance=bitacoraa, files=request.FILES)

		if formulario.is_valid():

			formulario.save()

			messages.success(request, "Modificado Correctamente")

			data["mensaje"]="Archivo Modificado"

		else:

			data["form"]=formulario

			data["mensaje"]="El archivo no existe"

		data["form"]=formulario

	return render(request, 'modificar.html', data) 


@login_required

def eliminar_Bitacora(request):

	bitacora = get_object_or_404(Bitacora, codBitacora=request.GET['codBitacora'])

	bitacora.delete()

	messages.success(request, "Eliminado Correctamente")

	return redirect(to="../lbitacora")

#------------------------------------------------------------------------------------------------

@login_required

def nuevoUsuario(request):

	data = {

		'form': UsuarioForm()

	}
	

	if request.method == "POST":

		user_creation_form = UsuarioForm(data=request.POST)

		if user_creation_form.is_valid():

			user_creation_form.save()
			print(user_creation_form.errors)
			return redirect("inicio")

		data["mensaje"]=user_creation_form.errors

		data["form"]=user_creation_form
	

	return render(request, 'nuevo.html', data)


@login_required

def ListadoUsuario(request):

	usuario=Usuario.objects.all()

	return render(request, "lusu.html",{"usuario":usuario})

@login_required    

def modificar_Usuario(request):   


	usuario=get_object_or_404(Usuario, id=request.GET['codUser'])#busca un elemento


	data={

		'form':UsuarioForm(instance=usuario),

		'titulo': "Editar usuario"

	}


	if request.method=='POST':

		formulario=UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)

		if formulario.is_valid():

			formulario.save()

			messages.success(request, "Modificado Correctamente")

			data["mensaje"]="Archivo Modificado"

			return redirect(to="../lusu")

		else:

			data["form"]=formulario

			data["mensaje"]="El archivo no existe"

		data["form"]=formulario

	return render(request, 'modificar.html', data) 

@login_required

def buscarUsuario(request):

	busqueda=request.GET.get("buscar")

	usuario=Usuario.objects.all()

	if busqueda:

		usuario = Usuario.objects.filter(

			Q(id__icontains = busqueda) | #or (o)

			Q(first_name__icontains = busqueda) |

			Q(email__icontains = busqueda) |

            Q(telefono__icontains = busqueda) |#_

            Q(username__icontains = busqueda) #_
			).distinct()


	return render(request, "lusu.html", {"usuario":usuario})

@login_required

def eliminar_Usuario(request):

	usuario = get_object_or_404(Usuario, id=request.GET['id'])
	usuario.delete()

	messages.success(request, "Eliminado Correctamente")

	return redirect(to="../lusu")

#------------------------------------------------------------------------------------------------

@login_required

def agregaEmpleado(request):
    data = {
        'form': EmpleadoForm(),
        'titulo': "Agregar Empleado",
        'es_empleado': True,
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            empleado = formulario.save()
            process_pdf(request)  # Procesar el PDF
            data["mensaje"] = "Guardado correctamente"
            return redirect('empleado')
        else:
            data["form"] = formulario
            data["mensaje"] = "El formulario no es válido"
    
    return render(request, 'nuevo.html', data)


@login_required

def agregaBitacora(request):
	data={

		'form': BitacoraForm(),

        'titulo' : "Agregar Bitacora"
	}
	if request.method =='POST':
		formulario = BitacoraForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():

			formulario.save()

			data["mensaje"]="guardado correctamente"
		else:
			data["form"]=formulario
			data["mensaje"]="el archivo ya existe"
	return render(request, 'nuevo.html', data)

@login_required

def agregaInstalacion(request):

	data={

		'form': InstalacionForm(),

        'titulo' : "Agregar Instalacion"

	}


	if request.method =='POST':

		formulario = InstalacionForm(data=request.POST, files=request.FILES)

		if formulario.is_valid():

			formulario.save()

			data["mensaje"]="guardado correctamente"

		else:

			data["form"]=formulario

			data["mensaje"]="el archivo ya existe"

	return render(request, 'nuevo.html', data)    




@login_required

def inicio(request):

	return render(request, 'inicio.html')



@login_required

def logIn(request):

	return render(request, 'login.html')


@login_required

def cuenta(request):

	return render(request, 'cuenta.html')


#----------------------------------------------------------------------------------------------------




class MyLoginView(LoginView):

    redirect_authenticated_user = True
    

    def get_success_url(self):

        return reverse_lazy('inicio') 
    

    def form_invalid(self, form):

        messages.error(self.request,'Invalid username or password')

        return self.render_to_response(self.get_context_data(form=form))


#--------------------------------------------------------------------

def get_data_user(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ''
    
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        paragraphs = text.split('\n\n')
        for paragraph in paragraphs:
            extracted_text += paragraph + '\n' 
            
    name_pattern = r"PARROQUIA\sSAN\sPIO\sX\s(.+?)CC\s(\d+)\s\d+\sAÑOS.+?(\w+)$"
    name_match = re.search(name_pattern, extracted_text, re.DOTALL)
    if name_match:
        name = name_match.group(1).strip()
        document_number = name_match.group(2).strip()
        position = name_match.group(3).strip() 
      
        information_user = name, document_number, position  # Se pasa una lista como argumento al join()
        print(information_user)
        return information_user
    return None, None, None
  
    
#---------------------------------------------------------------------

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from reportlab.lib.units import inch  
def process_pdf(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        name, document_number, position = get_data_user(pdf_file)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Recomendaciones médicas laborales SG-SST.pdf"'
        fecha_actual = datetime.now().strftime("%d/%m/%Y")

        image_path = 'static/sources/logocolegio.jpg'  
        img = Image(image_path)
        img.drawHeight = 1.25 * inch 
        img.drawWidth = 1.25 * inch



		
        contenido_nueva_tabla = [
            ["De acuerdo al asunto en mención me permito remitir recomendaciones médicas laborales de acuerdo al examen médico ocupacional. Desde seguridad y salud en el trabajo estaremos atentos a su buen estado de salud."]
        ]
        styles = getSampleStyleSheet()
        estilo_normal = styles["Normal"]
        estilo_contenido = ParagraphStyle(
            name='ContenidoStyle',
            parent=estilo_normal,
            fontSize=10,
            leading=12
        )
        parrafos_contenido = [Paragraph(texto[0], estilo_contenido) for texto in contenido_nueva_tabla]
        data_tabla_informacion = [
            ["Fecha:", fecha_actual],
            ["Asunto:", "Recomendaciones medicas laborales"],
            ["Apellidos y nombres:", name],
            ["Documento de identificación:", document_number],
            ["Cargo:", "Sacristan"],
			["Responsable del SG-SST:", ""],
        ]
        data_tabla_texto = [
            parrafos_contenido, 
        ]
        data_tabla_recomendaciones = [
			["Recomendaciones Hábitos y \nEstilos de Vida Saludables", "HÁBITOS SALUDABLES, FORTALECIMIENTO MUSCULAR, \nCONTROL DE PESO, ACTIVIDAD FÍSICA AERÓBICA, \nHACER DEPORTE, DIETA BALANCEADA"],
			["Recomendaciones Médicas", "USAR CORRECCIÓN VISUAL, \n EXAMEN VISUAL DE CONTROL EN UN AÑO, \nAUDIOMETRÍA DE CONTROL EN UN AÑO"],
			["Recomendaciones Ocupacionales", "USO DE EPP, SVE VISUAL, \nSVE AUDITIVO"],
		]
        data_tabla_extra = [
			["Recomendaciones Médicas Laborales"],
		]
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.bisque),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        estilo_tabla_texto = TableStyle([
    		('BACKGROUND', (0, 0), (-1, -1), colors.bisque), 
    		('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    		('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    		('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    		('GRID', (0, 0), (-1, -1), 1, colors.black)
		]
		)
        estilo_tabla_extra = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        estilo_tabla_img = TableStyle([
    		('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
		]
		)
        data_tabla = [[img]]
        tabla_informacion = Table(data_tabla_informacion)
        tabla_texto = Table(data_tabla_texto)
        tabla_extra = Table(data_tabla_extra)
        tabla_recomendaciones = Table(data_tabla_recomendaciones)
        tabla_img = Table(data_tabla)
        tabla_informacion.setStyle(estilo_tabla)
        tabla_texto.setStyle(estilo_tabla_texto)
        tabla_extra.setStyle(estilo_tabla_extra)
        tabla_recomendaciones.setStyle(estilo_tabla_texto)
        tabla_img.setStyle(estilo_tabla_img)
        tabla_img._argW[0] = 400 
        doc = SimpleDocTemplate(response)

        content = [tabla_img, Spacer(1, 24), tabla_informacion, Spacer(1, 24), tabla_texto, Spacer(1, 24), tabla_extra, tabla_recomendaciones]
        doc.build(content)
		
        return response
   
    return render(request, 'pdf.html')


#-----------------------------------------------------------------

@login_required

def calen(request):  

    all_events = Events.objects.all()

    context = {

        "events":all_events,

    }

    return render(request,'calendario.html',context)
 

@login_required

def all_events(request):                                                                                                 

    all_events = Events.objects.all()                                                                                    

    out = []                                                                                                             

    for event in all_events:                                                                                             

        out.append({                                                                                                     

            'title': event.name,                                                                                         

            'id': event.id,                                                                                              

            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         

            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             

        })                                                                                                               
                                                                                                                      

    return JsonResponse(out, safe=False) 


@login_required 

def add_event(request):

    start = request.GET.get("start", None)

    end = request.GET.get("end", None)

    title = request.GET.get("title", None)

    event = Events(name=str(title), start=start, end=end)

    event.save()

    data = {}

    return JsonResponse(data)


@login_required 

def update(request):

    start = request.GET.get("start", None)

    end = request.GET.get("end", None)

    title = request.GET.get("title", None)

    id = request.GET.get("id", None)

    event = Events.objects.get(id=id)

    event.start = start

    event.end = end

    event.name = title

    event.save()

    data = {}

    return JsonResponse(data)


@login_required 

def remove(request):

    id = request.GET.get("id", None)

    event = Events.objects.get(id=id)

    event.delete()

    data = {}

    return JsonResponse(data)

