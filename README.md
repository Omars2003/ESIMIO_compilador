## Esimio_compilador
compilador c++
En este repertorio encontrara el compilador completo, 
el Archivo CompiladorMx.py es el main, que verifica que haya un archivo fuente como entrada, lee el archivo y lo pasar por el archivo lex(lexer) que se encarga de generar tokens, posterior a eso los tokens se pasan al archivo parser.py para que los analize sintacticamente de acuerdo a la gramtica(grammar.txt) y asi genera un árbol de desiciones de manera estructurada y con sentido.
La ultimas 3 fases se basaron en generación de codigo intermedio, optimización y codigo objeto.

Como se vio en clase un compilador es capaz de ejecutarse de diferentes maneras de acuerdo a la computadora en la que se esta trabajando y las aplicaciones que ella tiene para poder realizar con exito la compilación, a continuación encontrara dos maneras de poder probar el compilador y generar codigo en c.
 
 
 Para probar el compilador realize los siguientes pasos:
 
 # 1.-Selecciones la parte de  <> code.
 ![image](https://user-images.githubusercontent.com/91102881/234360588-4a9987f6-b2da-4cc2-80c3-b03a48ea484c.png)
 
 # 2.- se le desplegara el siguiente menu: y seleccionamos descargar ZIP
![image](https://user-images.githubusercontent.com/91102881/234360843-ba4703f3-12b0-488d-a8b1-2bc8bef19d8c.png)


# 3.-una vez descargado, extraiga los archivos en una carpeta,seleccione la carpeta y presione abrir con Visual Studio Code
![image](https://user-images.githubusercontent.com/91102881/234361303-7be74c81-d477-4229-b0d7-bc54a4cace41.png)

# 4.-abra una terminar en la carpeta
![image](https://user-images.githubusercontent.com/91102881/234361509-5cac68f5-0c6c-45fc-bc96-c6c321a6fb22.png)

# 5.-Escriba el siguiente comando:
podra ver como el codigo que esta en el archivo ejemplo1.tiny se agrupa e identifica las funciones que hay en cada linea de codigo, completandose asi las primeras fases de la creacion de un compilador
![image](https://user-images.githubusercontent.com/91102881/234361857-9e379ac2-06b9-48ae-8635-3e96127cb1cb.png)





OMAR MARTINEZ GARCIA COMPILADORES
MORALES JIMENEZ OLIVER
