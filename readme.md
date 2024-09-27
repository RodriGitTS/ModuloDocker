# Configurar odoo con Docker compose

Software necesario
- Docker desktop
- Windows PowerShell (Con permisos de administrador)
  
## Empezar un servidor PostgreSQL y una instancia de Odoo
```
$ docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:15

```
```
$ docker run -p 8069:8069 --name odoo --link db:db -t odoo

```
## Crear rama de directorios con la estructura

doocker modulo
	docker-compose.yml
	dev-addons
	odoo/
		config_odoo/
			odoo.conf
	logs	
### Contenido de "docker-copose.yml"
Es el contenido a pegar dentro del archivo
```
version: '3.1'

services:

  web:

    image: odoo:17.0

    depends_on:

      - db

    ports:

      - "8069:8069"

    volumes:

      - odoo-web-data:/var/lib/odoo

      - ./config_odoo:/etc/odoo

      - ./dev-addons:/mnt/extra-addons

      - ./log:/var/log/odoo

    environment:

      - HOST=db

      - USER=odoo

      - PASSWORD=odoo

  db:

    image: postgres:latest

    environment:

      - POSTGRES_DB=postgres

      - POSTGRES_PASSWORD=odoo

      - POSTGRES_USER=odoo

      - PGDATA=/var/lib/postgrestsql/data/pgdata

    volumes:

      - odoo-db-data:/var/lib/postgres/data/pgdata

  

volumes:

  odoo-web-data:

  odoo-db-data:
```

### Contenido de odoo.conf
```
[options]
addons_path = /mnt/extra-addons
data_dir = /var/lib/odoo
admin_passwd = alia
logfile = /var/log/odoo/odoo-server.log
```
## Montar el contenido en el docker

Para ello, habrá que entrar en el PowerShell con permisos de administrador, buscar la carpeta con los archivos creados y ejecutar el siguiente comando
```
docker-compose up -d
```

## Añadir el contenido dentro de los directorios

Para añadir los archivos necesarios para el funcionamiento del módulo se utiliza el siguiente comando
```
odoo scaffold dam
```


Tras realizar esto al ejecutarse el docker usando enlace host debería entrar a Odoo correctamente
