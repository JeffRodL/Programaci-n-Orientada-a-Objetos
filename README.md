# POO Python

# Objetivos

1. Entender cómo funciona POO.
2. Entender cómo medir la eficiencia temporal y espacial de nuestros algoritmos.
3. Entender cómo y por qué graficar.
4. Aprender a resolver problemas de búsqueda, ordenación y optimización.

# Programación orientada a Objetos

La clave para entender programación orientada a objetos es entender la programación orientada a objetos como agrupaciones de datos y los métodos que operan en dichos datos. 

La POO nos permite modelar cosas reales y concretas del mundo y sus relaciones con otros objetos. 

Para definir una clase, simplemente utilizamos la palabra `class` pro ejemplo

```python
class Hotel:
	pass
```

una vez que tenemos una clase llamada Hotel podemos generar una instancia llamando al constructor de la clase

```python
hotel = Hotel()
```

## Atributos de la instancia:

Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos el método especial __init__ para definir el estado inicial de nuestra instancia. Recibe como parámetro obligatorio *self* que es simplemente referencia a la instancia.}

```python
class Hotel:
	def __init__(self,
numero_maximo_de_huespedes,
lugares_de_estacionamiento):
				self.numero_maximo_de_huespedes =
numero_maximo_de_huespedes
				self.lugares_de_estacionamiento =
lugares_de_estacionamiento
				self.huespedes = 0

hotel = Hotel(numero_maximo_de_huespedes = 50, lugares_de_estacionamiento = 20)
print(hotel.lugares_de_estacionamiento) #20
```

## Métodos de instancia

Mientras que los atributos de la instancia describen lo que representan el objeto, los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase y normalmente operan en las mencionados atributos. Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben self como primer argumento 

```python
class Hotel:
    def __init__(self,
    numero_maximo_de_huespedes,
    lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def añadir_huespedes(self, cantidad_de_huespedes):  #Función que añade un huesped 
        self.huespedes += cantidad_de_huespedes
    
    def checkout(self, cantidad_de_huespedes):          #Función que quita un huesped
        self.huespedes -= cantidad_de_huespedes
    
    def ocupacion_total(self):                          #Función que da el dato de huespedes totales.
        return self.huespedes

hotel = Hotel(numero_maximo_de_huespedes = 50, lugares_de_estacionamiento = 20)
hotel = Hotel(50,20)
hotel.añadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() #2
```

# Tipos de datos abstractos y clases, Instancias

- En python todo es un objeto y tiene un tipo. Representaciones de datos y formas de interactuar con ellos.
- Formas de interactuar con un objeto: creación, manipulación y destrucción.

Definición de clase:

```python
class /nombre_de_la_clase/(/super_class/):
	/expresion/

def /nombre_del_metodo/(self, /parametros/):
	/expresion/
```

Ejemplo:

```python
#definición 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

david = Persona('David', 35)
erika = Persona('Erika', 32)

david.saluda(erika)
```

Tenemos la clase persona, en su constructor recibe los parámetros nombre y edad. Se inicializa las variables de instancia. Cuando se inicializa una variable de instancia se utiliza self.nombre_de_variable. Con el dot notation podemos utilizar las funciones de las clases. 

## Instancias

- Mientras que las clases es un molde, a los objetos creados se les conoce como instancias.
- Cuando se crea una instancia, se ejecuta el método __init__
- Todos los métodos de una clase reciben implicitamente como primer parámetro self.

Los atributos de clase nos permiten:

- Representar datos.
- Procedimientos para interactuar con los mismos (métodos)
- Mecanismos para esconder la representación interna.

Se accede a los atributos con la notación del punto.

Puede tener atributos privados. Por convención empiezan con _

```python
#clase coordenada

#Clase que toma dos parámetros x y y
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Funcion que da la distancia entre dos puntos
    def distancia(self, otra_coordenada): 
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        return (x_diff+y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)

    #Imprimimos la distancia entre la coordenada coord1 y coord2
    print(coord_1.distancia(coord_2))
    #Se imprime si la coord_2 es instancia de la clase Coordenada
    print(isinstance(coord_2, Coordenada))
```

# Decomposición

- Partir un problema en problemas más pequeños
- Las clases permiten crear mayores abstracciones en forma de componentes.
- Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener.

