import streamlit as st
import pandas as pd
import os
from io import BytesIO, StringIO
import zipfile

st.set_page_config(page_title="Prevalidador_de_archivos_ST", page_icon="📄", layout="centered")

st.title("📄 Prevalidador_de_archivos_ST")
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
            columna_factura_nombre = "H"  # Columna 8
            columna_factura_index = 7  # Índice 7 (columna H)
            prefijo_archivo = "Archivo_Det"
            st.info(f"📋 Procesando hoja: **{nombre_hoja}** | Número de factura en columna **{columna_factura_nombre} (columna 8)**")
        else:  # Carátula
            nombre_hoja = "Caratula"
            columna_factura_nombre = "B"  # Columna 2
            columna_factura_index = 1  # Índice 1 (columna B)
            prefijo_archivo = "Archivo_Car"
            st.info(f"📋 Procesando hoja: **{nombre_hoja}** | Número de factura en columna **{columna_factura_nombre} (columna 2)**")
        
        # Leer el archivo Excel
        df = pd.read_excel(uploaded_file, sheet_name=nombre_hoja)
        
        st.success(f"✅ Archivo cargado exitosamente: {uploaded_file.name}")
        st.write(f"**Total de filas:** {len(df)}")
        st.write(f"**Total de columnas:** {len(df.columns)}")
        
        # Mostrar las columnas disponibles
        with st.expander("🔍 Ver columnas disponibles"):
            for i, col in enumerate(df.columns):
                letra = chr(65+i) if i < 26 else f"Col{i}"
                st.text(f"Columna {i} ({letra}): {col}")
        
        # Opción para cambiar la columna manualmente
        st.markdown("---")
        usar_columna_manual = st.checkbox("🔧 Cambiar columna de factura manualmente", value=False)
        
        if usar_columna_manual:
            columna_factura_index = st.number_input(
                "Número de columna (0 = A, 1 = B, 2 = C, etc.)",
                min_value=0,
                max_value=len(df.columns)-1,
                value=columna_factura_index
            )
            st.info(f"Usando columna {columna_factura_index} ({df.columns[columna_factura_index]})")
        
        st.markdown("---")
        
        # Verificar que la columna existe
        if columna_factura_index >= len(df.columns):
            st.error(f"❌ La columna {columna_factura_nombre} no existe en la hoja {nombre_hoja}")
            st.stop()
        
        # Obtener el nombre de la columna de factura
        nombre_columna_factura = df.columns[columna_factura_index]
        st.write(f"**Columna de factura:** {nombre_columna_factura}")
        
        # Mostrar valores únicos en la columna de factura
        valores_factura_todos = df.iloc[:, columna_factura_index]
        valores_no_nulos = valores_factura_todos.dropna()
        valores_unicos = valores_no_nulos.unique()
        
        st.write(f"**Total valores en columna:** {len(valores_factura_todos)}")
        st.write(f"**Valores no nulos:** {len(valores_no_nulos)}")
        st.write(f"**Facturas únicas encontradas:** {len(valores_unicos)}")
        
        # Mostrar una muestra de los valores
        if len(valores_unicos) > 0:
            muestra = list(valores_unicos[:5])
            st.write(f"**Muestra de facturas:** {muestra}")
        else:
            st.warning("⚠️ No se encontraron facturas en esta columna. Verifique que la columna correcta.")
            # Mostrar las primeras filas de la columna
            with st.expander("Ver primeros valores de la columna de factura"):
                st.write(df.iloc[:10, columna_factura_index])
        
        # Mostrar vista previa
        with st.expander("👁️ Ver vista previa de los datos"):
            st.dataframe(df.head(10))
        
        st.markdown("---")
        
        if st.button(f"🚀 Generar Archivos de {tipo_archivo}", type="primary"):
            with st.spinner(f'Generando archivos de {tipo_archivo}...'):
                # Crear un buffer de memoria para el archivo ZIP
                zip_buffer = BytesIO()
                
                # Obtener facturas únicas (sin valores nulos)
                facturas_unicas = df.iloc[:, columna_factura_index].dropna().unique()
                
                st.write(f"📊 Procesando {len(facturas_unicas)} facturas únicas...")
                
                archivos_generados = []
                errores = []
                
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    for factura in facturas_unicas:
                        try:
                            # Filtrar los datos por número de factura
                            df_filtrado = df[df.iloc[:, columna_factura_index] == factura].copy()
                            
                            if len(df_filtrado) == 0:
                                errores.append(f"Factura {factura}: Sin datos")
                                continue
                            
                            # Convertir a CSV SIN ENCABEZADOS
                            csv_string = df_filtrado.to_csv(index=False, sep=',', encoding='utf-8', lineterminator='\n', header=False)
                            csv_bytes = csv_string.encode('utf-8')
                            
                            # Crear nombre del archivo (limpiar caracteres no válidos)
                            factura_limpia = str(factura).replace('/', '_').replace('\\', '_').replace(' ', '_').strip()
                            nombre_archivo = f"RS_{factura_limpia}_{prefijo_archivo}.txt"
                            
                            # Agregar al ZIP
                            zip_file.writestr(nombre_archivo, csv_bytes)
                            archivos_generados.append(nombre_archivo)
                            
                            st.text(f"✓ Generado: {nombre_archivo} ({len(df_filtrado)} filas)")
                        
                        except Exception as e:
                            errores.append(f"Error con factura {factura}: {str(e)}")
                
                # Preparar el ZIP para descarga
                zip_buffer.seek(0)
                
                if len(archivos_generados) > 0:
                    st.success(f"✅ Se generaron {len(archivos_generados)} archivos correctamente")
                    
                    # Mostrar errores si los hay
                    if len(errores) > 0:
                        with st.expander(f"⚠️ Advertencias ({len(errores)})"):
                            for error in errores:
                                st.warning(error)
                    
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
                else:
                    st.error("❌ No se pudo generar ningún archivo. Verifique los datos.")
                    if len(errores) > 0:
                        st.write("**Errores encontrados:**")
                        for error in errores:
                            st.error(error)
    
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {str(e)}")
        st.info("💡 Verifique que el archivo Excel contenga la hoja correcta y tenga el formato esperado.")
        import traceback
        with st.expander("Ver detalles del error"):
            st.code(traceback.format_exc())
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
- **Los archivos NO incluyen encabezados (solo datos)**
- Todos los archivos se descargan en un archivo ZIP
""")
