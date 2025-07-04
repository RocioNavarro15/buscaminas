# import pygame
# import random
# import csv

# #Caracteristicas pantalla
# def inicializar_caracteristicas_pantalla(ancho:int, largo:int, titulo_juego:str, ruta_icono:str) -> pygame.Surface: #?
#     """
#     Esta función permite inicializar la pantalla en general.
    
#     Recibe:
#         ancho (int): ancho de la pantalla.       
#         largo (int): largo de la pantalla.
#         titulo_juego (str): titulo del juego, en este caso, "Buscaminas".
#         ruta_icono (str):imagen del icono de la ventanita.
    
#     Retorna:
#         pygame.Surface: superficie de la pantalla.
    
#     """
#     pantalla = pygame.display.set_mode((ancho, largo))
#     pygame.display.set_caption(titulo_juego)
#     icono_ventana = pygame.image.load(ruta_icono)
#     pygame.display.set_icon(icono_ventana)

#     return pantalla

# #Pantalla inicio
# def dibujar_boton(pantalla:pygame.Surface, x:int, y:int, ancho:int, alto:int, texto:str, color_boton:int, color_texto_boton:str) -> None:
#     """
#     Esta función permite dibujar un boton.
    
#     Recibe:
#         pantalla (pygame.Surface): pantalla en al cual se quiere dibujar el boton.
#         x (int): coordenada horizontal en donde se va a ubicar el boton.
#         y (int): coordenada vertical en donde se va a ubicar el boton.
#         ancho (int): ancho del boton.
#         alto (int): alto del boton.
#         texto (str): texto que va estar adentro de ese boton.
#         color_boton (int): color del boton que se va a dibujar.
#         color_texto_boton (str): color del texto que está adentro del boton.

#     """
#     pygame.draw.rect(pantalla, color_boton, (x, y, ancho, alto)) #fijate #, width=5, border_radius=10

#     fuente_letras = pygame.font.SysFont("Arial", 80)
#     texto = fuente_letras.render(texto, True, color_texto_boton)

#     texto_rectangulo = texto.get_rect(center=(x + ancho // 2, y + alto // 2))

#     pantalla.blit(texto, texto_rectangulo)

# def mostrar_pantalla_inicio(pantalla:pygame.Surface, ruta_imagen:str) -> None:
#     """
#     Esta función permite mostrar la pantalla de incio, incluidos sus botones.
    
#     Recibe:
#         pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
#         ruta_imagen (str): imagen de fondo de la pantalla de inicio.
    
#     """
#     imagen_inicio = pygame.image.load(ruta_imagen)
#     imagen_inicio  = pygame.transform.scale(imagen_inicio, pantalla.get_size())
#     pantalla.blit(imagen_inicio, (0,0))

#     ancho_boton = 500
#     alto_boton = 120
#     espacio_entre_botones = 50
#     posicion_horizontal_boton = 918
#     posicion_vertical_boton = 95

#     dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton, ancho_boton, alto_boton, "Jugar", (169, 156, 140), (156, 106, 69))
#     dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton + 1*(alto_boton + espacio_entre_botones), ancho_boton, alto_boton, "Dificultad",(169, 156, 140), (156, 106, 69))
#     dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton + 2*(alto_boton + espacio_entre_botones), ancho_boton, alto_boton, "Puntajes", (169, 156, 140), (156, 106, 69))
#     dibujar_boton(pantalla, posicion_horizontal_boton, posicion_vertical_boton + 3*(alto_boton + espacio_entre_botones), ancho_boton, alto_boton, "Salir", (169, 156, 140), (156, 106, 69))

# def obtener_accion_pantalla_inicio(x:int, y:int) -> str:
#     """
#     Esta función permite obtener la acción del click del mouse en la pantalla de inicio.

#     Recibe:
#         x (int): coordenada horizontal en donde se hizo click.
#         y (int): coordenada vertical en donde se hizo click.

#     Retorna:
#         str: acción a realizar según click del mouse.
#     """
#     accion = None
#     ancho_del_boton = 500
#     alto_del_boton = 120
#     espacios_entre_los_botones = 50
#     posicion_horizontal_boton = 918 #x
#     posicion_vertical_incial_boton = 95 #y

#     if posicion_horizontal_boton <= x <= posicion_horizontal_boton + ancho_del_boton:
#         if posicion_vertical_incial_boton <= y <=  posicion_vertical_incial_boton + alto_del_boton:
#             accion = "Jugar"
#         elif posicion_vertical_incial_boton + alto_del_boton + espacios_entre_los_botones <= y <= posicion_vertical_incial_boton + 2*(alto_del_boton + espacios_entre_los_botones):
#             accion = "Dificultad"
#         elif posicion_vertical_incial_boton + 2*(alto_del_boton + espacios_entre_los_botones) <= y <= posicion_vertical_incial_boton + 3 *(alto_del_boton + espacios_entre_los_botones):
#             accion = "Puntajes"
#         elif posicion_vertical_incial_boton + 3 * (alto_del_boton + espacios_entre_los_botones) <= y <= posicion_vertical_incial_boton + 4 *(alto_del_boton + espacios_entre_los_botones):
#             accion = "Salir"
#     return accion

