# galapagosApp-back
Framework DJANGO, conectado con PostgreSQL

### Probar endpoints
- localhost:{puerto}/swagger/


### Trabajar en un entorno virtual para evitar inconvenientes
- pip install virtualenv
- virtualenv env
- env/Scripts/.\activate

### Comandos 
- pip install -r requerimientos.txt -> (instalar todas las dependencias necesarias)
- python manage.py makemigrations app -> (crear migraciones en base a los modelos)
- python manage.py migrate app -> (aplicar migraciones a la base de datos)
- python manage.py runserver -> (levantar el servidor con las configuraciones por defecto del settings.py)
