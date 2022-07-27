import random

rd = random.randint(1, 3)
if rd == 1:
    comp== "s"
elif rd == 2:
    comp= "w"
else:
    comp= "g"

you= input("choose snake(s), water(w) or gun(g): ")
if comp==you:
    print(f"comp choose {comp} and you choose {you}, the game is tie")

elif comp =="s":
    if you=="w":
        print(f"comp choose {comp} and you choose {you}\n YOU LOSE")
    else:
        print(f"comp choose {comp} and you choose {you}\n YOU WIN")


elif comp=="w":
    if you=="s":
        print(f"comp choose {comp} and you choose {you}\n YOU WIN")
    else:
        print(f"comp choose {comp} and you choose {you}\n YOU LOSE")

else:
    if you=="w":
        print(f"comp choose {comp} and you choose {you}\n YOU WIN")
    else:
        print(f"comp choose {comp} and you choose {you}\n YOU LOSE")
