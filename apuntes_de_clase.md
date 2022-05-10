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

## Clase 5

Spark o DataBricks tienen muchas similitudes con Pandas
Los tipos de datos object Pandas son cuando son Strings o mezclas de Strings y otros tipos de datos.
Hay tipo de índice explícitos (si les ponemos nombre nosotros, por ej si les ponemos nombre a las columnas) e implícitos (automático). El implícito por ejemplo tiene el tipo de dato RangeIndex. Cuando es uno explícito, generalmente es tipo de datos "object".
- Para índices implícitos, se usa df.iloc[filas, columnas]. No se incluye el último elemento en el slicing
- Para índices explícitos, se usa df.loc[filas, columnas]. Incluye el último elemento en el slicing  

Sirve las máscaras booleanas para el iloc y el loc.
Averiguar sobre el garbage collector para eliminar los datos que no se usan más en el código (por ejemplo df que se creó uno desde ese y no se usa más)

shift+tab abre la documentación. También se puede usar ? al final del método y correr la celda.

## Clase 6

Espacio muestreal ($\Omega$). TODAS las posibilidades de los resultados de un experimento.  
Un evento es un espacio más pequeño, parte del espacio muestreal  
Variable aleatoria: le asignan un valor a cada unidad ($\omega$) del espacio muestreal (lo lleva a un número real)  
En probabilidades discretas, se puede cuantificar cada opción, en cambio en la contínua no se puede dar la probabilidad de que un evento específico ocurra, se dice que por ejemplo es la probabilidad de medir entre X e Y.  
Cuando son variables aleatorias discretas independientes, la probabilidad total es el producto de las probabilidades de cada variable  
Función de distribución va dando la probabilidad acumulada de que ocurra. Siempre estará entre 0 y 1.

- Número combinatorio: Cantidad de resultados x exitosos en n intentos. 


### Distribuciones discretas
- Distribución uniforme: Equiprobable. La probabilidad de X es constante 1/n  
    Se representa como X ~ unif{x1,x2,x3,x4...}
- Bernoulli: Dos resultados posibles. éxito probabilidad p, fracaso probabilidad 1-p  
    p $\in$ (0,1) X ~ Be(p)
- Binomial: Número de éxitos en una secuencia de n ensayos con probabilidad fija. 
- Poisson: Cantidad de eventos en un período de tiempo dado. $\lambda$ es un parámetro que define la frecuencia que ocurre el evento, siempre positivo. Se debe poder discretizar el tiempo de tal manera que ocurra un sólo evento en ese tiempo.  

### Distribuiciones contínuas
- Distribución uniforme: Se dice que tiene una distribución uniforme en el intervalo (x,y). La probabilidad es 1/(b-a)  
    Función de distribución acumulada es (x-a)/(b-a) en el itnervalo, 0 antes y 1 después
- Distribución exponencial: Intervalos de tiempos entre eventos en un proceso de Poisson. 
- Distribución normal: La más utilizada, la siguen por ejemplo los errores en una medición, o incluso las medias de medición de muchos ensayos de las mismas características (ver Teorema central del límite).  
    Parámetros: Varianza ($\sigma$2) y media ($\mu$)  
    

## Clase 7

`$conda env list` muestra la lista de ambientes, y un asterisco al lado del que está activo
Si al instalar GeoPandas, te tira el error `$could not find or load spatialindex_c-64.dll` tenés que ir a la consola (dentro del mismo ambiente) y poner `$pip uninstall rtree`

## Clase 8

Clase de repaso
https://pythontutor.com/visualize.html#mode=edit Útil para ver cada paso de un código de python
array.reshape(1,-1): El -1 completa para llegar a lo necesario para mantener la cantidad de datos. Se puede poner en cualquier lado, y siempre completará

##  Clase 9
EDA

https://www.epochconverter.com/ para convertir de timestamp (unix epoch time) a fecha correctamente.  

5 pasos de limpieza de datos:
- Asignar tipos de datos correctos. 
- Estandarizar categorías. mismo nombre para mismo valor, ej: 'ar', 'arg', 'argentina'.
- Corregir valores erróneos.
- Completar datos faltantes.
- Organizar correctamente el dataset. Son útiles las reglas del "tidy data"

**tidy data:**
- Cada variable es una columna
- Cada observación es una fila
- Cada tipo de unidad observacional forma una tabla

## Clase 10
Visualización con MatplotLib

No tomé apuntes, tengo que repasarla mejor

## Clase 11
Join con Pandas

`df.pivot_table()` :   Pivot table como en excel, power BI y cualquier otra herramienta de esas. 
`pd.cut(Series, ['valor_De_corte_1', 'valor_de_corte_2', 'valor_de_corte_3'], labels=['label1','label2'], retbins=True)` : Sirve para cortar en partes una Series, por ejemplo por cada percentil. El retbins te devuelve un segundo objeto con los valores de corte.  
`pd.qcut(Series, q=4)` : Parte en la cantidad deintervalos que se pase, según los percentiles.  
**Puede servir para reducir valores, por ejemplo rangos de edades en vez de edades**

## Clase 12
DataWrangling y dudas de notebooks prácticas anteriores.

Tomé algunos apuntesdirecto en los .md del repo de "apuntes y modelos".

## Clase 13
Data Visualization 2
Bokeh y plotly

from bokeh.paletter import set2
set2 es un diccionario con varios sets de colores. (el 2 es un ejemplo)

Las notebooks se pueden exportar como html, exportando también los gráficos y después embebiendolo en una página.   

En los jupyter notebooks se pude usar código LaTeX para mostrar ecuaciones por ejemplo. Tengo que investigarlo más.  

Plotly parece más simple y directo de usar que Bokeh.   
vtk es una librería para gráficos de alto rendimiento, generalmente sirve para gráficos matemáticos complejos, tomografías, etc.

## Clase 14
TP1 - EDA

`pd.set_option("display.max_colwidth",200)` : Sirve para cambiar el ancho máximo de columna y poder ver mejor las de String

## Clase 16
Estadística inferencial - Pruebas de hipótesis

Definir que p-valor es el que rechazará nuestra hipótesis nula. **NO** es la probabilidad de que sea cierta.  
Nivel de significancia (Alfa): Es el error que se está aceptando del extremo de la gaussiana, en este rango se rechaza la hipotesis. 5% sería Z=1.645 por ejemplo si sólo se considera un lado, sino se divide el porcentaje en los dos extremos.  
El a/b test me parece muy útil para sacar conclusiones de negocio, averiguar más a futuro.   

## Clase 17
Intro a machine learning

**plot_tree** sirve para mostrar como es el árbol con las reglas que definió el modelo. Debe haber funciones similares para los demás modelos de árboles
