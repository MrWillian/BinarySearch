# Returns index of x in array if present
def binarySearch(array, l, r, x):

  # check base case
  if r >= l:

    middle = l + (r - l)//2 #Get the middle index

    # If element is present at the middle returns itself
    if array[middle] == x:
      return middle

    # If element is smaller than middle, then it can only be present in left subarray
    elif array[middle] > x:
      return binarySearch(array, l, middle-1, x)

    # Else the element can only be present in right subarray
    else:
      return binarySearch(array, middle+1, r, x)

  else:
    # Element is not present in the array
    return -1
