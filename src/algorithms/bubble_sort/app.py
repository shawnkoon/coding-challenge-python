from typing import List


class BubbleSort:
    """
    Source : Practice

    Create Bubble sort algorithm.

    Before_array : [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

    After_array : [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    """

    def sort(self, ara: List[int]):
        for i in range(len(ara)):  # 0 1 2
            for j in range(1, len(ara) - i):  # 3 2 1*
                if ara[j] < ara[j - 1]:
                    ara[j - 1], ara[j] = ara[j], ara[j - 1]
