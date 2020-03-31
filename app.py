from binarySearch import binarySearch;

class App(object):
  print "Your array is: 2, 3, 4, 10, 40"
  array = [ 2, 3, 4, 10, 40 ]

  x = input("Please, insert the element thar you can search: ")

  result = binarySearch(array, 0, len(array)-1, x)

  if result != -1:
    print "Element is present at index %d ;)" % result
  else:
    print "Element is not present in array :("
