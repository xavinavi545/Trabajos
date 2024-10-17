# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Instalar las dependencias necesarias para psycopg2 y compilar extensiones
RUN apt-get update && apt-get install -y libpq-dev gcc iputils-ping && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que utiliza la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
