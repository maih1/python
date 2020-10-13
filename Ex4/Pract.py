#Hoàn thiện hàm findUniq(a), tìm và trả lại giá trị xuất hiện duy nhất 1 lần trong danh sách a

# def findUniq(a):
#     # setNew = set(a)
#     temp = 0

#     for i in range(0, len(a)-1):
#         count = 0
#         j = i + 1
        
#         for j in range(0, len(a)):
            
#             if (a[i] == a[j]):
#                 count += 1
        
#         if (count == 1):
#             temp = a[i]
                
#     return temp

def findUniq(a):
    d = dict()
    
    for i in a:
        d[i] = d.get(i, 0) + 1
    
    for i in d:
        if (d[i] == 1):
            return i   

a = [1,2,3,2,3,1,4,5,4]
print(findUniq(a))