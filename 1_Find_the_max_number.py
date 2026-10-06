'''🟢 Problem 1 — Find Maximum
Write:
def find_max(numbers):    ...


Example:
Input:  [4, 8, 2, 10, 5]
Output: 10

Your task
Don't use:
max(numbers)


Implement it yourself.
Also tell me:
Time Complexity:O(n)
Space Complexity:
'''

def find_max(numbers):
  if not numbers:
    return None
  max=numbers[0]
  for i in numbers:
     if i>max:
      max=i
  return max
  
def main():
  numbers=[1,5,6,81,19]
  maximum=find_max(numbers)
  print(f"The maximum number is : {maximum}")

main()