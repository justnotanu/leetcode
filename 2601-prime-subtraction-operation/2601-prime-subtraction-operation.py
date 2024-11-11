class Solution:
    def sieve_of_eratosthenes(self, max_val: int) -> List[int]:
        sieve = [True] * (max_val + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for i in range(2, int(max_val**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_val + 1, i):
                    sieve[j] = False

        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        return primes

    def primeSubOperation(self, nums: List[int]) -> bool:
        max_val = max(nums)
        primes = self.sieve_of_eratosthenes(max_val)

        for i in range(len(nums)):
            # Calculate the difference needed
            diff = nums[i] - 1 if i == 0 else nums[i] - nums[i - 1] - 1
            
            # Find the largest prime less than or equal to diff
            lb = self.lower_bound(primes, diff)

            if lb == len(primes) or primes[lb] > diff:
                lb -= 1
            
            if lb < 0:
                # If we can't find a suitable prime
                if i == 0 or nums[i] > nums[i - 1]:
                    continue
                else:
                    return False
            
            # Subtract the prime from nums[i]
            nums[i] -= primes[lb]
        
        return True

    def lower_bound(self, primes: List[int], key: int) -> int:
        low, high = 0, len(primes)
        while low < high:
            mid = (low + high) // 2
            if primes[mid] < key:
                low = mid + 1
            else:
                high = mid
        return low  # Return the index of the first element >= key
            