FROM python:3.10

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto Django al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto en el que tu servidor Django está corriendo (por defecto, 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
