# Proyecto de Resolución de Laberintos

Este proyecto fue realizado por:

- Emanuel Soto Leal
- Jacksem Cortes Vasquez

## Requisitos

- Python 3.10
- Librerías requeridas: psutil, matplotlib, numpy

Puedes instalar estas librerías usando el siguiente comando:

```bash
pip install psutil matplotlib numpy
```

## Rendimiento de los Algoritmos

Velocidad
En laberintos de tamaño 200x200, la velocidad de los diferentes algoritmos de resolución es la siguiente:

DepthFirstSearch: 0.006 segundos
BreadthFirstSearch: 0.1028 segundos
AStar: 0.1503 segundos
El algoritmo DepthFirstSearch supera significativamente a los demás en términos de velocidad.

## Consumo de Memoria
En laberintos de tamaño 200x200, el consumo de memoria de los algoritmos es el siguiente:

Dijkstra: 8328 KB
BellmanFord: 6838 KB
A Star: 5836 KB
El algoritmo Dijkstra es el que consume más memoria, seguido por BellmanFord y A Star.

## Conclusión
Se observa que un algoritmo que tarda más en completar la resolución del laberinto tiende a consumir más memoria. En este proyecto, el algoritmo DepthFirstSearch se destaca por su velocidad, mientras que el algoritmo Dijkstra consume la mayor cantidad de memoria.

¡Gracias por visitar nuestro proyecto!