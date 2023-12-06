# PROYECTO CARPLAY PERALTA

<h2> Configurar y desplegar el proyecto </h2>
Todo el proyecto se ha realizado en Windows, y toda la configuración y despliegue explicado posteriormente se debe realizar en Windows. 

### Instalar Python 3.10

Se debe tener Pyhton instalado con la versión 3.10. Puedes instalártelo desde:
1. La [pagina web](https://www.python.org/downloads/windows/)
2. Desde [MicrosoftStore](https://www.microsoft.com/store/productId/9PJPW5LDXLZ5?ocid=pdpshare)

Una vez instalado debemos comprobar si esta instalado correctamente, debemos ir a la CMD del sistema y poner:
```
python --version
```

Debe salirte algo así, asegurate que sea la versión 3.10:
```
Python 3.10.11  
```

### Crear el entorno virtual de python

Debemos ir a la consola del sistema y poner el siguiente código, 'my_env' es el nombre del entorno virtual, puedes cambiarlo al que quieras:
```
py -m venv my_env
```

Ahora vamos a activar el entorno virtual:
```
.\my_env\Scripts\activate
```

### Instalar Django 4 

Para ello utilizaremos el comando pip que pertenece a python. Escribe el siguiente comando en la cmd para instalar Django 4
```
pip install Django~=4.1.0
```

Esto instalará la última versión de Django 4.1. Para verificar que se ha instalado correctamnete, escribe:
```
python -m django --version
```

### Clonar repositorio 

Para clonar el repositorio, solo debemos escribir en la cmd de la carpeta donde queramos descargar el repositorio lo siguiente:
```
git clone https://github.com/pabparmen/carplay_Peralta.git
```

### Aplicando migraciones a la base de datos y runear el proyecto

Para completar la configuración del proyecto, es necesario crear las tablas asociadas a los modelos de las aplicaciones Django por defecto, para ello accedemos a la carpeta el proyecto:
```
cd carplay_Peralta
```

Y tras entrar en la carpeta ponemos lo siguiente: 
```
python manage.py migrate
```

Deberá aparecer esto en tu pantalla:  
```  
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying admin.0003_logentry_add_action_flag_choices... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying auth.0009_alter_user_last_name_max_length... OK
Applying auth.0010_alter_group_name_max_length... OK
Applying auth.0011_update_proxy_permissions... OK
Applying auth.0012_alter_user_first_name_max_length... OK
Applying sessions.0001_initial... OK
```
Cuando las migraciones han terminado, es momento de runear el proyecto, y para ello debemos escribir esto:
```
python manage.py runserver
```

Deberá aparecer algo asi en la cmd:
```
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
January 01, 2022 - 10:00:00
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Accediendo a `http://127.0.0.1:8000/` podremos entrar en la pagina web del proyecto desde el punto de vista del usuario.

Si accedemos a `http://127.0.0.1:8000/admin/` entraremos a la pagina web del administrador. 

hay que instalar stripe, está en el requirements.txt pero tambien sirve hacer esto dentro del entorno virtual:
```
pip install stripe == 4.0.2
```

Para testear pagos, seguir guía de aqui:
https://stripe.com/docs/testing

Result Test Credit Card CVC Expiry date
Successful payment 4242 4242 4242 4242 Any 3 digits Any future date
Failed payment 4000 0000 0000 0002 Any 3 digits Any future date

Los pagos se ven en la cuenta de stripe y se pueden exportar desde ahí a un csv


Para testear Webhook (notificación de pagos en tiempo real): 
(esto es para testear webhook en un ordenador, con hacerlo 1 vez ya puedes testearlo en ese sistema)

Si estamos en macOS o linux con homebrew, instalamos Stripe CLI usando este comando:
```
brew install stripe/stripe-cli/stripe
```

Si usamos Windows, o macOS/Linux sin homebrew, descargamos la release desde el siguiente enlace:
```
https://github.com/stripe/stripe-cli/
releases/latest
```
Y extraemos el zip. Si estamos usando Windows, ejecutamos el archivo .exe desde el cmd

Ejecutamos el siguiente comando:
```
stripe login
```
que nos mostrará la siguiente salida:
```
Your pairing code is: xxxx-yyyy-zzzz-oooo
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit https://dashboard.stripe.com/
stripecli/confirm_auth?t=...
```
Presionamos enter para que nos lleve a la url

Comprobamos que el codigo en la url sea el mismo que el que nos muestra la cmd y si es asi, le damos a "Permitir Acceso", con eso nos deberia de salir en la web un mensaje tipo:
```
Acceso concedido
Ahora puedes cerrar esta ventana y volver a la CLI.
```
despues de eso, ejecuta en el cmd:
```
stripe listen --forward-to localhost:8000/payment/webhook/
```
Utilizamos este comando para indicarle a Stripe que escuche eventos y los envíe a nuestro servidor local. Utilizamos el puerto 8000, o el que sea donde se este ejecutando el servidor de desarrollo de Django, y la ruta /payment/webhook/, que coincide con el patrón de URL de nuestro webhook.

Despues de esto, deberiamos ver la siguiente salida en el cmd y copiar la clave que nos indican en settings.py, en STRIPE_WEBHOOK_SECRET:
```
Getting ready... > Ready! You are using Stripe API Version [2022-08-01]. Your 
webhook signing secret is xxxxxxxxxxxxxxxxxxx (^C to quit)
```
abre el enlace https://dashboard.stripe.com/test/webhooks y deberia de salir el dispositivo vinculado, bajo el nombre "oyente local" deberiamos poder ver nuestro PC

En el cmd donde estamos ejecutando Stripe, es donde aparecerán los diferentes eventos que ocurren

Las claves de Webhook caducan a los 90 dias de haberse generado, y recordad que deben permanecer en secreto.


### Despliegue de la aplicación con Docker

Para efectuar el despliegue con Docker, debemos seguir los siguientes pasos:

  1. Si usted no cuenta con la instalación de Docker en su dispositivo, la forma más fácil para instalarlo es la siguiente(Windows):
    -Acuda al siguiente enlace y descargue la versión pertinente para su dispositivo: https://www.docker.com/products/docker-desktop/
    -Instale el producto siguiendo los pasos y reinicie su dispositivo.
    -Vuelva a abrir la aplicación Docker Desktop y elija la opción de entrar sin iniciar sesión (o bien puede registrarse si lo desea)
  2. Abra su términal y vaya a la carpeta base del proyecto (Para evitar problemas lance su entorno de Python(env) previamente)
  3. Ejecute el comando: "docker-compose up --build"
  4. Cuando termine la ejecución(Observará por pantalla algo parecido a web-1 started), vaya a la dirección localhost:8000

Y con ello bastaría para realizar el despliegue :)
     
