class Solution:
    def numberToWords(self, num: int) -> str:
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def helper(n):  # deal with the number less than 1000
            if n == 0:
                return ''
            if n < 20:
                return LESS_THAN_20[n]
            if n < 100:
                return TENS[n // 10] + ' ' + LESS_THAN_20[n % 10]
            return LESS_THAN_20[n // 100] + ' Hundred ' + helper(n % 100)

        if num == 0:
            return 'Zero'
        i = 0f
        res = ''
        while num:
            if num % 1000:
                res = helper(num % 1000) + ' ' + THOUSANDS[i] + ' ' + res
            i += 1
            num //= 1000
        return ' '.join(res.split())
