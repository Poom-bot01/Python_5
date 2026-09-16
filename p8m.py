import p8f

if __name__ == "__main__":
  n, k = input("Enter n and k: ").split()
  n = int(n); k = int(k)
  CnK = (p8f.fact(n)) / (p8f.fact(k) * p8f.fact(n-k))
  print(f"C({n},{k}) = {Cnk}")
