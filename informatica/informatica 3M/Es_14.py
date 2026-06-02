import math

p_greco = math.pi
raggio =0
for r in range(1,21):
    area= math.pi *(r**2)
    circonferenza= (r*2)*math.pi

    print("Area",int(area),"Circonferenza",int(circonferenza))