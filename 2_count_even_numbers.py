'''Problem 2 — Count Even Numbers
Write:
def count_even(numbers):    ...


Example:
Input:
[1, 2, 3, 4, 6, 7]

Output:
3

Think about:
How many times do you need to inspect an element?'''

def count_even(numbers):
  counter = 0
  if not numbers:
    return counter
  for i in numbers:
    if i%2==0:
      counter +=1
  return counter

def main():
  numbers=[12,33,56,88,99]
  answer= count_even(numbers)
  print(f"Count of Even numbers is:{answer}")
  
main()