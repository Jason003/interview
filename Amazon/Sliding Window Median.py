'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
'''
'''
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        Comparator<Integer> comparator = new Comparator<>(){
             public int compare(Integer a, Integer b) {
                if (nums[a] != nums[b]) {
                    return Integer.compare(nums[a], nums[b]);
                }
                else {
                    return a - b;
                }
            } 
        };
        TreeSet<Integer> left = new TreeSet<>(comparator.reversed());
        TreeSet<Integer> right = new TreeSet<>(comparator);
        double[] res = new double[nums.length - k + 1];

        for (int i = 0; i < k; i++) {
            left.add(i);
        }
        balance(left, right);
        res[0] = getMedian(k, nums, left, right);

        int r = 1;
        for (int i = k; i < nums.length; i++) {
            if(!left.remove(i - k)) {
                right.remove(i - k);
            }
            right.add(i); 
            left.add(right.pollFirst());
            balance(left, right); 
            res[r] = getMedian(k, nums, left, right);
            r++;
        }

        return res;
    }
    
    private void balance(TreeSet<Integer> left, TreeSet<Integer> right) {
        while (left.size() > right.size()) {
            right.add(left.pollFirst());
        }
    }
    
    private double getMedian(int k, int[] nums, TreeSet<Integer> left, TreeSet<Integer> right) {
        if (k % 2 == 0) {
            return ((double) nums[left.first()] + nums[right.first()]) / 2;
        }
        else {
            return (double) nums[right.first()];
        }
    }
}
'''