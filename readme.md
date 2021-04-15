## Instruciones

1. Descargar imagen de mysql en docker

```
docker run -d -p 3306:3306 --name transporte -e MYSQL_ROOT_PASSWORD=secret mysql:5.7

```
2. Crear una base de datos llamada **transporte**

3. Verificar mediente el comando **docker ps** que la base de datos esté corriendo y ver el id de la base de datos. En caso que la base de datos no esté corriendo consulte el id del contenedor con el comando **docker ps -a** y ejecute el comando **docker start id_mysql** siendo id_mysql el id del contenedor.

4. Mediante el siguiente comando verifique en que DB_HOST está corriendo la base de datos y modifiquelo en el DB_HOST del comando del paso 5. (Debe reeamplazar **id_mysql** por el id del contenedor de la base de datos)

```
docker inspect --format='{{range .NetworkSettings.Networks}}{{println .IPAddress}}{{end}}' id_mysql
```
5. Dentro del directorio **transport_ms** ejecutar el siguiente comando:

**Comando al ejecutar por primera vez**

```
docker build -t transport_ms . && docker run -p 4000:4000 -e DB_HOST=172.17.0.2 -e DB_PORT=3306 -e DB_USER=root -e DB_PASSWORD=secret -e DB_NAME=transporte -e URL=0.0.0.0:4000 transport_ms
```
**Comando si ya existe el contenedor**

```
docker run -p 4000:4000 -e DB_HOST=172.17.0.2 -e DB_PORT=3306 -e DB_USER=root -e DB_PASSWORD=secret -e DB_NAME=transporte -e URL=0.0.0.0:4000 transport_ms
```

6.  Dentro del directorio **transport_api** ejecutar el comando

**Comando al ejecutar por primera vez**

```
docker build -t transport_api . && docker run -p 5000:5000 transport_api
```
**Comando si ya existe el contenedor**

```
docker build -t transport_api . && docker run -p 5000:5000 transport_api
```

7.  Abrir  GraphQL : http://localhost:5000/graphiql

8.  Hacer las siguientes consultas:

Crear un medio de transporte y retornar el tipo de transporte y sus características
```
mutation {createTransporte(transporte:
{    id_usuario: 3, tipo_transporte:"Bicicleta",    carac_transporte:"Bicicleta de ciclomontañismo con rin 28" ,    color_transporte:"Negro"
})
{    tipo_transporte, carac_transporte}
}
```

Actualizar  un medio de transporte y retornar sus atributos

```
mutation {
updateTransporte(id:1, transporte:{    
id_usuario: 3,
tipo_transporte:"Modificada Bicicleta",
carac_transporte:"Bicicleta en fibra de carbono con suspención" ,    
color_transporte:"Azul Marino"
}){
id_usuario
tipo_transporte
carac_transporte
color_transporte
}
}
```

Consultar todos los medios de transporte registrados

```
query {
  allTransportes {    
tipo_transporte
carac_transporte
}
}
```
Consultar un medio de transporte por si ID

```
query 
{transporteById(id:1){
 id_transporte    
 tipo_transporte
color_transporte
}
}
```
Eliminar un medio de transporte por su ID

```
mutation {deleteTransporte(id:1)}
```