#Our cute and adorable walrus operator :=
a = "Helloooooooo!"

if ((n := len(a)) > 10):
  print(f"too long {n} elements")

#Removing letters 
while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]
print(a)