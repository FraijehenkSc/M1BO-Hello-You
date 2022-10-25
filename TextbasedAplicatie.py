import os
import time

def start():

    print("Welkom! Dit is de 1e versie van de eindopdracht dingen kunnen dus snog veranderen.\nBeantwoord de vragen met A of B om verder te gaan anders gebeurt er niks :)\n")
    print("Voordat we verder gaan, hoe wil je aangesproken worden in het verhaal?\n\nIk wil graag aangesproken worden als...\n\nA. Een meisje \nB. Een jongen")
    gender = input(">>>")
    if gender.lower == "a":
        print("")
    elif gender.lower == "b":
        print("")
    else:
        required()
    print("Oke! Het spel start nu, succes!")
    time.sleep(3)
    os.system("cls")
    intro()

def required():
    print("Niks doen is geen optie! antwoord met 'a' of 'b'\n")
    time.sleep(3)

def intro():
    while True: 
        print("Je bed schudt heen en weer, een aardbeving? Je wordt langzaam wakker. Je merkt op dat je niet in je bed ligt maar op de achterbank van de pickup truck van je oudere zus.\n‘Oja’ Denk je. ‘We zijn op weg naar de Avnásá, een ruimteschip die bedoelt is om een klein groepje gezonde en bekwaamde mensen over te brengen naar Ed’raa, een nieuwe bewoonbare planeet.’")
        print("‘SPELER Ben je wakker geworden?’ vraagt je zus. ‘Ja, met jouw rijstijl is dat ook niet heel gek. ‘ denk je. Je zegt het toch maar niet hardop.\n\nNa een tijdje rijden hoor je de stem van je zus weer: ‘We zijn er {speler}, ik hoop dat je goed bent uitgerust.‘\nJe kijkt uit het raam en ziet een grote futuristische loods met ervoor een lange rij met goed geklede mannen en vrouwen. Jullie stappen uit.\nEen man in wat lijkt een soldaten uniform spreekt jullie aan.") 
        print("‘Jullie twee, Deze kant op’\n\nJullie…\n \nA. Luisteren, en volgen de man.\nB. Negeren de man, en lopen richting de lange rij.")
        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje1()
            break
        elif keuze.lower() == "b":
            stukje2()
            break
        else:
            required()

def stukje1():
    while True:
        print("De soldaat leidt jullie naar een 2e loods die een stuk kleiner is maar evengoed groot genoeg om een paar walvissen in op te bergen. ‘Mevrouw u mag door die rechter deur daar.’ (jongen/meisje), jij gaat door de linker. ‘Wacht even, waarom mogen we niet allebei door dezelfde deur?’ vraagt je zus. ‘Ik heb geen tijd om aan iedereen alles uit te leggen, plus ik heb daar ook niet echt bepaald zin in. Dus je kan of luisteren en door de juiste deur gaan of hier op Aarde blijven.")
        print("\njullie kiezen ervoor om…")
        print("A. Met tegenzin te luisteren, en door de deur te lopen\nB. De soldaat aan te vallen")
        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje3()
            break
        elif keuze.lower() == "b":
            stukje4()
            break
        else:
            required()

def stukje2():
    print("Wat een onsympathieke man… Jullie besluiten de soldaat te negeren en richting de lange rij te lopen. ‘BLIJF STAAN’ de rillingen lopen over je rug. Je realiseert je dat je toch niet zo’n zin heb om eigenwijs te zijn vandaag. Jullie lopen terug naar de soldaat. ")
    time.sleep(10)
    os.system("cls")
    stukje1()

def stukje3():
    while True:
        print("Je wordt wakker door wat je denkt een aardbeving te zijn. ‘Alweer?’ denk je. Je hoofd is net zo wazig als je zicht. Je wordt wakker in wat een luxe hotel kamer lijkt te zijn. Je kijkt om je heen, geen ramen, geen deuren en wat je het meest dwars zit, geen zus.") 
        print("Plotseling gaat draait een deel van de muur om. ‘Ah dat was dus de deur’. Je bent wel wat voorzichtig maar je wilt zo snel mogelijk onderzoeken wat er allemaal gaande is.")
        print("Je loopt je kamer uit. Je kan 2 kanten op links of rechts. Er komen stemmen vanaf links.")
        print("Je loopt naar…\n\n ")
        

        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje11()
            break
        elif keuze.lower() == "b":
            stukje9()
            break
        else:
            required()

def stukje4():
    while True:
        print("Je hebt van de week nog John Wick gekeken, dus het leek je een goed idee om de soldaat op z’n plek te zetten. Dit gaat toch iets lastiger dan je had verwacht. De soldaat is duidelijk getraind in verschillende vechtsporten, ook heeft hij z’n geweer al in zijn handen.")
        print("Je kiest er voor om…\n\n A. Een leg sweep te proberen.\nB. Toch maar niet de held uit te hangen en door de deur te lopen.")

        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje5()
            break
        elif keuze.lower() == "b":
            stukje3()
            break
        else:
            required()

def stukje5():
    while True:
        print("Oke je gaat ervoor. Je gaat eerst laag naar de grond, strekt je been uit en raakt de zijkant van de soldaat z’n been. De soldaat blijft staan als of er niks gebeurt is. Je kijkt omhoog en wordt begroet met een boze blik. ‘Uhh… tijd voor een Hail Mary’ denk je.")
        print("Dit is wat je doet…\n\n A.Gewoon nog een keer proberen toch, waarom niet?\nB. Je verzint een excuus")

        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje6()
            break
        elif keuze.lower() == "b":
            stukje7()
            break
        else:
            required()

def stukje6():
    print("Ja tuurlijk! Als het de eerste keer niet lukt, gewoon nog een keer proberen! Met meer kracht en precisie deel je de 2e leg sweep van vandaag uit. De soldaat heeft genoeg van je onzin en begint te schieten. Je wordt geraakt in meerdere vitale organen. Je bent dood!")
    end()

def end():
    print("Je bent aan het eind gekomen van het spel! Ben je tevreden met je einde? Hoe dan ook, je kan het opnieuw proberen en een ander einde proberen te halen, of stoppen.")
    print("Wat wil je doen?\n\nA.Opnieuw Spelen\nB. Stoppen")

    keuze = input(">>>")
    if keuze.lower() == "a":
        start()
    elif keuze.lower() == "b":
        print("Oke dan, hopelijk was 't een beetje leuk :). Tot ziens!")
        time.sleep(8)
        quit()

def stukje7():
    while True:
        print("Excuses verzinnen is een van je sterke punten! Je moet wel snel zijn, je ziet aan het gezicht van de soldaat dat hij zijn geduld aan het verliezen is.")
        print("‘Sorry meneer! Dit is zo’n stressvolle situatie. Als ik zenuwachtig ben ga ik vaak dansen en in dit geval dus breakdancen. Het was niet de bedoeling om uw been te raken. Sorry!’")
        print("Zo’n slap excuus heb je nog nooit verzonnen. ‘Dit is het dan’ denk je.") 
        print("‘Van de stress gaan we allemaal gekke dingen doen (jongen/meisje). Ik ken het’ zegt de soldaat. Je mond valt open van verbazing. Gelukkig neemt je zus het over voordat je het weer kan verpesten. ‘Bedankt dat u zo begripvol bent tegenover ons, het zal vast ook niet makkelijk voor u zijn. Ik moet door deze deur toch?’  ‘Ja, jij moet door die deur en je (Broertje / Zusje) door de andere.") 
        print("Jullie…")

        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje3()
            break
        elif keuze.lower() == "b":
            stukje8()
            break
        else:
            required()



    
            
            



start()
  