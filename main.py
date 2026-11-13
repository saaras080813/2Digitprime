# Loop through all 2-digit numbers (from 10 to 99)
for num in range(10, 100):
  # Assume the number is prime until proven otherwise
  is_prime = True

  # Check if 'num' can be divided evenly by any number from 2 up to num - 1
  for i in range(2, num):
    if num % i == 0:
      is_prime = False
      break  # Stop checking once a factor is found

  # If no factors were found, print the prime number
  if is_prime:
    print(num, end=" ")
