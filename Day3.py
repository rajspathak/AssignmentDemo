'''
Implement a decorator mod_div() which assures that the numerator
is always greater than the denominator e.g. if a = 2, b = 4, 
then div(a, b) should return 2.0 as the output and not 0.5
'''
def div(a, b):
  print(b / a)

def div_rev(fun):
  
  def inner(a, b):
    if a > b:
      a, b = b, a
    fun(a, b)    
 
  return inner

div = div_rev(div) 

div(4, 2) 