# #Pantallas Seleccion niveles
# def mostrar_pantalla_de_niveles(pantalla:pygame.Surface, ruta_imagen:str) -> None:
#     """
#     Esta función permite mostrar la pantalla de seleccion de los niveles, incluidos sus botones.
    
#     Recibe:
#         pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
#         ruta_imagen (str): imagen de fondo de la pantalla de seleccion de niveles.

#     """
#     imagen_seleccion_de_niveles = pygame.image.load(ruta_imagen)
#     imagen_seleccion_de_niveles = pygame.transform.scale(imagen_seleccion_de_niveles, pantalla.get_size())
#     pantalla.blit(imagen_seleccion_de_niveles, (0,0))

#     ancho_botones_niveles = 400
#     alto_botones_niveles = 150

#     ancho_boton_volver = 200
#     alto_boton_volver = 100

#     posicion_horizontal_boton_facil = 400 #x
#     posicion_vertical_boton_facil = 250 #y

#     posicion_horizontal_boton_medio = 950
#     posicion_vertical_boton_medio = 250

#     posicion_horizontal_boton_dificil = 650
#     posicion_vertical_boton_dificil = 450

#     posicion_horizontal_boton_volver = 1200
#     posicion_vertical_boton_volver = 675

#     dibujar_boton(pantalla, posicion_horizontal_boton_facil, posicion_vertical_boton_facil, ancho_botones_niveles, alto_botones_niveles, "Facil", (55,41,22), (156,106,69))
#     dibujar_boton(pantalla, posicion_horizontal_boton_medio, posicion_vertical_boton_medio,ancho_botones_niveles, alto_botones_niveles, "Medio", (55,41,22), (156,106,69))
#     dibujar_boton(pantalla, posicion_horizontal_boton_dificil, posicion_vertical_boton_dificil, ancho_botones_niveles, alto_botones_niveles, "Dificil",(55,41,22), (156,106,69))
#     dibujar_boton(pantalla, posicion_horizontal_boton_volver, posicion_vertical_boton_volver, ancho_boton_volver, alto_boton_volver, "Volver",(55,41,22), (156,106,69))

# def crear_fondos_de_textos(pantalla:pygame.Surface, timer:int, fuente_timer:pygame.font.Font, color_timer:tuple, banderas_colocadas:int, minas:int) -> None:
#     """
#     Esta función permite crear los fondos para los textos de la pantalla de juego.
    
#     Recibe:
#         pantalla (pygame.Surface): pantalla en la cual se dibujan los fondos.
#         timer (int): timer que se pone arriba del fondo.
#         fuente_timer (pygame.font.Font): fuente del timer.
#         color_timer (tuple): color del texto del timer.
#         banderas_colocadas (int): texto de banderas.
#         minas (int): minas colocadas. ????

#     """
    
#     x_rectangulo_timer = 920
#     y_rectangulo_timer = 80
#     ancho_rectangulo_timer = 500
#     alto_retangulo_timer = 100

#     x_rectangulo_banderas = 920
#     y_rectangulo_banderas = 250
#     ancho_rectangulo_banderas = 500
#     alto_retangulo_banderas = 100

#     rectangulo_timer = pygame.Rect(x_rectangulo_timer,y_rectangulo_timer,ancho_rectangulo_timer,alto_retangulo_timer)
#     pygame.draw.rect(pantalla,(0,0,0),rectangulo_timer)

#     rectangulo_banderas = pygame.Rect(x_rectangulo_banderas,y_rectangulo_banderas,ancho_rectangulo_banderas,alto_retangulo_banderas)
#     pygame.draw.rect(pantalla,(0,0,0),rectangulo_banderas)

#     texto_timer = crear_texto_timer(timer, fuente_timer, color_timer)
#     rectangulo_para_texto_timer = texto_timer.get_rect()
#     rectangulo_para_texto_timer.center = rectangulo_timer.center
#     pantalla.blit(texto_timer, rectangulo_para_texto_timer)

#     fuente_banderas = pygame.font.SysFont("Arial", 50)
#     texto_banderas = fuente_banderas.render(f"Banderas: {banderas_colocadas}/{minas}", True, (255,0,0))
#     rectangulo_para_texto_banderas = texto_banderas.get_rect()
#     rectangulo_para_texto_banderas.center = rectangulo_banderas.center
#     pantalla.blit(texto_banderas, rectangulo_para_texto_banderas)

