def commonDivisor(numerator, denominator):
        numerator = abs(numerator)
        u = []

        for i in range(1, numerator + 1):
            for j in range(1, denominator + 1):
                if((i == j) and ((numerator % i == 0) and (denominator % j == 0))):
                    u.append(i)

        return max(u)

class Fraction:
    '''
     Lớp thực hiện tạo đối tượng phân số cùng với các phép toán phân số,
     Tử số và mẫu số là số nguyên
     Các phép toán trên phân số gồm phép cộng, phép trừ, phép nhân, phép chia,
     Các phép toán này trả lại kết quả là một phân số ở dạng tối giản,
     ví dụ 2/3 + 7/3 thì kết quả là 3/1
     
    '''
    
    def __init__(self,numerator, denominator):
        '''
            Hàm dựng  của phân số gồm tử số numerator, và mẫu số denominator
            Chú ý tên của thuộc tính tử số và mẫu số đặt giống như trên (numerator và denominator)
        '''
        self.numerator = numerator
        self.denominator = denominator    
    
    def addFraction(self, frac):
        '''
            Hàm trả lại kết quả là phép cộng của phân số hiện tại với phân số frac
            ví dụ 2/3 + 7/3 thì kết quả là 3/1
        '''
        addNumerator = 0
        addDenomitor = 0

        if(self.denominator == frac.denominator):
            addNumerator = self.numerator + frac.numerator
            addDenomitor = self.denominator
        else:
            addNumerator = self.numerator * frac.denominator + frac.numerator * self.denominator
            addDenomitor = self.denominator * frac.denominator

        add = Fraction(addNumerator, addDenomitor)
        self.simplify(add)
        return add
        
    def subFraction(self, frac):
        '''
            Hàm trả lại kết quả là phép trừ của phân số hiện tại với phân số frac
            ví dụ 2/3 - 7/3 thì kết quả là -5/3
        '''
        subNumerator = 0
        subDenominator = 0

        if(self.denominator == frac.denominator):
            subNumerator = self.numerator - frac.numerator
            subDenominator = self.denominator
        else:
            subNumerator = self.numerator * frac.denominator - frac.numerator * self.denominator
            subDenominator = self.denominator * frac.denominator

        sub = Fraction(subNumerator, subDenominator)
        self.simplify(sub)

        return sub

    def multiFraction(self, frac):
        '''
            Hàm trả lại kết quả là phép nhân của phân số hiện tại với phân số frac
            ví dụ 2/3 * 7/3 thì kết quả là 14/9
        '''
        mulNumerator = self.numerator * frac.numerator
        mulDenominator = self.denominator * frac.denominator

        mul = Fraction(mulNumerator, mulDenominator)
        self.simplify(mul)

        return mul    
    
    def divFraction(self, frac):
        '''
            Hàm trả lại kết quả là phép chia của phân số hiện tại với phân số frac
            ví dụ 2/3 : 7/3 thì kết quả là 2/7
        '''
        divNumerator = self.numerator * frac.denominator
        divDenominator = self.denominator * frac.numerator

        div = Fraction(divNumerator, divDenominator)
        self.simplify(div)

        return div
    
   

    def simplify(self,frac):
        '''
            Hàm trả lại phân số tối giản của phân số frac
            ví dụ frac = 6/21 thì kết quả trả lại là 2/7
            thuật toán tìm phân số tối giản là chia cả tử số và mẫu số cho ước chung lớn nhất của tử số và mẫu số
        '''
        greatestCommonDivisor = commonDivisor(frac.numerator, frac.denominator)
        frac.numerator = frac.numerator // greatestCommonDivisor
        frac.denominator = frac.denominator // greatestCommonDivisor
        
        return frac
    
    def toString(self):
        '''
            Hàm trả lại chuỗi biểu diễn phân số bởi tử số và mẫu số, ví dụ tử số  = 5, mẫu số = 7, kết quả trả lại chuỗi 5/7
            Hàm này đã được viết sẵn, sinh viên không chỉnh sửa.
        '''
        return str(self.numerator)+'/'+str(self.denominator)


'''
    Chú ý, các phương thức sẽ được gọi đến để chấm điểm, 
    do vậy bài nộp của sinh viên cần phải bỏ hết (hoặc comment #) các lệnh in ra màn hình
     
'''

def testDemo():

    a = Fraction(2,3)
    b = Fraction(7,3)
    
    print(a.addFraction(b).toString())
    print(a.subFraction(b).toString())
    print(a.multiFraction(b).toString())
    print(a.divFraction(b).toString())

    # c = Fraction(9, 3)
    # print(c.commonDivisor(c))
    # print(c.simplify(c).toString())
    # print(c.addFraction(Fraction(1, 2)))
    # print(a.addFraction(b))

'''
Bỏ comment lệnh testDemo() dưới đây để chạy chương trình, và comment lại lệnh đó khi nộp bài
'''
testDemo()