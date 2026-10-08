'''🟢 Problem 3 — Contains Duplicate
Given:
numbers = [1, 2, 3, 4, 2]


Return:
True

because 2 occurs twice.
But:
[1, 2, 3, 4]


should return:
False

Challenge
Think of two approaches:
Approach A
Don't use a set.
Approach B
Use a set.
Then compare their complexity.
This is our first introduction to:
Trading space for time.'''

def contains_duplicate_1(numbers):
  for i in range(0,len(numbers)):
    num=numbers[i]
    for j in range(i+1,len(numbers)):
      if numbers[j]==num:
        return True
  return False

def contains_duplicate_2(numbers):
  seen = set()
  for num in numbers:
    if num in seen:
      return True
    seen.add(num)
  return False  

def main():
  numbers=[1,2,3,2]
  answer_1=contains_duplicate_1(numbers)
  print(f"Duplicates using method 1 :{answer_1}")
  answer_2=contains_duplicate_2(numbers)
  print(f"Duplicates using method 2 :{answer_2}")  
  
main()