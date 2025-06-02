# Coloca el código de tu juego en este archivo.

# NO ME DIGAS, EN SERIO?!?!?! :O (contexto: el comentario de arriba aparece cuando creas un nuevo proyecto en Ren'Py)

init python:
    import os, pygame, random
    """ si por si acaso quiero hacer algo con ventanas (creo que para una posible segunda alpha)
    import renpygame
    import renpygame as pygame
    from renpygame.locals import *
    """

# Personajes:

define n = Character("Narrador", image=f"characters{os.sep}narrator.png", color="#107492", what_size=50) # Narrador.
define n_man = Character("Narrador", image=f"characters{os.sep}narrator.png", color="#1d1092", what_font=f"fonts{os.sep}Badd-Mono.ttf", what_size=50) # Narrador manipulado (es diferente por un font en específico).

define Byn = Character("Brayn", image=f"characters{os.sep}Brayn.png", color="#6d1092", what_font=f"fonts{os.sep}JetBrainsMono.ttf", what_size=50) # un nuevo personaje llamado Brayn, que te ayudará en la aventura


image n =       f"characters{os.sep}narrator.png"             # Narrador normal
image n_unw =   f"characters{os.sep}narrator_unwilling.png"   # Narrador sin ganas
image n_happy = f"characters{os.sep}narrator_happy.png"       # Narrador feliz
image n_ang =   f"characters{os.sep}narrator_angry.png"       # Narrador enfadado
image n_sad =   f"characters{os.sep}narrator_sad.png"         # Narrador triste
image n_man =   f"characters{os.sep}narrator_manipulated.png" # Narrador manipulado
image n_wat =   f"characters{os.sep}narrator_what.png"        # Narrador que no sabe porque elegiste...eso...

# Brayn, un nuevo personaje de la historia :p
image Brayn =   f"characters{os.sep}Brayn.png"

python:
    '''
    def chimg_n(img=null): #, fondo=0

    if   img == n: renpy.show(n)             #, at_list=[hs]
    elif img == n_unw:   renpy.show(n_unw)   #, at_list=[hs]
    elif img == n_happy: renpy.show(n_happy) #, at_list=[hs]
    elif img == n_ang:   renpy.show(n_ang)   #, at_list=[hs]
    elif img == n_sad:   renpy.show(n_sad)   #, at_list=[hs]
    elif img == n_man:   renpy.show(n_man)   #, at_list=[hs]
    elif img == n_wat:   renpy.show(n_wat)   #, at_list=[hs]
    elif img == null:    print("se te olvidó poner algo")
    else:                print("...no hay ninguna imagen que sea esa")
    '''

    '''
    if fondo == 1: 
            renpy.scene(principal_room)
    elif fondo == 2: 
        renpy.scene(lights_out_room)
    elif fondo == 3: 
        renpy.scene(kittens_room)
    elif fondo == 0: 
        renpy.scene(principal_room)
    else: print("pon un fondo!!!")
    '''
    


# El juego comienza aquí.
# en un mundo muy cuadrado, ok no

# ahora me toca escribir :p (poco xd...un poquito...unas líneas de código, para naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaada es tremendo texto que ocupa 571 lineas de codigo)

