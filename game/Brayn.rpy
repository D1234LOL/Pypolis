label Brayn:
    show Brayn at center
    Byn "...disculpe, usted quién es?"
    Chr "eeeehhh...y-yo soy [Usrn]"
    if Verify_num(Usrn) == True:
        Byn "...es de borma, verdad? :/"
        Chr "nop"
        Byn "no me gusta criticar nombres, pero sinceramente es un nombre raro..."
        Byn "casi ni parece un nombre..."
        Byn "aún que parece más un nombre de alguien de por aquí o algún que otro número suelto en el aire..."
        Byn "bueno, qué mas dá"
    
    Byn "me presento, soy Brayn, alguien que le gusta mucho explorar ciudades y otros lugares"
    Byn "por lo que veo, eres nuevo por aquí, así que, qué te gustaría hacer o conocer sobre este mundo? :3"
    $ question1   = True
    $ question2   = True
    $ question3   = True
    $ question4   = True
    $ stayInHouse = False

    while True:
        menu:
            "qué es esto?" if question1 == True:
                Byn "bueno, te explico lo que es este lugar y este mundo en general"
                Byn "este mundo es un lugar donde las funcioones y los números son lo que verás por aquí"
                Byn "aún que te puedes encontrar con algún que otro programa o aplicación"
                Byn "en este mundo, hay muchas ciudades y lugares que puedes visitar, yo te acompañaré a donde quieras ir para que no te pierdas por el camino ^^"
                Byn "aún que ten cuidado, porque pueden haber algunas funciones, programas maliciosos y algún que otro error que pueden hacerte daño..."
                Byn "pero cuando vives en un lugar donde hace aproximádamente unos 65 años no existía, es algo que puede ser bastante preocupante... Menos mal que me tienes a mí para ayudarte por estos lugares :p"
                $ question1 = False
            "cómo supiste que era alguien nuevo?" if question2 == True:
                Byn "eso es fácil, porque todos los que siempre veo son iguales y casi nunca cambian, a pesar de algún que otro programa maliciooso o error que puede haber por aquí o en otros lugares"
                $ question2 = False
            "puedo...estar en tu casa?" if question3 == True:
                Byn "no."
                Byn "...Es broma, puedes estar si quieres charlar un rato, pero tengo que organizar la casa, hacía mucho tiempo que no me encontraba a alguien como tú"
                $ stayInHouse = True
                $ question3 = False
            "qué te gusta hacer normalmente?" if question4 == True and question1 == False:
                Byn "mmm, la verdad es que no tengo una que me guste como tal, es cierto quevoy a ciudades para simplemente ir y ver lo que pasa por ahí"
                Byn "tampoco no hago la gran cosa, también hago códigos por mero aburrimiento y creo cosas con lo que me encuentro por ahí"
                Byn "si te tengo que decir algo, es que hacer que tu código sea accesible para todos, es lo mejor que puedes hacer para esta comunidad"
                Byn "pero bueno, quieres aentrar a mi casa aunque sea un desastre?"
                menu:
                    "vale":
                        Byn "está bien, pasa"
                        "mientras ella te mantiene la puerta abierta para que entres y tomas un asiento en el salón"
                        call BraynHouse from _call_BraynHouse
                    "no":
                        Byn "está bien"
                        Byn "qué me quieres decir?"
    
    label BraynHouse:
        "a."
    "aquí es cuando entras a la casa de Brayn, pero no te la voy a mostrar porque necesito compilarla.... -_-"
    "siento las molestias por no poder hacer la casa por dentro, pero seguramente lo verás en la beta y, por supuesto, en la versión final del juego"
        
    
    # final...
    
    $ end_of_alpha = True
    if not end_of_alpha:
        Byn "te presento 3 opciones de ciudades que puedes elejir"
        Byn "cuál eligirás?"
        Byn "derrepente te da 3 opciones..."
        menu:
            "C-Town":
                "es una opción interesante, sinceramente hablando :3"
                "así que, vamos ahí"
                call C from _call_C
            "Bashtopia":
                call Bash from _call_Bash
            "CPP-Town":
                call Cpp from _call_Cpp
    else:
        call fin from _call_fin