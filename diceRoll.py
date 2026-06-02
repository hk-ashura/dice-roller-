import random 

while True:
    
    x=input("roll tthe dice ( y/ n)").lower()

    if x == "y" :
        z=random.randint(1,6)
        print(z)
        
    elif x == "n" :
         print("thanks for coming")
         break;
    else :
        print("invalid input, please input y for yes and n for no ")

     





        