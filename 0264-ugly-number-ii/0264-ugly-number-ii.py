class Solution:
    def nthUglyNumber(self, n: int) -> int:
        t = [0] * (n + 1)  # Initialize the array to store ugly numbers
        t[1] = 1  # The first ugly number is 1

        i2, i3, i5 = 1, 1, 1  # Pointers for 2, 3, and 5

        for i in range(2, n + 1):
            i2th_ugly = t[i2] * 2
            i3rd_ugly = t[i3] * 3
            i5th_ugly = t[i5] * 5

            # The next ugly number is the minimum of the three candidates
            t[i] = min(i2th_ugly, i3rd_ugly, i5th_ugly)

            # Increment the pointers based on which candidate was used
            if t[i] == i2th_ugly:
                i2 += 1
            if t[i] == i3rd_ugly:
                i3 += 1
            if t[i] == i5th_ugly:
                i5 += 1

        return t[n]  # Return the nth ugly number