```python
#decomposición de un automovil 
class Automovil:
    def __init__(self, modelo,marca,color):
        self.modelo = modelo 
        self.marca = marca 
        self.color = color  
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)              #que no tiene valor
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasensed(3)
            
class Motor:
    def __init__(self, cilindros, tipo='gasolina'): #default
        self.cilindros = cilindros 
        self.tipo = tipo  
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        pass
```

# Abstracción

- Enfocarnos en la información relevante.
- Separar la información central de los detalles secundarios.
- Podemos utilizar variables y métodos (privados y públicos)

```python
class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = 'Caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'llenando el tanque con agua {temperatura}')
    
    def _añadir_jabon(self):
        print('añadiendo jabón')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
```

En la física se puede usar la abstracción cuando definimos un gas podemos definir como se mueven las moléculas, como se mueve uno de los materiales, temperatura y presión. 

Si se define movimiento, utilizando las ecuaciones de Newton podemos hacer abstracciones. 

# Funciones: base de los decoradores

El concepto de decorador en Python es algo que podríamos ubicar en un nivel “intermedio” en el manejo del lenguaje, por lo que es buena idea que tengas una base sólida, sobre todo en cuanto a funciones al momento de profundizar e implementarlas.

Los decoradores son una forma sencilla de llamar funciones de orden mayor, es decir, funciones que toman otra función como parámetro y/o retornan otra función como resultado. De esta forma un decorador añade capacidades a una funcuón sin modificarla.

un ejemplo de esto son las llantas de un automóvil. Si les colocas cadenas para la nieve, el automóvil aún puede andar y además extiende su funcionalidad para conducir terrenos.

## Recordando sobre funciones

Antes de abordar el tema de decoradores haremos un pequeñp repaso por las funciones, las cuales retornan un valor ante la entrada de un argumento.

Ejemplo donde una función que multiplica un número se eleva a la tercera potencia:

```python
## Función que multiplica un número se eleva a la tercera potencia

def elevar_cubo(numero):
    return numero * numero * numero 

elevar_cubo(3)
```

Si damos argumentos a la función tendremos 27 como resultado. 

## Funciones como objetos de primera-clase

Otro concepto importante a tener en cuenta es que en python las funciones son objetos de primera-clase, es decir, que pueden ser pasados utilizados como argumentos al igual que cualquier otro objeto 

veamos un ejemplo  donde definomos 3 funciones que haremos de manera conjunta 

```python
def presentarse(nombre):
    return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
    return f"hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
    return funcion_entrante("David")
```

Las primeras dos funciones son obvias en su resultado, donde nos mostrarán un mensaje con el valor de la variable nombre. La tercera puede ser más compleja de predecir, ya que toma otra función como entrada. Veamos que pasa si colocamos una función como atributo

```python
consume_funciones(presentarse)
#'Me llamo David'
consume_funciones(estudiemos_juntos)
#'hey David, aprendamos Python!'
```

pongamos atención en cómo la función consume_funciones() se escribe con paréntesis para ser ejecutada, mientras que la función presentarse y estudiemos_juntos solo hace referencia a estas.

## Funciones anidadas

al igual que los condicionales y bucles también puedes colocar funciones dentro de otra función. 

```python
def funcion_mayor():
    print("esta es una función mayor y su mensaje de salida")

    def librerias():
        print("Algunas librerías de Python son: Scikit-Learn, NumPy y Tensorflow")

    def frameworks():
        print("Algunos frameworks de Python son: Django, Flask y Dash")

    frameworks()
    librerias()

funcion_mayor()
```

```python
Out[]: esta es una función mayor y su mensaje de salida
Algunos frameworks de Python son: Django, Flask y Dash
Algunas librerías de Python son: Scikit-Learn, NumPy y Tensorflow
```

Debemos considerar que las funciones anidadas dentro de funcion_mayor no se ejecutan hasta que se llama a esta primera, siendo muestra del scope o alcance de las funciones. Si las llamamos obtendremos error.

# Setter, getters y decorador property

En este punto se da comienzo a conceptos de python que  comienzan a ser avanzados, por lo que es normal que parezcan algo complejos. 

Análisis del siguiente código

