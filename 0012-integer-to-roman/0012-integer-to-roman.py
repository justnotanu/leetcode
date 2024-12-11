class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mapping of integer values to Roman numerals
        val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        roman_numeral = ""
        
        # Iterate through the value map
        for value, symbol in val_map:
            while num >= value:
                roman_numeral += symbol  # Append symbol
                num -= value              # Subtract value from num
        
        return roman_numeral
