plate = int(input())
fairy = int(input())
while plate >= 0 and fairy >= 0:
    if fairy == 0 and plate != 0:
        print("Моющее средство закончилось. Осталось", plate,"тарелок")
    if plate == 0 and fairy != 0:
        print ("Все тарелки вымыты. Осталось", fairy,"ед. моющего средства")
    if plate == 0 and fairy == 0:
        print ("Все тарелки вымыты, моющее средство закончилось")
    fairy -= .5
    plate -= 1