```python
def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje...")
    return wrapper

def zumbido():
    print("Buzzzzzzzzzzzzzzzz")

zumbido = funcion_decoradora(zumbido) 
zumbido()
```

¿Qué pasa si llamamos a la función zumbido()? 

sucede lo siguiente:

```python
Out[]: Este es el último mensaje...
			 Buzzzzzzzzzzzzzzzz
			 Este es el primer mensaje...
```

La función wrapper() recibió la función zumbido() cómo parámetro y coloca su salida entre los otros dos prints.

Todo lo que sucede se conoce en programación cómo metaprogramación, ya que una parte del programa trata de modificar a otra durante el tiempo de compilación. En tanto un decorador básicamente toma una función, le añade alguna funcionalidad y la retorna.

## Mejorando la Sintaxis

Definitivamente la forma en que decoramos la función es complejo, pero afortunadamente Python lo tiene en cuenta y podemos utilizar decoradores con el símbolo @ volviendo al mismo ejemplo de funcion_decoradora(), podemos simplificarlo así:

```python
@funcion_decoradora
def zumbido():
    print("Buzzzzzzzzzzzzzzzz")
```

y tenemos el mismo resultado. 

# ¿Qué son getters y setters?

A diferencia de otros lenguajes de Programación, en Python los getters y setters tienen el objetivo de asegurar el encapsulamiento de datos. Cómo habrás visto, si declaramos una variable privada en Python al colocar un guión bajo al inicio de esta (*) y normalmente son utilizados para:* añadir lógica de validación al momento de obtener y definir un valor. Para evitar el acceso directo al campo de una clase.

La realidad es que en python no existen variables netamente privadas, pues aunque se declares con un guión bajo podemos seguir accediendo a estas. En programación Orientada a Objetos esto es peligroso, pues podemos alterar el método de alguna cláse y tener efectos colaterales que afectan la lógica de nuestra aplicación.

## Clases sin getters y setters

Veamos un ejemplo con una clase que almacena un dato de distancia recorrida en millas y lo convierte a kilómetros 

```python
class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia
    
    def convertir_a_kilometros(self):
        return (self.distancia*1.609344)
    

# Creamos un nuevo objeto
avion = Millas()

# indicamos la distancia
avion.distancia = 200

#obtenemos el atributo de la distancia
print(avion.distancia)

#Obtenemos el método convertir_a_kilometros
print(avion.convertir_a_kilometros())
```

## Utilizando getters y setters

Incluyamos un par de métodos para obtener la distancia y otro para que no acepte valores inferiores a cero, pues no tendría sentido que un vehículo recorra una distancia negativa. Estos son métodos getters y setters.

```python
class Millas:
    def __init__(self, distancia=0):
        self.distancia = distancia;
    
    def convertir_a_kilometros(self):
        return (self.distancia*1.609344)
    
    #Metodo getter
    def obtener_distancia(self):
        return self._distancia 
    
    #Metodo setter 
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias negativas.")
        self._distancia = valor
```

El método getter obtendrá el valor de la distancia y el método setter se encargará de añadir una restricción. También debemos notar cómo `distancia` fue reemplazado por `_distancia` denotando que es una variable privada.

Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizado. Esto no es nada escalable si tenemos cientos o miles de líneas de código.

## Función property()

Esta función está incluida en Python, en particular crea y retorna la propiedad de un objeto. La propiedad de un objeto posee los métodos getter(), setter() y del().

En tanto la función tiene cuatro atributos: property(fget, fset, fdel, fdoc):

- fget: trae el valor de un atributo.
- fset: define el valor de un atributo.
- fdel: elimina el valor de un atributo.
- fdoc: crea un docstring por atributo.

veamos el ejemplo del mismo caso implementando la función property()

```python
class Millas:
    def __init__(self):
        self._distancia = 0
    
    #Función para obtener el valor de _distancia.
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia 
    
    #función para definir el valor de _distancia.
    def definir_distancia(self, recorrido):
        print("Llamada al método setter")
        self._distancia = recorrido

    # función para eliminar el atributo _distancia.
    def eliminar_distancia(self):
        del self._distancia

    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

#Creamos un nuevo objeto
avion = Millas()

#Indicamos la distancia 
avion.distancia = 200

#Obtenemos su atributo _distancia.
print(avion.distancia)
```

