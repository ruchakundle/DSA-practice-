"""
Problem: Maximum Profit from Stock Prices

Ratan is a lucky investor who buys low and sells high. Given an array of stock prices where each element represents the price on a given day, return the maximum profit Ratan can achieve.

Rules:
- He can buy only once and sell only once
- Buying must happen before selling
- If no profit is possible, return 0

Example:
Input: [1, 9, 2, 11, 1, 9, 2]
Output: 10 (Buy at 1, sell at 11)
"""

n = int(input("enter no. of days : "))
prices = list(map(int,input("enter prices per day :").split()))

min_price = float('inf')
max_price = 0

for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_price:
        max_price = price - min_price
        
        
print("the max profit is",max)        