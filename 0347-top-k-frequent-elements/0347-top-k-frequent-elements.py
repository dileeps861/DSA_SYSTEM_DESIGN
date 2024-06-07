class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        numsValues = list(counts.keys())
        n = len(numsValues)

        def partition(low, high, pivot_index):
            pivot_frequency = counts[numsValues[pivot_index]]
            # Move pivot to end
            numsValues[pivot_index], numsValues[high] = (
                numsValues[high],
                numsValues[pivot_index],
            )
            store_index = low
            for i in range(low, high):
                if counts[numsValues[i]] < pivot_frequency:
                    numsValues[store_index], numsValues[i] = (
                        numsValues[i],
                        numsValues[store_index],
                    )
                    store_index += 1
            # Move pivot to its final place
            numsValues[store_index], numsValues[high] = (
                numsValues[high],
                numsValues[store_index],
            )
            return store_index

        def quickselect(low, high, k_smallest):
            if low == high:
                return
            pivot_index = random.randint(low, high)
            pivot_index = partition(low, high, pivot_index)
            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(low, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, high, k_smallest)

        quickselect(0, n - 1, n - k)
        return numsValues[n - k:]