aunque en este ejemplo hay una sola llamada a print, tenemos tres líneas como salida pues esta llama a los primeros dos métodos. Por lo que la propiedad `distancia` es una propiedad de objeto que ayuda a mantener el acceso de forma privada.

## Decorador @property

Este decorador es uno de varios con los que ya cuenta Python, el cual nos permite utilizar getters y setters para hacer más fácil la implementación de la programación orientada a objetos en Python cambiando los métodos o atributos de las clases de forma que no modifiquemos el código. Veamos un ejemplo

```python
class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos su atributo distancia
print(avion.definir_distancia)
```

de esta manera usamos el decorador @property para utilizar getters y setters de una forma más prolija e incluimos una nueva funcionalidad a nuestro método. 

`definir_distancia()` , al mismo tiempo protegemos el acceso a nuestras variables privadas y cumplimos con el principio de encapsulación.

> Lo siguiente es información complementaria encontrada en blogs de programadores en python.
> 

# ¿Qué es el encapsulamiento en Python?

En programación modular y más especificamente en programación orientada a objetos se denomina encapsulamiento al ocultamiento del estado, es decir, de los datos miembros de un objeto de manera que solo se pueda cambiar mediante las operaciones definidas para ese objeto. 

Cada objeto está aislado del exterior, es un módulo natural y la aplicación entera se reduce a un agregado o rompecabezas de objetos. El aislamiento protege a los datos asociados de un objeto contra su modificación por quien no tenga derecho a acceder a ellos, eliminando efectos secundarios e interacciones.

De esta forma, el usuario de la clase puede obviar la implementación de los métodos y propiedades para concentrarse solo en cómo usarlos. Por otro lado se evita que el usuario pueda cambiar su estado de maneras imprevistas e incontroladas.

Se define entonces como el “ocultamiento del estado” es decir “los datos miembros de un objeto”. Hablamos de ocultar datos de atributos o métodos, mas específicamente de protegerlos para que solo puedan ser cambiados mediante “operaciones definidas”. Esto indica que no se puede modificar un atributo si no es a través de un método que se haya creado específicamente para eso. Es de eso que nacen los getter, setter y deleter. 

## ¿Qué es el ámbito “protegito, privado”?

> En Python las propiedades y métodos privados no existen, por lo que son fácilmente sobre-escribibles.
> 

### Atributos  protegidos

Del siguiente código:

```python
## Atributos protegidos en Python

class usuario(object):
    def __init__(self, name, password):
        self.name = name
        self._password = password

Usuario1 = usuario("Jefferson","1234")
print(Usuario1.name,Usuario1._password)
```

con outpu[]: Jefferson, 1234. 

El atributo password está con un guión bajo, lo que indica que es un atributo protegido. Lo cual establece que solo puede ser accedido por esa clase y sus sub-clases. Es decir, aquellas que hereden de la clase padre. Se suele ver muy a menudo como una buena práctica para atributos o métodos de uso interno y también para evitar colisión de los mismo nombres de métodos o atributos causados por herencia. S

### Atributos privados

En el caso de atributos privado, estamos indicando que este solo podrá ser accedido o modificado si se específica la clase precedida por un guión bajo seguida del atributo precedido por un doble guión bajo

```python
#Atributos privados en python

class usuario (object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave
        
Usuario1 = usuario ("Roberto", "qwerty")
print (Usuario1.nombre, Usuario1.__clave)
```

Esto dará error: **AttributeError: ‘usuario’ object has no attribute ‘__clave’**

La forma correcta de acceder a el sería especificando primero la clase a la que pertenece de la siguiente manera:

```python
class usuario(object):
    def __init__(self, name, password):
        self.name = name
        self.__password = password 

Usuario1 = usuario("Jefferson", "123qwe")
print(Usuario1.name, Usuario1._usuario__password)
```

Como se ve se puede acceder igualmente a un atributo por más que sea privado y modificarlo de la misma manera. Pero no es lo que se “considere correcto”. Por lo que para ello si deseamos implementar métodos que nos permitan modificar estos atributos de la forma que se suele hacer en otros lenguajes donde se aplica “encapsulamiento” podemos hacerlo utilizando getter, setter y deleter mediante el uso decorador @Property

