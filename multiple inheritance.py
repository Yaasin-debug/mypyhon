# multiple inheritance
class A:
  def fun1(self):
    print("fun1")
class B(A):
  def fun2(self):
    print("fun2")
    obj=B()
    obj.fun1()
    obj.fun2()
