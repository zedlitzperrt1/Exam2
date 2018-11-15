""" Due end of class Thursday
/
BONUS EXAM 1

NAMES: 
    Paul Davis
    Gabby Lazo
    Tiffany Perry
    Daniel Gomez
    
Write pseudo code in your script, then list all solutions in Python

Section 3.1
    3-7 (1 point each)
    30-33 (3 points each)
    Selection Sort (3 points)
    
p.233 Shaker sort (5 points)
"""
from math import ceil, floor

"""
#3
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    sum = 0
    for i=1 to n
        sum += L[i]
    return sum
Output: sum of integers in list

"""

def number3(self):
    temp_sum = 0
    for i in range(0, len(self)):
        temp_sum += self[i]
    return temp_sum

"""
#4
Input: (L = a1<=a2<=...<=an: where each ai is an integer), X integer
Algorithm:
    index = set()
    for i=1 to n
        if L[i] == X
            index.add(i)
    return index
Output: Location of occurrences of X in L

"""

def number4(self, x):
    index = set()
    for i in range(0, len(self)):
        if self[i] == x:
            index.add(i)
    return index

"""
#5
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    max = 0
    min = 0
    for i=1 to n
        if max < i:
            max = i
        if min > i:
            min = i
    return max and min
Output: The maximum, and minimum element in L
"""

def number5(self):
    temp_max = self[0]
    temp_min = self[0]
    for i in range(0, len(self)):
        if temp_max < self[i]:
            temp_max = self[i]
        if temp_min > self[i]:
            temp_min = self[i]
    return print(f'The max element is {temp_max} and the min element is {temp_min}')

"""
#6
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    negatives = 0
    for i=1 to n
        if L[i] < 0:
            negatives += 1
    return negatives
Output: The total number of negative integers in the list
"""

def number6(self):
    negatives = 0
    for i in range(0, len(self)):
        if self[i] < 0:
            negatives += 1
    return negatives

"""
#7
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    k = 1
    for i=1 to n
        if L[i] is even:
            k = L[i]
    return k
Output: The location of the last even integer in the list
"""

def number7(self):
    lasteven = 0
    for i in range(0, len(self)):
        if self[i] % 2 == 0:
            lasteven = i
    return lasteven

"""
#8
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    k = 0
    for i=1 to n
        if L[i] is even and greater than or equal to L[k]:
            k = i
    return k
Output: The location of the highest even integer in the list
"""

def number8(self):
    k = 0
    for i in range(0, len(self)):
        if self[i] % 2 == 0 and self[i] >= self[k]:
            k = i
    return k

"""
16.  Describe an algorithm for finding the smallest integer in a finite sequence of natural numbers.

Make an array of natural numbers
Store the first element in the array as a temp variable.
Begin a loop that starts at the first element and continues to the last element.
If the current element is smaller than the temp variable, swap them.

Output: The smallest variable
"""
17. Describe an algorithm that locates the first occurrence of the largest element in a finite list of integers, 
where the intgers in the list are not necessrily distinct.

Make an array of ints
Store the first element in the array as a temp variable.
Begin a loop that starts at the first element and continues to the last element.
If the current element is larger than the temp variable, swap them.
Cycle through the array again from the first element, if element=temp, return location of element.

Output: Element of first occurence of smallest number.
"""

18. Descrie an algorithm that locates the last occurence of the smallest element in a finite list of ints, where 
the ints are not necessarily distinct.

Make an array of ints
Store the first element in the array as a temp variable.
Begin a loop that starts at the first element and continues to the last element.
If the current element is smaller than the temp variable, swap them.
Cycle through the array again from the first element, if element=temp, store location of element in seperate list.
Sort the list of locations.
The last occurence equals the largest location number.

Output: Element of last occurence of smallest number.
"""

19. Describe an algorithm that produces the max, median, mean ,and min of a set of 3 ints.

Make an array of 3 integers 

1.Sort the array
Begin a loop that starts at the first element.
If the current element is smaller than previous element, swap them. 
Loop through entire array until the number of swaps is 0.

2.Find the min
Min equals the first element.

3.Find the max
Max equals the last element.

4.Find the median
Divide the largest element number by two (in this case, three)
(Return the data stored in the given element.)

5.Find the mean
Add all of the data in the elements once.
Divide by two.


Output: min,max, median, mean, min.
"""

20. Describe an algorithm for finding both the largest and the smallest integers in a finite
sequence of integers.

Make an array of integers

1.Sort the array
Begin a loop that starts at the first element.
If the current element is smaller than previous element, swap them.
Loop through entire array until the number of swaps is 0.

2.Find the min
Min equals the first element.

3.Find the max
Max equals the last element.


31. Devise an algorithm that finds the first term of a sequence
of integers that equals some previous term in the
sequence.

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    for i=1 to n
        for j=0 to i
            if L[i] == L[j]
                return L[i]
OUTPUT: First element that is duplicate with some previous element
"""
def number31(self):
    for i in range(0, len(self)):
        for j in range(0, i):
            if self[i] == self[j]:
                return self[i]

"""
32. Devise an algorithm that finds all terms of a finite sequence
of integers that are greater than the sum of all
previous terms of the sequence.

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    sum = 0
    temp = set
    for i=1 to n
        if L[i] > sum
            temp.add(L[i])
        sum += L[i]
    return temp
OUTPUT: A set containing all elements that are larger than the sum of previous
elements
"""

def number32(self):
    temp_sum = self[0]
    temp_set = set()
    for i in range(1, len(self)):
        if self[i] > temp_sum:
            temp_set.add(self[i])
        temp_sum += self[i]
    if temp_set != set():
        return temp_set
    else:
        return print("No elements meet conditions")
    
"""
33. Devise an algorithm that finds the first term of a sequence
of positive integers that is less than the immediately preceding
term of the sequence

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    for i=1 to n
        if self[i] < self[i-1]:
            return self[i]
        
OUTPUT: First element that is less than preceding element
"""

def number33(self):
    for i in range(1, len(self)):
        if self[i] < self[i-1]:
            return self[i]
        
 """
 41. Sort these lists using selection sort
 a)3,5,4,1,2....1,3,5,4,2....1,2,3,5,4....1,2,3,4,5
 b)5,4,3,2,1....1,5,4,3,2....1,2,5,4,3....1,2,3,5,4.....1,2,3,4,5
 c)na
 
 """
42. Write the selection sort algorithm in pseudocode

        
        
