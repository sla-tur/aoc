file = open("aoc2024day11test.txt", "r")
lst = [int(i) for i in file.readline().split()]
print(lst)

def blink(elem, count, memo):
  global sum
  print(elem)

  if count == 25:
    print("Count reached!")
    return elem
  else:
    count += 1
    if elem in memo.keys():
      print(f"{count}:{elem} in memo: {memo[elem]}")
      blink(memo[elem], count, memo)
    if len(str(elem)) % 2 == 0:
      index = len(str(elem))//2
      left = int(str(elem)[:index])
      right = int(str(elem)[index:])
      sum += 1
      print(f"Left part of {elem}")
      memo.update({left: blink(left, count, memo)})
      print(f"Right part of {elem}")
      memo.update({right: blink(right, count, memo)})
    else:
      #print(f"{count}:{elem}: 2024 operation")
      memo.update({elem: blink(elem*2024, count, memo)})

memo = {0:1}
sum = len(lst)
for i in lst:
  print(f"Now on element {i}:")  
  blink(i, 0, memo)

print(sum)