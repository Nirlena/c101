import random

response = 'y'
while response == 'y':
    no = random.randint(1,6)
    if(no == 1):
        print("[-----]")
        print("[     ]")
        print("[  1  ]")
        print("[     ]")
        print("[-----]")
    if(no == 2):
        print("[-----]")
        print("[     ]")
        print("[2   2]")
        print("[     ]")
        print("[-----]")
    if(no == 3):
        print("[-----]")
        print("[     ]")
        print("[ 333 ]")
        print("[     ]")
        print("[-----]")
    if(no == 4):
        print("[-----]")
        print("[4   4]")
        print("[     ]")
        print("[4   4]")
        print("[-----]")
    if(no == 5):
        print("[-----]")
        print("[5   5]")
        print("[  5  ]")
        print("[5   5]")
        print("[-----]")
    if(no == 6):
        print("[-----]")
        print("[6   6]")
        print("[6   6]")
        print("[6   6]")
        print("[-----]")
    response = input("Pressione Y para jogar novamente ou N para sair: ")
    print("\n")
        