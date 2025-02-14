'''
Optimized Approach
- Store prefix product values in self.products list and track cumulative product till now using self.product.
- Handle zeros efficiently: If a zero is added, reset self.products and self.product since any subsequent product involving zero would be invalid.
- Retrieve product in O(1) time using division (products[-1] / products[-k-1]) to get the product of the last k elements instead of recalculating from scratch.
    - If k exceeds available numbers, return 0.

Complexity
Time complexity: O(1)
Space complexity: O(N) in worst case, O(1) if frequent resets occur
'''
class ProductOfNumbers:
    def __init__(self):
        self.products = []
        self.product = 1

    def add(self, num: int) -> None:
        if num:
            self.product *= num
            self.products.append(self.product)
        else: #when num == 0
            self.products = []
            self.product = 1
            
    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0 
        elif k == len(self.products):
            return self.products[-1]
        else:
            return int(self.products[-1]/self.products[-1-k])
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

'''
Brute Force Approach
- Maintain a list (self.data) to store all added numbers.
- Appends num to self.data.
- To retrieve product, slice the last k elements from self.data.

Complexity
Time complexity: O(k)
Space complexity: O(N)
'''
class ProductOfNumbers:
    def __init__(self):
        self.data = []

    def add(self, num: int) -> None:
        self.data.append(num)
        return None

    def getProduct(self, k: int) -> int:
        product = prod(self.data[-k : ])
        return product
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

