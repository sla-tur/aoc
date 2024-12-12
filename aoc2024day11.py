def blink(elem, count, n, memo):

  if count >= n:
    return elem
  count += 1

  if elem in memo.keys():
    return blink(memo[elem], count+1, memo)
  elif len(str(elem)) % 2 == 0:
    middle_element = str(elem)[len(str(elem))//2]
    memo[elem] = blink(int(middle_element),)
    return blink(int(middle_element),count, n, memo)
    
  