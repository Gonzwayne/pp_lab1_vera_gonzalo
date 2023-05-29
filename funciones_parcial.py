import re
import json
import os

def clear_console() -> None:
    """
    La función borra la pantalla de la consola y espera a que el usuario presione Enter antes de
    continuar con el menú.
    """
   
    _ = input('Presiona Enter para continuar al menu...')
    os.system('cls')


def leer_archivo(nombre_archivo):
    """
    Esta función lee un archivo JSON que contiene una lista de héroes y devuelve la lista de héroes o
    una lista vacía si el archivo no existe o tiene un formato incorrecto.
    
    :param nombre_archivo: El nombre del archivo que queremos leer y extraer datos
    :return: una lista de héroes extraída de un archivo JSON. Si el archivo no existe o no se puede
    decodificar, devuelve una lista vacía e imprime un mensaje de error.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            lista_jugadores = json.loads(contenido)
            return lista_jugadores["jugadores"]
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return []
    except json.JSONDecodeError:
        print(f"No se pudo decodificar el archivo '{nombre_archivo}'. Verifica que tenga el formato correcto.")
        return []

lista_jugadores = leer_archivo(r"C:\Users\gonza\OneDrive\Documentos\ejercicios python\zzzz_1er_parcial\dt.json")

def mostrar_jugadores(lista):
    """
    La función "mostrar_jugadores" toma una lista de diccionarios que contienen información del jugador
    e imprime su nombre y posición, al mismo tiempo que devuelve una lista de mensajes formateados.
    
    :param lista: una lista de diccionarios que representan a los jugadores, donde cada diccionario
    contiene las claves 'nombre' (name) y 'posicion' (posición)
    :return: una lista llamada `lista_nueva` que contiene cadenas con el nombre y la posición de cada
    jugador en la entrada `lista`.
    """
    lista_nueva = []
    for jugador in lista:
        mensaje = "{0}, {1}".format(jugador['nombre'], jugador['posicion'])
        print(mensaje)
        lista_nueva.append(mensaje)
    return lista_nueva

def mostrar_estadisticas_jugador(lista):
    """
    Esta función toma una lista de jugadores y permite al usuario seleccionar un jugador por índice y
    muestra sus estadísticas.
    
    :param lista: El parámetro "lista" es una lista de diccionarios, donde cada diccionario representa a
    un jugador y contiene su nombre y estadísticas
    :return: una lista llamada `lista_nueva` que contiene un único mensaje de cadena con el nombre y las
    estadísticas del jugador elegido.
    """
    
    for i, jugador in enumerate(lista):
        msg = "{0} - {1}".format(i+1,jugador["nombre"])
        print(msg)

    while True:
        indice = input("Ingrese el índice del jugador para ver sus estadísticas: ")
        if indice.isdigit():
            indice = int(indice) - 1
            if 0 <= indice < len(lista):
                break
            else:
                print("Índice fuera de rango. Ingrese un índice válido.")
        else:
            print("Entrada inválida. Ingrese un índice numérico.")
    jugador_elegido = lista[indice]
    
    mensaje = "{0}, {1}, {2}, \n".format(jugador_elegido['nombre'],jugador_elegido['posicion'], jugador_elegido['estadisticas'])
    print(mensaje)
    
    return jugador_elegido

def guardar_archivo_csv(nombre_archivo: str, contenido: str) -> bool:
    """
    Esta función guarda el contenido de una cadena en un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operación fue exitosa o no.

    Parametros: 
        -nombre_archivo: Una cadena que representa el nombre del archivo que se va a crear o
        sobrescribir

        -contenido: El contenido que se escribirá en el archivo. Debería ser una cadena

    :retorno: 
        -un valor booleano, ya sea True o False, según si el archivo se creó correctamente o no.
    """
 
    with open(nombre_archivo, 'w') as archivo:
        resultado = None 
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

    
def genera_texto(dicinario_jugador: dict)-> str:
    """
    Esta función toma un diccionario de las estadísticas de un jugador y devuelve una cadena formateada
    que contiene su nombre, posición y estadísticas.
    
    :param dicinario_jugador: Un diccionario que contiene información sobre un jugador, incluido su
    nombre, posición y estadísticas
    :type dicinario_jugador: dict
    :return: una cadena que contiene el nombre, la posición y las estadísticas del jugador en un formato
    específico.
    """


    jugador_indice_ingresado = dicinario_jugador
    jugador_estadisticas = jugador_indice_ingresado["estadisticas"]
    nombre_posicion = "{0}, {1}".format(jugador_indice_ingresado["nombre"], \
                                        jugador_indice_ingresado["posicion"])
    
    lista_claves = ["nombre", "posicion"]
    lista_valores = []

    for clave, valor in jugador_estadisticas.items():
        lista_claves.append(clave)
        lista_valores.append(str(valor))

    claves_str = ",".join(lista_claves)
    valores_str = ",".join(lista_valores)

    datos_str = "{0}\n{1},{2}".format(claves_str ,nombre_posicion ,valores_str)
    return datos_str


def mostrar_logros_jugador(lista):
    """
    Esta función toma una lista de jugadores y permite al usuario ingresar el nombre de un jugador para
    mostrar sus logros.
    
    :param lista: una lista de diccionarios que representan a los jugadores y sus logros. Cada
    diccionario contiene las claves "nombre" (nombre del jugador) y "logros" (logros del jugador)
    """
    for i, jugador in enumerate(lista):
        msg = "{0} - {1}".format(i+1, jugador["nombre"])
        print(msg)

    nombre = input("Ingrese el nombre del jugador para ver sus logros: ").lower().capitalize()


    for jugador in lista:
        if re.search(jugador["nombre"][0:4], nombre[0:4]) != None:
            mensaje = "Logros de {0}: {1}\n".format(jugador['nombre'], jugador['logros'])
            print(mensaje)
            break
    else:
        print("No se encontró ningún jugador con ese nombre.")

def promedio_por_key(lista:list[dict],key:str):
    """
    Esta función calcula el promedio del valor de una clave específica en una lista de diccionarios y
    devuelve el resultado.
    
    :param lista: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista: list[dict]
    :param key: El parámetro clave es una cadena que representa la clave en el diccionario que contiene
    el valor que se va a promediar. En este caso, se utiliza para calcular la media de puntos por
    partido de una lista de jugadores
    :type key: str
    :return: un mensaje que muestra el promedio calculado.
    """
    """
    Esta función calcula el promedio de puntos por juego para una lista de jugadores y devuelve el
    resultado.
    """
    acumulador = 0
    contador = 0

    #validar lista vacia
    for jugador in lista:
        acumulador += jugador["estadisticas"][key]
        contador +=1

    if contador > 0:
        promedio = acumulador / contador
    else:
        return "Error"
    mensaje = print("El promedio es : {0}".format(promedio))
    return mensaje

def lista_jugadores_alfabeticamente(lista:list):
    """
    Esta función toma una lista de diccionarios que contienen información de jugadores y devuelve una
    lista de nombres de jugadores ordenados alfabéticamente.
    """
    nombres = list()

    for jugador in lista:
        nombres.append(jugador["nombre"])

    nombres.sort()
    print(nombres)
    return nombres

def mostrar_salon_de_la_fama_jugador(lista):
    """
    Esta función muestra una lista de jugadores de baloncesto en el Salón de la Fama y permite al
    usuario ingresar el nombre de un jugador para ver si es miembro y mostrar sus logros.
    
    :param lista: una lista de diccionarios que representan a los jugadores de baloncesto y sus logros.
    Cada diccionario contiene las claves "nombre" (nombre) y "logros" (logros)
    """
    for i, jugador in enumerate(lista):
        msg = "{0} - {1}".format(i+1, jugador["nombre"])
        print(msg)

    nombre = input("Ingrese al menos las primeras 4 letras del nombre del jugador para ver sus logros: ").lower().capitalize()
    flag = True
    for jugador in lista:
        if re.search(jugador["nombre"][0:4], nombre[0:4]) != None:
            logros = jugador["logros"]
            for logro in logros:
                if "Miembro del Salon de la Fama del Baloncesto" == logro:
                    print(jugador["nombre"], logro)
                    flag = False
            if flag:print("el jugadaor no pertenece al salon de la fama")    
            break
    else:
        print("No se encontró ningún jugador con ese nombre.")

def calcular_max(lista, key):
    """
    Esta función calcula el valor máximo de una clave dada en una lista de diccionarios.
    
    :param lista: una lista de diccionarios, donde cada diccionario representa a un jugador y sus
    estadísticas
    :param key: El parámetro "clave" es una cadena que representa la clave del diccionario dentro de
    cada elemento del parámetro "lista". Esta clave se utiliza para acceder a un valor específico dentro
    del diccionario y compararlo con los otros elementos de la lista
    :return: La función `calcular_max` devuelve al jugador con el valor más alto para la clave
    especificada en sus estadísticas. Si la lista de entrada está vacía, devuelve `Ninguno`.
    """
    lista_vacia = []
    if not lista:
        return None
    max_valor = lista[0]
    for jugador in lista:
        if jugador["estadisticas"][key] > max_valor["estadisticas"][key]:
            max_valor = jugador

    
    for jugador in lista:
        if jugador["estadisticas"][key] == max_valor["estadisticas"][key]:
            lista_vacia.append(jugador["nombre"])
            lista_vacia.append(max_valor["estadisticas"][key])
            
    print(lista_vacia)
    return max_valor


def calcular_min(lista, key):
    """
    Esta función calcula el valor mínimo de una clave específica en una lista de diccionarios.
    
    :param lista: una lista de diccionarios, donde cada diccionario representa a un jugador y sus
    estadísticas
    :param key: El parámetro "clave" es una cadena que representa la clave del diccionario dentro de
    cada elemento del parámetro "lista". Esta clave se utiliza para acceder a un valor específico dentro
    del diccionario y compararlo con los otros elementos de la lista
    :return: La función `calcular_min` devuelve el jugador con el valor mínimo para la clave
    especificada en sus estadísticas. Si la lista de entrada está vacía, devuelve `Ninguno`.
    """
    if not lista:
        return None
    min_valor = lista[0]
    for jugador in lista:
        if jugador["estadisticas"][key] < min_valor["estadisticas"][key]:
            min_valor = jugador
    return min_valor


def calcular_max_min_dato(lista,calculo,key)->dict:
    """
    Esta función calcula el valor máximo o mínimo de una clave dada en una lista.
    
    :param lista: una lista de diccionarios
    :param calculo: una cadena que indica si se debe calcular el valor máximo o mínimo
    :param key: La clave es una función que se utiliza para extraer un valor de cada elemento de la
    lista. Este valor se usa luego para determinar el elemento máximo o mínimo en la lista, según el
    cálculo especificado. La función clave debe tomar un argumento (un elemento de la lista) y devolver
    un valor que
    :return: un diccionario con el valor máximo o mínimo de una clave dada en una lista, dependiendo del
    valor del parámetro 'calculo'.
    """

    if calculo == 'maximo':
        return calcular_max(lista, key)
    elif calculo == 'minimo':
        return calcular_min(lista, key)
    else:
        print("El tipo de cálculo debe ser 'maximo' o 'minimo'")

def mostrar_jugadores_max_min_promedio(lista:list,key,condicion:str):
    """
    La función toma una lista de jugadores y sus estadísticas, una clave para acceder a una estadística
    específica y una condición (ya sea "menor" o "mayor"), y devuelve una lista de jugadores cuya
    estadística es menor o mayor que un usuario -valor introducido.
    
    :param lista: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista: list
    :param key: La clave es una cadena que representa la estadística específica que queremos comparar
    (por ejemplo, "puntos", "rebotes", "asistencias")
    :param condicion: La condición por la que filtrar a los jugadores. Puede ser "menor" (menor que) o
    "mayor" (mayor que)
    :type condicion: str
    :return: una lista de jugadores cuyas estadísticas cumplen la condición especificada (ya sea mayor o
    menor que un valor dado) para una clave determinada.
    """
    
    lista_promedio = []
    promedio = int(input("ingrese el valor del promedio"))
    print("El promedio es :",promedio)

    for jugador in lista:
        if(condicion == "menor"):
            if(jugador["estadisticas"][key] < promedio):
                mensaje = "{0} {1}".format(jugador['nombre'],jugador["estadisticas"][key])
                print(mensaje)
                lista_promedio.append(jugador)
        else:
            if(jugador["estadisticas"][key] > promedio):
                mensaje = "{0} {1}".format(jugador['nombre'],jugador["estadisticas"][key])
                print(mensaje)
                lista_promedio.append(jugador) 

    return lista_promedio    

def calcular_promedio_menos_jugadormin(lista:list,key):
    """
    Esta función calcula el promedio de una estadística específica para todos los jugadores excepto el
    que tiene el promedio de puntos más bajo por juego y devuelve una lista con un mensaje que indica
    qué jugador fue excluido.
    
    :param lista: una lista de diccionarios que representan a los jugadores de baloncesto y sus
    estadísticas
    :type lista: list
    :param key: El parámetro clave es una cadena que representa la estadística específica para la que
    queremos calcular el promedio, como "rebotes_por_partido" o "asistencias_por_partido"
    :return: una lista llamada "lista_promedio" que contiene un mensaje de cadena sobre el jugador con
    el puntaje promedio más bajo que se excluye del cálculo, además de imprimir el puntaje promedio
    calculado.
    """
   
    lista_promedio = []
    acumulador = 0
    contador = 0
    jugador_min = calcular_min(lista, "promedio_puntos_por_partido")

    for jugador in lista:
        if jugador_min != jugador: 
            acumulador += jugador["estadisticas"][key]
            contador += 1

    promedio = acumulador /contador
    print("El promedio es :",promedio)

    mensaje = "{0} es el jugador excluido con promedio: {1}".format(jugador_min['nombre'],jugador_min["estadisticas"][key])
    print(mensaje)
    lista_promedio.append(mensaje)
        
    return lista_promedio        

def obtener_jugador_mas_logros(lista_jugadores):
    """
    La función devuelve el nombre del jugador con más logros de una lista de jugadores.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene las claves "nombre" (cadena) y "logros" (lista de cadenas). La función devuelve el nombre
    del jugador con más logros (es decir, el jugador cuya lista de "logros" tiene más elementos)
    :return: el nombre del jugador con más logros en la lista de jugadores proporcionada como entrada.
    """
    
    jugador_mayor_logros = None
    mayor_cantidad_logros = 0

    for jugador in lista_jugadores:

        cantidad_logros = len(jugador["logros"])
        if cantidad_logros > mayor_cantidad_logros:
            mayor_cantidad_logros = cantidad_logros
            jugador_mayor_logros = jugador["nombre"]

    return jugador_mayor_logros   

def lista_jugadores_por_posicion(lista:list):
    """
    Esta función toma una lista de diccionarios que contienen información sobre los jugadores y devuelve
    una lista ordenada de sus posiciones.
    
    :param lista: Una lista de diccionarios que representan a los jugadores de un equipo deportivo,
    donde cada diccionario contiene información sobre un jugador, como su nombre, posición y
    estadísticas
    :type lista: list
    :return: una lista ordenada de todas las posiciones de los jugadores en la lista de entrada.
    """
   
    posicion = list()

    for jugador in lista:
        posicion.append(jugador["posicion"])

    posicion.sort()
    print(posicion)
    return posicion

def imprimir_elegir_menu():
    """
    Esta función muestra un menú de opciones para que el usuario elija y ejecuta la función
    correspondiente según la entrada del usuario.
    """
    flag_punto_2 = False
    while True:
        clear_console()
        print("----- Menú de opciones -----")
        print("1. Mostrar lista de todos los jugadores.")
        print("2. Mostrar estadisticas de un jugador.")
        print("3. Guardar estadísticas de ese jugador en CSV.")
        print("4. Buscar jugador por su nombre y mostrar sus logros.")
        print("5. Mostrar promedio del equipo Dream Team, ordenado por nombre de manera ascendente.")
        print("6. Buscar si un jugador es miembro del salon de la fama.") 
        print("7. Mostrar jugador con la mayor cantidad de rebotes totales.")
        print("8. Mostrar jugador con el mayor porcentaje de tiros de campo.")
        print("9. Mostrar jugador con la mayor cantidad de asistencias totales.")
        print("10. Mostrar jugadores que han promediado más puntos por partido que un valor ingresado.")
        print("11. Mostrar jugadores que han promediado más rebotes por partido que un valor ingresado.")
        print("12. Mostrar jugadores que han promediado más asistencias que un valor ingresado.")
        print("13. Mostrar jugador con la mayor cantidad de robos totales.")
        print("14. Mostrar jugador con la mayor cantidad de bloqueos totales.")
        print("15. Mostrar jugadores con un porcentaje de tiros libres superior al valor ingresado.")
        print("16. Mostrar promedio de puntos por partido del equipo excluyendo al jugador con menor cantidad")
        print("17. Mostrar jugador con la mayor cantidad de logros obtenidos")
        print("18. Mostrar jugadores que tengan un porcentaje de tiros triples superior al valor ingresado")
        print("19. Mostrar jugador con mayor cantidad de temporadas jugadas")
        print("20. Mostrar los jugadores ordenados por posición en la cancha, que tengan un porcentaje de tiros de campo superior a un valor")
        
        opcion = input("\nIngrese la opción deseada: ")
        validacion = r"^[1-9]|1[0-9]|20$"
        if re.match(validacion,opcion):

            
            if opcion == "1":
                mostrar_jugadores(lista_jugadores)
            elif opcion == "2":
                lista_nueva = mostrar_estadisticas_jugador(lista_jugadores)
                flag_punto_2 = True
            elif opcion == "3":
                if flag_punto_2 == True:
                    nombre_archivo = "lista_nueva.csv"
                    contenido = genera_texto(lista_nueva)
                    guardar_archivo_csv(nombre_archivo, contenido)
                else: 
                    print(" Error primero realice el punto 2")    
            elif opcion == "4":
                mostrar_logros_jugador(lista_jugadores)           
            elif opcion == "5":
                promedio_por_key(lista_jugadores,"promedio_puntos_por_partido")
                lista_jugadores_alfabeticamente(lista_jugadores)
            elif opcion == "6":
                mostrar_salon_de_la_fama_jugador(lista_jugadores)
            elif opcion == "7":
                calcular_max_min_dato(lista_jugadores,"maximo","rebotes_totales")
            elif opcion == "8":
                calcular_max_min_dato(lista_jugadores,"maximo","porcentaje_tiros_de_campo")
            elif opcion == "9":
                calcular_max_min_dato(lista_jugadores,"maximo","asistencias_totales")
            elif opcion == "10":
                mostrar_jugadores_max_min_promedio(lista_jugadores,"promedio_puntos_por_partido","mayor")         
            elif opcion == "11":
                mostrar_jugadores_max_min_promedio(lista_jugadores,"promedio_rebotes_por_partido","mayor")   
            elif opcion == "12":
                mostrar_jugadores_max_min_promedio(lista_jugadores,"promedio_asistencias_por_partido","mayor")       
            elif opcion == "13":
                jugador_max = calcular_max_min_dato(lista_jugadores,"maximo","robos_totales")
                print("nombre {0} , robos totales: {1}".format(jugador_max["nombre"],jugador_max["estadisticas"]["robos_totales"]))
            elif opcion == "14":
                calcular_max_min_dato(lista_jugadores,"maximo","bloqueos_totales")
            elif opcion == "15":
                mostrar_jugadores_max_min_promedio(lista_jugadores,"porcentaje_tiros_libres","mayor")  
            elif opcion == "16":
                calcular_promedio_menos_jugadormin(lista_jugadores,"promedio_puntos_por_partido")           
            elif opcion == "17":
                jugador_con_mas_logros = obtener_jugador_mas_logros(lista_jugadores)
                print("El jugador con la mayor cantidad de logros obtenidos es:", jugador_con_mas_logros)
            elif opcion == "18":
                mostrar_jugadores_max_min_promedio(lista_jugadores,"porcentaje_tiros_libres","mayor")
            elif opcion == "19":
                calcular_max_min_dato(lista_jugadores,"maximo","temporadas")
            elif opcion == "20":
               lista = mostrar_jugadores_max_min_promedio(lista_jugadores,"porcentaje_tiros_de_campo","mayor")
               lista_jugadores_por_posicion(lista)

        else:
            print("opcion no valida ingrese opcion del 1 al 20") 


print("---------------------------------------------------------------------------")
print("|     Jugador          |    Puntos  |   Rebotes |  Asistencias  |  Robos  |")
print("---------------------------------------------------------------------------")
for jugador in lista_jugadores:
    print("|  {:19s} | {:^10d} | {:^9d} | {:^13d} | {:^7d} |".format(jugador["nombre"], jugador["estadisticas"]["puntos_totales"], jugador["estadisticas"]["rebotes_totales"], jugador["estadisticas"]["asistencias_totales"], jugador["estadisticas"]["robos_totales"]))
print("---------------------------------------------------------------------------")





