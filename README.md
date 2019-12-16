# Challenge Deep Vision

> Gonzalo Zigarán

Challenge para Deep-Vision sobre el algoritmo **NMS (Non-Maximum Suppression)** y la mejora de **soft-NMS**

El algoritmo está implementado en [`utils.py`](blob/master/utils.py), junto con sus funciones auxiliares y una función para crear un *dataset* de prueba.

En el notebook [`challenge.ipynb`](blob/master/challenge.ipynb), se ejecuta el algoritmo **NMS** y se comparan los algoritmos **NMS** y **soft-NMS**.

Con el archivo `Dockerfile` se puede crear la imagen para poder ejecutr el notebook.

### Ejecutar con Docker

En el directorio del repositorio crear la imagen con:

```bash
$ docker build -t challenge_dv .
```

Correr la imagen de Docker con:

```bash
$ docker run -p 8888:8888 -v "$PWD":/home/jovyan/work challenge_dv
```

Se monta en el directorio `work/` los archivos del repositorio y se obtiene el link para abrir jupyter notebook en un navegador. 
