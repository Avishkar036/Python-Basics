'''🟡 Problem 6 — Reverse a List
Implement:
def reverse_list(numbers):    ...


Example:
Input:
[1, 2, 3, 4, 5]

Output:
[5, 4, 3, 2, 1]

Constraint
First solve it without:
numbers.reverse()


or:
numbers[::-1]


We'll later revisit this problem using two pointers.'''

def reverse_list(numbers):
  reversed_num=[]
  for i in range(len(numbers)-1,-1,-1):
     reversed_num.append(numbers[i])
  return reversed_num

def main():
  numbers=[1,2,3,4,5]
  reversed=reverse_list(numbers)
  print(f'Reversed list is {reversed}')