# def obtener_accion_pantalla_niveles(x:int, y:int) -> str:
#     """
#     Esta función permite obtener la acción del click del mouse en la pantalla de seleccion de niveles.
    
#     Recibe:
#         x (int): coordenada horizontal en donde se hizo click.
#         y (int): coordenada vertical en donde se hizo click.
    
#     Retorna:
#         str: acción a realizar según click del mouse.
    
#     """
#     accion = None
    
#     ancho_botones_niveles = 400
#     alto_botones_niveles = 150

#     ancho_boton_volver = 200
#     alto_boton_volver = 100

#     posicion_horizontal_boton_facil = 400 #x
#     posicion_vertical_boton_facil = 250 #y

#     posicion_horizontal_boton_medio = 950
#     posicion_vertical_boton_medio = 250

#     posicion_horizontal_boton_dificil = 650
#     posicion_vertical_boton_dificil = 450

#     posicion_horizontal_boton_volver = 1200
#     posicion_vertical_boton_volver = 675

#     if posicion_horizontal_boton_facil <= x <= posicion_horizontal_boton_facil + ancho_botones_niveles and posicion_vertical_boton_facil <= y <= posicion_vertical_boton_facil + alto_botones_niveles:
#         accion = "Facil"

#     elif posicion_horizontal_boton_medio <= x <= posicion_horizontal_boton_medio + ancho_botones_niveles and posicion_vertical_boton_medio <= y <= posicion_vertical_boton_medio + alto_botones_niveles:
#         accion = "Medio"

#     elif posicion_horizontal_boton_dificil <= x <= posicion_horizontal_boton_dificil + ancho_botones_niveles and posicion_vertical_boton_dificil <= y <= posicion_vertical_boton_dificil + alto_botones_niveles:
#         accion = "Dificil"
    
#     elif posicion_horizontal_boton_volver <= x <= posicion_horizontal_boton_volver + ancho_boton_volver and posicion_vertical_boton_volver <= y <= posicion_vertical_boton_volver + alto_boton_volver:
#         accion = "Volver"
    
#     return accion

# #Pantalla nivel elegido
# def cargar_fondo_segun_nivel_elegido(pantalla:pygame.Surface, nivel:str) -> pygame.Surface: #?
#     """
#     Esta función permite cargar el fondo de pantalla segun el nivel que se elige.
    
#     Recibe:
#         pantalla (pygame.Surface): superficie en donde va a estar la pantalla
#         nivel (str): nivel elegido.
    
#     Retorna:
#         pygame.Surface: superficie de la pantalla.
    
#     """

#     posicion_horizontal_boton_volver = 920
#     posicion_vertical_boton_volver = 650

#     ancho_boton_volver = 500
#     alto_boton_volver = 100

#     posicion_horizontal_boton_reinicio = 920
#     posicion_vertical_boton_reinicio = 500
    
#     ancho_boton_reiniciar = 500
#     alto_boton_reiniciar = 100

#     if nivel == "Facil":
#         imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Nivel_facil.png")
#         color_texto = (255,255,255)
#         color_fondo_boton = (0,0,0)
#     elif nivel == "Medio":
#         imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Nievel_medio.png")
#         color_texto = (255,255,255)
#         color_fondo_boton = (0,0,0)
#         #pygame.display.update()
#     elif nivel == "Dificil":
#         imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Nivel_dificil.png") 
#         color_texto = (255,255,255)
#         color_fondo_boton = (0,0,0)
#         #pygame.display.update()
    
#     imagen_fondo = pygame.transform.scale(imagen_fondo, pantalla.get_size())
#     pantalla.blit(imagen_fondo, (0,0))

#     dibujar_boton(pantalla, posicion_horizontal_boton_volver, posicion_vertical_boton_volver, ancho_boton_volver, alto_boton_volver, "Volver",color_fondo_boton, color_texto)
#     dibujar_boton(pantalla, posicion_horizontal_boton_reinicio, posicion_vertical_boton_reinicio, ancho_boton_reiniciar, alto_boton_reiniciar, "Reiniciar",color_fondo_boton, color_texto)
        
#     return imagen_fondo
        

# def obtener_accion_buscaminas(x:int, y:int) -> str:
#     """
#     Esta función permite obtener la acción del click del mouse en la pantalla de juego.
    
#     Recibe:
#         x (int): coordenada horizontal en donde se hizo click.
#         y (int): coordenada vertical en donde se hizo click.
    
#     Retorna:
#         str: acción a realizar según click del mouse.
    
#     """
#     accion = None

