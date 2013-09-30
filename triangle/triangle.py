'''
Created on Sep 24, 2013

@author: thuy
'''

#check dau vao la so thuc ?
def checknumber(a,b,c):
    if (a>0 and b>0 and c>0 and a <= 2**32 - 1 and b<=2**32 - 1 and c<=2**32 - 1):
        return 1
    else:
        return 0
#ep kieu
def change_stringToNumber(value):
    if (isinstance(value, str) ):
            try:
                return int(value)
            except ValueError:
                
                try:
                    return float(value)
                except ValueError:
                    return False
    else:
        return value
        
        

def detect_triangle(a, b, c):
    '''
    change_stringToNumber(a)
    change_stringToNumber(b)
    change_stringToNumber(c)
    '''
    EPSILONE = 10**-10
    if ((type(a) in [float,int,long]) and (type(b) in [float,int,long]) and (type(c) in [float,int,long] )):
        if ( checknumber(a, b, c) == 1):
        
            if ((a+b > c) and (a+c > b) and (b+c >a)):
                if ((abs(a - b) < EPSILONE) or (abs(b - c) < EPSILONE) or (abs(c - a) < EPSILONE)):
                    if (abs(a * a + b * b - c * c) < EPSILONE) or (abs(b * b + c * c - a * a) < EPSILONE) or (abs(a * a + c * c - b * b) < EPSILONE):
                        return 'tam giac vuong can'
                    else:
                        if (a == b and b == c):
                            return 'tam giac deu'
                        elif( a == b or b == c or c == a):
                            return 'tam giac can'
                else:
                    if ((pow(a, 2)+pow(b, 2) == pow(c, 2)) or (pow(b, 2)+pow(c, 2) == pow(a, 2)) or (pow(a, 2)+pow(c, 2) == pow(b, 2))):
                        return 'tam giac vuong'
                    else:
                        return 'tam giac thuong'
            else:
                return 'khong phai tam giac'
        else: 
            return 'khong nam trong mien gia tri xac dinh'
    else:
        return 'du lieu vao khong hop le'
