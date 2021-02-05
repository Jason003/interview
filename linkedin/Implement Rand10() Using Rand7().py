class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        res = 40
        # generate uniform distribution on [0, 39]
        while res >= 40:
            res = (rand7() - 1) * 7 + (rand7() - 1)
        return res % 10 + 1

'''
Idea: rand7() -> rand49() -> rand40() -> rand10()

Think of rand7() as having a 7 sided die.
Since we need rand10() (a 10 sided die) and 10 is greater than 7, we need to roll the 7 sided die multiple times.
Rolling the 7 sided die twice yields 49 different combinations:
(1,1)
(1,2)
(1,3)
...
(7,7)

Now we need to distinguish between these 49 different outcomes somehow. How can we map our two 7 sided die rolls to these different outcome numbers (1-49)?
The first thing that comes to mind is to multiply the two numbers in each tuple together. But that results in a non-uniform distribution because you would get
(1,1) = 1
(1,2) = 2
(2,1) = 2
See how the outcome of "2" has a chance of appearing twice, whereas the outcome of "1" has a chance of appearing once? This is because multiplication does not care about order.

One way to fix this problem is to think of each dice roll as the row/col of a 7x7 matrix.

  1  2  3  4  5  6  7
1
2
3
4
5
6
7
So position (1,1) maps to outcome 1.
Position (1,2) maps to outcome 2.
...
Position (1,7) maps to outcome 7.
Position (2,1) maps to outcome 8.
How do we get this number using math for a given (x,y) position?
7(x-1) + y

So why does OP do 7(x-1) + (y-1) ?
Because it makes %10 cleaner. Instead of making the outcome space 1-49. The OP makes it 0-48.

public int rand10() {
    int result = 40;
    while (result >= 40) {result = 7 * (rand7() - 1) + (rand7() - 1);}
    return result % 10 + 1;
}
Time Complexity
The total number of iterations follows geometric distribution. For each iteration in the while loop, the probabilty of exiting the loop is p = 40/49. So the average time complexity T(n) = O(1/p) = O(49/40) = O(1).

Correctness
Note that rand49() generates a uniform random integer in [1, 49], so any number in this range has the same probability to be generated. Suppose k is an integer in range [1, 40], P(rand49() = k) = 1/49

   P(result = k)
= P(rand49() = k in the 1st iteration) +
   P(rand49() > 40 in the 1st iteration) * P(rand49() = k in the 2nd iteration) +
   P(rand49() > 40 in the 1st iteration) * P(rand49() > 40 in the 2nd iteration) * P(rand49() = k in the 3rd iteration) +
   P(rand49() > 40 in the 1st iteration) * P(rand49() > 40 in the 2nd iteration) * P(rand49() > 40 in the 3rd iteration) * P(rand49() = k in the 4th iteration) +
   ...
= (1/49) + (9/49) * (1/49) + (9/49)^2 * (1/49) + (9/49)^3 * (1/49) + ...
= (1/49) * [1 + (9/49) + (9/49)^2 + (9/49)^3 + ... ]
= (1/49) * [1/(1-9/49)]
= (1/49) * (49/40)
= 1/40

Generalization
Implement randM() using randN() when M > N:
Step 1: Use randN() to generate randX(), where X >= M. In this problem, I use 7 * (rand7() - 1) + (rand7() - 1) to generate rand49() - 1.
Step 2: Use randX() to generate randM(). In this problem, I use rand49() to generate rand40() then generate rand10.

Note: N^b * (randN() - 1) + N^(b - 1) * (randN() - 1) + N^(b - 2) * (randN() - 1) + ... + N^0 * (randN() - 1) generates randX() - 1, where X = N^(b + 1).

More Examples
(1) Implement rand11() using rand3():

public int rand11() {
    int result = 22;
    while (result >= 22) {result = 3 * 3 * (rand3() - 1) + 3 * (rand3() - 1) + (rand3() - 1);}
    return result % 11 + 1;
}
Idea: rand3() -> rand27() -> rand22 -> rand11
Time Comlexity: O(27/22)

(2) Implement rand9() using rand7():

public int rand9() {
    int result = 45;
    while (result >= 45) {result = 7 * (rand7() - 1) + (rand7() - 1);}
    return result % 9 + 1;
}
Idea: rand7() -> rand49() -> rand45() -> rand9()
Time Comlexity: O(49/45)

(3) Implement rand13() using rand6():

public int rand13() {
    int result = 26;
    while (result >= 26) {result = 6 * (rand6() - 1) + (rand6() - 1);}
    return result % 13 + 1;
}
Idea: rand6() -> rand36() -> rand26 -> rand13()
Time Comlexity: O(36/26)
'''