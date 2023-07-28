def modular_addition(a, b, m):
  """Returns the modular addition of a and b modulo m."""
  return (a + b) % m

def modular_subtraction(a, b, m):
  """Returns the modular subtraction of a and b modulo m."""
  return (a - b) % m

def modular_multiplication(a, b, m):
  """Returns the modular multiplication of a and b modulo m."""
  return (a * b) % m

def modular_exponentiation(a, b, m):
  """Returns the modular exponentiation of a and b modulo m."""
  result = 1
  for i in range(b):
    result = modular_multiplication(result, a, m)
  return result

def main():
  a = 10
  b = 5
  m = 15
  print(modular_addition(a, b, m))
  print(modular_subtraction(a, b, m))
  print(modular_multiplication(a, b, m))
  print(modular_exponentiation(a, b, m))

if __name__ == "__main__":
  main()
