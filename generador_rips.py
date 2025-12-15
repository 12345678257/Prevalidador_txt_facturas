import streamlit as st
import pandas as pd
import os
from io import BytesIO
import zipfile

st.set_page_config(page_title="Generador de Archivos RIPS", page_icon="📄", layout="centered")

st.title("📄 Generador de Archivos RIPS")
st.markdown("---")

# Selector de tipo de archivo
tipo_archivo = st.radio(
    "Seleccione el tipo de archivo a generar:",
    ["Detalle", "Carátula"],
    horizontal=True
)

st.markdown("---")

uploaded_file = st.file_uploader("Seleccione el archivo Excel", type=['xlsx', 'xls'])

if uploaded_file is not None:
    try:
        # Determinar el nombre de la hoja y la columna según el tipo seleccionado
        if tipo_archivo == "Detalle":
            nombre_hoja = "Detalle"
            columna_factura = 7  # Columna 8 (índice 7)
            prefijo_archivo = "Archivo_Det"
            st.info(f"📋 Procesando hoja: **{nombre_hoja}** | Número de factura en columna **H (8)**")
        else:  # Carátula
            nombre_hoja = "Caratula"
            columna_factura = 1  # Columna 2 (índice 1)
            prefijo_archivo = "Archivo_Car"
            st.info(f"📋 Procesando hoja: **{nombre_hoja}** | Número de factura en columna **B (2)**")
        
        # Leer el archivo Excel
        df = pd.read_excel(uploaded_file, sheet_name=nombre_hoja)
        
        st.success(f"✅ Archivo cargado exitosamente: {uploaded_file.name}")
        st.write(f"**Total de filas:** {len(df)}")
        
        # Mostrar vista previa
        with st.expander("👁️ Ver vista previa de los datos"):
            st.dataframe(df.head(10))
        
        st.markdown("---")
        
        if st.button(f"🚀 Generar Archivos de {tipo_archivo}", type="primary"):
            with st.spinner(f'Generando archivos de {tipo_archivo}...'):
                # Crear un buffer de memoria para el archivo ZIP
                zip_buffer = BytesIO()
                
                # Obtener los valores únicos de la columna de factura
                facturas_unicas = df.iloc[:, columna_factura].unique()
                
                archivos_generados = []
                
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for factura in facturas_unicas:
                        # Filtrar los datos por número de factura
                        df_filtrado = df[df.iloc[:, columna_factura] == factura]
                        
                        # Convertir a CSV en memoria (separado por comas)
                        csv_buffer = BytesIO()
                        df_filtrado.to_csv(csv_buffer, index=False, sep=',', encoding='utf-8')
                        csv_content = csv_buffer.getvalue()
                        
                        # Crear nombre del archivo
                        nombre_archivo = f"RS_{factura}_{prefijo_archivo}.txt"
                        
                        # Agregar al ZIP
                        zip_file.writestr(nombre_archivo, csv_content)
                        archivos_generados.append(nombre_archivo)
                
                # Preparar el ZIP para descarga
                zip_buffer.seek(0)
                
                st.success(f"✅ Se generaron {len(archivos_generados)} archivos correctamente")
                
                # Mostrar lista de archivos generados
                with st.expander(f"📁 Ver archivos generados ({len(archivos_generados)})"):
                    for archivo in archivos_generados:
                        st.text(f"• {archivo}")
                
                # Botón de descarga
                st.download_button(
                    label=f"⬇️ Descargar Archivos de {tipo_archivo} (ZIP)",
                    data=zip_buffer,
                    file_name=f"archivos_{tipo_archivo.lower()}_rips.zip",
                    mime="application/zip"
                )
    
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {str(e)}")
        st.info("💡 Verifique que el archivo Excel contenga la hoja correcta y tenga el formato esperado.")
else:
    st.info("👆 Por favor, cargue un archivo Excel para comenzar")

# Información adicional
st.markdown("---")
st.markdown("""
### ℹ️ Información
- **Detalle**: Lee la hoja "Detalle", número de factura en columna H (8)
- **Carátula**: Lee la hoja "Caratula", número de factura en columna B (2)
- Los archivos se generan con el formato: `RS_{numero_factura}_{Archivo_Det/Car}.txt`
- El separador utilizado es la coma (`,`)
- Todos los archivos se descargan en un archivo ZIP
""")
