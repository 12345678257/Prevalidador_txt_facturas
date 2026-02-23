import streamlit as st
import pandas as pd
import zipfile
from io import BytesIO
from datetime import datetime
import os

st.set_page_config(
    page_title="Conversor Excel a TXT - FEEV",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Conversor Excel a Archivos TXT Individuales")
st.markdown("### Convierte cada fila del Excel en un archivo TXT con formato FEEV")

st.info("⚠️ **Importante:** El archivo Excel debe tener los datos a partir de la columna 4 (las primeras 3 columnas pueden estar vacías). Cada archivo se nombra como RS_{NumeroFactura}_Archivo_DET_{NumeroSecuencial}.txt")

# Sidebar con información
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("""
    **Formato de salida:**
    - Cada fila = 1 archivo TXT
    - Campos separados por `,` (coma)
    - Fechas en formato DD-MM-YYYY
    - Nombre: `RS_{NumFactura}_Archivo_DET_{#}.txt`
    
    **Ejemplo:**
    `RS_98353_Archivo_DET_1.txt`
    
    **Desarrollado por:**
    Luis German
    """)
    
    st.markdown("---")
    st.markdown("### 📋 Estructura esperada")
    st.code("""
    Campo 1: Código
    Campo 2: Tipo (FEEV)
    Campo 3: Fecha
    Campo 4: Documento
    Campo 5: Tipo Doc
    Campo 6: Autorización
    Campo 7: Procedimiento
    ...y más campos
    """)

# Función para formatear fecha
def format_date(date_value):
    """Convierte fecha a formato DD-MM-YYYY"""
    if pd.isna(date_value):
        return ""
    if isinstance(date_value, datetime):
        return date_value.strftime("%d/%m/%Y")
    if isinstance(date_value, str):
        try:
            dt = pd.to_datetime(date_value)
            return dt.strftime("%d/%m/%Y")
        except:
            return str(date_value)
    return str(date_value)

# Función para formatear valor
def format_value(value):
    """Formatea un valor para el TXT"""
    if pd.isna(value):
        return ""
    if isinstance(value, (int, float)):
        # Si es un número entero, no mostrar decimales
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(int(value)) if isinstance(value, float) and value == int(value) else str(value)
    return str(value).strip()

# Función principal de conversión
def convert_excel_to_txt(df, codigo_factura="98353"):
    """Convierte el DataFrame a archivos TXT individuales"""
    txt_files = []
    
    # Procesar cada fila
    for idx, row in df.iterrows():
        values = []
        
        # Obtener el número de factura de la columna 0 para el nombre del archivo
        numero_factura = format_value(row.iloc[0])
        if numero_factura == "":
            numero_factura = codigo_factura
        
        # Procesar las 21 columnas (columnas 0 a 20)
        for i in range(21):
            if i < len(row):
                # Campos de fecha (columnas 2 y 19)
                if i == 2 or i == 19:
                    values.append(format_date(row.iloc[i]))
                else:
                    values.append(format_value(row.iloc[i]))
            else:
                # Si no existe la columna, agregar vacío
                values.append("")
        
        # Crear contenido del archivo TXT
        txt_content = ",".join(values)
        
        # Nombre del archivo: RS_{numero_factura_de_columna_0}_Archivo_DET.txt
        filename = f"RS_{numero_factura}_Archivo_DET.txt"
        
        txt_files.append({
            'filename': filename,
            'content': txt_content,
            'row_number': idx + 1,
            'codigo': numero_factura
        })
    
    return txt_files

# Upload del archivo
uploaded_file = st.file_uploader(
    "📁 Selecciona el archivo Excel",
    type=['xlsx', 'xls'],
    help="Sube el archivo Excel que deseas convertir"
)

if uploaded_file is not None:
    try:
        # Leer el archivo Excel
        with st.spinner("📖 Leyendo archivo Excel..."):
            # Primero leer sin header para analizar
            df_test = pd.read_excel(uploaded_file, header=None)
            
            # Detectar si la primera fila es un encabezado
            # (contiene strings en lugar de números/fechas)
            primera_fila = df_test.iloc[0]
            es_encabezado = sum(1 for x in primera_fila if isinstance(x, str) and not x.isdigit()) > len(primera_fila) * 0.5
            
            # Leer el archivo correctamente
            uploaded_file.seek(0)  # Volver al inicio del archivo
            if es_encabezado:
                df = pd.read_excel(uploaded_file, header=0)
                st.info("✅ Se detectó encabezado en el archivo - Los datos comienzan en la fila 2")
            else:
                df = pd.read_excel(uploaded_file, header=None)
                st.info("✅ No se detectó encabezado - Los datos comienzan en la fila 1")
        
        # Mostrar información del archivo
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Total de filas", len(df))
        with col2:
            st.metric("📋 Total de columnas", len(df.columns))
        with col3:
            st.metric("📄 Archivos TXT a generar", len(df))
        
        # Vista previa de los datos
        with st.expander("👀 Vista previa del Excel (primeras 5 filas)"):
            st.dataframe(df.head(), use_container_width=True)
        
        # Configuración
        st.markdown("### ⚙️ Configuración")
        col1, col2 = st.columns(2)
        
        with col1:
            codigo_factura = st.text_input(
                "Código por defecto (opcional)",
                value="98353",
                help="Solo se usa si una fila no tiene número de factura en la columna 1"
            )
        
        with col2:
            preview_count = st.number_input(
                "Archivos a previsualizar",
                min_value=1,
                max_value=10,
                value=3,
                help="Cantidad de archivos TXT a mostrar en la vista previa"
            )
        
        # Botón de conversión
        if st.button("🔄 Convertir a TXT", type="primary", use_container_width=True):
            with st.spinner(f"⚙️ Generando {len(df)} archivos TXT..."):
                txt_files = convert_excel_to_txt(df, codigo_factura)
            
            st.success(f"✅ Se generaron exitosamente {len(txt_files)} archivos TXT")
            
            # Vista previa de algunos archivos
            st.markdown("### 📋 Vista previa de archivos generados")
            for i, txt_file in enumerate(txt_files[:preview_count]):
                with st.expander(f"📄 {txt_file['filename']}"):
                    st.code(txt_file['content'], language=None)
            
            if len(txt_files) > preview_count:
                st.info(f"ℹ️ Mostrando {preview_count} de {len(txt_files)} archivos. Descarga el ZIP para ver todos.")
            
            # Crear archivo ZIP
            st.markdown("### 📦 Descargar archivos")
            
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for txt_file in txt_files:
                    zip_file.writestr(txt_file['filename'], txt_file['content'])
            
            zip_buffer.seek(0)
            
            # Botón de descarga
            st.download_button(
                label="⬇️ Descargar todos los archivos TXT (ZIP)",
                data=zip_buffer,
                file_name=f"archivos_txt_feev_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                mime="application/zip",
                type="primary",
                use_container_width=True
            )
            
            # Estadísticas
            st.markdown("### 📊 Estadísticas de conversión")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total de archivos", len(txt_files))
            with col2:
                total_size = sum(len(f['content'].encode('utf-8')) for f in txt_files)
                st.metric("Tamaño total", f"{total_size / 1024:.2f} KB")
            with col3:
                avg_size = total_size / len(txt_files) if txt_files else 0
                st.metric("Tamaño promedio", f"{avg_size / 1024:.2f} KB")
    
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {str(e)}")
        st.exception(e)

else:
    # Mensaje de bienvenida
    st.markdown("""
    ### 🚀 Cómo usar esta aplicación:
    
    1. **Sube tu archivo Excel** usando el botón de arriba
    2. **Revisa la vista previa** de los datos
    3. **Configura** el código de factura si es necesario
    4. **Haz clic en Convertir** para generar los archivos TXT
    5. **Descarga el archivo ZIP** con todos los archivos generados
    
    ---
    
    ### 📝 Notas importantes:
    
    - Cada fila del Excel se convertirá en un archivo TXT individual
    - Los campos se separarán con coma (`,`)
    - Las fechas se formatearán como DD/MM/YYYY
    - Los archivos se nombrarán como: `RS_{NumeroFactura}_Archivo_DET_{NumeroSecuencial}.txt`
    - El número secuencial evita que archivos con el mismo código se sobrescriban
    - Los archivos se empaquetarán en un archivo ZIP para fácil descarga
    
    ---
    
    ### 💡 Ejemplo de formato de salida:
    
    **Nombre del archivo:** `RS_98353_Archivo_DET_1.txt`
    
    **Contenido:**
    ```
    98353,FEEV,04-09-2025,1001198272,CC,31366-2547915007,8641050003,,1,938709,938709,0,0,90300,0,0,0,848409,0,04-09-2025,RESECCIONDETUMORBENIGNODEPIEL...
    ```
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Desarrollado por Luis German | Conversor Excel a TXT FEEV</p>
    </div>
    """,
    unsafe_allow_html=True
)
