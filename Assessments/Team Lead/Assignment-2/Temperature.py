import random
while 1:
    Temperature=float(random.randint(10,30));
    Humidity=int(random.randint(30,50));
    print("Temperature : ",Temperature)
    print("Humidity % : ",Humidity)
    if Temperature>=20 :
        print(" --------- Temperature is very high ---------")
    else:
        print(" --------- Temperature is within the range --------")
