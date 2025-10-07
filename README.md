# 🧩 Proyecto **Urban Grocers – Automatización de pruebas**

## 📘 Descripción del proyecto

Este proyecto contiene la **automatización de pruebas** para la aplicación **Urban Grocers**, iniciando desde la creación de usuario y la **generación del token de autenticación** mediante solicitudes `request`.

El objetivo principal es validar la correcta **creación de kits** mediante el uso de los parámetros `auth_token` y `kit_body`.

## ⚙️ Indicaciones técnicas

- **Endpoint:** `/api/v1/kits`  
- **Método:** `POST`

### 🔹 Reglas para la creación de kits

1. Es obligatorio pasar **Authorization** o **cardId** para crear el kit.  
2. Si se recibe el encabezado **Authorization** con un `authToken`, el kit se creará para ese usuario.  
3. Si se recibe el parámetro **cardId**, el kit se creará dentro de la tarjeta correspondiente.  
4. Si no se pasa ninguno de los parámetros → **400 Bad Request**  
5. Si se pasan ambos parámetros, **Authorization** tiene prioridad.

### 🔹 Encabezado

| Campo | Tipo | Descripción |
|--------|------|-------------|
| Authorization | string | Encabezado de autorización en formato `Bearer {authToken}`. Si se pasa, se devuelven todos los kits creados por el usuario. |

### 🔹 Parámetros

| Campo | Tipo | Descripción |
|--------|------|-------------|
| name | string | Nombre del kit que se registrará en la tabla `kit_model`. |

## 📤 Respuestas del servidor

| Código | Descripción |
|--------|--------------|
| 201 | Creado correctamente |
| 400 | Solicitud incorrecta |
| 500 | Error interno del servidor |

## 🧰 Librerías utilizadas

- `pytest`  
- `requests`  
- `json`

## 🗂️ Estructura del proyecto

| Archivo | Descripción |
|----------|--------------|
| **configuration.py** | Contiene las rutas y URLs del proyecto. |
| **data.py** | Contiene los datos y solicitudes `POST` utilizadas. |
| **sender_stand_request.py** | Almacena las solicitudes empleadas en las pruebas. |
| **create_kit_name_kit_test.py** | Contiene la lista de comprobación (tests positivos y negativos). |
| **README.md** | Descripción general del proyecto. |
| **.gitignore** | Define los archivos y carpetas excluidos del repositorio. |

## ▶️ Instrucciones de ejecución

1. En **configuration.py**, asigna la URL generada tras reiniciar el servidor a `URL_SERVICE`.  
2. En **data.py**, completa el diccionario `user_data` con los datos de usuario.  
3. Ejecuta el archivo **create_kit_name_kit_test.py** para correr las pruebas.  
   - Asegúrate de estar en el archivo actual (`currentFile`) antes de ejecutar.  

El conjunto de pruebas incluye **casos positivos y negativos**, mostrando resultados esperados y reales.

## 🧾 Resultados y conclusiones

Se ejecutaron **9 pruebas** en total:
- ✅ **5** pasaron correctamente.  
- ❌ **4** no arrojaron los resultados esperados.

### Detalles de fallos detectados:
| Test | Resultado esperado | Resultado obtenido | Observación |
|------|---------------------|--------------------|--------------|
| test_create_kit_0_characters | 400 | 201 | Se creó un kit con nombre vacío. |
| test_create_kit_512_characters | 400 | 201 | Se creó un kit con más caracteres de los permitidos. |
| test_create_kit_empty_body | 400 | 500 | Error del servidor en lugar de solicitud incorrecta. |
| test_create_kit_integer_type_name | 400 | 201 | Se creó un kit con nombre numérico. |

## 💬 Conclusión

El proyecto permitió validar los distintos comportamientos del endpoint de creación de kits, identificando errores en la gestión de validaciones del backend.  
Este trabajo demuestra el uso de **pytest** y **requests** para realizar pruebas automáticas de API REST, contribuyendo a la mejora de la calidad del software.


