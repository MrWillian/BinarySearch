# BinarySearch

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. 

One of the most common ways to use binary search is to find an item in an array. For example, the Tycho-2 star catalog contains information about the brightest 2,539,913 stars in our galaxy. Suppose that you want to search the catalog for a particular star, based on the star's name. If the program examined every star in the star catalog in order starting with the first, an algorithm called linear search, the computer might have to examine all 2,539,913 stars to find the star you were looking for, in the worst case. If the catalog were sorted alphabetically by star names, binary search would not have to examine more than 22 stars, even in the worst case.


# Getting Started

To use this repository, simply clone it, after that, just enter your folder through the terminal and run the app.py file:

  > python app.py

The array is predefined in the app.py file and shown to you when you run it, at the same time, you will need to enter the number you want to search for. When entering the number, the result will be shown.

![Print](https://i.imgur.com/OS1rhH9.jpg)


# References

https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
https://www.geeksforgeeks.org/python-program-for-binary-search/
