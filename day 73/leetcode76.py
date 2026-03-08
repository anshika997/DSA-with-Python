class StockSpanner:
    def __init__(self):
        self.stack = []   # stack will store (price, span)

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span


# prices given
prices = [100, 80, 60, 70, 60, 75, 85]

spanner = StockSpanner()

for price in prices:
    print(spanner.next(price))