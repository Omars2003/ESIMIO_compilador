## Esimio_compilador
compilador c++
En este repertorio encontrara el compilador completo, 
el Archivo CompiladorMx.py es el main, que verifica que haya un archivo fuente como entrada, lee el archivo y lo pasar por el archivo lex(lexer) que se encarga de generar tokens, posterior a eso los tokens se pasan al archivo parser.py para que los analize sintacticamente de acuerdo a la gramtica(grammar.txt) y asi genera un árbol de desiciones de manera estructurada y con sentido.

La ultimas 3 fases se basaron en generación de codigo intermedio, optimización y codigo objeto, por medio de un programa emit.py y por medio de un script de construcción.

Como se vio en clase un compilador es capaz de ejecutarse de diferentes maneras de acuerdo a la computadora en la que se esta trabajando y las aplicaciones que ella tiene para poder realizar con exito la compilación, a continuación encontrara dos maneras de poder probar el compilador y generar codigo en c, por lo que nuestra mejor opción es abrirlo en en un Github Codespaces, que es un entorno de desarrollo en la nube proporcionado por GitHub. Permite a los desarrolladores crear y acceder a un entorno de desarrollo completo y personalizado directamente desde el navegador web o desde su editor de código preferido, asi ya tendra todas las dependencias que nosotros como desarrolladores ocupamos.



 
 
 Para probar el compilador realize los siguientes pasos:
 
 # 1.-Selecciones la parte de  <> code.
 ![image](https://user-images.githubusercontent.com/91102881/234360588-4a9987f6-b2da-4cc2-80c3-b03a48ea484c.png)
 
 # 2.- se le desplegara el siguiente menu: y seleccionamos Codespaces
![image](https://user-images.githubusercontent.com/91102881/234360843-ba4703f3-12b0-488d-a8b1-2bc8bef19d8c.png)

 # 3.- Una vez abierto Codespaces seleccionara Crear en Main, recuerda tener una cuenta para poder alojar el software y poder abrir el compilador.
 ![image](https://github.com/Omars2003/ESIMIO_compilador/assets/91102881/f59e6ae0-7ccb-46f0-a888-c26f8de58812)


# 3.-una vez abierto se le abrirla el editor de texto con todos los programas que conforman el compilador.
![image](https://github.com/Omars2003/ESIMIO_compilador/assets/91102881/80c7bdb0-adbc-4eec-bf5e-0db4ebd6c17e)


# 4.-Abra una terminar en el editor de texto de la siguiente manera.
![image](https://github.com/Omars2003/ESIMIO_compilador/assets/91102881/13114f67-a104-4d5c-8347-ca2836cc3bc7)



# 5.-Escriba el siguiente comando:
Para poder   automatizar y controlar el proceso de compilación y construcción del proyecto, creamos un script de construcción, que hara mas facil la creacion del codigo objeto.

para poder comprobar que el Compilador ha tenido exito, generaremos el codigo objeto en c de cualquiera de nuestros programas como ejemplo.
![image](https://github.com/Omars2003/ESIMIO_compilador/assets/91102881/5d952630-180b-45f2-9c22-215473c399fd)

# 6.- Una vez escirtos los comandos anteriores podra ver un nuevo archivo .c para  ejemplo2.tiny, confirmando que ha tenido exito.

![image](https://github.com/Omars2003/ESIMIO_compilador/assets/91102881/0b000ea0-25ad-45ea-b4f0-f8e17a95d5d6)



Si tiene alguna duda, mandarnos mensaje a nuestros correos electronicos



 COMPILADORES
OMAR MARTINEZ GARCIA   omar.paps3012003@gmail.co 
MORALES JIMENEZ OLIVER