## Atributos de clase en Python: Getter, Setter y Deleter

> En python dentro de las clases podríamos decir que todo son atributos, incluso los métodos podríamos definirlos como “atributos llamables” y las propiedades “atributos personalizables”. Por ende ahora:
Las  propiedades son atributos que “manejamos” mediante getter, setter y deleter.
”Atributos manejables” que nos permiten invocar código personalizado al ser creados, modificados o eliminados.
> 

Las propiedades nos permiten por ejemplo llamar código personalizado cuando un atributo, método, variable es mostrado, modificado, borrado.

## @Property en python

La función integrada property() nos permitirá interceptar la escritura, lectura, borrado de los atributos y además nor permiten incorporar una documentación sobre los mismos. La sintaxis para invocarla es la siguiente:

```python
@property
```

1. Getter: se encargará de interceptar la lectura del atributo.
2. Setter: Se encargará de interceptar cuando se escriba.
3. Deleter: Se encarga de interceptar cuando es borrado.
4. Doc: Recibirá una cadena para documentar el atributo.

Ejemplificado con un código

```python
class Perros(object):                   #Declaramos la clase principal Perros
    def __init__(self, nombre, peso):   #Definimos los parámetros 
        self.nombre = nombre;           #Declaramos los atributos (Privados ocultos)
        self.__peso = peso              
    @property 
    def nombre(self):                   #Definimos el método para obtener el nombre
        "Documentación del método nombre"#Documento del método 
        return self.__nombre            #Aquí simplemente estamos retornando el atributo privado oculto 

    # Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter 
    #Ahora vamos a utilizar setter y deleter para modificarlos  

    @nombre.setter                      #Propiedad Setter 
    def nombre(self,nuevo):
        print("Modificando nombre..")
        self.__nombre = nuevo
        print("El nombre se ha modificado por")
        print(self.__nombre)
    #Aquí vuelvo a pedir que retorne el atributo para confirmar
    @nombre.deleter                     #Propiedad Deleter
    def nombre(self):
        print("Borrando nombre...")
        del self.__nombre 
#-------------------Hasta aquí llega Property------------------------------------

    def peso(self):                     #Definimos el método para obtener el pase
        return self.__peso              #Aquí simplemente estamos retornando el atributo privado 

#Instanciamos 
Tomas = Perros('Tom', 27)
print(Tomas.nombre)                     #Imprimimos el nombre de Tomas. Se hace a través de getter
                                        #Que en este caso como esta luego de property lo toma como el primer método...
Tomas.nombre = 'Tomasito'               #Cambiamos el atributo nombre que se hace a través de setter. 
del Tomas.nombre                        #Borramos el nombre utilizando deleter.
```

Con el output[]:  

Modificando nombre..
El nombre se ha modificado por
Tom
Tom
Modificando nombre..
El nombre se ha modificado por
Tomasito
Borrando nombre...

Se define primero `property`  y luego de ella el método mediante el cual retornamos el nombre (get) que en este caso al ser el primer método luego de property lo toma automáticamente como Getter (línea 10). Luego especificamos el (set) que nos permite lanzar un print al modificar el atributo privado nombre. Y luego (deleter) que nos permite lanzar otro print al borrarlo.

Si se agrega el peso se tiene entonces.

```python
class Perros(object):                       #Declaramos la clase principal Perros
    def __init__(self, nombre, peso):       #Definimos los parámetros 
        self.__nombre = nombre              #Declaramos los atributos
        self.__peso = peso
    @property
    def nombre(self):                       #Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla" # Doc del método
        return self.__nombre                #Aquí simplemente estamos retornando el atributo privado
#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
#Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre)               #Aquí vuelvo a pedir que retorne el atributo para confirmar
    @nombre.deleter                         #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
        
    @property
    def peso(self):                         #Definimos el método para obtener el peso #Automáticamente GETTER
        return self.__peso                  #Aquí simplemente estamos retornando el atributo privado
    @peso.setter
    def peso(self, nuevopeso):
        self.__peso = nuevopeso
        print ("El peso ahora es")
        print (self.__peso)
    @peso.deleter                           #Propiedad DELETER
    def peso(self): 
        print("Borrando peso..")
        del self.__peso
#Instanciamos
Tomas = Perros('Tom', 27)
print (Tomas.nombre)                        #Imprimimos el nombre de Tomas. Se hace a través de getter
                                            #Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito'                   #Cambiamos el atributo nombre que se hace a través de setter
print (Tomas.nombre)                        #Volvemos a imprimir
Tomas.peso = 28
del Tomas.nombre                            #Borramos el nombre utilizando deleter
```

