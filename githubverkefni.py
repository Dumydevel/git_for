#github verkefni
#kaj arnar jörgensen
#27.1.17
## comment

svar = 0
while (svar == 0):
    print ("veldu 1-3")
    print ("veldu 1 fyir lið1")
    print ("veldu 2 fyrir lið2")
    print ("veldu 3 fyrir lið3")
    print ("veldu 4 fyrir að hætta")
    val = int(input("veldu lið  :  "))

    #liður1
    if val == 1:
        tolulisti = []
        for tala in range (2):
            tala = int(input("sláðu inn tölu :"))
            tolulisti.append(tala)
        print (tolulisti)
        print ("summa talnana er" , sum(tolulisti))
        margfeldi = int(input("Sláðu inn margfeldi :"))
        print ("margfeldi talnana er :", sum(tolulisti) * margfeldi )
        print ("liður eitt er búinn")



    #liður2
    if val == 2:
        nafn = input("sláðu inn Fornafn  :")
        nafn2 = input ("sláðu inn eftirnafn  :")
        print ("halló" , nafn , nafn2)
        print ("liður tvö er búin")



    #liður3
    if val == 3:
        hastafir = 0
        lagstafir = 0
        lagstafirha = 0
        texti = input("sláðu inn texta")
        for x in range(len(texti)):
            if (texti[x].isalpha() and texti [x].isupper()):
                hastafir +=1    #hastafir = hastafir + 1
                if x != len(texti)-1:
                    if (texti[x +1]. islower()):
                        lagstafirha +=1
            if (texti[x]. isalpha() and texti[x]. islower()):
                lagstafir +=1
        print(texti)
        print ("það eru svonna margir hástafir", hastafir)
        print ("það eru svona margir lágstafir", lagstafir)
        print ("svonar margir lágstafir komma efir hástaf", lagstafirha)
        print ("liður 3 er búinn")




    if val == 4:
        break











