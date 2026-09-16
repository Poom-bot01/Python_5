def fact(x):
  #x * x-1 * x-2 * ... * x - n
  fact_val = 1
  for i in range(x,0,-1):
    fact_val = fac_val * i
  return fact_val
if __name__ == "__main__":
  print(fact(80))
  print(fact(5))
