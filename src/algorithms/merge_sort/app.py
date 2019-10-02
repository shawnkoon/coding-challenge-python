from typing import List


class MergeSort:
    """
    Source : Practice

    Implement MergeSort.

    Before_array : [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

    After_array : [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    """

    def merge_sort(self, array):
        if len(array) == 1:
            return array

        mid = len(array) // 2  # 5 -> 2 , 4 -> 2

        l_array = array[:mid]
        r_array = array[mid:]

        return self.merge(self.merge_sort(l_array), self.merge_sort(r_array))

    def merge(self, left_array, right_array):
        l = r = 0
        res = []

        while True:
            if l >= len(left_array):
                return res + right_array[r:]

            if r >= len(right_array):
                return res + left_array[l:]

            if left_array[l] < right_array[r]:
                res.append(left_array[l])
                l += 1
            else:
                res.append(right_array[r])
                r += 1
