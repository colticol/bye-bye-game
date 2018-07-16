import random

def main():
  total = 0
  num = 10000000
  max_money = 0
  for i in range(num):
    money = 1
    while random.choice([True, False]):
      money *= 2
    total += money
    max_money = max(money, max_money)
  print float(total) / num
  print max_money

if __name__ == '__main__':
  main()
