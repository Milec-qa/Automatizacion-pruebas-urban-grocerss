# Proyecto Urban Grocers 
Proyecto Sprint 7.
Presentado por: Milena Collazos, Grupo 13 , Sprint 7

# Descripción del proyecto:
Este proyecto contiene la automatización de pruebas, donde todo parte de la creación de usuario
y generación de token , a través de solicitudes request , para la aplicación Urban Grocers.

Importante tener en cuenta que para la creación de Kits; se tiene en cuenta estos parámetros; auth_token, kit_body

# Indicaciones: 
a.Endpoint para crear una kit de una tarjeta específica O de usuario
b.Es obligatorio pasar el encabezado Authorization O el parámetro cardId, para crear la kit
c.Si se recibe una solicitud con un encabezado Authorization que contenga el authToken de un/a usuario/a en particular 
se creará la kit de este/a usuario/a.
d. Si se recibe el parámetro cardId, se creará un kit dentro de la tarjeta correspondiente.
e. Si no se pasa ninguno de los parámetros, se devolverá un error.
f. Cuando se pasan ambos parámetros, Authorization es la prioridad

Para crear un kit, se realiza a través de una solicitud POST bajo el endopint /api/v1/kits
# El encabezado 
Campo: Authorization (opcional) 
Tipo: string 
Descripción: Encabezado de autorización en formato Bearer {authToken}. 
Cuando se pasa - se devuelven todos las kits creadas por el/la usuario/a.

# Parámetro:
Campo:name
Tipo: string
Descripción: El nombre de la kit, que será escrito en el campo correspondiente de la
de la tabla kit_mode.

Recibiremos como respuesta:201 Creado
En caso que no se hayan trasmitido ninguno de los parámetros tendras como respuesta:400 Bad request.

# Para este proyecto se tuvieron en cuenta los siguientes librerías:
1. Instalaciones realizadas; 
a. PyTest
b. request
c. json

# Contenido del proyecto
Este proyecto tiene 6 archivos distribuidos de la siguiente manera:
1. configuration.py
En este archivo se encuentra almacenadas todas las rutas para el archivo.

2. data.py
En este archivo se encuentran todas las solicitudes POST.

3. sender_stand_request.py
En este archivo tenemos todas las solicitudes almacenadas que se necesitaron
para resolver este proyecto.

4. create_kit_name_kit_test.py
En este archivo se encuentra la lista de comprobación completa, de nuestro proyecto.

5. README.md
Es este archivo que estas leyendo, acá encuentras la descripción del proyecto.

6. .gitignore
Este archivo incluye todas las carpetas y archivos que no serán incluidos al realizar el COMMIT
en el repositorio


# Instrucciones para ejecutar el proyecto
1. Debes ir al archivo configuration.py y colocar en la URL_SERVICE = la Url que te genera
una vez reiniciado el servidor.
2. Debes ir al archivo data.py y llenar los campos de usuario en el diccionario user_data
3. En el archivo create_kit_name_kit_test podrás ejecutar la lista de comprobación de pruebas con resultados.
Pruebas positivas y negativas
(Valida que estes en currentFile para que realmente puedas ejecutar las pruebas)

De esta manera puedes conocer el desarrollo del proyecto, te invito a ejecutar la lista
de comprobación y observar sus resultados.

## Nota: Como conclusión de este proyecto se realizaron 9 pruebas de las cuales 5 se obtuvieron los resultados esperados, 4 de ellas no.
1. Se evidencia que test_create_kit_0_characters fallo ya que se esperaba 400 como código de respuesta y el kit si se está creando con código 201, y no debía crearse ya que el nombre tenía 0 caracteres. 
2. Se evidencia que test_create_kit_512_characters fallo ya que se esperaba 400 como código de respuesta y el kit si se está creando con código 201 y no debía crearse ya que el máximo permitido de caracteres es 511
3. Se evidencia que test_create_kit_empty_body fallo ya que se esperaba 400 como código de respuesta y el código de error recibido es 500
4. Se evidencia que test_create_kit_integer_type_name fallo ya que se esperaba 400 como código de respuesta y el kit si se está creando con código 201, y no debía crearse ya que el nombre enviado es de tipo numérico.


!Gracias! Que tengas un buen día.
Saludos, 
Milena Collazos , Grupo 13, Sprint 7

