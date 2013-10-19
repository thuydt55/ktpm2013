'''
Created on Oct 15, 2013

@author: Thuy
'''
from input import main
import re
import unittest
import collections
from itertools import *
import itertools

def getValue():
    a = main.__doc__
    b = a.split('\n')
    for i in b:
        if(b[0] == ''):
            del b[0]
        t = len(b) -1
        while t != 0:
            if(b[t] == ''):
                del b[t]
            t = t-1
    k = len(b)-1
    index =0
    array = []
    while index != k:
        number = re.findall(r'\d+', '%s' %(b[index]))
        number = map(int,number)
        array.append(number)
        index = index +1
    
    return array

def check_input(arr):
    a = []
    for i in range(len(arr)):
        a.append(len(arr[i]))
        if (a[i]%2!=0) or (a[i] == 0) or (a[i]>6) or (len(arr)>10):
            raise Exception, "Wrong input"
            break
        for j in range(0,len(arr[i]),2):
            if(arr[i][j] >= arr[i][j+1]):
                raise Exception, "Wrong input"
                break
        
    return True

def check_equivalence(arr):
    if check_input(arr):
        d = []
        for a in range(0,len(arr)):
            q = []
            for b in range(0,len(arr[a]),2):
                q.extend(range(arr[a][b],arr[a][b+1]+1))
            d.append(q)
            t=collections.Counter(d[a])
            if len(([i for i in t if t[i]>1])) > 0:
                raise Exception, "Wrong input"
                break
        return True
def get_input_test (arr):
    if check_equivalence(arr):
        l = []
        for i in range(0,len(arr)):
            sublist = []
            for j in range(0,len(arr[i]),2):
                sublist.append(arr[i][j])
            l.append(sublist)
        return l
        
class MainTest (unittest.TestCase):
    pass
def test_generator(a):
    def wrapper (func,args):
        func(*args)
    params = len(a)
    def test(self):
        try:
            if params == 0:
                result = main(*a)
                self.assertEqual(result,result)
            elif params > 0:
                test = []
                for i in range(0,params):
                    test.append(a[i])
                result = wrapper(main,a)
                self.assertEquals(result,result)
        except:
            self.fail("Raised an exception")
    return test

if __name__ == '__main__':
    
    array = []
    array.extend(getValue())
    input = get_input_test(array)
    output = list (itertools.product(*input))
    i = 0
    for arr in output:
        test_name = 'test_%d' % i
        i = i + 1
        test = test_generator(arr)
        setattr(MainTest, test_name, test)
    
    unittest.main()

