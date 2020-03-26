import sys
def is_even(num):
  if(num%2==0):
    return true
  return false
print("Hello world!")
print("after Integration")
print("{} is even/odd: {}".format(sys.argv[1],is_even(int(sys.argv[1]))))
