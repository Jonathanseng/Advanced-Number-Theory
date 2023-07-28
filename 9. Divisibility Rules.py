def is_divisible_by_2(n):
  """Returns True if n is divisible by 2, False otherwise."""
  return n % 2 == 0

def is_divisible_by_3(n):
  """Returns True if n is divisible by 3, False otherwise."""
  sum_of_digits = 0
  while n > 0:
    sum_of_digits += n % 10
    n //= 10
  return sum_of_digits % 3 == 0

def is_divisible_by_4(n):
  """Returns True if n is divisible by 4, False otherwise."""
  return n % 4 == 0

def is_divisible_by_5(n):
  """Returns True if n is divisible by 5, False otherwise."""
  return n % 5 == 0

def is_divisible_by_6(n):
  """Returns True if n is divisible by 6, False otherwise."""
  return is_divisible_by_2(n) and is_divisible_by_3(n)

def is_divisible_by_7(n):
  """Returns True if n is divisible by 7, False otherwise."""
  sum_of_digits = 0
  while n > 0:
    sum_of_digits += n % 10
    n //= 10
  if sum_of_digits % 7 == 0:
    return True
  else:
    return False

def main():
  n = 15
  print(is_divisible_by_2(n))
  print(is_divisible_by_3(n))
  print(is_divisible_by_4(n))
  print(is_divisible_by_5(n))
  print(is_divisible_by_6(n))
  print(is_divisible_by_7(n))

if __name__ == "__main__":
  main()
