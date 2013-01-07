# -*-coding: 850 -*--

import pygame,time,sys,os
pygame.init()


pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

pygame.mixer.music.set_volume(1.0)

print " *******  Bienvenido a otro juego de - escoja su propia aventura -  ****** \n"

print "  ***************   Presione cualquier tecla para continuar..  ************* \n"

inp= raw_input()

print "      ***************** Que comience su aventura.. **************** \n"

time.sleep(3)

os.system("cls")

fondo=pygame.mixer.Sound("fondo.wav")

fondo.play(-1)

sonido=pygame.mixer.Sound("Memo01.wav")

sonido.play()

print "Abres los ojos, un fuerte dolor en tu cabeza."

time.sleep(3)

print "Te levantas y viendo a tu alrededor,"

print "ves que estas dentro de un cuarto oscuro."

time.sleep(5)

print "Puedes escuchar la lluvia afuera,y por la falta de luz,"

print "asumes que debe ser de noche."

time.sleep(5)

print "No recuerdas que paso, ni como llegaste aqu¡,"

print "pero tienes un mal presentimiento."

time.sleep(5)

print "Con la poca visibilidad que tienes, ves una puerta a tu derecha."

print "Decides.."

time.sleep(8)

sonido24=pygame.mixer.Sound("Memo24.wav")

sonido25=pygame.mixer.Sound("Memo25.wav")

#time.sleep(25)

repetir = True;

