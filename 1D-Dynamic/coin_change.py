class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def calcChange(cur_amount):
            if cur_amount == 0:
                return 0
            if cur_amount in cache:
                return cache[cur_amount]

            minNumCoins = amount + 1
            for coin in coins:
                if cur_amount - coin >= 0:
                    minNumCoins = min(minNumCoins, 1 + calcChange(cur_amount - coin))
            cache[cur_amount] = minNumCoins 
            return minNumCoins
        
        minCoins = calcChange(amount)
        return -1 if minCoins >= amount + 1 else minCoins