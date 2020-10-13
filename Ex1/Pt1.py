def first_de(a, b):
    if (a != 0):
        x = -b / a
        print("Phuong trinh co nghiem x = ", x)
    elif (b == 0):
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")

a = float(input("Nhap he so a = "))
b = float(input("Nhap he so b = "))

first_de(a, b)