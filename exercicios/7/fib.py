n = int(input("Digite um número: "))

def fib(num):
  if num <=1:
    return num

  return fib(num-1)+fib(num-2)

print(fib(n))

print("Sequência:")
for i in range(n+1):
  print(fib(i))