# Encapsulamiento, getters y setters

**Un Decorator:** Usar ropa es un ejemplo del uso de decoradores en la vida real. Cuando tienes frío, te envuelves en un suéter. Si todavía tienes frío con un suéter, puedes usar una chaqueta en la parte superior. Si está lloviendo, puedes ponerte un impermeable. Todas estas prendas “amplían” tu comportamiento básico, pero no son parte de ti, y pueden quitarse fácilmente cuando no las necesites.

**Un Decorator en código:** No es más que un objeto que agrega nuevas funcionalidades al objeto original.

El encapsulamiento permite:

- Permite agrupar datos y su comportamiento.
- Controla el acceso a dichos datos.
- Previene modificaciones no autorizadas.

En la definición de la clase el atributo región es privado y está inicializado en None. Al ser privado no debería poder accederse a su valor desde fuera de la clase directamente, sino que debería hacerse mediante un método que retorne su valor. De la misma manera no debería poder modificarse su valor desde fuera, así que es necesario un método para eso.

```python
#Encapsulamiento, getters y setters
class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')

casilla = CasillaDeVotacion(123,['Guatemala','Zacapa'])
print(casilla.region)
casilla.region = 'Guatemala'
print(casilla.region)
```

El decorador @property otorga funcionalidades al método región. En ese momento región puede ser:

- **getter:** un método que retorne el valor del atributo.
- **setter:** un método que asigne un valor al atributo.

Por eso podemos hacer @region.metodo, en este caso @region.setter y definir un método que me permita controlar que valor va a ser asignado a ese atributo. Si el valor no es el correcto, con raise indicando un error.

# Herencia

- Permite modelar una jerarquía de clases.
- Permite compartir comportamiento común en la jerarquí.
- Al padre se le conoce como superclase y al hijo como subclase.

Un aspecto importante de la herencia es la posibilidad de reutilizar código. La reutilización es uno de los pilares de POO, de manera que evitamos reinventar la rueda cada vez. Si tenemos un comportamiento que es común entre una serie de objetos de la misma categoría, este comportamiento debe enviarse a una clase superior que permita compartirlo con sus clases hijas. Esto facilita la mantenibilidad del código haciéndolo más estable. 

```python
#Herencia

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura

# En python para heredar una clase se utiliza de la siguiente manera
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())
#lo interesante de las herencias es que pueden utilizar métodos de la clase padre
    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
```

Output[]: 12
               25

# Polimorfismo

El polimorfismo es una forma de herencia en la que la implementación base se altera, entonces el polimorfismo sería una herencia editada. 

- La habilidad de tomar varias formas.
- En python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self._action = 'Ando caminando'

    def avanza(self):
        print(f'{self._action}')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
        self._action = 'Ando moviendome en mi bicicleta'

    def avanza(self):
        super().avanza()

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()
```

# Introducción a la complejidad algorítmica

- ¿Por qué comparamos la eficiencia de un algoritmo?
- Complejidad temporal vs complejidad espacial.
- Podemos definirlo como T(n)

Es importante tener el control de cuánto tiempo, espacio de memoria y poder de cómputo se necesita para poder ejecutar ciertos algoritmos. Algunos pueden ayudarnos a optimizar mejor el tiempo.

La función T(n) determina el tiempo que tarda un algoritmo en ejecutarse. Esta función nos ayuda a 

- Cronometrar el tiempo en el que corre un algoritmo.
- Contar los pasos con una medida abstracta de operación.
- Contar los pasos conforme nos aproximamos al infinito.

```python
# Complejidad algoritmica en Python 
import time

#Implementación factorial 

def factorial(n):
    respuesta = 1
    while n>1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial_r(n):
    if n == 1: 
        return 1
    return  n*factorial_r(n-1)

