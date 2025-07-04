import pygame
from biblioteca_funciones import *
from configuraciones import *

pygame.init()
pygame.mixer.init()

pantalla = inicializar_caracteristicas_pantalla(ANCHO_PANTALLA, ALTO_PANTALLA, NOMBRE_JUEGO, RUTA_ICONO_VENTANITA)

pygame.mixer.music.load(RUTA_MUSICA_JUEGO)
pygame.mixer.music.set_volume(0.5)
sonido_victoria = pygame.mixer.Sound(RUTA_MUSICA_VICTORIA)
sonido_derrota = pygame.mixer.Sound(RUTA_MUSICA_DERROTA)
icono_musica_on = pygame.image.load(RUTA_ICONO_MUSICA_ON).convert_alpha()
icono_musica_off = pygame.image.load(RUTA_ICONO_MUSICA_OFF).convert_alpha()


evento_segundo = pygame.USEREVENT + 1
pygame.time.set_timer(evento_segundo, 1000)
fuente_timer = pygame.font.SysFont(FUENTE_DEL_TIMER, TAMANIO_FUENTE_TIMER)



while corriendo_juego:
    eventos = pygame.event.get()
    
    max_ancho_tablero = ANCHO_PANTALLA * 0.9  # que el tablero use hasta 60% ancho pantalla
    max_alto_tablero = ALTO_PANTALLA * 0.9   # y hasta 70% alto pantalla

    for evento in eventos:
        if evento.type == pygame.QUIT:
            corriendo_juego = False

        elif evento.type == evento_segundo:
            if (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and tiempo_inicializado == True and perdi == False and gane == False:
                        segundos += 1
                        if segundos == 60:
                            minutos += 1
                            segundos = 0
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            if pantalla_actual == "Inicio":
                if click_icono_sonido != None and click_icono_sonido.collidepoint(pos) == True:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        musica_activa = False
                    else:
                        pygame.mixer.music.unpause()
                        musica_activa = True
                    continue
                accion = obtener_accion_pantalla_inicio(pantalla, x, y)
                if accion == "Jugar":
                    # pygame.mixer.music.stop()
                    pantalla_actual = "Seleccion niveles"
                elif accion == "Puntajes":
                    # pygame.mixer.music.stop()
                    pantalla_actual = "Puntajes"
                elif accion == "Salir":
                    corriendo_juego = False
                elif accion == "Resolución":
                    cantidad_resoluciones = len(resoluciones)
                    indice_resolucion_actual += 1
                    if indice_resolucion_actual >= cantidad_resoluciones:
                        indice_resolucion_actual = 0
                    nueva_resolucion = resoluciones[indice_resolucion_actual] 
                    ANCHO_PANTALLA = nueva_resolucion[0]
                    ALTO_PANTALLA = nueva_resolucion[1]
                    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

            elif pantalla_actual == "Seleccion niveles":
                accion = obtener_accion_pantalla_niveles(pantalla, x, y)
                if accion == "Facil" or accion == "Medio" or accion == "Dificil":
                    pantalla_actual = accion
                    dificultad_actual = accion
                    matriz_oculta = None
                    minutos = 0
                    segundos = 0
                    mina_explota = None
                    primer_click_realizado = False
                    banderas_colocadas = 0
                    tiempo_inicializado = False
                    perdi = False
                    gane = False
                    
                    if accion == "Facil":
                        filas = 8
                        columnas = 8
                        minas = 10
                        tamanio_celda = 90
                
                    elif accion == "Medio":
                        filas = 16
                        columnas = 16
                        minas = 50
                        tamanio_celda = 45

                    elif accion == "Dificil":
                        filas = 24
                        columnas = 24
                        minas = 120
                        tamanio_celda = 30
                
                    tamanio_celda_ancho = int(max_ancho_tablero / columnas)
                    tamanio_celda_alto = int(max_alto_tablero / filas)
                    
                    if tamanio_celda_ancho < tamanio_celda_alto:
                        tamanio_celda = tamanio_celda_ancho
                    else:
                        tamanio_celda = tamanio_celda_alto
                
                    matriz_oculta = inicializar_matriz(filas, columnas, 0)
                    matriz_visible = inicializar_matriz(filas, columnas, " ")
                    bandera_buscaminas = insertar_iconos_al_buscaminas(RUTA_IMAGEN_BANDERA, tamanio_celda, tamanio_celda)
                    mina_buscaminas = insertar_iconos_al_buscaminas(RUTA_IMAGEN_MINA, tamanio_celda,tamanio_celda )
                
                elif accion == "Volver":
                    pantalla_actual = "Inicio"

            elif (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and matriz_oculta != None:
                accion_buscaminas = obtener_accion_buscaminas(pantalla, x, y)
                
                if accion_buscaminas == "Volver":
                    pantalla_actual = "Inicio"
                elif accion_buscaminas == "Reiniciar":
                    primer_click_realizado = False
                    banderas_colocadas = 0
                    minutos = 0
                    segundos = 0
                    tiempo_inicializado = False
                    mina_explota = None
                    perdi = False
                    gane = False
                    matriz_oculta = inicializar_matriz(filas, columnas, 0)
                    matriz_visible = inicializar_matriz(filas, columnas, " ")
                    pantalla_actual = dificultad_actual
                    
                else:
                    posicion = localizar_posicion_click(evento, filas, columnas, tamanio_celda, 50, 40)
                
                    if posicion != None:
                        pos = posicion
                        fila = pos[0]
                        col = pos[1]

                        if primer_click_realizado == False:
                            if primer_click_realizado == False:
                                matriz_oculta = preparar_tablero_primer_click(matriz_oculta, fila, col, filas, columnas, minas)
                                primer_click_realizado = True
                                tiempo_inicializado = True

                        
                        if evento.button == 1 and matriz_visible[fila][col] != "F":
                                if matriz_oculta [fila][col] == "X":
                                    mina_explota = (fila, col)
                                    revelar_tablero_final(matriz_oculta, matriz_visible)
                                    sonido_derrota.play()
                                    perdi = True
                                    tiempo_transicion = pygame.time.get_ticks()

                                else:
                                    revelar_celdas(matriz_oculta,matriz_visible, fila, col)
                                    if verificar_ganador(matriz_oculta, matriz_visible):
                                        revelar_tablero_final(matriz_oculta,matriz_visible)
                                        sonido_victoria.play()
                                        gane = True
                                        tiempo_transicion = pygame.time.get_ticks()
                        
                        elif evento.button == 3:
                            if matriz_visible[fila][col] == " " and banderas_colocadas < minas:
                                matriz_visible[fila][col]= "F"
                                banderas_colocadas += 1
                            elif matriz_visible[fila][col] == "F":
                                matriz_visible[fila][col] = " "
                                banderas_colocadas -= 1

            elif pantalla_actual == "Puntajes":
                accion = obtener_accion_pantalla_puntajes(pantalla, x, y)
                if accion == "Volver":
                    pantalla_actual = "Inicio"

    # Mostrar pantallas y lógica
    if pantalla_actual == "Inicio":
        ancho = resoluciones[indice_resolucion_actual][0]
        alto = resoluciones[indice_resolucion_actual][1]
        # mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO, ancho, alto)
        if musica_activa == True and pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play(-1)
        click_icono_sonido = mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO, ANCHO_PANTALLA, ALTO_PANTALLA, icono_musica_on, icono_musica_off, musica_activa)
        if pantalla_actual != "Inicio":
            pygame.mixer.music.stop()
    
    elif pantalla_actual == "Seleccion niveles":
        mostrar_pantalla_de_niveles(pantalla, RUTA_IMAGEN_SELECCION_DE_NIVELES)

    elif pantalla_actual == "Puntajes":
        fuente_puntitos = pygame.font.SysFont(FUENTE_PUNTITOS_PUNTAJES, TAMANIO_FUENTE_PUNTITOS)
        mostrar_pantalla_de_puntajes(pantalla, RUTA_IMAGEN_PUNTAJES, RUTA_ARCHIVO_PUNTAJES, fuente_puntitos) #fuente creada anteriormente 

    elif pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil":
        cargar_fondo_segun_nivel_elegido(pantalla, pantalla_actual)
        x, y = pygame.mouse.get_pos() #chusmea estooO!!!
        accion_buscaminas = obtener_accion_buscaminas(pantalla, x, y)
        dibujar_buscaminas(pantalla, filas, columnas, COLOR_LINEAS_BUSCAMINAS, COLOR_FONDO_BUSCAMINAS, tamanio_celda, matriz_visible, bandera_buscaminas, mina_buscaminas, mina_explota)
        crear_fondos_de_textos(pantalla, minutos, segundos, COLOR_DEL_TIMER, banderas_colocadas, minas)

    elif pantalla_actual == "Ingresar nombre" and fue_ganador == True:
        total_segundos = minutos * 60 + segundos
        puntaje = calcular_puntaje(dificultad_actual, total_segundos, banderas_colocadas, minas, fue_ganador)
        fuente_puntaje = pygame.font.SysFont(FUENTE_PUNTAJES, TAMANIO_FUENTE_PUNTAJES)
    
        imagen_fondo = pygame.image.load(RUTA_IMAGEN_GANASTE)

        imagen_fondo = pygame.transform.scale(imagen_fondo, pantalla.get_size())

        nombre_usuario = pedir_nombre_usuario(pantalla, COLO_CAJA_TEXTO_PEDIR_NOMBRE, COLOR_TEXTO_CAJA_PEDIR_NOMBRE, imagen_fondo)
        
        if nombre_usuario != "":
            guardar_puntaje(nombre_usuario, puntaje)
            pantalla_actual = "Puntajes"

    tiempo_actual = pygame.time.get_ticks()
    tiempo = tiempo_actual - tiempo_transicion
    if gane == True and tiempo >= TIEMPO_DE_TRANSICION:
        pantalla_actual ="Ingresar nombre"
        fue_ganador = True
        gane = False

    elif perdi == True and tiempo >= TIEMPO_DE_TRANSICION:
            fue_ganador = False

    actualizar_musica_juego(pantalla_actual, musica_activa)
    pygame.display.update()


pygame.quit()
quit()











# import pygame
# from biblioteca_funciones import *
# from configuraciones import *

# pygame.init()
# pygame.mixer.init()

# origen_x = int(ANCHO_PANTALLA * 0.05)  # 5% del ancho total
# origen_y = int(ALTO_PANTALLA * 0.05)   # 5% del alto total #0.10? #0.5?

# pantalla = inicializar_caracteristicas_pantalla(ANCHO_PANTALLA, ALTO_PANTALLA, NOMBRE_JUEGO, RUTA_ICONO_VENTANITA)

# pygame.mixer.music.load(RUTA_MUSICA_JUEGO)
# pygame.mixer.music.set_volume(0.5)
# sonido_victoria = pygame.mixer.Sound(RUTA_MUSICA_VICTORIA)
# sonido_derrota = pygame.mixer.Sound(RUTA_MUSICA_DERROTA)
# icono_musica_on = pygame.image.load(RUTA_ICONO_MUSICA_ON).convert_alpha()
# icono_musica_off = pygame.image.load(RUTA_ICONO_MUSICA_OFF).convert_alpha()


# evento_segundo = pygame.USEREVENT + 1
# pygame.time.set_timer(evento_segundo, 1000)
# fuente_timer = pygame.font.SysFont(FUENTE_DEL_TIMER, TAMANIO_FUENTE_TIMER)


# while corriendo_juego:
#     eventos = pygame.event.get()
    
#     max_ancho_tablero = ANCHO_PANTALLA * 0.9  # que el tablero use hasta 60% ancho pantalla
#     max_alto_tablero = ALTO_PANTALLA * 0.9   # y hasta 70% alto pantalla

#     for evento in eventos:
#         if evento.type == pygame.QUIT:
#             corriendo_juego = False

#         elif evento.type == evento_segundo:
#             if (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and tiempo_inicializado == True:
#                 if perdi == False:
#                     if gane == False:
#                         segundos += 1
#                         if segundos == 60:
#                             minutos += 1
#                             segundos = 0
        
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             x = pos[0]
#             y = pos[1]

#             if pantalla_actual == "Inicio":
#                 if click_icono_sonido != None and click_icono_sonido.collidepoint(pos) == True:
#                     if pygame.mixer.music.get_busy():
#                         pygame.mixer.music.pause()
#                         musica_activa = False
#                     else:
#                         pygame.mixer.music.unpause()
#                         musica_activa = True
#                     continue
#                 accion = obtener_accion_pantalla_inicio(pantalla, x, y)
#                 if accion == "Jugar":
#                     # pygame.mixer.music.stop()
#                     pantalla_actual = "Seleccion niveles"
#                 elif accion == "Puntajes":
#                     # pygame.mixer.music.stop()
#                     pantalla_actual = "Puntajes"
#                 elif accion == "Salir":
#                     corriendo_juego = False
#                 elif accion == "Resolución":
#                     indice_resolucion_actual += 1
#                     if indice_resolucion_actual >= len(resoluciones):
#                         indice_resolucion_actual = 0
#                     nueva_resolucion = resoluciones[indice_resolucion_actual] 
#                     ANCHO_PANTALLA = nueva_resolucion[0]
#                     ALTO_PANTALLA = nueva_resolucion[1]
#                     pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

#             elif pantalla_actual == "Seleccion niveles":
#                 accion = obtener_accion_pantalla_niveles(pantalla, x, y)
#                 if accion == "Facil" or accion == "Medio" or accion == "Dificil":
#                     pantalla_actual = accion
#                     dificultad_actual = accion
#                     matriz_oculta = None
#                     minutos = 0
#                     segundos = 0
#                     mina_explota = None
#                     primer_click_realizado = False
#                     banderas_colocadas = 0
#                     tiempo_inicializado = False
#                     perdi = False
#                     gane = False
                    
#                     if accion == "Facil":
#                         filas = 8
#                         columnas = 8
#                         minas = 10
#                         tamanio_celda = 90
                
#                     elif accion == "Medio":
#                         filas = 16
#                         columnas = 16
#                         minas = 50
#                         tamanio_celda = 45

#                     elif accion == "Dificil":
#                         filas = 24
#                         columnas = 24
#                         minas = 120
#                         tamanio_celda = 30
                
#                     tamanio_celda_ancho = int(max_ancho_tablero / columnas)
#                     tamanio_celda_alto = int(max_alto_tablero / filas)
                    
#                     if tamanio_celda_ancho < tamanio_celda_alto:
#                         tamanio_celda = tamanio_celda_ancho
#                     else:
#                         tamanio_celda = tamanio_celda_alto
                
#                     matriz_oculta = inicializar_matriz(filas, columnas, 0)
#                     matriz_visible = inicializar_matriz(filas, columnas, " ")
#                     bandera_buscaminas = insertar_iconos_al_buscaminas(RUTA_IMAGEN_BANDERA, tamanio_celda, tamanio_celda)
#                     mina_buscaminas = insertar_iconos_al_buscaminas(RUTA_IMAGEN_MINA, tamanio_celda,tamanio_celda )
                
#                 elif accion == "Volver":
#                     pantalla_actual = "Inicio"

#             elif (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and matriz_oculta != None:
#                 accion_buscaminas = obtener_accion_buscaminas(pantalla, x, y)
                
#                 if accion_buscaminas == "Volver":
#                     pantalla_actual = "Inicio"
#                 elif accion_buscaminas == "Reiniciar":
#                     primer_click_realizado = False
#                     banderas_colocadas = 0
#                     minutos = 0
#                     segundos = 0
#                     tiempo_inicializado = False
#                     mina_explota = None
#                     perdi = False
#                     gane = False
#                     matriz_oculta = inicializar_matriz(filas, columnas, 0)
#                     matriz_visible = inicializar_matriz(filas, columnas, " ")
#                     pantalla_actual = dificultad_actual
                    
#                 else:
#                     posicion = localizar_posicion_click(evento, filas, columnas, tamanio_celda, 50, 40)
                
#                     if posicion != None:
#                         pos = posicion
#                         fila = pos[0]
#                         col = pos[1]

#                         if primer_click_realizado == False:
#                             if primer_click_realizado == False:
#                                 matriz_oculta = preparar_tablero_primer_click(matriz_oculta, fila, col, filas, columnas, minas)
#                                 primer_click_realizado = True
#                                 tiempo_inicializado = True

                        
#                         if evento.button == 1 and matriz_visible[fila][col] != "F":
#                                 if matriz_oculta [fila][col] == "X":
#                                     mina_explota = (fila, col)
#                                     revelar_tablero_final(matriz_oculta, matriz_visible)
#                                     sonido_derrota.play()
#                                     perdi = True
#                                     tiempo_transicion = pygame.time.get_ticks()

#                                 else:
#                                     revelar_celdas(matriz_oculta,matriz_visible, fila, col)
#                                     if verificar_ganador(matriz_oculta, matriz_visible):
#                                         revelar_tablero_final(matriz_oculta,matriz_visible)
#                                         sonido_victoria.play()
#                                         gane = True
#                                         tiempo_transicion = pygame.time.get_ticks()
                        
#                         elif evento.button == 3:
#                             if matriz_visible[fila][col] == " " and banderas_colocadas < minas:
#                                 matriz_visible[fila][col]= "F"
#                                 banderas_colocadas += 1
#                             elif matriz_visible[fila][col] == "F":
#                                 matriz_visible[fila][col] = " "
#                                 banderas_colocadas -= 1

#             elif pantalla_actual == "Puntajes":
#                 accion = obtener_accion_pantalla_puntajes(pantalla, x, y)
#                 pantalla_actual = "Inicio"

#     # Mostrar pantallas y lógica
#     if pantalla_actual == "Inicio":
#         ancho = resoluciones[indice_resolucion_actual][0]
#         alto = resoluciones[indice_resolucion_actual][1]
#         # mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO, ancho, alto)
#         if musica_activa == True and pygame.mixer.music.get_busy() == False:
#             pygame.mixer.music.play(-1)
#         click_icono_sonido = mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO, ANCHO_PANTALLA, ALTO_PANTALLA,icono_musica_on, icono_musica_off, musica_activa)
#         if pantalla_actual != "Inicio":
#             pygame.mixer.music.stop()
    
#     elif pantalla_actual == "Seleccion niveles":
#         mostrar_pantalla_de_niveles(pantalla, RUTA_IMAGEN_SELECCION_DE_NIVELES)

#     elif pantalla_actual == "Puntajes":
#         fuente_puntitos = pygame.font.SysFont(FUENTE_PUNTITOS_PUNTAJES, TAMANIO_FUENTE_PUNTITOS)
#         mostrar_pantalla_de_puntajes(pantalla, RUTA_IMAGEN_PUNTAJES, RUTA_ARCHIVO_PUNTAJES, fuente_puntitos, 750,1500,170,50) #fuente creada anteriormente 

#     elif pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil":
#         cargar_fondo_segun_nivel_elegido(pantalla, pantalla_actual)
#         x, y = pygame.mouse.get_pos() #chusmea estooO!!!
#         accion_buscaminas = obtener_accion_buscaminas(pantalla, x, y)
#         dibujar_buscaminas(pantalla, filas, columnas, COLOR_LINEAS_BUSCAMINAS, COLOR_FONDO_BUSCAMINAS, tamanio_celda, matriz_visible, bandera_buscaminas, mina_buscaminas, mina_explota)
#         crear_fondos_de_textos(pantalla, minutos, segundos, COLOR_DEL_TIMER, banderas_colocadas, minas)

#     elif pantalla_actual == "Ingresar nombre":
#         total_segundos = minutos * 60 + segundos
#         puntaje = calcular_puntaje(dificultad_actual, total_segundos, banderas_colocadas, minas, fue_ganador)
#         fuente_puntaje = pygame.font.SysFont(FUENTE_PUNTAJES, TAMANIO_FUENTE_PUNTAJES)

#         if fue_ganador == True:
#             imagen_fondo = pygame.image.load(RUTA_IMAGEN_GANASTE)
#         else:
#             imagen_fondo = pygame.image.load(RUTA_IMAGEN_PERDISTE)

#         imagen_fondo = pygame.transform.scale(imagen_fondo, pantalla.get_size())

#         nombre_usuario = pedir_nombre_usuario(pantalla, fuente_puntaje, COLO_CAJA_TEXTO_PEDIR_NOMBRE, COLOR_TEXTO_CAJA_PEDIR_NOMBRE, imagen_fondo)
        
#         if nombre_usuario != "":
#             guardar_puntaje(nombre_usuario, puntaje)
#             pantalla_actual = "Puntajes"

#     tiempo_actual = pygame.time.get_ticks()
#     tiempo = tiempo_actual - tiempo_transicion
#     if perdi == True and tiempo >= TIEMPO_DE_TRANSICION:
#         pantalla_actual = "Ingresar nombre"
#         fue_ganador = False
#         perdi = False

#     elif gane == True and tiempo >= TIEMPO_DE_TRANSICION:
#         pantalla_actual ="Ingresar nombre"
#         fue_ganador = True
#         gane = False

#     actualizar_musica_juego(pantalla_actual, musica_activa)
#     pygame.display.update()


# pygame.quit()
# quit()

































































# import pygame
# from biblioteca_funciones import *
# from configuraciones import *
# pygame.init()
# pygame.mixer.init()

# pantalla = inicializar_caracteristicas_pantalla(1534, 801, NOMBRE_JUEGO, RUTA_ICONO_VENTANITA)


# pantalla_actual = "Inicio"
# corriendo_juego = True

# # Temporizador
# evento_segundo = pygame.USEREVENT + 1
# pygame.time.set_timer(evento_segundo, 1000) #poner constante
# timer = 0
# fuente_timer = pygame.font.SysFont(FUENTE_DEL_TIMER, TAMANIO_FUENTE_TIMER)

# matriz_oculta = None
# matriz_visible = None
# primer_click_realizado = False
# banderas_colocadas = 0
# perdi = False
# gane = False
# tiempo_transicion = 0
# pantalla_fin = False
# fue_ganador = False
# tiempo_inicializado = False


# filas = 0 
# columnas = 0 
# minas = 0 
# tamanio_celda = 0



# while corriendo_juego:

#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             corriendo_juego = False

#         elif evento.type == evento_segundo:
#             if (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and tiempo_inicializado == True:
#                 if perdi == False:
#                     if gane == False:
#                         timer += 1

#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()

#             if pantalla_actual == "Inicio":
#                 accion = obtener_accion_pantalla_inicio(x, y)
#                 if accion == "Jugar" or accion == "Dificultad":
#                     pantalla_actual = "Seleccion niveles"
#                 elif accion == "Puntajes":
#                     pantalla_actual = "Puntajes"
#                 elif accion == "Salir":
#                     corriendo_juego = False

#             elif pantalla_actual == "Seleccion niveles":
#                 accion = obtener_accion_pantalla_niveles(x, y)
#                 if accion == "Facil" or accion == "Medio" or accion == "Dificil":
#                     pantalla_actual = accion
#                     matriz_oculta = None
#                     timer = 0
#                     primer_click_realizado = False
#                     banderas_colocadas = 0
#                     tiempo_inicializado = False
                    
#                     if accion == "Facil":
#                         filas = 8
#                         columnas = 8
#                         minas = 10
#                         tamanio_celda = 90
#                     elif accion == "Medio":
#                         filas = 16
#                         columnas = 16
#                         minas = 50
#                         tamanio_celda = 45

#                     elif accion == "Dificil":
#                         filas = 24
#                         columnas = 24
#                         minas = 120
#                         tamanio_celda = 30
                    
#                     matriz_oculta = inicializar_matriz(filas, columnas, 0)
#                     matriz_visible = inicializar_matriz(filas, columnas, " ")
#                     ruta_imagen_bandera = pygame.image.load(RUTA_IMAGEN_BANDERA)
#                     ruta_imagen_bandera = pygame.transform.scale(ruta_imagen_bandera, (tamanio_celda, tamanio_celda))
#                     ruta_imagen_mina = pygame.image.load(RUTA_IMAGEN_MINA)
#                     ruta_imagen_mina = pygame.transform.scale(ruta_imagen_mina, (tamanio_celda,tamanio_celda ))
#                 elif accion == "Volver":
#                     pantalla_actual = "Inicio"

#             elif (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and matriz_oculta != None:
#                 accion_buscaminas =obtener_accion_buscaminas(x,y)
#                 if accion_buscaminas == "Volver":
#                     pantalla_actual = "Inicio"
#                 elif accion_buscaminas == "Reiniciar":
#                     primer_click_realizado = False
#                     banderas_colocadas = 0
#                     timer = 0
#                     tiempo_inicializado = False
#                     matriz_oculta = inicializar_matriz(filas, columnas, 0)
#                     matriz_visible = inicializar_matriz(filas, columnas, " ")
                    
#                 else:
#                     posicion = localizar_posicion_click(evento, filas, columnas, tamanio_celda, 50, 40) #Fijar constante si podes
                
#                     if posicion != None:
#                         fila, col = posicion #chequea esto


#                         if primer_click_realizado == False:
#                             while True:
#                                 generar_minas(matriz_oculta, minas)
#                                 if matriz_oculta[fila][col] != "X":
#                                     break
#                             asignar_contadores(matriz_oculta)
#                             primer_click_realizado = True
#                             tiempo_inicializado = True

                        
#                         if evento.button == 1 and matriz_visible[fila][col] != "F":
#                                 if matriz_oculta [fila][col] == "X":
#                                     revelar_tablero_final(matriz_oculta, matriz_visible)
#                                     perdi = True
#                                     tiempo_transicion = pygame.time.get_ticks()
#                                 else:
#                                     revelar_celdas(matriz_oculta,matriz_visible, fila, col)
#                                     if verificar_ganador(matriz_oculta, matriz_visible):
#                                         revelar_tablero_final(matriz_oculta,matriz_visible)
#                                         gane = True
#                                         tiempo_transicion = pygame.time.get_ticks()
                        
#                         elif evento.button == 3:
#                             if matriz_visible[fila][col] == " " and banderas_colocadas < minas:
#                                 matriz_visible[fila][col]= "F"
#                                 banderas_colocadas += 1
#                             elif matriz_visible[fila][col] == "F":
#                                 matriz_visible[fila][col] = " "
#                                 banderas_colocadas -= 1

#             elif pantalla_actual == "Puntajes":
#                 accion = obtener_accion_pantalla_puntajes(x, y)
#                 pantalla_actual = "Inicio"

#     # Mostrar pantallas y lógica
#     if pantalla_actual == "Inicio":
#         mostrar_pantalla_inicio(pantalla, RUTA_IMAGEN_INICIO)

#     elif pantalla_actual == "Seleccion niveles":
#         mostrar_pantalla_de_niveles(pantalla, RUTA_IMAGEN_SELECCION_DE_NIVELES)

#     elif pantalla_actual == "Puntajes":
#         fuente_puntitos = pygame.font.SysFont(FUENTE_PUNTITOS_PUNTAJES, TAMANIO_FUENTE_PUNTITOS)
#         mostrar_pantalla_de_puntajes(pantalla, RUTA_IMAGEN_PUNTAJES, "BUSCAMINAS_PYGAME/puntajes.csv", fuente_puntitos, 750,1500,170,50) #fuente creada anteriormente 

#     elif pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil":
#         cargar_fondo_segun_nivel_elegido(pantalla, pantalla_actual)
#         x, y = pygame.mouse.get_pos()       
#         accion_buscaminas = obtener_accion_buscaminas(x,y)
#         dibujar_buscaminas(pantalla, filas, columnas, COLOR_LINEAS_BUSCAMINAS, COLOR_FONDO_BUSCAMINAS, tamanio_celda, matriz_visible, ruta_imagen_bandera, ruta_imagen_mina)
#         crear_fondos_de_textos(pantalla, timer, fuente_timer, COLOR_DEL_TIMER, banderas_colocadas, minas)


#     elif pantalla_actual == "Fin":
#         dificultad = pantalla_actual
#         puntaje = calcular_puntaje(dificultad, timer, banderas_colocadas, minas)
#         fuente_puntaje = pygame.font.SysFont(FUENTE_PUNTAJES, TAMANIO_FUENTE_PUNTAJES)
#         mostrar_pantalla_fin_del_juego(pantalla, fuente_puntaje, fue_ganador, puntaje)
#         # if fue_ganador == True: #chequealo!!!!!!!!!!!!
#         pantalla_actual = "Puntajes"

#     tiempo_actual = pygame.time.get_ticks()
#     if perdi and tiempo_actual - tiempo_transicion >= TIEMPO_DE_TRANSICION:
#         pantalla_actual = "Fin"
#         fue_ganador = False
#         perdi = False

#     if gane and tiempo_actual - tiempo_transicion >= TIEMPO_DE_TRANSICION:
#         pantalla_actual = "Fin"
#         fue_ganador = True
#         gane = False

#     pygame.display.update()


# pygame.quit()
# quit()























# import pygame
# from biblioteca_funciones import *

# pygame.init() 
# pygame.mixer.init()

# pantalla = inicializar_caracteristicas_pantalla(1534, 801, "Buscaminas", "BUSCAMINAS_PYGAME/Imagenes/icono_ventanita.png")

# #Rutas
# ruta_imagen_inicio = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_ inicio.png"
# ruta_imagen_seleccion_de_niveles = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_niveles.png"
# ruta_imagen_puntajes = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_puntajes.png"

# pantalla_actual = "Inicio"
# corriendo_juego = True


# while corriendo_juego == True:

#     if pantalla_actual == "Inicio":
#         #pantalla.fill((255, 255, 255))
#         mostrar_pantalla_inicio(pantalla, ruta_imagen_inicio)
#         pygame.display.update()

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 corriendo_juego = False

#             elif evento.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 accion_inicio = obtener_accion(x,y)

#                 if accion_inicio == "Jugar" or accion_inicio == "Dificultad":
#                     pantalla_actual = "Seleccion niveles" 

#                 elif accion_inicio == "Puntajes":
#                     pantalla_actual ="Puntajes"
                
#                 elif accion_inicio == "Salir":
#                     corriendo_juego = False
    
#     elif pantalla_actual == "Seleccion niveles":
#         mostrar_pantalla_de_niveles(pantalla, ruta_imagen_seleccion_de_niveles)
#         pygame.display.update()

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 corriendo_juego = False

#             elif evento.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 accion_niveles = obtener_accion_pantalla_niveles(x,y)

#                 if accion_niveles == "Facil":
#                     #cargar_fondo_segun_nivel_elegido(pantalla, "Facil")
#                     pantalla_actual = "Facil"

#                 elif accion_niveles == "Medio":
#                     #cargar_fondo_segun_nivel_elegido(pantalla, "Medio")
#                     pantalla_actual = "Medio"

#                 elif accion_niveles == "Dificil":
#                     #cargar_fondo_segun_nivel_elegido(pantalla, "Dificil")
#                     pantalla_actual = "Dificil"
                
#                 elif accion_niveles == "Volver":
#                     pantalla_actual = "Inicio"
    
#     if pantalla_actual in ["Facil", "Medio", "Dificil"]:
#         cargar_fondo_segun_nivel_elegido(pantalla, pantalla_actual)
        
#         #dibujar todo

#         if pantalla_actual == "Facil":
#             filas, columnas, minas, tamanio_celda = 8, 8, 10, 68
#         elif pantalla_actual == "Medio":
#             filas, columnas, minas, tamanio_celda = 16, 16, 50, 45
#         elif pantalla_actual == "Dificil":
#             filas, columnas, minas, tamanio_celda = 24, 24, 120, 30

        
#         dibujar_buscaminas(pantalla, filas, columnas, 0,0,0,(220,220,220), tamanio_celda)
#         # matriz= inicializar_matriz(filas, columnas, 0)
#         # posicion_click(matriz, filas,columnas,tamanio_celda, 0,0)
#         pygame.display.update()

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 corriendo_juego = False
                
#             elif evento.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()       
#                 accion_buscaminas = obtener_accion_buscaminas(x,y)

#                 if accion_buscaminas == "Volver":
#                     pantalla_actual = "Inicio"

#                 elif accion_buscaminas == "Reiniciar":
#                     #logica para reiniciar el tablero
#                     print("Reinicia todo")

    

#     elif pantalla_actual == "Puntajes":
#         mostrar_pantalla_de_puntajes(pantalla, ruta_imagen_puntajes)
#         pygame.display.update()
        
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 corriendo_juego = False  
            
#             elif evento.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = pygame.mouse.get_pos()
#                 accion_puntajes = obtener_accion_pantalla_puntajes(x,y)
#                 pantalla_actual = "Inicio"




# #pantalla.fill((255,255,255))

#     #pygame.display.update()
# pygame.quit()

# import pygame
# from biblioteca_funciones import *

# pygame.init()
# pygame.mixer.init()

# pantalla = inicializar_caracteristicas_pantalla(1534, 801, "Buscaminas", "BUSCAMINAS_PYGAME/Imagenes/icono_ventanita.png")

# # Rutas
# ruta_imagen_inicio = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_ inicio.png"
# ruta_imagen_seleccion_de_niveles = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_niveles.png"
# ruta_imagen_puntajes = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_puntajes.png"
# ruta_imagen_ganaste = "BUSCAMINAS_PYGAME/Imagene/Pantalla_ganaste.png"
# ruta_imagen_perdiste = "BUSCAMINAS_PYGAME/Imagenes/Pantalla_perdiste.png"

# pantalla_actual = "Inicio"
# corriendo_juego = True

# # Temporizador
# evento_segundo = pygame.USEREVENT + 1
# pygame.time.set_timer(evento_segundo, 1000)
# timer = 0
# fuente_timer = pygame.font.SysFont("Arial", 30)
# color_timer = (0, 0, 255)

# matriz = None

# while corriendo_juego:

#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             corriendo_juego = False

#         elif evento.type == evento_segundo:
#             if pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil":
#                 timer += 1

#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()

#             if pantalla_actual == "Inicio":
#                 accion = obtener_accion_pantalla_inicio(x, y)
#                 if accion == "Jugar" or accion == "Dificultad":
#                     pantalla_actual = "Seleccion niveles"
#                 elif accion == "Puntajes":
#                     pantalla_actual = "Puntajes"
#                 elif accion == "Salir":
#                     corriendo_juego = False

#             elif pantalla_actual == "Seleccion niveles":
#                 accion = obtener_accion_pantalla_niveles(x, y)
#                 if accion == "Facil" or accion == "Medio" or accion == "Dificil":
#                     pantalla_actual = accion
#                     matriz = None
#                     timer = 0
#                 elif accion == "Volver":
#                     pantalla_actual = "Inicio"

#             elif pantalla_actual == "Puntajes":
#                 accion = obtener_accion_pantalla_puntajes(x, y)
#                 pantalla_actual = "Inicio"
            
#             # Lógica para clicks DENTRO del juego (cuando la pantalla_actual es un nivel)
#             # elif (pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil") and not juego_termiando:
#                 # Aquí iría la llamada a tu función que maneja el click en el tablero
#                 # y que actualiza las variables 'juego_termiando' y 'ganador'
                
#                 # EJEMPLO (esto lo debes reemplazar con tu lógica real)
#                 # Si tu función se llama 'manejar_click_en_tablero' y retorna el estado del juego:
#                 # estado_juego_actual = manejar_click_en_tablero(matriz, x, y, tamanio_celda)
#                 # if estado_juego_actual == "perdio":
#                 #     juego_termiando = True
#                 #     ganador = False
#                 # elif estado_juego_actual == "gano":
#                 #     juego_termiando = True
#                 #     ganador = True
#                 # elif estado_juego_actual == "jugando":
#                 #     pass # El juego sigue, no hay cambios en juego_termiando
                
#                 # --- Tu bloque de lógica de click original iría aquí ---
#                 # Si necesitas las variables 'filas', 'columnas', 'minas', 'tamanio_celda'
#                 # para tu función de click, asegúrate de que estén disponibles globalmente
#                 # o pasalas a la función.
#                 pass # Reemplaza este 'pass' con tu lógica de manejo de click en el tablero


#     # Mostrar pantallas y lógica
#     if pantalla_actual == "Inicio":
#         mostrar_pantalla_inicio(pantalla, ruta_imagen_inicio)

#     elif pantalla_actual == "Seleccion niveles":
#         mostrar_pantalla_de_niveles(pantalla, ruta_imagen_seleccion_de_niveles)

#     elif pantalla_actual == "Puntajes":
#         mostrar_pantalla_de_puntajes(pantalla, ruta_imagen_puntajes)

#     elif pantalla_actual == "Facil" or pantalla_actual == "Medio" or pantalla_actual == "Dificil":
#         cargar_fondo_segun_nivel_elegido(pantalla, pantalla_actual)

#         if matriz == None:
#             if pantalla_actual == "Facil" and timer == 0:
#                 filas, columnas, minas, tamanio_celda = 8, 8, 10, 90
                
#             elif pantalla_actual == "Medio" and timer == 0:
#                 filas, columnas, minas, tamanio_celda = 16, 16, 50, 45

#             elif pantalla_actual == "Dificil" and timer == 0:
#                 filas, columnas, minas, tamanio_celda = 24, 24, 120, 30
                
#             matriz = inicializar_matriz(filas, columnas, 0)
#             # posicion_click(filas, columnas, tamanio_celda, origen_x=50, origen_y=40)
#             generar_minas(matriz, minas)
#             asignar_contadores(matriz)
#             juego_termiando = False #Pantallas paa terminar jeugo.
#             ganador = False #Pantallas paa terminar jeugo.
        

#         dibujar_buscaminas(pantalla, filas, columnas, (0, 0, 0), (220, 220, 220), tamanio_celda, matriz)

#         # texto_timer = crear_texto_timer(timer, fuente_timer, color_timer)
#         # pantalla.blit(texto_timer, (800, 590))

#         # if evento.type == pygame.MOUSEBUTTONDOWN and not juego_termiando:
#         #     x, y = pygame.mouse.get_pos()
#             #funcion para manejar el click en el tablero
#             #retora si se hizo click e una mina o si el juego teerminó

#             #LOGICA DETECCION DE VICTORIA/DERROTA
#             #funcion que recibe el cick y actualice el estado del juego
#             #ejemplo: manejar_click_tablero = true pierse, false gane

#             # Ejemplo (ESTO DEBE VENIR DE TU LÓGICA DEL BUSCAMINAS):
#             # resultado_click = tu_funcion_click_en_celda(matriz, x, y, tamanio_celda)
#             # if resultado_click == "mina":
#             #     juego_terminado = True
#             #     ganaste = False
#             # elif resultado_click == "victoria":
#             #     juego_terminado = True
#             #     ganaste = True

#         # if juego_termiando:
#         #     if ganador == True:
#         #         pantalla_actual = "Ganador"
#         #     else:
#         #         pantalla_actual = "Perdedor"
#         #     tiempo_puntaje = timer #guarda el tiempo final del juego
#         #     timer = 0 #Reinicia el timer para el proximo juego
#         #     #El juego nose vuelve a inicializar hasta que empieze uno nuevo
#         #     matriz = None #Fuerza reinicializaion del jeugo

#         #
#     elif pantalla_actual == "Ganador":
#         #Maejar patalla fin juego, true oara ganar
#         #mostrar_pantalla_fin_del_juego(pantalla, "Arial", True, puntaje)
#         pantalla_actual = "Puntajes"
    
#     elif pantalla_actual == "Perdedor":
#         #Maejar patalla fin juego, true oara ganar
#         #mostrar_pantalla_fin_del_juego(pantalla, "Arial", False, puntaje)
#         pantalla_actual = "Puntajes"



#     pygame.display.update()


# pygame.quit()
# quit()
