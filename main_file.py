import sys
def is_even(num):
  num=int(num)
  if(num%2==0):
    return True
  return False
print("Hello world!")
print("after Integration")
print("{} is even/odd:{}".format(sys.argv[1],is_even(sys.argv[1])))
