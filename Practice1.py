def buycheapest(rice_prices):
    def cheapest_price(rice_prices):
        if len(rice_prices) == 1:
            return rice_prices[0]
        elif rice_prices[0] <= rice_prices[1]:
            return cheapest_price(rice_prices[:1] + rice_prices[2:])
        elif rice_prices[0] > rice_prices[1]:
            return cheapest_price(rice_prices[1:])

    def rest_of_the_prices(rice_prices, cheapest):
        if rice_prices == ():
            return ()
        elif rice_prices[0] == cheapest:
            return (rice_prices[0],) + rest_of_the_prices(rice_prices[1:], cheapest)
        
    return (cheapest_price(rice_prices),) + (rest_of_the_prices(rice_prices, cheapest_price(rice_prices)),)