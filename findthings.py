def findthings(x):
    lst_cosas=["juguete","aguja","mesa","aguja","silla","pizarra","aguja","agujas"]
    count_things=0
    for i in lst_cosas :
        if i==x:
            count_things=count_things+1
    return count_things

a=findthings("aguja")
print("la cantidad de ocurrencias que hay es : " , a)
if a !=0 :
    print("la cantidad de ocurrencia es : ", a)
else :
    print ("no lo encontre")