#     posicion_horizontal_boton_volver = 920
#     posicion_vertical_boton_volver = 650

#     ancho_boton_volver = 500
#     alto_boton_volver = 100

#     posicion_horizontal_boton_reinicio = 920
#     posicion_vertical_boton_reinicio = 500
    
#     ancho_boton_reiniciar = 500
#     alto_boton_reiniciar = 100

#     if posicion_horizontal_boton_volver <= x <= posicion_horizontal_boton_volver + ancho_boton_volver and posicion_vertical_boton_volver <= y <= posicion_vertical_boton_volver + alto_boton_volver:
#         accion = "Volver"
#     elif posicion_horizontal_boton_reinicio <= x <= posicion_horizontal_boton_reinicio + ancho_boton_reiniciar and posicion_vertical_boton_reinicio <= y <= posicion_vertical_boton_reinicio + alto_boton_reiniciar:
#         accion = "Reiniciar"
    
#     return accion


# #Busaminas
# def localizar_posicion_click(evento:str, filas:int, columnas:int, tamanio_celda:int, inicio_tablero_x:int, inicio_tablero_y:int) -> int:
#     """
#     Esta función permite localizar el click en el tablero..
    
#     Recibe:
#         evento (_type_): evento a localizar.
#         filas (_type_): fila.
#         columnas (_type_): columna.
#         tamanio_celda (_type_): tamaño de la celda.
#         inicio_tablero_x (_type_): incio de la coordenada x del tablero.
#         inicio_tablero_y (_type_): inicio de la coordena y del tablero.
    
#     Retorna:
#         int: posicion fila y columna.
    
#     """
#     # Recorremos todos los eventos que ocurrieron en esta iteración del juego
#     fila_columna = None
    
#     # Verificamos si el evento fue un clic del mouse
#     if evento.type == pygame.MOUSEBUTTONDOWN:

#         # Verificamos si el botón del mouse presionado fue el izquierdo (1) o el derecho (3)
#         if evento.button == 1 or evento.button == 3:

#             # Obtenemos la posición absoluta del mouse en la ventana
#             x, y = evento.pos

#             # Calculamos la posición relativa del clic respecto al tablero
#             # Esto resta el "margen" que hay desde el borde de la ventana hasta donde empieza el tablero
#             x_relativo = x - inicio_tablero_x
#             y_relativo = y - inicio_tablero_y

#             # Calculamos en qué fila y columna de la matriz se encuentra el clic
#             # Dividimos la posición relativa por el tamaño de cada celda
#             fila = y_relativo // tamanio_celda
#             columna = x_relativo // tamanio_celda

#                 # Verificamos si el clic fue dentro de los límites del tablero
#             if fila >= 0 and fila < filas and columna >= 0 and columna < columnas:
                
#                 # fila_columna = fila, columna
                
#                 if evento.button == 1:
#                     # Si está dentro del tablero, devolvemos la posición clickeada (fila y columna)
#                     print(f"Clic en la celda [{fila}, {columna}]")

#                 elif evento.button == 3:
#                     print(f"Clic en la celda [{fila}, {columna}] BANDERA")

#                 fila_columna = fila, columna

#             else:
#                 print("Click fuera del tablero")
                
#     # Si no hubo clic válido, devolvemos None (no se seleccionó ninguna celda)
#     return fila_columna


# def crear_texto_timer(timer:int, fuente, color:tuple):
#     # timer: entero que representa la cantidad de segundos que querés mostrar en el texto.
#     # Ejemplo: 30 (segundos), 90 (un minuto y medio), etc.
#     #La fuente que debe recibir es algo asi -> fuente = pygame.font.SysFont("Arial", 24) -> "Ariel"(tipo de letra), 24(tamaño de la letra) 
#     #Lo guardo en una variable fuente y esa misma es la que tiene que recibir el parametro fuente de esta funcion
#     return fuente.render(f"Tiempo: {timer} segundos", True, color)

# def dibujar_buscaminas(pantalla, filas, columnas, color_lineas, color_fondo, tamanio_celda, matriz_visible, ruta_imagen_bandera,ruta_imagen_mina, origen_x = 50, origen_y=40):
#     fuente = pygame.font.SysFont("Arial", tamanio_celda //2)

#     for fila in range(filas):
#         for columna in range(columnas):
#             x = origen_x + columna * tamanio_celda
#             y = origen_y + fila * tamanio_celda
#             rectangulo = pygame.Rect(x,y, tamanio_celda, tamanio_celda)
            
#             #pygame.draw.rect(pantalla, color_fondo, rectangulo)

#             valor_matriz = matriz_visible[fila][columna]
#             if valor_matriz == " ":
#                 color_celda = color_fondo
#             else:
#                 color_celda = (199,191,184)
#             pygame.draw.rect(pantalla, color_celda, rectangulo)

