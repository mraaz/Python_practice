def main():
    stock_prices = [10, 7, 11, 8, 1, 22]
    #stock_prices = [10, 7, 5, 8, 11, 9]

    cur_lowest_stock_price = float('inf')
    foundLowStock = False
    cur_highest_stock_price = 0
    
    LowestStock = float('inf')
    HighestStock = 0
    
    for x in range(len(stock_prices)-1):
        if stock_prices[x] < cur_lowest_stock_price:
            cur_lowest_stock_price = stock_prices[x]
            foundLowStock = True
            cur_highest_stock_price = 0
        
        if foundLowStock:
            if stock_prices[x+1] > cur_highest_stock_price:
                cur_highest_stock_price = stock_prices[x+1]
        
        if (cur_highest_stock_price - cur_lowest_stock_price) > (HighestStock - LowestStock):
            HighestStock = cur_highest_stock_price
            LowestStock = cur_lowest_stock_price
            

    profit  = HighestStock - LowestStock
    print("Best time to buy is %s and best time to sell is %s with a profit of $%s" % (LowestStock, HighestStock, profit))
 
 
if __name__ == "__main__":
    main()


https://www.interviewcake.com/question/python/stock-price