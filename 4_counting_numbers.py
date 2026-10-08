'''🟡 Problem 4 — Frequency Counter
Input:
numbers = [2, 3, 2, 4, 3, 2]


Output:
{    2: 3,    3: 2,    4: 1}


Write:
def frequency_count(numbers):    ...


Don't use:
collections.Counter


Build the dictionary yourself.'''

def frequency_count(numbers):
  count={}
  for num in numbers:     
   if num in count:
     count[num]+=1
   else:
     count[num]=1
  return count  

def main():
  numbers={1,2,3,2,1,4}
  count_number=frequency_count(numbers)
  print(f"The count number are as follows :{count_number}")

main()