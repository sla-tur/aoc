def blink(elem, count, n, memo):

  if count >= n:
    return elem
  count += 1

  if elem in memo.keys():
    for 
      return memo[elem]
  
  else:
    if len(str(elem)) % 2 == 0:
      mid = len(str(elem))//2
      left = int(str(elem)[:mid])
      right = int(str(elem)[mid:])
      memo[elem] = blink(left, count, n, memo), blink(right, count, n, memo)
    else:
      memo[elem] = blink(elem*2024, count, n, memo)
    
file = open("aoc2024day11test.txt", "r")
lst = [int(elem) for elem in file.readline().split()]
print(lst)

for i in range(len(lst)):
  lst[i] = blink(lst[i], 0, 1, {0: 1})

print(lst)