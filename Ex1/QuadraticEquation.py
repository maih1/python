import math

def first_de(a, b):
    if (a != 0):
        x = -b / a
        print("Phuong trinh co nghiem x = ", x)
    elif (b == 0):
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")

def quadraticEquation(a, b, c):
    if(a == 0):
        first_de(b, c)
    else:
        delta = b * b - 4 * a * c

        if(delta < 0):
            print("Phuong trinh vo nghiem")
        elif(delta == 0):
            x = -b / (2 * a)
            print("Phuong trinh co nghiem kep: x = ", x)
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("Phuong trinh co hai nghiem phan biet: x1 = ", x1, ", x2 = ", x2)

a = float(input("Nhap he so a = "))
b = float(input("Nhap he so b = "))
c = float(input("Nhap he so c = "))


quadraticEquation(a, b, c)
    