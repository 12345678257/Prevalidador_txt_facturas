# 🚀 Inicio Rápido

## Opción 1: Ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/conversor-excel-txt-feev.git
cd conversor-excel-txt-feev

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

## Opción 2: Ejecutar con Python venv

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/conversor-excel-txt-feev.git
cd conversor-excel-txt-feev

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
streamlit run app.py
```

## Opción 3: Ejecutar con Docker (próximamente)

```bash
# Construir imagen
docker build -t conversor-excel-txt .

# Ejecutar contenedor
docker run -p 8501:8501 conversor-excel-txt
```

## ⚡ Comandos útiles

```bash
# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Ver versión de Streamlit
streamlit --version

# Limpiar caché de Streamlit
streamlit cache clear
```

## 🐛 Solución de problemas

### Error: "Module not found"
```bash
pip install -r requirements.txt --force-reinstall
```

### Error de permisos en Windows
```bash
# Ejecutar PowerShell como administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error de puerto ocupado
```bash
# Usar un puerto diferente
streamlit run app.py --server.port 8502
```

## 📱 Abrir en un dispositivo móvil

1. Ejecuta la aplicación en tu computadora
2. Busca tu dirección IP local: `ipconfig` (Windows) o `ifconfig` (Linux/Mac)
3. En tu dispositivo móvil (conectado a la misma red), abre: `http://[TU_IP]:8501`

Ejemplo: `http://192.168.1.100:8501`
