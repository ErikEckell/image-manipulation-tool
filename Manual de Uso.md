Instrucciones para usar el programa de imágenes:

-Primero, descargar la carpeta con los archivos del programa y abrirla con un editor de código para python.

-El programa se inicia desde el archivo "main.py" al correrlo con el editor de código.

-Se desplegará un menu con cuatro opciones (crear/abrir proyecto, trabajar en un proyecto, ver proyecto actual, salir) para el usuario donde se deberá seleccionar una de ellas. No se podra acceder a la segunda ni a la tercera opcion si un proyecto no ha sido creado.

-Al elegir la opcion uno, se podra crear un proyecto, abrir un proyecto ya existente o guardar el proyecto actual. Para crear el proyecto sera necesario ingresar el archivo de la imagen que se quiere editar (Ej: Imagen.png / Imagen2.jpg). Cada vez que se solicite al usuario ingresar un archivo se tendrá que hacer con el mismo formato que al crear un proyecto.

-La segunda opcion llevara al usuario a un menu con opciones para editar la imagen. Dependiendo de la selección del usuario se aplicara la opcion seleccionada de manera directa o en el caso de filtros, composiciones y dibujo se le llevara a otro menu especificos de cada opcion. En este ultimo menu especifico para cada opcion, el usuario podra elegir que accion aplicarle a la foto y en caso de ser necesario se le pediran los parametros para poder hacerlo.

-La tercera opcion simplemente mostrara el estado actual del proyecto en la pantalla.

-Para finalizar el programa se deberá elegir la cuarta opcion del menu principal.

-Detalles a considerar:
-Cuando pregunta por 'x' e 'y' se refiere a las coordenadas en la imagen, estas varían según el tamaño de la imagen, partirán desde el extremo superior izquierdo y siempre serán positivas.
-Al preguntar por 'r','g','b' se refiere al espacio de color RGB o red,green,blue, estos valores se mueven de 0 a 255.
