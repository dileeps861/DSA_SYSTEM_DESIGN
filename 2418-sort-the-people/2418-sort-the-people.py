class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped_height = zip(heights, names)
        sorted_names = sorted(zipped_height)
        sorted_names = sorted_names[::-1]
        return [name for _, name in sorted_names]
