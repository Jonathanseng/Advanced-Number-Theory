def factorial(n):
  """Returns the factorial of n."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def is_even(n):
  """Returns True if n is even, False otherwise."""
  if n % 2 == 0:
    return True
  else:
    return False

def mathematical_induction(n):
  """Returns True if n is even for all integers n >= 0, False otherwise."""
  base_case = is_even(0)
  if not base_case:
    return False
  inductive_step = True
  for i in range(1, n + 1):
    if not is_even(i):
      inductive_step = False
      break
  return base_case and inductive_step

def main():
  n = 10
  is_even_n = mathematical_induction(n)
  print(is_even_n)

if __name__ == "__main__":
  main()
