class Solution:
    def calculate(self, s: str) -> int:
        ops = []
        nums = []
        sign = 1
        res = 0
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                res += sign * num
                num = 0
                if c == '+': sign = 1
                elif c == '-': sign = -1
                elif c == '(':
                    ops.append(sign)
                    nums.append(res)
                    res = 0
                    sign = 1
                elif c == ')':
                    res = nums.pop() + res * ops.pop()
        return res + sign * num

    def calculateII(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        s = s.replace(' ', '') + ' '
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    n = stack.pop()
                    stack.append((-1 if n * num < 0 else 1) * (abs(n) // abs(num)))
                num = 0
                sign = c
        return sum(stack)

    def calculateIII(self, s: str) -> int:
        stack_num = []
        stack_opt = []
        i = 0
        priorty = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if '0' <= s[i] <= '9':
                j = i
                while i + 1 < len(s) and '0' <= s[i + 1] <= '9':
                    i += 1
                num = int(s[j:i + 1])
                stack_num.append(num)
            elif s[i] == '(':
                stack_opt.append(s[i])
            elif s[i] == ')':
                while stack_opt[-1] != '(':
                    opt = stack_opt.pop()
                    A = stack_num.pop()
                    B = stack_num.pop()
                    res = self.calc(A, B, opt)
                    stack_num.append(res)
                stack_opt.pop()
            else:
                while stack_opt and priorty[stack_opt[-1]] >= priorty[s[i]]:
                    opt = stack_opt.pop()
                    A = stack_num.pop()
                    B = stack_num.pop()
                    res = self.calc(A, B, opt)
                    stack_num.append(res)
                stack_opt.append(s[i])
            i += 1

        while stack_opt:
            opt = stack_opt.pop()
            A = stack_num.pop()
            B = stack_num.pop()
            res = self.calc(A, B, opt)
            stack_num.append(res)
        return stack_num[-1]

    def calc(self, num1, num2, opt):
        if opt == '+':
            return int(num1) + int(num2)
        elif opt == '-':
            return int(num2) - int(num1)
        elif opt == '*':
            return int(num2) * int(num1)
        elif opt == '/':
            return int(num2) // int(num1)