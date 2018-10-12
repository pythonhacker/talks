import itertools
import operator

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

def stocks_to_trade(conditions, prices):
    """ Find stocks to trade in """

    # Mapping to operator
    functions = {'>=': operator.ge,
                 '>': operator.gt,
                 '<': operator.lt,
                 '==': operator.eq,
                 '<=': operator.le}

    # Make it easy to write code!
    f, c, p = functions, conditions, prices
    selectors = {stock: f[c[stock][1]](p[stock],c[stock][0]) for stock in prices}
    return list(itertools.compress(selectors.keys(), selectors.values()))

if __name__ == "__main__":
    print 'Stocks to trade are',stocks_to_trade(stock_limits, stock_prices)
    
