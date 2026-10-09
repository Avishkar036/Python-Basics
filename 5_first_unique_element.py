'''🟡 Problem 5 — First Unique Element
Given:
numbers = [4, 5, 1, 2, 1, 5, 4]


Return:
2

Because:
4 → duplicate
5 → duplicate
1 → duplicate
2 → unique

Think carefully.
You may need to combine:
List
+
Dictionary'''

def first_unique_element(numbers):
  counter={}
  for num in numbers:
    if num  in counter:
      counter[num]+=1
    else:
      counter[num]=1
  for k,v in counter.items():
    if v==1:
      unique=k
      break
  if unique== None:
    return None
  return unique