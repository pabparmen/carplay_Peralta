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
