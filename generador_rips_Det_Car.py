import streamlit as st
import pandas as pd
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

        # Configuración según tipo
        if tipo_archivo == "Detalle":
            nombre_hoja = "Detalle"
            columna_factura_index = 7  # H
            prefijo_archivo = "Archivo_Det"
            st.info("📋 Procesando hoja: Detalle | Factura columna H (8)")
        else:
            nombre_hoja = "Caratula"
            columna_factura_index = 1  # B
            prefijo_archivo = "Archivo_Car"
            st.info("📋 Procesando hoja: Caratula | Factura columna B (2)")

        # Leer Excel
        df = pd.read_excel(uploaded_file, sheet_name=nombre_hoja)

        st.success(f"✅ Archivo cargado: {uploaded_file.name}")
        st.write(f"Filas: {len(df)}")
        st.write(f"Columnas: {len(df.columns)}")

        # Vista columnas
        with st.expander("🔍 Ver columnas"):
            for i, col in enumerate(df.columns):
                st.text(f"{i} → {col}")

        st.markdown("---")

        # Validar columna factura
        if columna_factura_index >= len(df.columns):
            st.error("❌ Columna factura no existe")
            st.stop()

        nombre_columna_factura = df.columns[columna_factura_index]
        st.write(f"Columna factura: {nombre_columna_factura}")

        facturas_unicas = df.iloc[:, columna_factura_index].dropna().unique()

        st.write(f"Facturas encontradas: {len(facturas_unicas)}")

        with st.expander("👁 Vista previa"):
            st.dataframe(df.head(10))

        st.markdown("---")

        # Botón generación
        if st.button(f"🚀 Generar Archivos {tipo_archivo}", type="primary"):

            with st.spinner("Generando archivos..."):

                zip_buffer = BytesIO()
                archivos_generados = []
                errores = []

                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:

                    for factura in facturas_unicas:

                        try:
                            # Filtrar factura
                            df_filtrado = df[df.iloc[:, columna_factura_index] == factura].copy()

                            if df_filtrado.empty:
                                errores.append(f"{factura}: sin registros")
                                continue

                            # ✅ CONVERSIÓN FECHAS (SOLUCIÓN PRINCIPAL)
                            for col in df_filtrado.columns:
                                try:
                                    df_filtrado[col] = pd.to_datetime(df_filtrado[col], errors='ignore')
                                    if pd.api.types.is_datetime64_any_dtype(df_filtrado[col]):
                                        df_filtrado[col] = df_filtrado[col].dt.strftime('%d-%m-%Y')
                                except:
                                    pass

                            # Exportar TXT
                            csv_string = df_filtrado.to_csv(
                                index=False,
                                header=False,
                                sep=',',
                                lineterminator='\n'
                            )

                            factura_limpia = str(factura).replace("/", "_").replace("\\", "_").replace(" ", "_")

                            nombre_archivo = f"RS_{factura_limpia}_{prefijo_archivo}.txt"

                            zip_file.writestr(nombre_archivo, csv_string.encode("utf-8"))

                            archivos_generados.append(nombre_archivo)

                            st.text(f"✓ {nombre_archivo} ({len(df_filtrado)} filas)")

                        except Exception as e:
                            errores.append(f"{factura}: {str(e)}")

                zip_buffer.seek(0)

                # Resultados
                if archivos_generados:

                    st.success(f"✅ Generados {len(archivos_generados)} archivos")

                    if errores:
                        with st.expander("⚠ Advertencias"):
                            for e in errores:
                                st.warning(e)

                    st.download_button(
                        "⬇ Descargar ZIP",
                        zip_buffer,
                        file_name=f"archivos_{tipo_archivo.lower()}_rips.zip",
                        mime="application/zip"
                    )

                else:
                    st.error("❌ No se generaron archivos")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        import traceback
        with st.expander("Detalle técnico"):
            st.code(traceback.format_exc())

else:
    st.info("👆 Cargue un Excel para iniciar")

st.markdown("---")
st.markdown("""
### ℹ Información
- Detalle → Hoja: Detalle | Factura: Col H  
- Carátula → Hoja: Caratula | Factura: Col B  
- TXT sin encabezados  
- Fechas formato DD-MM-YYYY  
- Descarga ZIP automática  
""")
