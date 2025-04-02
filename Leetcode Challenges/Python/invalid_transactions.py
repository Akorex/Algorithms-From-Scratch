"""
Solution to Leetcode problem #1169 - Invalid Transactions

https://leetcode.com/problems/invalid-transactions/description/

"""
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        transactions_data = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            transactions_data.append((name, int(time), int(amount), city, transaction))


        for i, (name1, time1, amount1, city1, original1) in enumerate(transactions_data):
            if amount1 > 1000:
                ans.append(original1)
                continue

            for j, (name2, time2, amount2, city2, original2) in enumerate(transactions_data):
                if i != j and name1 == name2 and city1 != city2 and abs(time1-time2) <= 60:
                    ans.append(original1)
                    break





        return ans