#             if valor_matriz == "F":
#                 pantalla.blit(ruta_imagen_bandera, (x,y))
#             elif valor_matriz == "X":
#                 pantalla.blit(ruta_imagen_mina, (x,y))
#             elif valor_matriz != " " and valor_matriz != 0:
#                 if valor_matriz == 1:
#                     color = (0,128,0)
#                 elif valor_matriz == 2:
#                     color = (0,0,255)
#                 elif valor_matriz == 3:
#                     color = (255,128,0)
#                 elif valor_matriz == 4:
#                     color = (255,0,0)
#                 else:
#                     color = (0,0,0)
#                 # color = (255,0,0) if valor_matriz == "X" else (0,0,0)
#                 texto = fuente.render(str(valor_matriz), True, color)
#                 pantalla.blit(texto, (x + tamanio_celda // 3, y +  tamanio_celda // 4))
    
    
#     for fila in range(filas + 1):
#         pygame.draw.line(pantalla, color_lineas, (origen_x, origen_y + fila * tamanio_celda), (origen_x + columnas * tamanio_celda, origen_y + fila * tamanio_celda), 1)

#     for columna in range(columnas + 1):
#         pygame.draw.line(pantalla, color_lineas, (origen_x + columna * tamanio_celda, origen_y), (origen_x + columna * tamanio_celda, origen_y + filas * tamanio_celda),1)
    
# def revelar_celdas(oculta, visible,f,c):
    
#     es_valido = True

#     if f < 0 or f >= len(oculta) or c < 0 or c >= len(oculta[0]):
#         es_valido = False
#     elif visible[f][c] != " ":
#         es_valido = False
    
#     if es_valido == True:
#         visible[f][c] = oculta[f][c]
#         if oculta[f][c] == 0:
#             for df in range(-1, 2):  # -1, 0, 1
#                 for dc in range(-1, 2): #Como seria su funcionamiento ????? averiguar
#                     if df != 0 or dc != 0:
#                         nueva_f = f + df
#                         nueva_c = c + dc
#                         revelar_celdas(oculta, visible, nueva_f, nueva_c)

#     # if f < 0 or f >= len(oculta) or c < 0 or c >= len(oculta[0]):
#     #     es_valido = False
#     # elif visible[f][c] != " ":
#     #     es_valido = False
    
#     # if es_valido:
#     #     visible[f][c] = oculta[f][c]
#     #     if oculta[f][c] == 0:
#     #         for df in [-1, 0,1]:
#     #             for dc in [-1,0,1]:
#     #                 if df != 0 or dc != 0:
#     #                     nueva_f = f + df
#     #                     nueva_c = c + dc
#     #                     revelar_celdas(oculta, visible, nueva_f, nueva_c)

# def revelar_tablero_final(oculta, visible):
#     for f in range(len(oculta)):
#         for c in range(len(oculta[0])):
#             if visible[f][c] != "F":
#                 visible[f][c] = oculta[f][c]



# def inicializar_matriz(filas:int, columnas:int, caracter_a_rellenar:int)->list[list]:
#     """Documentacion:
#     creamos una matriz y la inicializamos con los 0 (ceros)"""
#     matriz = []

#     for _ in range(filas):
#         fila = []
#         for _ in range(columnas):
#             fila.append(caracter_a_rellenar)
#         matriz.append(fila)

#     return matriz #La retorno unicamente porque la estoy creando dentro de la funcion, de lo contrario no haria falta ya que es mutable


# def mostrar_matriz(matriz:list[list])->None:
#     """Documentacion: 
#     Solo imprimimos la matriz que recibimos por parametro"""
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             print(matriz[i][j], end=" ")
#         print()


# def generar_minas(tablero:list[list], cant_minas:int)->None:
#     """
#     Documentacion:
#     Recibimos una lista simulando el tablero, y la cantidad de minas a colocar
#     en lugares aleatorios 
#     """
#     numero = 0
#     while cant_minas > 0:
#         fila = random.randint(0, len(tablero) - 1) #Elegimos una fila al azar que va de 0 hasta el ultimo elemento, por eso el -1 para q no se pase
#         columna = random.randint(0, len(tablero[0]) - 1) #Hacemos lo mismo con columnas, elegimos al azar que va de 
#         # 0 hasta el ultimo elemento, por eso el -1 para q no se pase
#         if tablero[fila][columna] == 0: # Cuando en la fila y columna en la que estamos parado es igual a 0 le asigno un 1
#             tablero[fila][columna] = "X" # Asigno 1 a la posicion en la que haya estado parado
#             cant_minas -= 1 # Voy descontando las cantidades de minas al colocarlas

