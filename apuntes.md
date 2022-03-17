# Apuntes del curso de Data Science en Digital House

## Clase 1

Trabajo en equipo de contestar rápido una pregunta sobre un dataset sobre alumnos de otro curso de DS.  
Explicación de las diferentes etapas del curso.


 ## Clase 2

Explicación de conceptos básicos de Python. La gran mayoría ya lo sabía, pero me sirvió para entender un par de cosas mejor.

- help() para ver la documentación! (equivalente al ? que ya usaba en los notebooks)

- El siguiente código te muestra qué tipo de error se levantó:
    ```python
    try:
        a = 0/0
    except Exception as ex:
        print(type(ex).__name__)
        exit()
    ```

Diferencia entre importaciones:
- import librería : Importa toda la librería, se llaman después usando "librería.metodo"
- from libreria import metodo : importa Sólo el método, asignanole el nombre en mi programa. Se llama después usando "metodo"
- from librería import * : NO USAR ASI. Guarda en tu programa TODOS los métodos, pudiendo sobreescribir cosas incluso.


## Clase 3

https://www.nature.com/articles/s41586-020-2649-2 texto útil sobrela "relevancia" de Numpy
