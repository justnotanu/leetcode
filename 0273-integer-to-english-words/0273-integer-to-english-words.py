class Solution:
    def __init__(self):
        # Unordered maps to store words for numbers less than 10, 20, and 100
        self.belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def solve(self, num: int) -> str:
        if num < 10:
            return self.belowTen[num]

        if num < 20:
            return self.belowTwenty[num - 10]

        if num < 100:
            return self.belowHundred[num // 10] + ((" " + self.belowTen[num % 10]) if num % 10 != 0 else "")

        if num < 1000:
            return self.solve(num // 100) + " Hundred" + ((" " + self.solve(num % 100)) if num % 100 != 0 else "")

        if num < 1000000:
            return self.solve(num // 1000) + " Thousand" + ((" " + self.solve(num % 1000)) if num % 1000 != 0 else "")

        if num < 1000000000:
            return self.solve(num // 1000000) + " Million" + ((" " + self.solve(num % 1000000)) if num % 1000000 != 0 else "")

        return self.solve(num // 1000000000) + " Billion" + ((" " + self.solve(num % 1000000000)) if num % 1000000000 != 0 else "")

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        return self.solve(num).strip()
