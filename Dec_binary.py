def dec_binary(in_put):
  if in_put == 0:
    return 0
  res = ""
  while in_put > 0:
    res = res + str(in_put%2)
    in_put = in_put//2
  res = res[::-1]
