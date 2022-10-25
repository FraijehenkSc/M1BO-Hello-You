import os
import time

def start():
    while True:
        print("Welkom! Dit is de 1e versie van de eindopdracht dingen kunnen dus snog veranderen.\nBeantwoord de vragen met A of B om verder te gaan anders gebeurt er niks :)\n")
        print("Voordat we verder gaan, hoe wil je aangesproken worden in het verhaal?\n\nIk wil graag aangesproken worden als...\n\nA. Een meisje \nB. Een jongen")
        gender = input(">>>")
        if gender.lower() == "a":
            print("je bent a ")
            break
        elif gender.lower() == "b":
            print("je bent b")
            break
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
        print("Je loopt naar…\n\nA. Rechts\nB. Links ")
        

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

def stukje8():
    print("Je duwt je geluk wel tot het uiterste he? Voordat jullie de soldaat kunnen aanvallen wordt je lichthoofdig en kort daarna val je flauw.")
    time.sleep(10)
    stukje3()

def stukje9():
    while True:
        print("Je komt aan in een soort lounge met allemaal verschillende mensen. Dit keer zijn er wel ramen. Het zat er al aan te komen maar als je uit het raam kijkt zie je alleen maar zwart en af en toe een glinstering. ‘we zijn al op het schip dus’ denk je. Een van de mensen loopt naar je toe en begroet je. Het is een lange brede man.")
        print("‘Hallo (knul/grietje), welkom aan boord!’ zegt de man lachend. Je vindt het allemaal maar raar maar je hebt geen andere keuze dan er in mee te gaan. Het voelt alsof je alle tijd hebt dus je besluit een vraag te stellen.") 
        print("Je vraagt…\n\n A. Wie bent u?\nB. jezelf af waarom je nog zinloos aan het praten bent")


        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje10()
            break
        elif keuze.lower() == "b":
            stukje19()
            break
        else:
            required()

def stukje10():
    while True:
        print("Wie ben ik? de man lacht weer. ‘Daar zou ik ook graag achter willen komen! Knul/Grietje, wie ben jij? ‘Oeps, misschien had ik mij eerst moeten voorstellen’ denk je. ‘Uhh Wacht even wie ben ik?’ Het leek zo’n simpele vraag maar je kan het antwoord niet vinden. ‘Ah jij hebt er dus ook last van hè? Iedereen hier heeft geen herinneringen meer voordat we aan boord kwamen. ‘Oh we zijn aan boord van een ruimteschip maar dat zag je denk ik al!’ Je hebt niet echt nuttige informatie opgedaan, dus je besluit wat anders te gaan doen.")
        print("Je gaat…\n\nA.Stoppen met praten. Je vindt dat je wel genoeg heb gepraat vandaag\nB.Richting je kamer zodat je dit keer naar links kan gaan")

        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje19()
            break
        elif keuze.lower() == "b":
            stukje11()
            break
        else:
            required()

def stukje11():
    while True:
        print("Je komt aan in een smal keukentje met vieze tegels en hangend plafondlampje, maar erg veel licht geeft ie niet. Dit lijkt je 3x niks. Je probeert gauw weer weg te lopen maar een hand pakt je bij je schouder. Je draait je om en ziet een jonge vrouw met middellang blond haar en bijna lichtgevende blauwe ogen.")
        print("Ze zit onder het bloed. Fight or Flight instinct komt naar boven.")
        print("En jouw instinct zegt…\n\nA. Fight \nB.Flight")

        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje12()
            break
        elif keuze.lower() == "b":
            stukje13()
            break
        else:
            required()

def stukje12():
    while True:
        print("Vechten dus! Je probeert je los te wringen en slaat wild om je heen. De vrouw ontwijkt met gemak alles. Ze zwaait met een snelle beweging door de lucht.  Je kijkt naar beneden. ‘Huh waarom ben ik nu degene die onder het bloed zit?’ Je strompelt wat en valt snel tegen de grond. Het laatste wat je ziet is de jonge vrouw met een onheilspellende glimlach. Je keel is doorgesneden door de vrouw, je bent dood!")
        time.sleep(10)
        end()

def stukje13():
    while True:
        print("Geweld is nooit de oplossing! Ofzo… |Je schud je los en zet het op het rennen. Je ziet voordat je het keukentje verlaat dat de vrouw ook een mes in haar hand had. Ben jij even blij dat je weg bent gerend! Het is helaas nog niet voorbij je voelt dat ze nog in de buurt is. ‘huh ik hoor nu bij m’n kamer te zijn.’ denk je. Je bent niks anders tegen gekomen onderweg. Waarom zie je nu dan een lange gang met wel 30 deuren. Tijd om keuzes te maken!")
        print("Je kiest ervoor om…\n\n A. Blijven rennen B. Een van de deuren te kiezen")
        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje17()
            break
        elif keuze.lower() == "b":
            stukje14()
            break
        else:
            required()

