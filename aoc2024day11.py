def blink(elem, count, n, memo):

  if count >= n:
    return elem
  count += 1

  if elem in memo.keys():
    return blink(memo[elem], count+1, memo)
  elif len(str(elem)) % 2 == 0:
    mid = len(str(elem))//2
    left = int(str(elem)[:mid])
    right = int(str(elem)[mid:])
    memo[elem] = blink(left, count, n, memo), blink(right, count, n, memo)
    
  