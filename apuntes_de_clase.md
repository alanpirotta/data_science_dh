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

## Clase 4

- %%timeit -o : Sirve para medir el promedio de tiempo que tarda en hacer un loop por ejemplo
- np.genfromtxt('Dirección', skip_header=1 `Si tiene encabezado`, delimiter= , dtype=) : Esta sirve para leer con Numpy un csv. No encuento una utilidad para esto teniendo el pd.read_csv.

### Medidas de asociación entre variables
- Covarianza: Asociación lineal entre variables. Positiva si al subir una sube la otra, negativa si es al revés.
Con Numpy es np.cov()

- Correlación: Es la covarianza estandarizada, queda entre -1 y 1. No tiene unidades.

Correlación de Pearson es para lineal, la de Spearman sirve para cuando no es lineal, pero se acerca (no sirve para cuadráticas por ej).

matriz.T : Sirve para transponer la matriz con Numpy

