"""
Problem 1 - A stock trader wants to trade in securities
that match certain conditions. For some securities,
it would be if it crosses a limit value, for some if
it goes below the limit value (possibly for shorting).

You are given a dictionary of securities and their
limit values and a condition as a dictionary.

The problem is to idiomatically solve the problem of
which securities he needs to buy according to his
conditions.
"""

# Stocks of interest
stocks = ['REL','INF','GLB','ACC','JIN','TRA','PAC']

# His conditions, given as the dictionary entry
# 'SYMBOL': (limit value, comparison operator)

stock_limits = {'REL' : (1200, '>='),
                'INF': (2500, '>'),
                'GLB': (850, '<'),
                'ACC': (1330, '=='),
                'JIN': (720, '<='),
                'TRA': (1800, '>='),
                'PAC': (95, '>')}

# Input - Current Market Price of the securities
stock_prices = {'REL': 1222,
                'INF': 2312,
                'GLB': 829,
                'ACC': 1335,
                'JIN': 755,
                'TRA': 1889,
                'PAC': 85}


# Problem - Get the list of securities he should trade on.

# Here is a basic implementation
def stocks_to_trade(conditions, prices):
    """ Find stocks to trade in """

    stocks = []
    
    for stock in conditions:
        limit, check = conditions[stock]
        # Apply the condition - Use operator module to
        # match the string to the condition
        price = prices[stock]
        ok = eval('%d %s %d' % (price, check, limit))
        
        if ok:
            stocks.append(stock)

    print 'Stocks to trade are',stocks

if __name__ == "__main__":
    stocks_to_trade(stock_limits, stock_prices)


