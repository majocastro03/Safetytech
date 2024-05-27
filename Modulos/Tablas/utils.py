from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from .models import Bitacora, Empleado, Instalacion, Usuario



#-------------------------------------------
def generar_pdfEM(request):
    # Recuperar los datos de la tabla de la base de datos
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Contenido del PDF
    contenido = []

    # Agregar un título al PDF
    titulo = Paragraph("Listado Empleados", styles['Heading1'])
    contenido.append(titulo)

    # Recuperar los datos de la tabla de la base de datos
    datos = Empleado.objects.all()

    # Crear la tabla con los datos
    tabla_datos = []
    for dato in datos:
        tabla_datos.append([dato.Identificacion, dato.nombre, dato.email, dato.cargo, dato.fecha_registro, dato.codadmin])
    tabla = Table(tabla_datos)

    # Establecer el estilo de la tabla
    estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.bisque),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    tabla.setStyle(estilo_tabla)

    contenido.append(tabla)

    # Construir el PDF
    pdf.build(contenido)
    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content

#--------------------------------------

def generar_pdfIN(request):
    # Recuperar los datos de la tabla de la base de datos
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Contenido del PDF
    contenido = []

    # Agregar un título al PDF
    titulo = Paragraph("Listado Instalacion", styles['Heading1'])
    contenido.append(titulo)

    # Recuperar los datos de la tabla de la base de datos
    datos = Instalacion.objects.all()

    # Crear la tabla con los datos
    tabla_datos = []
    for dato in datos:
        tabla_datos.append([dato.codInstalacion, dato.nombre, dato.fecha_instalacion])
    tabla = Table(tabla_datos)

    # Establecer el estilo de la tabla
    estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.bisque),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    tabla.setStyle(estilo_tabla)

    contenido.append(tabla)

    # Construir el PDF
    pdf.build(contenido)
    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content

#------------------------------

def generar_pdfBI(request):
    # Recuperar los datos de la tabla de la base de datos
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Contenido del PDF
    contenido = []

    # Agregar un título al PDF
    titulo = Paragraph("Listado Bitacora", styles['Heading1'])
    contenido.append(titulo)

    # Recuperar los datos de la tabla de la base de datos
    datos = Bitacora.objects.all()

    # Crear la tabla con los datos
    tabla_datos = []
    for dato in datos:
        tabla_datos.append([dato.codBitacora, dato.nombre, dato.estado, dato.cantidad, dato.observaciones, dato.ubicacion, dato.nivel_riesgo, dato.fecha_registro, dato.codInstalacion])
    tabla = Table(tabla_datos)

    # Establecer el estilo de la tabla
    estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.darkred),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.bisque),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    tabla.setStyle(estilo_tabla)

    contenido.append(tabla)

    # Construir el PDF
    pdf.build(contenido)
    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content