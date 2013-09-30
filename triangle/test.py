'''
Created on Sep 24, 2013

@author: thuy
'''
import unittest
import math


#---------------------
# UnitTest
# This pulls our function in form the other file:

from decimal import Decimal
from triangle import detect_triangle

class test_triangle (unittest.TestCase):
   
    '''
    # test tam giac can: 
    #-------------------------------------------------------
    '''
    
    def test_cantaiA(self):
        result = detect_triangle(2, 2**32 -1, 2**32 -1)
        self.assertEqual(result, 'tam giac can')
    
    def test_cantaiB(self):
        result = detect_triangle(2**32 - 1, 2, 2**32 -1)
        self.assertEqual(result,'tam giac can')
    
    def test_cantaiC(self):
        result = detect_triangle(2**32 -1, 2**32 -1, 2)
        self.assertEqual(result,'tam giac can')
    
    '''
    ----------------------------------------------------------
    '''
        
    '''
    # test tam giac deu:
    ----------------------------------------------------------
    '''
    
    def test_tamgiacdeu(self):
        result = detect_triangle(5.0, 5.0, 5.0)
        self.assertEqual(result, 'tam giac deu')
    '''
    ----------------------------------------------------------
    '''
        
    '''
    #test tam giac vuong:
    ---------------------------------------------------------
    '''
    
    def test_vuongtaiA(self):
        result = detect_triangle(3.0, 4, 5)
        self.assertEquals(result, 'tam giac vuong')
    
    def test_vuongtaiB(self):
        result = detect_triangle(4,5,3)
        self.assertEqual(result,'tam giac vuong')
    
    def test_vuongtaiC(self):
        result = detect_triangle(5, 3, 4)
        self.assertEqual(result,'tam giac vuong')
    '''
    --------------------------------------------------------------
    '''
        
    '''
    #test tam giac vuong can
    -------------------------------------------------------------
    '''
    
    def test_vuongcantaiA(self):
        result = detect_triangle(10, math.sqrt(200), 10)
        self.assertEqual(result,'tam giac vuong can')
    
    def test_vuongcantaiB(self):
        result = detect_triangle(3, 3.0, math.sqrt(18))
        self.assertEqual(result, 'tam giac vuong can')
    
    def test_vuongcantaiC(self):
        result = detect_triangle(math.sqrt(200), 10, 10)
        self.assertEqual(result,'tam giac vuong can')
        
    def test_try(self):
        result = detect_triangle(2**32 - 1, 2**32 -1, 4.0)
        self.assertEqual(result,"tam giac vuong can")
    
    def test_vuongcan2(self):
        result = detect_triangle(2**32 - 1, 4.0, 2**32 -1)
        self.assertEqual(result,"tam giac vuong can")
    
    def test_vuongcan3(self):
        result = detect_triangle( 4.0, 2**32 - 1, 2**32 -1)
        self.assertEqual(result,"tam giac vuong can")
    
    '''
    -------------------------------------------------------------
    '''
    
    '''
    tam giac thuong 
    -------------------------------------------------------------
    '''
    def test_tamgiacthuong(self):
        result = detect_triangle(3, 2.0, 4.0)
        self.assertEqual(result, 'tam giac thuong')
        
    '''
    ------------------------------------------------------------
    '''
    '''
    test khong phai tam giac
    --------------------------------------------------------------
    '''
    def test_khongphaitamgiac(self):
        result = detect_triangle(3, 2, 1)
        self.assertEqual(result, 'khong phai tam giac')
    
    def test_khongphaitamgiac2(self):
        result = detect_triangle(Decimal(2**31 - 1), Decimal(10**-9 ), Decimal(2**31 -1))
        self.assertEqual(result,'khong phai tam giac')
   
    '''
    --------------------------------------------------------------
    '''
    
    def test_kieudulieuA(self):
        result = detect_triangle('a', 2.0, 3.9)
        self.assertEqual(result, "du lieu vao khong hop le")
        
    
    def test_kieudulieuB(self):
        result = detect_triangle(3, 'bb', 8)
        self.assertEqual(result,'du lieu vao khong hop le')
    
    
    def test_kieudulieuC(self):
        result = detect_triangle(3, 8, 'value_c')
        self.assertEqual(result,'du lieu vao khong hop le')
    
    '''
    # test dau vao khong nam trong mien xac dinh
    -----------------------------------------------------------
    '''
  
    def test_miengiatricanduoiA(self):
        result = detect_triangle(0, 1, 3)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
   
  
    def test_miengiatricanduoiB(self):
        result = detect_triangle(2, 0, 3)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
   
  
    def test_miengiatricanduoiC(self):
        result = detect_triangle(2, 1, 0)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
           
  
    def test_miengiatricantrenA(self):
        result = detect_triangle(2**32 ,2,1)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
  
    def test_miengiatricantrenB(self):
        result = detect_triangle(2 ,2**32,1)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
    
  
    def test_miengiatricantrenC(self):
        result = detect_triangle(2 ,2,2**32)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
    
  
    def test_miengiatriA(self):
        result = detect_triangle(-1, 2**32 -1, 2**32 -1)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')

    def test_miengiatriB(self):
        result = detect_triangle(2**32 -1, -1, 2**32 -1)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')

    def test_miengiatriC(self):
        result = detect_triangle(2**32 -1, 2**32 -1, -2)
        self.assertEqual(result,'khong nam trong mien gia tri xac dinh')
    '''
    -------------------------------------------------------------------
    '''
    
    
    
# main
if __name__ == '__main__':
    unittest.main()