while repetir:
    
    sonido2=pygame.mixer.Sound("Memo02.wav")

    sonido2.play()

    os.system("cls")
    
    print "1. Quedarte en el cuarto, esperando por alguien\n"
    
    print "2. Salir por la puerta \n"
    
    print "Ingrese su opci¢n:"

    time.sleep(8)

    
    selection = raw_input()

    if selection == "1":
        
        os.system("cls")
       
        sonido3=pygame.mixer.Sound("Memo03.wav")

        print "Ha escogido quedarse en el cuarto, esperando por alguien\n"

        time.sleep(1)

        os.system("cls")

        sonido3.play()
        
        print "Ser¡a mejor esperar; no conoces este lugar,"

        time.sleep(2)

        print "y ser¡a peor que te perdieras."

        time.sleep(2)

        print "Esperas por varios minutos, algo que se siente como una eternidad,"

        time.sleep(5)

        print "cuando escuchas un ruido de atr s de la puerta. "

        time.sleep(5)

        print "Se escuchan unos fuertes pasos, y el golpeteo de unas cadenas."

        time.sleep(5)

        print "Apenas tienes tiempo para retroceder a la pared,"

        time.sleep(3)

        print "cuando la puerta se abre con un estruendo."

        time.sleep(3)

        print "En medio de la oscuridad,"

        time.sleep(2)

        print "unos sangrientos ojos rojos miran en tu direcci¢n. "

        time.sleep(3)

        print "El hombre de negro lentamente se acerca,"

        time.sleep(2)
        
        print "con cadena en mano, hacia ti. "

        time.sleep(2)

        print "Apenas puedes moverte, paralizado de miedo."

        time.sleep(3)

        print "El hombre extiende una mano hacia ti,"

        time.sleep(2)

        print "y lo £ltimo que se escucha de ti es un grito de horror."

        time.sleep(4)
        
        os.system("cls")
        
        sonido24.play()
        
        time.sleep(5)
        
        print "Usted ha sido asesinado ! Fin del juego! "

        time.sleep(3)

        repetir =False

    elif selection == "2":

        os.system("cls")
       
        sonido4=pygame.mixer.Sound("Memo04.wav")

        sonido4.play()
        
        print "Ha escogido salir por la puerta \n"

        time.sleep(3)
        
        os.system("cls")

        print "Es muy peligroso quedarse aqu¡. "
        
        time.sleep(30)


        repetir2 = True;

        while repetir2:

            sonido5=pygame.mixer.Sound("Memo05.wav")

            sonido5.play()

            time.sleep(9)

            print "1. Vas a la izquierda, sigue buscando una salida.\n"

            print "2. Vas a la derecha, a ver por la ventana.\n"

            print "Ingrese su opcion: "

            opcion = raw_input()


            if opcion == "1":

                print "Ha escogido ir por la izquierda, buscando una salida\n"

                time.sleep(3)

                os.system("cls")
                
                sonido6=pygame.mixer.Sound("Memo06.wav")

                sonido6.play()

                print "Que importa donde est‚s en este momento,"
		time.sleep(3)
                print "lo que importa ahora es buscar c¢mo salir."
		time.sleep(3)
                print "Sigues avanzando por el pasillo, "
		time.sleep(3)
                print "girando por la esquina, "
		time.sleep(3)
                print "y te encuentras en un corredor con varias puertas."
		time.sleep(3)
                print "Con desesperaci¢n, pruebas cada una de las puertas,"
                time.sleep(3)
		print "y todas dan el mismo resultado: cerrada. "
		time.sleep(3)
                print "Puedes levemente escuchar el sonido de unas cadenas a lo lejos,"
                time.sleep(3)
		print "haciendo que te desesperes a£n m s. "
		time.sleep(3)
                print "Al final del pasillo hay dos puertas: "
                time.sleep(3)
		print "una al frente tuyo, y una a tu derecha. "
                time.sleep(3)
		print "Sin ninguna otra salida, decides.."
		time.sleep(3)
                

                repetir3 = True;

                while repetir3:

                    sonido7=pygame.mixer.Sound("Memo07.wav")

                    sonido7.play()

                    time.sleep(8)

                    print "1.	Tomar la puerta del frente.\n"

                    print "2.	Tomar la puerta de la derecha.\n"

                    print "Ingrese su opcion: "

                    opcion2 = raw_input()


                    if opcion2 == "1":

                        print "Ha escogido tomar la puerta de en frente\n"

                        time.sleep(3)

                        os.system("cls")

                        
                        sonido8=pygame.mixer.Sound("Memo08.wav")

                        sonido8.play()

                        print "Decides probar una puerta m s. "
			time.sleep(3)
                        print "A diferencia de las otras, "
			time.sleep(3)
                        print "la puerta del frente no est  cerrada con seguro. "
			time.sleep(3)
                        print "Sientes un poco m s de confianza al ver que detr s de la puerta"
			time.sleep(3)
                        print "se encuentran las escaleras. "
			time.sleep(3)
                        print "Con esto, estas a un paso m s de escapar."
			time.sleep(3)
                        print "Una vez bajado las escaleras, "
			time.sleep(3)
                        print "te encuentras en una sala poco iluminada. "
			time.sleep(3)
                        print "Tomas unos pasos con cuidado, "
			time.sleep(3)
                        print "cuando notas a tu izquierda un peque¤o perro mir ndote mientras te mueves. "
			time.sleep(3)
                        print "Te detienes por un momento;"
			time.sleep(3)
                        print "recuerdas que en una pel¡cula que viste, "
			time.sleep(3)
                        print "un perro ayudo al protagonista y lo rescato de un asesino. "
			time.sleep(3)
                        print "Tal vez, si encari¤as al perro, "
			time.sleep(3)
                        print "este puede ayudarte en un futuro. Decides.."
			time.sleep(3)


                        repetir4 = True;

                        while repetir4:

                            sonido9=pygame.mixer.Sound("Memo09.wav")

                            sonido9.play()

                            time.sleep(11)

                            print "1. Olvidalo; esto no es un juego, ignora al perro.\n"

                            print "2. Sera mejor encariniar al perro. Acercatele.\n"
                         
                            print "Ingrese su opcion: "

                            opcion3 = raw_input()

        
                            if opcion3=="1":


                                print "Ha escogido ignorar al perro \n"

                                time.sleep(3)

                                os.system("cls")

                                            

                                sonido10=pygame.mixer.Sound("Memo10.wav")

                                sonido10.play()

                                print "No! . No es bueno intentar cruzar la ficci¢n con la realidad. "
				time.sleep(3)
                                print "Por el momento decides cuidadosamente alejarte del perro, "
				time.sleep(3)
                                print "y seguir con tu camino."
				time.sleep(2)
                                print "M s adelante en la sala, "
				time.sleep(2)
                                print "te encuentras en una clase de recepci¢n."
				time.sleep(2)
                                print "A tu derecha puedes ver unas grandes puertas, "
				time.sleep(2)
                                print "con peque¤as ventanas en ellas."
				time.sleep(3)
                                print "Mirando a trav‚s de estas, "
				time.sleep(3)
                                print "te das cuenta que puedes ver la calle afuera."
				time.sleep(3)
                                print "­Al fin has encontrado una salida! "
				time.sleep(3)
                                print "Con alegr¡a, giras la manija, y.."
				time.sleep(2)
                                print "Encuentras que la puerta est  cerrada."
				time.sleep(2)
                                print "Claro.! No podr¡a ser tan f cil. "
				time.sleep(2)
                                print "Sin embargo, estas seguro de que la llave debe de estar cerca."
				time.sleep(3)
                                print "Buscando en la sala no da frutos,"
				time.sleep(3)
                                print "pero encuentras una puerta m s."
				time.sleep(3)
                                print "Con el fin de esta pesadilla cerca,"
				time.sleep(3)
                                print "decides buscar por esta nueva puerta."
				time.sleep(3)
                                print "Despu‚s de pasar por un sucio y oscuro corredor, "
				time.sleep(3)
                                print "te encuentras en un cuarto oscuro, "
				time.sleep(3)
                                print "repleto de cajones. "
				time.sleep(2)
                                print "Sin otra opci¢n, decides buscar en estos cajones."
				time.sleep(3)
                                print "Varios de estos cajones est n vac¡os."
				time.sleep(3)
                                print "Despu‚s de una corta b£squeda, metes tu mano en otro caj¢n."
				time.sleep(3)
                                print "Una sensaci¢n de algo movi‚ndose sobre tu mano te espanta,"
				time.sleep(3)
                                print "causando que des un peque¤o grito."
				time.sleep(3)
                                print "El grito, al parecer,"
				time.sleep(3)
                                print "despert¢ a un perro enjaulado en la esquina del cuarto."
				time.sleep(3)
                                print "Este empieza a ladrar fuertemente,"
				time.sleep(3)
                                print "y el ruido de las cadenas se hace cada vez m s fuerte. "
				time.sleep(3)
                                print "Sin ninguna salida, tu.."


                                time.sleep(2)

                                repetir5 = True;

                                while repetir5:

                                    sonido11=pygame.mixer.Sound("Memo11.wav")

                                    sonido11.play()

                                    time.sleep(9)

                                    print "1. Manten la calma, busca la llave en el otro cajon."

                                    print "2.	Olvidalo, tengo que salir de aqui."

                                    print "Ingrese su opcion: "

                                    opcion4 = raw_input()

                
                                    if opcion4=="1":


                                        print "Ha escogido buscar la llave en otro cajon \n"

                                        time.sleep(3)

                                        os.system("cls")

                                        sonido12=pygame.mixer.Sound("Memo12.wav")

                                        sonido12.play()


                                        print "No debes permitir que el miedo te controle."
					time.sleep(3)
                                        print "R pidamente, abres el ultimo caj¢n, "
					time.sleep(3)
                                        print "y en el encuentras un llavero con dos llaves. "
					time.sleep(3)
                                        print "Sin dudarlo, tomas el llavero, y sales corriendo por donde viniste."
					time.sleep(5)
                                        print "En la recepci¢n, corres hacia la puerta, "
					time.sleep(4)
                                        print "cuando notas una figura acerc ndose desde la derecha."
					time.sleep(3)
                                        print "El hombre de negro con ojos rojos lentamente se acerca hacia ti,"
					time.sleep(3)
                                        print "un gran cuchillo en sus manos."
					time.sleep(3)
                                        print "El miedo se apodera de ti."
					time.sleep(3)
                                        print "Si no te apresuras, no saldr s de aqu¡ con vida."
					time.sleep(5)
                                        print "En tu mano, el llavero, y sin tiempo que perder, coges.."


                                        time.sleep(5)

                                        repetir6 = True;

                                        while repetir6:

                                            sonido13=pygame.mixer.Sound("Memo13.wav")

                                            sonido13.play()

                                            time.sleep(6)

                                            print "1. La llave blanca"

                                            print "2.  La llave roja"

                                            print "Ingrese su opcion: "

                                            opcion5 = raw_input()

                        
                                            if opcion5=="1":

                                                os.system("cls")

                                                print "Ha escogido la llave con borde blanco\n"

                                                time.sleep(3)

                                                os.system("cls")

                                                
                                                sonido14=pygame.mixer.Sound("Memo14.wav")

                                                sonido14.play()
                                                
                                                print "La llave con borde blanco. "
						time.sleep(3)
                                                print "Intentas abrir la puerta, pero.."
						time.sleep(3)
                                                print "La llave no entra en la cerradura."
						time.sleep(3)
                                                print "Tu desesperaci¢n llega a su l¡mite. "
						time.sleep(3)
                                                print "Te apresuras en coger la otra llave, pero en tu apuro, se te cae el llavero."
						time.sleep(4)
                                                print "No tienes tiempo de agacharte cuando"
						time.sleep(3)
                                                print "un cuchillo se clava en tu hombro."
						time.sleep(3)
                                                print "El dolor es inaguantable, y caes en el suelo, indefenso."
						time.sleep(3)
                                                print "Apenas puedes ver el rostro cubierto del asesino,"
						time.sleep(3)
                                                print "quien extiende su mano hacia ti."
						time.sleep(3)
                                                print "Esos ojos rojos sangrientos es lo £ltimo que ves antes de perder la conciencia."
						time.sleep(5)
                                               

                                                os.system("cls")
                                                
                                                sonido24.play()
                                                                                
                                                print "Usted ha sido asesinado ! Fin del juego! "

                                                time.sleep(8)

                                                repetir6= False
                                                
                                                repetir5=False

                                                repetir4=False
                                                
                                                repetir3= False

                                                repetir2 =False
                                                
                                                repetir = False

                                            elif opcion5=="2":

                                                os.system("cls")

                                                print "Ha escogido la llave con borde rojo\n"

                                                time.sleep(3)
                                                
                                                os.system("cls")
                                                
                                                sonido15=pygame.mixer.Sound("Memo15.wav")

                                                sonido15.play()


                                                print "La llave con borde rojo. Intentas abrir la puerta..."
                                               
 
                                                
                                                time.sleep(4)

                                                sonido16=pygame.mixer.Sound("Memo16.wav")

                                                sonido16.play()

                                                print "Con un fuerte sonido, la puerta se abre,"
						time.sleep(3)
                                                print "y sales corriendo lo m s lejos posible de este lugar."
						time.sleep(3)
                                                print "No importa el dolor en tus piernas por cansancio,"
						time.sleep(3)	
                                                print "lo £nico que quieres es vivir."
						time.sleep(3)
                                                print "Eso fue lo £ltimo que supiste de ese lugar, "
						time.sleep(3)
                                                print "y el sonido de las cadenas sigui¢ grabado en tus pesadillas."

                                                time.sleep(3)

                                                sonido24.play()
                                                
                                                time.sleep(5)

                                                repetir6= False
                                                
                                                repetir5=False

                                                repetir4=False
                                                
                                                repetir3= False

                                                repetir2 =False
                                                
                                                repetir = False


                                            else:

                                                sonido25.play()
                                                
                                                time.sleep(4)

                                                sys.stdout.flush()

                                                os.system("cls")

                   
                                    elif opcion4=="2":

                                        os.system("cls")

                                        print "Ha escogido salir de ahi.\n"

                                        time.sleep(3)
                                        
                                        os.system("cls")
                                       
                                        sonido17=pygame.mixer.Sound("Memo17.wav")

                                        sonido17.play()
                                        
                                        print "El ruido de las cadenas se acerca cada vez m s y m s. "
					time.sleep(3)
                                        print "Tu desesperaci¢n llega al l¡mite, y decides correr. "
					time.sleep(4)
                                        print "Pero, por el mismo corredor del que viniste,"
					time.sleep(3)
                                        print "puedes ver unos ojos rojos y sangrientos lentamente acerc ndose hacia ti."
					time.sleep(5)
                                        print "El miedo toma control; ya no sabes que hacer. "
					time.sleep(3)
                                        print "Tu cuerpo se mueve por s¡ solo,"
					time.sleep(3)
                                        print "y sales corriendo lo m s lejos de esta persona."
					time.sleep(3)
                                        print "Al llegar a la pared,"
					time.sleep(3)
                                        print "te das cuenta de una puerta que no notaste por la oscuridad."
					time.sleep(5)
                                        print "Desesperadamente, empujas y empujas, esperando alejarte de tu perseguidor."
					time.sleep(5)
                                       

                                        sonido16=pygame.mixer.Sound("Memo16.wav")

                                        sonido16.play()

                                        print "Con un fuerte sonido, la puerta se abre, "
					time.sleep(3)
                                        print "y sales corriendo lo m s lejos posible de este lugar. "
					time.sleep(3)
                                        print "No importa el dolor en tus piernas por cansancio,"
					time.sleep(3)
                                        print "lo £nico que quieres es vivir."
					time.sleep(3)
                                        print "Eso fue lo £ltimo que supiste de ese lugar, "
					time.sleep(3)
                                        print "y el sonido de las cadenas sigui¢ grabado en tus pesadillas."
                                        
                                        time.sleep(3)

                                        sonido24.play()
                                        
                                        time.sleep(5)
                                        
                                        repetir5=False

                                        repetir4=False
                                        
                                        repetir3= False

                                        repetir2 =False
                                        
                                        repetir = False
                                        
                                        
                                    else:
                                           
                                        sonido25.play()
                                        
                                        time.sleep(4)

                                        sys.stdout.flush()

                                        os.system("cls")

                                

                            elif opcion3=="2":


                                os.system("cls")
                               
                                sonido18=pygame.mixer.Sound("Memo18.wav")

                                sonido18.play()
                                
                                print "Ha escogido acercarse al perro y encariniarlo.\n"

                                time.sleep(3)
                                
                                os.system("cls")
                                
                                print "Bueno, no puede doler intentar encari¤ar al perro."
				time.sleep(3)
                                print "Te acercas con cuidado al perro, e intentas acariciarlo. "
				time.sleep(3)
                                print " \"Hola, amiguito \", le dices. \" No temas. Solo quiero conocerte.\" "
				time.sleep(6)
                                print "Lentamente acercas la mano para acariciar al perro,"
				time.sleep(3)
                                print "cuando este te muerde por instinto."
				time.sleep(3)
                                print "R pidamente alejas la mano,"
				time.sleep(3)
                                print "un fuerte dolor donde el perro te mordi¢. "
				time.sleep(3)
                                print "El perro empieza a rodearte, ladrando fuertemente contra ti."
				time.sleep(6)
                                print "En el fondo, el ruido de las cadenas se hace m s fuerte."
				time.sleep(3)
                                print "Intentas todo lo posible para calmar al animal,"
				time.sleep(3)
                                print "tu desesperaci¢n aumentando. "
				time.sleep(3)
                                print "De repente, sientes un fuerte dolor en el pecho,"
				time.sleep(3)
                                print "y gotas de sangre caen al suelo."
				time.sleep(3)
                                print "Lentamente observas hacia abajo y"
				time.sleep(3)
                                print "ves una especie de cuchillo saliendo de tu pecho,"
				time.sleep(3)
                                print "tu sangre corriendo de ‚l. "
				time.sleep(3)
                                print "Intentas voltear la cabeza, y ves unos ojos rojos regres ndote la mirada. "
				time.sleep(6)
                                print "Tu cuerpo sin vida colapsa en el suelo."

                                time.sleep(3)

                                sonido24.play()
                                
                                time.sleep(5)
                                
                                print "Usted ha sido asesinado ! Fin del juego! "

                                time.sleep(3)

                                repetir4=False
                                
                                repetir3= False

                                repetir2 =False
                                
                                repetir = False

                            else:
                                
                                sonido25.play()
                        
                                time.sleep(4)

                                sys.stdout.flush()

                                os.system("cls")

                       

                    elif opcion2 == "2":

                        

                        os.system("cls")
                       
                        sonido19=pygame.mixer.Sound("Memo19.wav")

                        sonido19.play()
                        
                        print "Ha escogido tomar la puerta de la derecha.\n"

                        time.sleep(3)
                        
                        os.system("cls")


                        print "Decides probar una puerta m s."
			time.sleep(3)
                        print "A diferencia de las otras, "
			time.sleep(3)
                        print "la puerta de la derecha no est  cerrada con seguro. "
			time.sleep(3)
                        print "Sientes un poco m s de confianza; "
			time.sleep(3)
                        print "puede que aqu¡ encuentres algo para defenderte,"
			time.sleep(3)
                        print "­hasta incluso una salida! "
			time.sleep(3)
                        print "El cuarto esta obscuro, pero aun as¡ es navegable."
			time.sleep(3)
                        print "Sin embargo, apenas das unos pasos, "
			time.sleep(3)
                        print "cuando tu pie golpea contra algo. "
			time.sleep(3)
                        print "Miras abajo y ves el cuerpo sin vida de una joven. "
			time.sleep(3)
                        print "Al ver esos ojos fr¡os y sin vida, no puedes evitar dar un grito."
			time.sleep(6)
                        print "Pero, en ese instante, una mano te agarra desde atr s, silenci ndote."
			time.sleep(6)
                        print "Intentas forcejear contra tu atacante, "
			time.sleep(3)
                        print "pero este simplemente pasa un objeto filoso a lado de tu cuello, y.."
			time.sleep(6)
                        print "Tu cuerpo sin vida colapsa en el suelo, "
			time.sleep(3)
                        print "un charco de sangre formando r pidamente a tu alrededor."

                       
                        time.sleep(3)

                        sonido24.play()
                        
                        time.sleep(5)
                        
                        print "Usted ha sido asesinado ! Fin del juego! "

                        time.sleep(3)

                        repetir3= False

                        repetir2 =False
                        
                        repetir = False

                        

                    else:

                        sonido25.play()
                        
                        time.sleep(4)

                        sys.stdout.flush()

                        os.system("cls")


                    
                
            elif opcion== "2":

                os.system("cls")
               
                sonido20=pygame.mixer.Sound("Memo20.wav")

                sonido20.play()
                
                print "Ha escogido ir por la derecha y observar por la ventana.\n"

                time.sleep(3)
                
                os.system("cls")
                
                time.sleep(11)

                repetir3=True

                while repetir3:

                    sonido21=pygame.mixer.Sound("Memo07.wav")

                    sonido21.play()

                    time.sleep(8)

                    print "1. Mirar que hay afuera."

                    print "2. Intentar abrir la ventana."

                    print "Ingrese su opcion: "

                    opcion3 = raw_input()

                    if opcion3=="1":

                        os.system("cls")
                       
                        sonido22=pygame.mixer.Sound("Memo22.wav")

                        sonido22.play()
                        
                        print "Ha escogido mirar afuera.\n"

                        time.sleep(3)
                        
                        os.system("cls")


                        print "Intentas observar a trav‚s de la ventana."
			time.sleep(3)
                        print "Apenas puedes ver la lluvia cayendo; "
			time.sleep(3)
                        print "sin ninguna fuente de luz, y con la oscuridad de la noche, "
			time.sleep(4)
                        print "no puedes ver que hay afuera. "
			time.sleep(3)
                        print "En fin, decides regresar y seguir buscando una salida."
			time.sleep(3)
                        print "Un ruido de cadenas se escucha detr s de ti."
			time.sleep(3)
                        print "En el instante que te volteas,"
			time.sleep(3)
                        print "sientes un terrible dolor en tu cabeza. "
			time.sleep(3)
                        print "Colapsas al suelo, sangre derram ndose alrededor tuyo."
			time.sleep(4)
                        print "Antes de perder la conciencia, "
			time.sleep(3)
                        print "puedes ver unos ojos rojos sangrientos mir ndote. "
			time.sleep(3)
                        print "El hombre de negro extiende su mano hacia ti, y no puedes ver m s."

                        
                        time.sleep(4)

                        sonido24.play()
                        
                        time.sleep(5)
                        
                        print "Usted ha sido asesinado ! Fin del juego! "

                        time.sleep(3)

                        repetir3= False

                        repetir2 =False
                        
                        repetir = False


                    elif opcion3=="2":

                        os.system("cls")
                       
                        sonido23=pygame.mixer.Sound("Memo23.wav")

                        sonido23.play()
                        
                        print "Ha escogido intentar abrir la ventana.\n"

                        time.sleep(3)
                        
                        os.system("cls")


                        print "Puede que sea dif¡cil de ver algo en la oscuridad. "
			time.sleep(3)
                        print "Lo mejor ser¡a abrir la ventana. "
			time.sleep(3)
                        print "Intentas abrirla con todo tu fuerza, "
			time.sleep(3)
                        print "pero al parecer, la ventana est  bien cerrada."
			time.sleep(3)
                        print "Sin importar, t£ sigues intentando, cada vez empujando m s y m s."
			time.sleep(3)
                        print "Despu‚s de poco, al fin logras abrir la ventana."
			time.sleep(3)
                        print "Decides echar un vistazo afuera. "
			time.sleep(3)
                        print "Las gotas de lluvia siguen cayendo fuertemente,"
			time.sleep(3)
                        print "e intentas observar los alrededores."
			time.sleep(3)
                        print "Apenas puedes escuchar un ruido de cadenas,"
			time.sleep(3)
                        print "que cada vez se hace m s y m s fuerte. "
			time.sleep(3)
                        print "Sin aviso, algo te empuja de la ventana, y caes hacia el suelo."
			time.sleep(3)
                        print "Lo £nico que puedes hacer es dar un grito de horror antes de impactar con el suelo."

                        
                        time.sleep(3)

                        sonido24.play()
                        
                        time.sleep(5)
                        
                        print "Usted ha sido asesinado ! Fin del juego! "

                        time.sleep(3)

                        repetir3= False

                        repetir2 =False
                        
                        repetir = False

                        

                    else:

                        sonido25.play()
                        
                        time.sleep(4)

                        sys.stdout.flush()

                        os.system("cls")  
                    
               
               
                
            else:
                    
                sonido25.play()
                
                time.sleep(4)

                sys.stdout.flush()

                os.system("cls")    
                

                          
    else:

        sonido25.play()
        
        time.sleep(4)

        sys.stdout.flush()

        os.system("cls")
