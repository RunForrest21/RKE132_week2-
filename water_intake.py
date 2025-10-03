recomended = 2000
glass = 250 
consumption = int(input("Mitu klaasi vett oled joonud?: "))
percent = (consumption*glass)/recomended*100
print(percent)
if percent < 50:
    print ("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print ("Tubli, jätka samas vaimus!")
elif percent >= 100:
    print ("Suurepärane, oled oma päevase eesmärgi täinud!")