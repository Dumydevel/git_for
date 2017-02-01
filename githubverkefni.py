#github verkefni
#kaj arnar jörgensen
#27.1.17


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








    if val == 4:
        break











