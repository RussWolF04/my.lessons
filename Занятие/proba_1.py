sm = int(input())

coins = [1, 5, 10, 25]

ls = [0] * (sm+1)

for i in range(1, sm+1):

   ls[i] = float('inf')

   for coin in coins:

       if coin <= i:

           ls[i] = min(ls[i], ls[i-coin]+1)

print(ls[-1])