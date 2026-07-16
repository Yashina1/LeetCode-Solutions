class Solution(object):
    def intersect(self, nums1, nums2):
        d = {}
        res = []

        for num in nums1:
            d[num] = d.get(num, 0) + 1

        for num in nums2:
            if d.get(num, 0) > 0:
                res.append(num)
                d[num] -= 1

        return res
        
