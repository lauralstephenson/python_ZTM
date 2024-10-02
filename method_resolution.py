#Method Resolution Order
#Which order Python runs methods
class A:
    num = 10
    
class B(A):
    pass
#B and C inherit from A
class C(A):
    num = 1
 #D inherits from B and C   
class D(B,C):
    pass

print(D.num)