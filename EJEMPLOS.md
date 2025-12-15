# 📚 Ejemplos de Uso

## Ejemplo 1: Conversión básica

### Entrada (Excel)
```
| Col1 | Col2 | Col3 | Codigo | Tipo | Fecha      | Doc        | TipoDoc | Autorizacion | Proc       | ... |
|------|------|------|--------|------|------------|------------|---------|--------------|------------|-----|
|      |      |      | 98353  | FEEV | 04/09/2025 | 1001198272 | CC      | 31366-...    | 8641050003 | ... |
|      |      |      | 98353  | FEEV | 08/09/2025 | 79736996   | CC      | 31366-...    | 5340010006 | ... |
```

### Salida (TXT)
```
Archivo: RS_98353_Archivo_DET_1.txt
Contenido: 98353,FEEV,04/09/2025,1001198272,CC,31366-2547915007,8641050003,,1,938709,938709,0,0,90300,0,0,0,848409,0,04/09/2025,RESECCION...

Archivo: RS_98353_Archivo_DET_2.txt
Contenido: 98353,FEEV,08/09/2025,79736996,CC,31366-2548495949,5340010006,,1,527028,527028,0,0,0,0,0,0,527028,0,08/09/2025,HERNIORRAFIA...
```

---

## Ejemplo 2: Múltiples códigos de factura

### Entrada (Excel)
```
| ... | Codigo | Tipo | ... |
|-----|--------|------|-----|
| ... | 98353  | FEEV | ... |
| ... | 16128  | FEEV | ... |
| ... | 16365  | FEEV | ... |
```

### Salida (TXT)
```
RS_98353_Archivo_DET_1.txt
RS_16128_Archivo_DET_2.txt
RS_16365_Archivo_DET_3.txt
```

---

## Ejemplo 3: Formato de fechas

### Diferentes formatos de entrada
- Excel: `2025-09-04` → TXT: `04/09/2025`
- Excel: `04/09/2025` → TXT: `04/09/2025`
- Excel: `9/4/2025` → TXT: `04/09/2025`

---

## Ejemplo 4: Manejo de valores numéricos

### Entrada
```
Campo: 938709.0 (float)
Campo: 0.0 (float)
Campo: 90300 (int)
```

### Salida
```
938709,0,90300
```

---

## Ejemplo 5: Campos vacíos

### Entrada
```
| Campo1 | Campo2 | Campo3 |
|--------|--------|--------|
| 98353  | (vacío)| 1234   |
```

### Salida
```
98353,,1234
```

---

## Caso de uso completo

### Escenario
Una entidad de salud necesita convertir 1000 registros de facturación FEEV del formato Excel a archivos TXT individuales para carga en el sistema FEVRIPS.

### Proceso
1. **Preparar el Excel**: Asegurarse de que tiene las 24 columnas requeridas
2. **Subir a la aplicación**: Cargar el archivo .xlsx
3. **Configurar**: Verificar que el código de factura sea correcto
4. **Convertir**: Generar los 1000 archivos TXT
5. **Descargar**: Obtener el archivo ZIP con todos los archivos
6. **Extraer**: Descomprimir el ZIP en la carpeta de carga del sistema
7. **Cargar**: Subir los archivos al sistema FEVRIPS

### Resultado
- 1000 archivos TXT individuales
- Nomenclatura correcta: RS_98353_Archivo_DET_1.txt a RS_98353_Archivo_DET_1000.txt
- Formato compatible con FEVRIPS
- Tiempo de procesamiento: ~30 segundos

---

## Errores comunes y soluciones

### Error: Columnas incorrectas
**Problema**: El Excel no tiene 24 columnas
**Solución**: Verificar que el archivo tenga la estructura correcta

### Error: Fechas inválidas
**Problema**: Formato de fecha no reconocido
**Solución**: Usar formato de fecha estándar en Excel (DD/MM/YYYY o YYYY-MM-DD)

### Error: Archivo muy grande
**Problema**: El archivo Excel supera los 200 MB
**Solución**: Dividir el archivo en partes más pequeñas

### Error: Caracteres especiales
**Problema**: Nombres de procedimientos con caracteres especiales
**Solución**: La aplicación maneja automáticamente los caracteres especiales

---

## Tips y mejores prácticas

1. **Verificar datos**: Revisar los primeros registros en la vista previa antes de convertir
2. **Respaldar**: Guardar el archivo Excel original antes de procesar
3. **Probar primero**: Usar un archivo pequeño para probar antes de procesar archivos grandes
4. **Revisar nombres**: Verificar que los nombres de archivo sean correctos antes de subir al sistema
5. **Documentar**: Guardar registro de qué archivos fueron generados y cuándo

---

## Automatización (avanzado)

Si necesitas procesar múltiples archivos regularmente, considera:

1. Crear un script Python que use el código de la aplicación
2. Programar tareas automáticas con cron (Linux) o Task Scheduler (Windows)
3. Integrar con tu sistema de gestión de archivos

Ejemplo de script:
```python
import pandas as pd
# ... (código de conversión)
```
