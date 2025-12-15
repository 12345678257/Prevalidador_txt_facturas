# 📄 Conversor Excel a TXT - FEEV

Aplicación web desarrollada con Streamlit para convertir archivos Excel en múltiples archivos TXT individuales, uno por cada fila, con formato específico para FEEV (Facturación Electrónica en el sector salud).

## 🎯 Características

- ✅ Convierte cada fila del Excel en un archivo TXT individual
- ✅ Separa campos con coma (`,`)
- ✅ Formatea fechas automáticamente a DD/MM/YYYY
- ✅ Nombra archivos como: `RS_{NumeroFactura}_Archivo_DET_{NumeroSecuencial}.txt`
- ✅ Genera un archivo ZIP con todos los archivos TXT
- ✅ Vista previa de archivos generados
- ✅ Interfaz amigable y fácil de usar
- ✅ Estadísticas de conversión en tiempo real

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/tu-usuario/conversor-excel-txt-feev.git
cd conversor-excel-txt-feev
```

2. **Crea un entorno virtual (opcional pero recomendado):**

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

## 💻 Uso

1. **Inicia la aplicación:**

```bash
streamlit run app.py
```

2. **Abre tu navegador:**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre, visita esa URL manualmente

3. **Sube tu archivo Excel:**
   - Haz clic en "Selecciona el archivo Excel"
   - Elige tu archivo `.xlsx` o `.xls`

4. **Configura y convierte:**
   - Revisa la vista previa de los datos
   - Ajusta el código de factura si es necesario (por defecto: 98353)
   - Haz clic en "Convertir a TXT"

5. **Descarga los resultados:**
   - Revisa la vista previa de los archivos generados
   - Descarga el archivo ZIP con todos los archivos TXT

## 📊 Estructura del archivo Excel

El archivo Excel debe tener la siguiente estructura:

- **Columnas 1-3:** Pueden estar vacías
- **Columna 4:** Código de factura
- **Columna 5:** Tipo (FEEV)
- **Columna 6:** Fecha
- **Columna 7:** Número de documento
- **Columna 8:** Tipo de documento
- **Columna 9:** Autorización
- **Columna 10:** Código de procedimiento
- **Columnas 11-22:** Valores numéricos y fechas
- **Columna 23:** Descripción del procedimiento

## 📝 Formato de salida

Cada archivo TXT tendrá el siguiente formato:

**Nombre de archivo:** `RS_98353_Archivo_DET_1.txt`

Donde:
- `98353` es el número de factura (viene del Excel)
- `1` es el número secuencial (evita sobrescritura de archivos)

**Contenido:**
```
98353,FEEV,04/09/2025,1001198272,CC,31366-2547915007,8641050003,,1,938709,938709,0,0,90300,0,0,0,848409,0,04/09/2025,RESECCIONDETUMORBENIGNODEPIEL...
```

Los campos se separan con coma (`,`) y las fechas se formatean como DD/MM/YYYY.

## 🛠️ Tecnologías utilizadas

- **[Streamlit](https://streamlit.io/):** Framework para crear aplicaciones web
- **[Pandas](https://pandas.pydata.org/):** Manipulación y análisis de datos
- **[OpenPyXL](https://openpyxl.readthedocs.io/):** Lectura de archivos Excel

## 📂 Estructura del proyecto

```
conversor-excel-txt-feev/
│
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
└── .gitignore            # Archivos a ignorar por Git
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Luis German**

- Desarrollador especializado en sistemas de salud
- Experto en facturación electrónica FEEV

## 📞 Soporte

Si tienes alguna pregunta o problema:

1. Abre un [Issue](https://github.com/tu-usuario/conversor-excel-txt-feev/issues)
2. Revisa la documentación en este README
3. Contacta al desarrollador

## 🔄 Versiones

### v1.0.0 (Diciembre 2025)
- ✨ Versión inicial
- ✅ Conversión de Excel a múltiples TXT
- ✅ Separador por comas
- ✅ Formato de nombres: `RS_{NumeroFactura}_Archivo_DET_{NumeroSecuencial}.txt`
- ✅ Descarga en formato ZIP
- ✅ Vista previa de archivos
- ✅ Soporte para múltiples códigos de factura en un mismo archivo

## 📸 Capturas de pantalla

_(Agrega capturas de pantalla de tu aplicación aquí)_

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!
