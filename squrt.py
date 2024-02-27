N = int(input("Enter value of N"))
if N == 1:
  print("Squrt of 1 is 1")
else:
  for i in range(2, N):
    if ((i * i) == N):
      print("Squrt of", N, "is", i)
      break
