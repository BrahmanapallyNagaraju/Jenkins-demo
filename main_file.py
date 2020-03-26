import sys
def even_odd(num):
  num=int(num)
  if(num%2==0):
    return "even"
  return "odd"
print("Hello world!")
print("after Integration")
print("{} is {}".format(sys.argv[1],is_even(sys.argv[1])))
