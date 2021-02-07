#Higher/Lower Game
print("Higher-Lower")
player=0
computer=0

numbers=[]
for i in range(1,101):
    numbers.append(i)

while player!=5 and computer!=5:
    choice=random.choice(numbers)
    print(choice)
    Highlow=input("H for higher and L for Lower:")
    while Highlow.upper()!="H" and Highlow.upper()!="L":
        print("Your previous input was invalid")
        Highlow=input("H for higher and L for Lower:")
    choicetwo=random.choice(numbers)
    print(choicetwo)
    if choice==choicetwo:
        print("no points this time")
    elif choice<choicetwo:
        print("It was higher")
        if Highlow.upper()=="H":
            player+=1
        else:
            computer+=1

    elif choice>choicetwo:
        print("It was lower")
        if Highlow.upper()== "L":
            player+=1
        else:
            computer+=1
    print("scores for player", player, "scores for computer", computer)
    print

if player==5:
    print(" Player wins!!!!")
else:
    print("computer wins!!!")