if __name__ == "__main__":
    n = 300000
    comienzo = time.time()
    factorial(n)
    #print(n,'!=',factorial(n))
    final = time.time()
    print('t=',final-comienzo)

    comienzo = time.time()
    #print(n,'!=',factorial_r(n))
    factorial_r(n)
    final = time.time()
    print('t_r=',final-comienzo)
```

El código ejecuta el factorial de un número n de forma norma y de forma recursiva para determinar el tiempo empleado de ejecución de cada manera. El tiempo tiende a tener un comporamiento cuadrático, por lo que a mayor número, el tiempo crece de forma grotesca.

## Conteo abstracto de operación

Existe una función que nos ayuda a conocer el comportamiento de cada uno de nuestros algoritmos. Por ejemplo, el siguiente código ejecuta algoritmo del tipo lineal y cuadrático. Para medir la complejidad, se utiliza la Big O Notation.

```python
#Conteo abstrarcto de operación
def f(x):
    respuesta = 0
    #Loop independiente 
    for i in range(1000):
        respuesta += 1
    #Loop dependiente
    for i in range(x):
        respuesta += x
    #Doble loop 2*x*x=2x^2 
    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1
    #respuesta = 1002 + x + 2x^2
    return respuesta
```

Esta función polinomial es del tipo $O(n^2)$.

## Notación asintótica

- No importa varicaciones pequeñas
- El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito.
- Mejor de los casos, promedio, peor de los casos.
- Big O
- Nada más importa el término de mayor tamaño

- Un loop
    - crecimiento lineal.
- Un lopp dentro de otro.
    - Crecimiento cuadratico.
- Llamadas recursivas
    - Crecimiento exponencial.
    

```python
# Ley de la suma

def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)

#O(n) + O(n) = O(n+n) = 0(2n) = 0(n)
```

Este ejemplo es uno lineal, y la suma de dos funciones lineales da como resultado un lineal.

```python
# Ley de la suma 

def f(n):
    for i in range(n):
        print(i)
    for i in range(n*n):
        print(i)

# O(n) + O(n*n) = O(n+n^2) = O(n^2)
```

El comportamiento del primer for es lineal, pero el segundo es cuadrático. La función de estas dos funciones es cuadrático dado que nos importa de manera asintótica el comportamiento de la función cuadrática.

```python
# Ley de la multiplicación

