# Prueba_linets

Clone el repositorio, y siga los siguientes pasos:
* **El proyecto esta basado en framework django con python y montado en un contenedor docker:**
* Para instalar docker en windows, acceda al siguiente enlace: https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows.
1. Una vez instalado docker, inicie "Docker Desktop".
2. Cuando docker este iniciado, acceda a la PowerShell, y ejecute el siguiente comando para verificar si docker esta instalado: docker --version
3. Ejecute el siguiente comando en la carpeta donde clono el repositorio,donde se encuentre el archivo "docker-compose": docker-compose up
4. El proyecto, será levantado en "localhost", puerto "8080", acceda desde el navegador al siguiente enlace: "localhost:8080/inventario"

## Pytest
* Para la ejecución de pruebas unitarias, se utiliza Pytest con coverage, el cual genera un archivo html donde ver el porcentaje de cumplimiento de las pruebas, este archivo se encuentra en la carpeta "htmlcov" y el archivo es "index.html".
* Las pruebas cubren 3 áreas: urls, models y views.
