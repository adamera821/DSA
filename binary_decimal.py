def binary_decima(i):
    r = 0
    p = 1 
    for i in reversed(i):
      r = r + int(i)*p
      p = p*2
    print(r)

000010