# def asignar_contadores(tablero:list[list], mina:str="X")->None:
#     """Documentacion:
#     recibimos la matriz que representa nuestro tablero, y como parametro opcional
#     le asignamos una mina como X para luego verificar donde se encuentran las X 
#     y poder contarlas"""
#     filas = len(tablero)
#     columnas = len(tablero[0])

#     for i in range(filas):
#         for j in range(columnas):
#             if tablero[i][j] == mina:
#                 continue
#             contador = 0
#             # Reviso manualmente las 8 posiciones posibles, con if para no salirme
#             # Arriba izquierda
#             if i > 0 and j > 0 and tablero[i-1][j-1] == mina:
#                 contador += 1
#             # Arriba
#             if i > 0 and tablero[i-1][j] == mina:
#                 contador += 1
#             # Arriba derecha
#             if i > 0 and j < columnas - 1 and tablero[i-1][j+1] == mina:
#                 contador += 1
#             # Izquierda
#             if j > 0 and tablero[i][j-1] == mina:
#                 contador += 1
#             # Derecha
#             if j < columnas - 1 and tablero[i][j+1] == mina:
#                 contador += 1
#             # Abajo izquierda
#             if i < filas - 1 and j > 0 and tablero[i+1][j-1] == mina:
#                 contador += 1
#             # Abajo
#             if i < filas - 1 and tablero[i+1][j] == mina:
#                 contador += 1
#             # Abajo derecha
#             if i < filas - 1 and j < columnas - 1 and tablero[i+1][j+1] == mina:
#                 contador += 1

#             if contador > 0:
#                 tablero[i][j] = contador

# # Código principal
# # matriz = inicializar_matriz(8, 8, 0)
# # generar_minas(matriz, 10)
# # asignar_contadores(matriz)
# # mostrar_matriz(matriz)

# #PANTALLA GANASTE O PERDISTE

# def verificar_ganador(matriz_oculta, matriz_visible):
#     ganador = True
#     for i in range(len(matriz_oculta)):
#         for j in range(len(matriz_oculta[0])):
#             if matriz_oculta[i][j] != "X" and matriz_visible[i][j] == " ":
#                 ganador = False
#     return ganador



# def pedir_nombre_usuario(pantalla: pygame.Surface, fuente: str, colo_caja_texto: tuple[int,int,int], color_texto:tuple[int,int,int], fondo):
#     nombre = ""
#     escribiendo = True

#     x_boton = 1000
#     y_boton = 500

#     ancho_boton_guardar = 300
#     alto_boton_guardar = 150
    
#     while escribiendo == True:
        
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#             # presionar tecla
#             elif evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_RETURN:
#                     if nombre.strip():
#                         escribiendo = False
#                 # si presiona enter, deja de escribir
#                 #simula borrar, letra por letra desde el iltimo caracter
#                 if evento.key == pygame.K_BACKSPACE:
#                     nombre = nombre[:-1]
#                 #nombre de menos de 12 caracteres
#                 elif len(nombre) < 20: #12?
#                         #convierte las teclas en str
#                     nombre += evento.unicode
            
#             elif evento.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 accion = obtener_accion_pantalla_fin_del_juego(x,y)
#                 if accion == "Guardar" and nombre.strip():
#                     escribiendo = False


#         pantalla.blit(fondo, (0,0))
#         # titulo, encima de caja de  texto
#         texto_titulo = fuente.render('Ingresá tu nombre:', True, (255, 255, 255))
#         pantalla.blit(texto_titulo, (950, 200))
        
#         #simula un cursor
#         #texto_nombre = fuente.render(nombre + '|', True, color_texto)#chusmear

#         #Caja de texto
#         caja_texto = pygame.Rect(810, 300, 700, 150)
#         pygame.draw.rect(pantalla, colo_caja_texto, caja_texto)

#         fuente_nombre = pygame.font.SysFont("Arial", 90)
#         texto_nombre = fuente_nombre.render(nombre, True, color_texto)
#         pantalla.blit(texto_nombre, (810, 300+10))

#         dibujar_boton(pantalla, x_boton, y_boton, ancho_boton_guardar, alto_boton_guardar, "Guardar",(200,200,200), (0,0,0))

#         pygame.display.flip()

#     return nombre.strip()

# def obtener_accion_pantalla_fin_del_juego(x:int, y:int) -> str:
#     accion = None

#     x_boton = 1000
#     y_boton = 500

#     ancho_boton_guardar = 300
#     alto_boton_guardar = 150

#     if x_boton <= x <= x_boton + ancho_boton_guardar and y_boton <= y <= y_boton + alto_boton_guardar:
#         accion = "Guardar"
#     return accion

