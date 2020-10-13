#Hoàn thiện hàm customSort

def parity(a):
    even = []
    odd = []

    for i in a:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    
    return even, odd

def sorts(a):
    even, odd = parity(a)

    even.sort()
    odd.sort(reverse = True)
    return even, odd

def customSort(a):
    '''
    Hàm thực hiện sắp xếp các phần tử trong a, theo thứ tự:
    - Chẵn bên trái, lẻ bên phải
    - Chẵn tăng dần, lẻ giảm dần
    ví dụ a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kết quả là [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
    '''
    
    even, odd = sorts(a)
    even.extend(odd)

    return even

# a = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

# print(customSort(a))