label start:
    # esto es para la habitación principal (las imágenes))
    image principal_room = f"rooms{os.sep}room.png"
    image lights_out_room = f"rooms{os.sep}room_lights_out.png"
    
    # gatitos ¿Porque gatitos? Porque me han pedido 
    image kittens_room = f"rooms{os.sep}room_2.png" # arreglar la escala a 1620 por 1080 redimensionando la imagen en el script
    image y-derrepente-PUM = f"rooms{os.sep}PUM_ya_esta_aqui_la_guerra.jpg"
    
    transform center:
        xalign 0.5
        yalign 0.3
    
    transform center_n:
        xalign 0.5
        yalign 0.1
    
    # El narrador tiene su propio transform porque el tiene que estar elevado un poquito para que se vea bien
    
    # variables
    $ decision_1 = False
    $ decision_2 = False
    $ anger_n = 0 # no lo hagas enfadar (te lo digo por los finales (en esta alpha no hay finales disponibles...creo xd))
    # funciones
    # verificador de números:
    init python:
        # Esto fue gracias a un amigo mio que me enseño el meme de 11037 (osea, Leon del videojuego Danganrompa (¿se podr´ia decir que es una referencia a ese juego?). Para el que no sabe el contexto, entro aqui para ver los comentarios y hacer un video al respecto), gracias por ese evento canónico, hice un sistema que detecta si una variable es un numero o no
        def Verify_num(a):
            if a.isnumeric():
                return True
            else:
                try:
                    a=float(a)
                    return True
                except:
                    return False
    # testing characters
    #show Brayn at center
    #Byn "prueba"
    #hide Brayn
    #show n_man at center
    #n_man "prueba test, Lorem Ipsum"
    #hide n_man

    # Brayn
    # Desde el principio
    #call Brayn
    # Desde el final
    #call BraynHouse
    
    # Presenta las líneas del diálogo. Oficialmente....aqui empieza esta historia epica....
    
    scene principal_room
    show n at center_n
    n "Hola! Bienvenid@ al cielo"
    n "ok no, me presento, yo soy Narrador, tu acompañante en esta aventura! ...o eso espero, creo que si, pero no lo sé con certeza"
    n "bueno, Te voy a hacer dos preguntas, la primera es..."
    n "cuál es tu genero?"
    label n_no_anger:
        pass # no lo hagas enfadar
    # para que lo sepas:
    # UsrGen puede ser
    # 1. woman
    # 2. man
    # 3. other
    #  3.1. other-woman
    #  3.2. other-man
    # 4. terrenator, va a ser como un chiste, así que, te sientes como un coche de juguete a radiocontrol...si...bueno, yo no juzgo si te sientes caracterizado como un planta de Plants Vs Zombies ¯\_(ツ)_/¯
    menu:
        "mujer":
            n "ah!...no es común ver por aquí mujeres...pero puedes conocer a las mujeres de este lugar o otros lugares ^^"
            n "lo importante es que te diviertas y/o aprendas algo nuevo"
            n "sino te molesta, te trateré como él, porque aveces me lío, así que, prefiero referirme a todos como él...ok?"
            menu:
                "ok":
                    n "gracias por entenderme :3"
                    $ UsrGen = "woman"
                    call inicio from _call_inicio
                "no":
                    hide n
                    show n_sad at center
                    n "....no quiero que te moleste, pero no puedo hacer nada al respecto :("
                    hide n_sad
                    show n at center_n
                    call inicio from _call_inicio_1
        "hombre":
            n "oh, bueno, no te preocupes, yo te enseñaré un poco este lugar y otros lugares :D"
            n "lo importante es que te diviertas y/o aprendas algo nuevo"
            n "eso es lo que me importa ahora mismo, después, te contaré la historia"
            $ UsrGen = "man"
        "otr@":
            n "...no sé si has contestado ese para no decir tu género o de verdad eres otr@ género"
            n "a pesar de eso, si te quieres sentir caracterizada como mujer, tengo que decirte algo..."
            n "así que, te gusta que te traten como mujer?"
            menu:
                "si":
                    n "Ok...sino te molesta, te trateré como él, porque aveces me lío, así que, prefiero referirme a todos como él...ok?"
                    menu:
                        "ok":
                            n "gracias por entenderme :3"
                            $ UsrGen = "other-woman"
                            call inicio from _call_inicio_6
                        "no":
                            hide n
                            show n_sad at center
                            n "....no quiero que te moleste, pero no puedo hacer nada al respecto :("
                            $ UsrGen = "other-woman"
                            call inicio from _call_inicio_2
                "no":
                    n "ok, eso está bien para mí porque me hago lío cuando quiero llamar a algunas amigas ^^"
                    $ UsrGen = "other-man"
                    call inicio from _call_inicio_3
        "...emmhhh...un Terrenator":
            n "...un Terrenator...en serio?"
            n "pensaba que ibas a ser hombre, mujer o...Otr@"
            n "Eso me parece muy curioso, siendo sincero!"
            hide n
            show n_ang at center_n
            n "Espero que no sea una broma de mal gusto...Verdad?"
            menu:
                "no, no es así!":
                    n "..."
                    hide n_ang
                    show n_wat at center_n
                    n "emmmh...vale :|?"
                    n "sinceramente, es la primera vez que escucho eso y que una persona sea esa...cosa..."
                    hide n_wat
                    $ UsrGen = "terrenator"
                    call inicio from _call_inicio_4
                "sí":
                    hide n_ang
                    show n_unw at center_n
                    n "... Sólo no lo hagas de nuevo por favor -_-*"
                    call n_no_anger from _call_n_no_anger
                "Eso no es verdad!":
                    n "..."
                    hide n_ang
                    show n at center_n
                    n "Vale, es raro que seas esa cosa, pero conozco cosas más raras que me han hablado..."
                    # ASR = A Suspicious Reference
                    $ ASR = 1
                    $ UsrGen = "terrenator"
                    call inicio from _call_inicio_5

    label inicio:
        show n at center_n
        n "Ya sabiendo cuál es tu género, así que..."

    # añadir una mini-broma para los que dicen mal Python, y es cambiar Pypolis por Pipolis
    $ Usrn_Name_Pipolis = 0

    # esto, hace esto...: leer un nombre y depositarlo en una variable
    label res:
        $ Usrn = renpy.input("cuál es tu nombre, persona curiosa como un pequeño gatito?")
    $ Usrn = Usrn.strip()
    
    # nombres de personajes
    if Usrn.lower() == "egepx":
        hide n
        show n_man at center_n
        n_man ". . ."
        n_man "porque me suena ese nombre?"
        n_man "parece ser que alguien se ha pasado el juego completo y quería ver qué pasaría si pone ese nombre en este juego"
        n_man "ese nombre está reservado...por quién será? Jejeje"
        hide n_man
        show n at center_n
        n "...."
        n "mis disculpas por eso...sólo elige otro nombre, por favor..."
        call res from _call_res
    
    if Usrn == "":
        n "..."
        hide n
        show n_unw at center_n
        n "Creo que ha sido un error de tu parte. -_-"
        call res from _call_res_0
    
    if Usrn.lower() == "i'm a snake":
        hide n
        show n_unw at center_n
        n "sinceramente, debería de haber aquí un juego PERO, la idea es terminar este juego, no hacer la copia número 186449968 del snake"
        #aquí comienza el snake chafa
        #python:
        #    Snake_game()


    if Usrn.lower() == "pypolis":
        n ". . ."
        n "cómo es posible que de tooooooooooooooooooooooooodos los nombres posibles nombres que puedas haber tenido, has escojido este?...."
        n "osea Pypolis"
        n "es en serio criaturita del señor??"
        n "bueh, tampoco no me importa"
        $ Usrn_Name_Pipolis = 1
        call res from _call_res_1
    if Usrn.lower() == "pipolis":
        if Usrn_Name_Pipolis == 1:
            n ". . ."
            n "No te creas que soy tan estúpido para no haberme dado cuenta de eso..."
            n "osea, no cuesta mucho"
            n "sólo"
            n "pon"
            n "tu"
            n "nombre"
            n "o"
            n "otro"
            hide n
            show n_ang at center_n
            n "nombre"
            n "de"
            n "Usuario"
            n "Por todos los códigos, no cuesta mucho!!!"
            hide n_ang
            show n at center_n
            n "...."
            hide n
            show n_man at center_n
            n_man "pon tu nombre real, no seas tonto"
            hide n_man
            show n at center_n
            n "........."
            n "ugh....perdón, no me quiero cabrear, es que...sabes, no importa"
            $ Usrn_Name_Pipolis = 2
            call res from _call_res_2
            
        if Usrn_Name_Pipolis == 2 or Usrn_Name_Pipolis == 0:
            n "..."
            n "no."
            n "...hay muchos nombres que no sólo sea ese"
            call res from _call_res_3
        
    if Usrn.lower() == "narrador" or Usrn.lower() == "narrator":
        n "..."
        hide n
        show n_unw at center_n
        n "...parece ser que ese nombre está reservado por la misma persona con la que estás hablando en estos momentos..."
        hide n_unw
        show n at center_n
        call res from _call_res_4
    
    if Verify_num(Usrn) == True:
        n "..."
        hide n
        show n_ang at center_n
        n "vamos a ver...qué demonios significa eso?"
        n "osea, tiene un significado esos números?"
        n "me estás tomando el pelo o qué?"
        menu:
            "Sí":
                n "..."
                hide n_ang
                "de repente, él inspira y espira lentamente"
                show n at center_n
                n "bueno...sólo pon algo que tenga sentido, pero por favor..."
                hide n
                show n_ang at center_n
                n "QUE NO ESTOY PARA JUEGUITOS ABSURDOS DE NUMERITOS..."
                
                hide n_ang
                show n at center_n
                if Usrn == "11037":
                    if ASR == 1:
                        hide n
                        show n_wat at center_n
                        n "tengo una pregunta para tí, porque actúas de forma tan rara?"
                        hide n_wat
                        show n at center_n
                        n "osea, no te quiero molestar, pero es que es como que tienes algo en contra de mí o...no se, a mí me parece eso"
                        n "después de decirte esa cosa qué te quería comentar"
                    else:
                        n "Espera...es una referencia o qué? :| ?"
                        n "bueno, ya que"
                else:
                    n "así que..."
                n "no me hagas de nuevo sino quieres terminar mal....ok? -_-"
                n "a pesar de eso..."
                call res from _call_res_5
            "No":
                hide n_ang
                show n at center_n
                n "wow...no me creo que tus padres te puedan elejir un nombre tan feo para tí.....o sólo eres...ugh..ya que"
                n "puede ser eso o que hayas escojido un nombre de usuario que se llame así....pero creo que eres buena persona y no has hecho eso"
                n "lo digo porque..."
                
                hide n_ang
                show n at center_n
                n "...porque eso espero de tí"
                hide n
                show n_wat at center_n
                n "bueno, quieres ese...nombre? ...si se le puede llamar así?"
                menu:
                    "Sí":
                        hide n_wat
                        show n_unw at center_n
                        n "está bien... si se quieren reir de tí, supongo"
                        call nxt from _call_nxt
                    "No":
                        hide n_wat
                        show n at center_n
                        n "...ok, está bien, inténtalo de nuevo. Podría haber sido un error estúpido de tu parte...o una referencia a algo que NO me estás contando?"
                        call res from _call_res_6
    if Usrn.lower() == "d1234lol":
        n "...emmmmhhhh...es una referencia o que?"
        n "Lo digo porque me había parecido eso porque le conozco"
        n "mejor, intenta orto nombre xd"
        call res from _call_res_7

    n "[Usrn] ...Estás seguro de que ese es tu nombre... o tu nombre de usuario?... *lo dijo un poco molesto e inseguro*"
    menu:
        "Sí":
            
            hide n
            show n_wat at center_n
            n "está bien... supongo???"
            call nxt from _call_nxt_1
        "No":
            n "está bien, inténtalo de nuevo."
            call res from _call_res_8
    # tu personaje, osea EL personaje principal...tú -_-
    define Chr = Character(f"[Usrn]", color="#a0a0a0", what_size=50)
    label nxt:
        hide n_wat
        show n at center_n
    n "Y no tengo nada más que decir, pero antes tengo una pregunta que hacerte."
    $ qst1_1 = True
    $ qst1_2 = True
    $ qst1_3 = True
    $ qst1_4 = True
    label question:
        n "puedo tener acceso a una parte de tu mente para ponerme comunicar directamente desde ahí....por favor *mientras intenta poner ojitos tiernos*"
    menu:
        "Sí" if qst1_1 == True:
            n "estás seguro?"
            menu:
                "Sí":
                    n "oh, ok, sólo dejame hacer esto.... Pero tienes que cerrar los ojos"
                    hide n
                    scene room_lights_out
                    "tu cierras los ojos, aún que sea a fuerza de tu voluntad para que el pueda hacer sus cosas sin que sufras daño"
                    # esta parte será automática
                    window auto # pause 0.5
                    "."
                    ".."
                    "..."
                    window auto False # revisar esta parte del código
                    # aquí se termina la parte automática
                    "después abres los ojos"
                    scene principal_room
                    show n at center_n
                    n "ya está :D"
                    $ decision_1 = True
                    call explorer from _call_explorer
                "No":
                    n "ok, piénsatelo de nuevo"
                    n "pero te voy a repetir la pregunta"
                    call question from _call_question
        "No" if qst1_2 == True:
            n "... ¿Estás seguro?"
            menu:
                "Sí":
                    n "....eh, en serio?! ... Bueno, tienes alguna idea para que me pueda comunicar contigo?"
                    "de rrepente se te ocurren 3 formas para que él se pueda comunicar contigo"
                    $ acc1_1 = True
                    $ acc1_2 = True
                    label i_have_a_idea:
                        menu:
                            "desde el cielo....porque...eres dios?" if acc1_1 == True:
                                hide n
                                show n_ang at center_n
                                n "...si, y quieres que te de mis ideas u otras dudas con ángeles de la guarda, no te...fastidia?"
                                n "no."
                                hide n_ang
                                show n at center_n
                                $ acc1_1 = False
                                call i_have_a_idea from _call_i_have_a_idea
                            '¿con un "walkie talkie"?':
                                n "...mmmmh, podría ser, pero con un objeto que te va a ayudar mucho"
                                n "saca unos audífonos"
                                n "unos audífonos, para tí, no para que se te enreden en el pantalón o nunca los uses :p"
                                "él procede a dártelos y tu decides ponértelos"
                                hide n
                                show n_happy at center
                                n "eso te servirá en tu aventura"
                                $ decision_2 = True
                                call explorer from _call_explorer_1

                            "alguien que funcione como intermediario/a" if acc1_2 == True:
                                n "oh, déjame ver en mi sótano de secu- digo de personas que están dispuestas a hacer eso para ayudate ':)"
                                hide n
                                "él procede a ver en su sótano..."
                                "después vuelve"
                                show n at center_n
                                n "Oh, parece ser que no hay nadie que te pueda ayudar como intermediario/a"
                                n "es una gran pena"
                                $ acc1_2 = False
                                call i_have_a_idea from _call_i_have_a_idea_1
                            "no se, lo siento" if acc1_1 and acc1_2 == False:
                                n "oh...ok"
                                n "lamantablemente no es una respuesta válida para mí en estos momentos, a pesar de todo ;)"
                                $ qst1_2 = False
                                call i_have_a_idea from _call_i_have_a_idea_2

        "Espera, que?!" if qst1_3 == True:
            n f"a ver [Usrn]...me refiero a que tú me prestes una parte de tu mente para ponerme comunicar contigo de forma más cómoda para mí"
            n "si por si acaso no lo has entendido, te repito la pregunta"
            $ qst1_3 = False
            call question from _call_question_1
        "....¿hay otra forma de que tengas mi permiso para no ver mis pensamientos?" if qst1_4 == True:
            n "oh, no voy a ver ninguno de tus pensamientos que tengas, no quiero meterme en tus pensamientos más profundos o algos por el estilo"
            n "no soy ningún cotilla o algo por el estilo"
            n "así que, si por si acaso hay dudas, te repito la pregunta"
            $ qst1_4 = False
            call question from _call_question_2
    
    # explroando pypolis (para más adelante (como capítulo 2 XD (no.)))
    label explorer:
        n "ok, ahora puedes explorar Pypolis :p"
    hide n
    # scene pypolis_citty
    "estás caminando hacia la ciudad, pero de repente, antes de entrar..."
    n "Oye, ¿Te he contado sobre la historia de la ciudad? O mejor dicho, ¿conoces la historia de esta ciudad?"
    menu:
        "Sí":
            n "Ok, Ok... Supongo que te lo dije antes o ya te la habían contado."
            n "pero si no te lo dije, siento no habértelo dicho antes."
            
        "No":
            n "Vale, está bien...para empezar la historia de Pypolis, tenemos que entender que este es un proyecto que lo hizo tu padre como regalo...qué suerte...espero que seas esa...persona..."
            n "bueno, esta ciudad lleva mucho tiempo en pie, aún que la más antigüa es la ciudad C (más conocida como C-Town) es la ciudad más antigüa de todas las ciudades"
            n 'y es casi la ciudad más antigüa del lugar.....a pesar de Assemblera pero esa ciudad es muy rara de escuchar por aquí, se podría decir que es el "patito feo" de las ciudades, para los que no tienen ni idea de este lugar'
            n "y sobre Pypolis, pues es una ciudad donde hay muchas personas y mucha gente por conocer :p ...sino fuera así, eso sería raro. . ."
            n "lo que sé es que puedes visitar 3 lugares en toda la ciudad :D"
            n "está ByteBank (que es banco de todo Pypolis, con su moneda propia que es el ByteCoin),"
            n "PyMart (donde puedes gastar tus ByteCoins)"
            n "y CodeCraft (que es un generador de dinero por exelencia) y eso sería todo. :D"
    
    n "bueno, mientras puedes seguir en esta ciudad, seguro que te va gustar conocer todas estas zonas en este mundo tan grande que casi es gigantesco, el límite es el código >:p"
    $ Pycoins = 0
    $ newer = 1
    $ Mart_act = True
    $ Craft_act = True
    label lugares:
        "te interesa la ciudad, pero antes, a dónde quieres ir primero? :3"
    menu:
        "a ByteBank" if newer == 1:
            n "Bibenvenido a ByteBank, espera...qué acabo de derir?..."
            n "Perdón, quería decir, Bienvenido a ByteBank :D"
            n "este es el banco de toooooooda la ciudad de Pypolis..."
            if Pycoins == 0:
                n "por el momento no tienes dinero, eso me da pena :("
                n "pero es mejor que no vuelvas aquí hasta más tarde"
                if newer == 1:
                    n "Oh! es cierto, eres nuevo por aquí, así que, me toca enseñarte :p"
                    n 'Aquí puedes guardar u usar dinero cuando lo tengas, el dinero aquí se llama "Pytecoins", estas monedas se representan con la abreviatura de Pycoins o simplemente PyC'
                    n "Esta es la moneda nacional de Pypolis, y se usa en toda la ciudad, en otros lugares, tienen sus propias monedas"
                    n "Pero no te preocupes porque se puede usar una moneda que es universal en cualquier ciudad, esta moneda es BitC, a pesar de algunas ciudades más abstractas, funciona bien en todas las ciudades"
                    n "Y no te preocupes, yo te hago el cambio de moneda, cuando sea necesario :p"
                    n "por el momento, puedes explorar otras ciudades"
                    $ newer = 0
                    call lugares from _call_lugares
                
        "a PyMart" if Mart_act == True:
            n "ooohh, PyMart, es una de las tiendas más reconocibles por estos lugares"
            n "me da muchos recuerdos porque cuando era más pequeño, siempre veía esa tienda y me parecía gigantesca y con muchas cosas"
            n "ahora me parece una tienda como otra cualquiera...."
            if Pycoins == 0:
                n "pero bueno, como no tienes Bytecoins, yo te recomiendo irte a otros lugares para ver qué tienen"
            $ Mart_act = False
        "a CodeCraft" if Craft_act == True:
            # para nada es una excusa para que entres a la casa
            "No puedes ir ahí, porque una multitud de gente te estaba tapando la entrada, haciendo que no peudas pasar, creo que sería mejor intentarlo más tarde"
            $ Craft_act = False
        "a...una casa que está cerca de la entrada???":
            "no eres una persona que le guste ser maleducada, así que, te acercas a la casa y llamas al timbre como una persona educada"
            "y derrepente..."
            scene y-derrepente-PUM
            "PUM!!!! >:D"
            scene principal_room
            "nah, es broma, jeje"
            "suena un timbre y después de unos momentos unas letras con texto crean una figura humanoide o algo así..."
            "No lo podías distinguir bien porque esta ocult@ en la oscuridad"
            "pero después sale para decirte algo (ahora lo/la ves mejor)"
            # "poner código aquí xdxd. . ."
            call Brayn from _call_Brayn
            # agregarle un nombre + apariencia del personaje
            #nch ""

            

    # ahora esta es la parte de los idiomas, para configurarlos y ponerlos (más tarde, me da weba)
    # corregir la atrocidad que fue tr/es
    
    label fin:
        
        hide n
        scene room_lights_out
        "fuera bromas, lo siento, porque aquí se termina la alpha de pypolis"
        "o cómo dicen algunos juegos de este estilo, la Alpha, NO el capítulo, la alpha"
        "espero que te o os haya gustado esta aventura :p"
        "...aún que no quería ser el que te dijera esto..."
        scene kittens_room
        "Pero oye, por el momento, toma esta imagen de unos bonitos gatitos comiendo :3"        
        return
    # Finaliza el juego:

    return