def f(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
f(10)
# O(n) * O(n) = O(n*n) = O(n^2)
```

Una iteración dentro de una iteración, la complejidad se multiplica.  Un loop dentro de un loop es complejidad cuadrática.

```python
#Recursividad múltiple
def fibonacci(n):
    if n == 0 or n ==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

# Algoritmo del tipo O(2^n)
```

Un fibonacci recursivo. Por cada llamada de fibonacci regresamos dos números. Entre más crece, llamamos más y más funciones de la forma 2**n. Si se llamara 3 veces sería 3**n, etc. 

## Clases de complejidad algorítmica

- O(1) constante.
    - No importa la cantidad de input que reciba, siempre demora el mismo tiempo.
- $O(n)$ lineal.
    - La complejidad crecerá de forma proporcional a medida que crezca el input.
- $O(\log n)$ logarítmico.
    - Nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabiliza.
- $O(n \log n)$ log lineal.
    - Crecerá de forma logarítmica pero junto con una constante.
- $O(n^2$) polinomial.
    - Crecerá de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
- $O(2^n)$ exponencial.
    - Crecerá de forma exponencial por lo que la carga es muy alta. Para nada recomendables en ningún caso, solo análisis conceptual.
- $O(n!)$ Factorial
    - Crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamás utilizar este tipo de algoritmos.
    
    ![Untitled](POO%20Python%20f1fa7c98eec648518166ee64b7cb1c8c/Untitled.png)
    

# Búsqueda Lineal

- Buscar en todos los elementos de manera secuencial.
- ¿Cuál es el peor caso?

```python
import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
```

Mejor caso: cuando el elemento se encuentra en la primera posición requiere decir que solo realiza 1 iteración el bucle for por lo tanto su complejidad es O(1) 

Peor caso: Cuando el elemento se encuentra en la última posicioń o no se encuentra dentro del array, la complejidad sería O(n).

# Busqueda binaria

- Divide y conquista.
- El problema se divide en 2 en cada iteración.
- ¿Cuál es el peor caso?

- Si tu lista está ordenada:
    - Usar algoritmo de buśqueda binaria.
- Si se utilizará muchas veces tu lista:
    - Lo mejor es ordenarla y utilizar algoritmo de busqueda binaria.
- Si tu lista no está ordenada y se va a utilizar solo una vez:S
    - Utilizar algoritmo de busqueda lineal.
    

```python
import random 

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    if comienzo > final:
        return False
    medio = (comienzo + final)//2 #División de enteros

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1 , final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
```

La búsqueda binaria toma dos valores, de comienzo y final. 

Si el comienzo es mayor que el final, entonces regresa False, porque se pasó.

La lista se divide en dos,  comienzo+final/2 sin residuos. 

Si la lista con el índice medio es igual al objetivo, lo encontramos. Sino, la lista en el medio es menor al objetivo, se realiza otra busqueda binaria. Comienza en medio+1 (el lugar donde estabamos nos corremos una casilla) y el final sigue siendo el mismo.

Si el elemento es mayor,  se hace otra búsqueda y se va una casilla hacia atrás. 

# Ordenamiento de burbuja

El ordenamiento de burbuja es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si estan en el orden incorrecto. Este procedimiento se repite hasta que no se requieren más intercambios, lo que indica que la lista se encuentra ordenada.

Bubble Sort da una garantía que el elemento más grande se encuentra siempre hasta el final. Si lo único que se requiere es el valor más alto, se usa el ordenamiento una sola vez O(n) para obtenerlo. 

```python
import random 

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
```

Las limitaciones de este problema es que tiene complejidad O(n^2). Esto limita a la hora de querer ordenar una lista gigantesca. 

# Ordenamiento por inserción

El ordenamiento por inserción es uno de los algoritmos más comunes que estudian los científicos de cómputo. Es intuitivo y fácil de implementar, pero es muy ineficiente para listas de gran tamaño.

Una de las características del ordenamiento por inserción es que ordena en “su lugar”. Es decir que no requiere memoria adicional para realizar el ordenamiento ya que simplemente modifican los valores de memoria.

La definición más simple:

Una lista es dividida entre una sublista ordenada y otra sublista desordenada. Al principio la sublista ordenada contiene un solo elemento, por lo que por definición se encuentra ordenada.

A continuación se evalua el primer elemento dentro la sublista desordenada para que podamos insertarlo en el lugar dentro de la lista ordenada. 

A continuación se evalua el primer elemento dentro la sublista desordenada para que podamos insertarlo en el lugar correcto dentro de la lista ordenada. 

La inserción se realiza al mover todos los elementos mayores al elemento que se está evaluando un lugar a la derecha.

# Ordenamiento por mezcla

El ordenamiento por mezcla es un algoritmo de divide y conquista. Primero divide una lista en partes iguales hasta que quedan sublistas de 1 a 0 elementos. Luego las recombina en forma ordenada. Merge Sort.

```python
import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
```

# Ambientes Virtuales

- Permiten aislar el ambiente para poder instalar diversas versiones de paquetes.
- A partir de Python 3 se incluye en la librería estándar en el módulo venv.
- Ningún ingeniero profesional de Python trabaja sin ellos.

# ¿Por qué graficar?

- Reconocimiento de patrones
- Predicción de una serie
- Simplifica la interpretación y las conclusiones acerca de los datos.

> No siempre debemos buscar patrones donde no los hay.
> 

## Graficado simple

- Bokeh permite construir gráficas complejas de manera rápida y con comandos simples.
- Permite Exportar a varios formatos como html, notebooks, imágenes, etc.
- Bokeh se puede utilizar en el servidor de Flask y Django.

```python
from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file = ('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuántos valores quiere graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []
    for i in x_vals:
        val = int(input(f'valor Y para {i}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)
```

# Introducción a la optimización

- El concepto de optimización permite resolver muchos problemas de manera computacional.
- Una función objetiva que debemos maximizar o minimizar.
- Una serie de limitantes que debemos respetar.

Problema P vs Np: 

No todos los problemas pueden ser resueltos de manera eficiente.

# El problema del morral

Imagina que eres un ladrón que quiere entrar a un museo pero te topas con un problema: solamente hay una mochila para cargar las cosas y debes elegir que objetos llevarte de mayor valor.