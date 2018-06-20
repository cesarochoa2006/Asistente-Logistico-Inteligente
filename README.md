# Asistente logístico Inteligente
Este proyecto ha sido desarrollado utilizando las tecnologías Python/Django y algunas herramientas enfocadas en la clasificación y análisis de datos usando algoritmos de inteligencia artificial. 
## Qué es
Es un asistente de labores logísticas a nivel empresarial basado en técnicas comunes de inteligencia artificial. Dentro de las tareas que realiza el agente se encuentran la asignación de rutas y horarios y/o fechas de entrega de productos a potenciales clientes, así como también la asignación inteligente de empresa encargada de la logística de la ruta y el estudio de la que potencialmente es la agenda de entregas basada en tiempo y distancia de un recorrido de entrega de productos a clientes óptimo

## Consideraciones:

1. El asistente está basado en el funcionamiento de una empresa general de productos que deben ser despachados desde la bodega o bodegas principales hasta la ubicación de entrega que exige el cliente. A cada pedido realizado por el cliente, se le debe asignar una fecha y horario de entrega respectiva. 
2. La empresa realiza subcontrataciones de agencias logísticas y de envío, las cuales se encargan de las labores de transporte de los productos desde la bodega principal de la empresa hasta los domicilios destinados por el cliente. 
3. Las fechas y horarios de entrega, la empresa logística y otras labores de clasificación normalmente son realizadas por asistentes logísticos humanos contratados por la empresa.

## Detalle de las funciones

1. Clasificación inteligente de datos: El asistente analiza un documento de excel que contiene información sobre clasificación previa de una empresa logística para el despacho de un pedido, asi como también contiene información sobre fechas y horarios de entregas que han sido asignadas a los clientes previamente. Como resultado de dicho análisis, el asistente logístico devuelve información sobre pedidos para los cuales no se ha realizado dicha clasificación, asignando una empresa logística encargada y una fecha y hora potencial de entrega. En esta categoría se realiza un análisis y clasificación basados en técnicas de Inteligencia Artificial (SVM). 
2. Una vez realizada la clasificación de los datos, ya están listos para el despacho, por lo que para el siguiente paso se debe ejecutar la asignación de ruta, en la cual, utilizando las tecnologías de google maps, se realiza un estudio de los puntos de entrega por grupos de entrega, dicha clasificación y asignación es realizada automáticamente por el asistente, sin embargo, también es posible asignar puntos de entrega de forma manual bien sea en el mapa o escribiendo la dirección del lugar. Una vez realizada la asignación de puntos de entrega con su respectiva localización en el mapa, el asistente, a travéz de tecnicas de inteligencia artificial (Algoritmos genéticos), evalua la que posiblemente será la ruta más óptima para la entrega de los pedidos. 

## Aportes y otros: 
-Para el funcionamiento de este proyecto, se utilizan las librerias de scikit-learn de inteligencia artificial. El código en esta parte del asistente, realiza un análisis utilizando recursos del servidor y está escrito en lenguaje Python. 
-Para la optimización de rutas, se ha realizado una modificación a nivel estructural del código fuente presente en el proyecto "googlemaps-tsp-ga", el cuál se encuentra disponible en Github. Para esta parte del proyecto, se realiza el análisis de las rutas utilizando recursos computacionales del cliente y está escrito en Javascript. 
