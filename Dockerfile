# Utilizar un entorno de ejecución oficial de Python como imagen principal
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el contenido del directorio actual en el contenedor en /app
COPY app.py /app

# Instala las dependencias necesarias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Hacer que el puerto 8080 esté disponible para el mundo fuera de este contenedor
EXPOSE 8080


CMD ["python","app.py"]