def stukje14():
    while True:
        print("Je kiest een willekeurige deur. Je beland terug in het vieze keukentje. ’Wat!? Waarom ben ik hier weer!?’ De vrouw is er ook weer en pakt een van je armen stevig vast. Je moet iets doen, en snel. \nHet wordt…\n\n A.Toch maar vechten dan!\nB. Proberen met de vrouw te praten.")
        
        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje12()
            break
        elif keuze.lower() == "b":
            stukje15()
            break
        else:
            required()

def stukje15():
    print("Je voelt dat het geen zin meer heeft om te rennen of te vechten. Ze is te snel + je blijft steeds terug komen in het keukentje. Nu je geen andere opties meer hebt besluit je maar proberen te praten. ‘Waarom doe je dit!’ schreeuw je. Kan het nog clichér? Voordat je antwoord op je vraag kan krijgen, wordt je vanaf de andere kant ook gegrepen en met gemak opgetild. Het is de lange brede man van daarnet! ‘Kom op knul/grietje, tijd om te rennen!’ ")
    input("Druk op enter om door te gaan.")
    stukje16()

def stukje16():
    while True:
        print("De man brengt je terug naar de lounge. ‘Hoe wist u waar ik was? Hoe wist u de weg terug? en… bedankt.’ Geen dank knul/grietje. Ik kwam je gelijk achter na om je te waarschuwen voor de keuken. En de weg terug…? Gewoon rennen! De man lacht weer. ‘De lounge is een veilige plek, vertelt de man. Een plek waar ‘zij’ niet kan komen. Niet dat het uitmaakt want we zijn al op onze bestemming!’ de man heeft gelijk. Je kijkt uit het raam en ziet bomen, planten en bebouwing, alles wat je thuis ook zag. Door de adrenaline heb je waarschijnlijk niks van de landing gemerkt. Iedereen wilt zo snel mogelijk uitstappen, jij bent daar ook een van. een luik schuift open met een soort roltrap naar de grond. Het is best relaxend op de roltrap. Mooie gebouwen en natuur om je heen, maar je mist iets. Je zet je eerste stap op je nieuwe planeet. EEN SCHOK GAAT DOOR JE HELE LICHAAM. Je weet het weer. Je zus. Jouw zus. ‘Blond middellang haar, blauwe ogen. Hoe kon ik niet zien dat zij het was!’")
        print("Er is maar een ding dat je wilt doen, maar  je brein bedenkt toch 2 keuzes voor jezelf…")
        
        keuze = input(">>>")
        if keuze.lower() == "a"or"b":
            stukje20()
            break
        else:
            required()
def stukje20():
    print("Het maakt niet uit wat voor keuzes je brein voor je bedenkt, je gaat terug dat schip in, en je gaat haar vinden. Zo makkelijk gaat het niet want je weet dat je alles vergeet als je het schip binnenstapt. Het maakt je niet uit. Je stapt het schip in en…")
    input("Druk op enter om door te gaan")
    stukje21()

def stukje21():
    print(".-. . ..-- -. .. . / -- . - / .--- . / --.. ..- ... --..-- / .... .- .--. .--. -.-- / . -. -..")
    input("Druk op enter om door te gaan")
    end()

def stukje17():
    while True:
        print("Je blijft rennen en rennen maar er komt geen einde aan. De vrouw is vlak achter je en zwaait haar mes met wilde bewegingen. ‘Knul/Grietje!’ De lange brede man van eerder verschijnt vlak voor je neus. Je moet een niet zo lastige keuze maken.") 
        print("Dus wat wordt ‘t?\n\nA.Stil staan en sterven\nB.Meegaan met de man")
        
        keuze = input(">>>")
        if keuze.lower() == "a":
            stukje18()
            break
        elif keuze.lower() == "b":
            stukje16()
            break
        else:
            required()

def stukje18():
    print("Je blijft stil staan… ‘Oke, dan doe we het zo!’ de man tilt je op gooit je over z’n schouder")
    input("Druk op enter om door te gaan")
    stukje16()

def stukje19():
    print("Ja, praten is een stuk vermoeiender dan je dacht. Je besluit lekker naar bed te gaan! Je komt je kamer in en duikt gelijk in bed. ‘Ah lekker’ denk je. Al dat gezeik met je zus zoeken ben je ook allang vergeten.  Het duurt nog geen 3 minuten of je gedachten gaan al richting dromenland.") 
    print("Wacht, je zus? Had je een zus? Hoe zag ze eruit dan? ‘blond, middellang haar en blauwe ogen. ‘Ja Ik had een zus’")
    print("Je schrikt wakker. Je had een droom maar je bent vergeten wat de inhoud was.")
    print("‘Eindelijk we zijn er!’ je hoort een groep mensen juichen. ‘We kunnen weer over de toekomst denken!’ De mensen klinken een stuk gelukkiger met de situatie dan jij. ‘Toekomst? Wat wil ik eigenlijk gaan doen hier?’ Je voelt je leeg alsof je iets belangrijks heb achter gelaten maar je weet niet wat.")
   
    























    
            
            



start()
  