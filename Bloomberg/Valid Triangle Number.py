def triangleNumber(nums) -> int:
    nums.sort()
    res = 0
    for k in range(len(nums)):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                res += j - i
                j -= 1
            else:
                i += 1
    return res


# follow up: what if we want to get non-repeated triples?
# get triangles with 3 equal edges, 2 equal edges and no equal edges
import collections


def triangleNumber2(nums):
    cnt = collections.Counter(nums)
    three_equal = sum(v >= 3 for v in cnt.values())
    two_equal = 0
    for i in cnt:
        if cnt[i] >= 2:
            for j in cnt:
                if i * 2 > j and j != i:
                    two_equal += 1
    return three_equal + two_equal + triangleNumber(list(cnt.keys()))


print(triangleNumber2([2, 2, 2, 2, 3, 4]))