# def calcular_puntaje(dificultad, tiempo, banderas_colocadas, minas, maximo_puntaje_tiempo:int=200):
#     """
#     Calcula el puntaje final del jugador sin usar max().

#     Parámetros:
#     - dificultad (str): "Facil", "Medio" o "Dificil"
#     - tiempo (int): tiempo en segundos que tardó en ganar
#     - filas, columnas (int): tamaño del tablero
#     - banderas_colocadas (int): cantidad de banderas colocadas por el jugador
#     - minas (int): cantidad total de minas en el tablero

#     Retorna:
#     - int: puntaje calculado
#     """
#     base_dificultad = {"Facil": 100, "Medio": 250, "Dificil": 500}
#     base = base_dificultad.get(dificultad, 0) #No se le ve mucho sentido al segundo parametro en este casooo.. 

#     # Calcular eficiencia banderas (entre 0 y 1)
#     proporcion_banderas = banderas_colocadas
#     if minas > 0:
#         proporcion_banderas = banderas_colocadas / minas
#     else:
#         proporcion_banderas = 0
    
#     # Evitamos valores negativos y limitamos las banderas
#     if proporcion_banderas < 0:
#         proporcion_banderas = 0
#     elif proporcion_banderas > 1:
#         proporcion_banderas = 1
    
#     eficiencia_banderas = proporcion_banderas * 50

#     # Puntaje tiempo: 200 - tiempo, no negativo
#     puntaje_tiempo = maximo_puntaje_tiempo - tiempo
#     if puntaje_tiempo < 0:
#         puntaje_tiempo = 0

#     puntaje = base + eficiencia_banderas + puntaje_tiempo

#     # No devolver puntaje negativo
#     if puntaje < 0:
#         puntaje = 0
    
#     resultado = int(puntaje) #casteo a entero

#     return resultado

# def guardar_puntaje(nombre, puntaje, ruta="BUSCAMINAS_PYGAME/puntajes.csv"):
#     # with open(ruta, mode='a', newline='') as archivo:
#     #     escritor = csv.writer(archivo)
#     #     escritor.writerow([nombre, tiempo])
#     nombre = nombre.strip()
#     nombres_registrados = {}
#     try: #lee datos que existen
#         with open(ruta, "r", newline="") as f:
#             for fila in csv.reader(f):
#                 if len(fila) == 2 and fila[1].isdigit():
#                     nombres_registrados[fila[0]] = int(fila[1])
#     except FileNotFoundError:
#         pass
#     # if nombre in nombres_registrados:
#     #     if puntaje > nombres_registrados[nombre]:
#     #         nombres_registrados[nombre] = puntaje
#     #     else:
#     #         nombres_registrados[nombre] = puntaje

#     if nombre:
#         if(nombre not in nombres_registrados) or (puntaje >nombres_registrados[nombre]):
#             nombres_registrados[nombre]= puntaje

#     filas_ordenadas = sorted(nombres_registrados.items(),key=lambda par: par[1], reverse=True)
#     # nombres_registrados = sorted(nombres_registrados.items(),key=lambda par:par[1],reverse=True)

#     with open(ruta, "w", newline="") as f:
#         # escribir = csv.writer(f).writerows([nombres_registrados])
#         escribir =csv.writer(f)
#         for fila in filas_ordenadas:
#             escribir.writerow(fila)
        

# def leer_puntajes(ruta:str='puntajes.csv'):
    
#     mejores_10_puntajes = []
#     with open(ruta, "r", newline="") as f:
#             for fila in csv.reader(f):
#                 if len(fila) == 2 and fila[1].isdigit():
#                     mejores_10_puntajes.append((fila[0], int(fila[1])))
    
#     mejores_10_puntajes.sort(key=lambda par: par[1], reverse=True )
    
#     return mejores_10_puntajes[:10]
        
#             # lector = csv.reader(archivo)
#             # print('\n------- Lista jugadores -------')
#             # for fila in lector:
#             #     if len(fila) == 2:
#             #         nombre, tiempo = fila
#             #         print(f'Nombre: {nombre} | Tiempo: {tiempo} segundos')

# def mostrar_pantalla_fin_del_juego(pantalla, fuente, ganador, puntaje):
#     if ganador == True:
#         imagen_fondo= pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Pantalla_ganaste.png")
#     else: 
#         imagen_fondo = pygame.image.load("BUSCAMINAS_PYGAME/Imagenes/Pantalla_perdiste.png")

#     imagen_fondo = pygame.transform.scale(imagen_fondo, pantalla.get_size())
#     pantalla.blit(imagen_fondo, (0,0))

#     texto_puntaje  = fuente.render(f"Tu punataje es: {puntaje}", True, (0,0,0))
#     pantalla.blit(texto_puntaje, (900, 150))

