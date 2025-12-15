# 📦 INSTRUCCIONES PARA SUBIR A GITHUB

## 📁 Archivos incluidos

✅ **app.py** - Aplicación principal de Streamlit
✅ **requirements.txt** - Dependencias del proyecto
✅ **README.md** - Documentación principal
✅ **QUICK_START.md** - Guía de inicio rápido
✅ **EJEMPLOS.md** - Ejemplos de uso
✅ **LICENSE** - Licencia MIT
✅ **.gitignore** - Archivos a ignorar por Git
✅ **.streamlit/config.toml** - Configuración de Streamlit

---

## 🚀 Paso a paso para subir a GitHub

### 1. Crear un nuevo repositorio en GitHub

1. Ve a https://github.com
2. Click en el botón **"+"** (arriba a la derecha) → **"New repository"**
3. Nombre del repositorio: `conversor-excel-txt-feev`
4. Descripción: `Aplicación Streamlit para convertir archivos Excel en archivos TXT individuales con formato FEEV`
5. Selecciona **"Public"** o **"Private"** según prefieras
6. **NO** selecciones "Initialize with README" (ya tienes uno)
7. Click en **"Create repository"**

### 2. Preparar tu máquina local

Abre tu terminal/cmd y ejecuta:

```bash
# Instalar Git si no lo tienes
# Windows: descargar de https://git-scm.com/
# Linux: sudo apt-get install git
# Mac: brew install git

# Configurar Git (primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### 3. Inicializar el repositorio local

```bash
# Navegar a la carpeta donde descargaste los archivos
cd /ruta/a/tu/carpeta/conversor-excel-txt-feev

# Inicializar Git
git init

# Agregar todos los archivos
git add .

# Hacer el primer commit
git commit -m "Initial commit: Conversor Excel a TXT FEEV"
```

### 4. Conectar con GitHub y subir

Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub:

```bash
# Conectar con el repositorio remoto
git remote add origin https://github.com/TU-USUARIO/conversor-excel-txt-feev.git

# Subir los archivos
git branch -M main
git push -u origin main
```

### 5. Verificar

1. Ve a tu repositorio en GitHub: `https://github.com/TU-USUARIO/conversor-excel-txt-feev`
2. Deberías ver todos los archivos subidos
3. El README.md se mostrará automáticamente en la página principal

---

## 🌐 Desplegar en Streamlit Cloud (OPCIONAL)

Si quieres que tu aplicación esté disponible en internet:

### 1. Crear cuenta en Streamlit Cloud

1. Ve a https://streamlit.io/cloud
2. Registrate con tu cuenta de GitHub

### 2. Desplegar la aplicación

1. Click en **"New app"**
2. Selecciona tu repositorio: `conversor-excel-txt-feev`
3. Branch: `main`
4. Main file path: `app.py`
5. Click en **"Deploy!"**

### 3. Compartir

Tu aplicación estará disponible en: `https://tu-usuario-conversor-excel-txt-feev.streamlit.app`

---

## 📝 Comandos Git útiles

```bash
# Ver estado de los archivos
git status

# Ver historial de commits
git log

# Actualizar después de hacer cambios
git add .
git commit -m "Descripción de los cambios"
git push

# Descargar cambios del repositorio
git pull

# Ver ramas
git branch

# Crear nueva rama
git checkout -b nombre-rama

# Cambiar de rama
git checkout nombre-rama
```

---

## 🔄 Actualizar el proyecto

Cuando hagas cambios a tu código:

```bash
# 1. Guardar cambios
git add .

# 2. Hacer commit con mensaje descriptivo
git commit -m "Descripción de los cambios realizados"

# 3. Subir a GitHub
git push
```

---

## 🐛 Solución de problemas

### Error: "Permission denied"
```bash
# Verificar configuración SSH o usar HTTPS
git remote set-url origin https://github.com/TU-USUARIO/conversor-excel-txt-feev.git
```

### Error: "Updates were rejected"
```bash
# Descargar cambios primero
git pull origin main
# Luego subir
git push
```

### Error: "Not a git repository"
```bash
# Asegurarse de estar en la carpeta correcta
pwd  # Linux/Mac
cd    # Windows

# Inicializar Git si es necesario
git init
```

---

## ✨ Agregar funcionalidades (próximos pasos)

Ideas para mejorar tu proyecto:

1. **Validación de datos**: Verificar que los datos cumplan con los requisitos
2. **Múltiples formatos**: Soportar CSV, XLSX, XLS
3. **Configuración avanzada**: Permitir personalizar separadores y formatos
4. **Logs de conversión**: Guardar registro de conversiones realizadas
5. **API REST**: Crear una API para automatizar el proceso
6. **Tests unitarios**: Agregar pruebas automáticas
7. **Docker**: Crear un contenedor Docker para fácil despliegue

---

## 📧 Soporte

Si tienes problemas:

1. Revisa la documentación en README.md
2. Revisa la sección de "Issues" en GitHub
3. Crea un nuevo "Issue" con tu problema
4. Contacta al desarrollador

---

## 🎉 ¡Listo!

Tu proyecto ya está listo para ser usado y compartido. 

**URL del repositorio**: `https://github.com/TU-USUARIO/conversor-excel-txt-feev`

¡Éxito con tu proyecto! 🚀
