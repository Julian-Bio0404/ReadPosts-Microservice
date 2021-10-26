# ReadPosts Microservice

ReadPosts es un microservicio construido en FastApi, que consulta los posts publicados por usuarios y las reacciones de estos, directamente a la base de datos del proyecto principal de Gaman.
Sólo atiende a las peticiones GET y responderá con los posts correspondientes tanto a los seguidos del usuario que realiza el request como los propios.

![](https://img.shields.io/badge/python-v3.9-blue)
![](https://img.shields.io/badge/FastApi-v0.70.0-blue)

## Run

Para correr el proyecto, ejecute:

```bash
docker-compose build
docker-compose up
```

## Contributors
- [Julian Hermida](https://github.com/Julian-Bio0404)