#     #?
#     pygame.display.update()

#     nombre_usuario = pedir_nombre_usuario(pantalla, fuente, (255,255,255), (0,0,0), imagen_fondo)
    
#     guardar_puntaje(nombre_usuario, puntaje)


# #Pantalla puntajes
# def mostrar_pantalla_de_puntajes(pantalla:pygame.Surface, ruta_imagen:str, ruta_puntajes, fuente:None, columna_x_nombre, columna_x_puntaje,y_primera_fila, espaciado) -> None:
#     """
#     Esta función permite mostrar la pantalla de puntajes, incluidos sus botones.
    
#     Recibe:
#         pantalla (pygame.Surface): superficie en donde va a estar la pantalla.
#         ruta_imagen (str): imagen de fondo de la pantalla de puntajes.
    
#     """    
#     imagen_puntajes = pygame.image.load(ruta_imagen)
#     imagen_puntajes = pygame.transform.scale(imagen_puntajes, pantalla.get_size())
#     pantalla.blit(imagen_puntajes, (0,0))

#     ancho_boton_volver = 200
#     alto_boton_volver = 100

#     posicion_horizontal_boton_volver = 1200
#     posicion_vertical_boton_volver = 675

#     dibujar_boton(pantalla, posicion_horizontal_boton_volver, posicion_vertical_boton_volver, ancho_boton_volver, alto_boton_volver, "Volver",(55,41,22), (156,106,69))

#     if fuente is None:
#         fuente = pygame.font.SysFont("Arial", 30)
    
#     # titulo = fuente.render("TOP 10 PUNTAJES", True, (0, 0, 0))
#     # pantalla.blit(titulo, (columna_x_nombre, y_primera_fila - 80))

#     # --- leer CSV -------------------------------------------------------------
#     with open(ruta_puntajes, newline="") as f:
#         filas = [fila for fila in csv.reader(f) if len(fila) == 2 and fila[0].strip()]

#     # asegurate de mostrarlos ordenados
#     filas.sort(key=lambda par: int(par[1]), reverse=True)
#     filas = filas[:10]

#     # --- dibujar cada fila ----------------------------------------------------
#     y = y_primera_fila
#     for nombre, puntaje in filas:
#         # ancho en píxeles de lo que ya tenemos
#         ancho_nombre   = fuente.size(nombre)[0]
#         ancho_puntaje  = fuente.size(puntaje)[0]
#         ancho_punto    = fuente.size(".")[0]

#         # espacio disponible para puntos
#         espacio_px = columna_x_puntaje - (columna_x_nombre + ancho_nombre) - ancho_puntaje
#         puntos = "." * max(2, espacio_px // ancho_punto)

#         linea = f"{nombre}{puntos}{puntaje}"
#         superficie = fuente.render(linea, True, (0, 0, 0))
#         pantalla.blit(superficie, (columna_x_nombre, y))
#         y += espaciado

#     pygame.display.flip()
#     # y = 50 #posicion para iniciar vertical
#     # with open(ruta_puntajes, mode="r") as archivo:
#     #     lector = csv.reader(archivo)
#     #     titulo = fuente.render("Tabla de Puntajes", True, (255,255,255))
#     #     pantalla.blit(titulo, (columna_x_nombre, y_primera_fila - 80))


        
#     #     for fila in lector:
#     #         if len(fila) == 2:
#     #             nombre = fila[0]
#     #             tiempo = fila[1]
#     #             caracteres_maximos  = 20
#     #             puntitos = " . " * (caracteres_maximos - len(nombre))
#     #             mostrar_texto = f"{nombre} {puntitos} {tiempo} segundos"
#     #             texto = fuente.render(mostrar_texto, True, (255,255,255))
#     #             pantalla.blit(texto, (50,y))
#     #             y+= 40
#     # pygame.display.flip()



# def obtener_accion_pantalla_puntajes(x:int, y:int) -> str:
#     """
#     Esta función permite obtener la acción del click del mouse en la pantalla de puntajes.
    
#     Recibe:
#         x (int): coordenada horizontal en donde se hizo click.
#         y (int): coordenada vertical en donde se hizo click.
    
#     Retorna:
#         str: acción a realizar según click del mouse.
    
#     """
#     accion = None

#     ancho_boton_volver = 200
#     alto_boton_volver = 100

#     posicion_horizontal_boton_volver = 1200
#     posicion_vertical_boton_volver = 675

#     if posicion_horizontal_boton_volver <= x <= posicion_horizontal_boton_volver + ancho_boton_volver and posicion_vertical_boton_volver <= y <= posicion_vertical_boton_volver + alto_boton_volver:
#         accion = "Volver"
    
#     return accion



