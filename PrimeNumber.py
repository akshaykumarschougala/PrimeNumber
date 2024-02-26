n = int(input("Number "))
if n == 1:
  print("not a prime number")
else:
  for i in range(2, n):
    if (n % i == 0):
      print("not a prime nubmer")
      break
    else:
      print(n, "is a prime number")
      break
