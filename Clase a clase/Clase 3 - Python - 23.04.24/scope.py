#El scope global se define a nivel de modulo, que es un modulo? el archivo .py es el nombre ue se le da, que es a nivel modulo? Es cuando estmos pegados al margen izquierdo 

a = 5

#defino con def
def funcion_1():
    print(a)
    b = 10  #si defino una segunda variable b y le pongo 10 y afuera decido hacer un "print" esto esta mal porque b es local si yo me voy de funcion 1 b no existe mas 
            #A b se lo definio dentro de un bloque de codigo adentro de un scope si salgo del scope no lo puedo ver de adentro se podria ver la b pero de afuera no 

funcion_1() #aca se invoca 

#print(b) #error de scope 

#Con las varibles globales podemos encontrar las constantes por ejemplo:

CONSTANTE_PI = 3.14
#Si bien me lo pone en color estando con mayuscula es por que no se puede tocar por que es un constante 
#Despues no hace falta que vuelva  escribir el 3.14 si no que voy a escribir su nombre que es CONSTANTE_PI
#Al poner todo el nombre en mayuscula estoy dando a entender que esta variable es constante que no se toca y no se puede modificar su valor.

CONSTANTE_PI = 15 #Si yo pongo eso no pasa nad no se va a romper pero esto es un error y no lo quiero hacer 

#Lo que yo quiero que recuerden que cuando yo defino variables quiero que recuerde que se utilizan como constantes globales 
#