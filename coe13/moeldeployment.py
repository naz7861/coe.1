def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) < 2:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        merged, split_inv = merge(left, right)
        return merged, left_inv + right_inv + split_inv

    def merge(left, right):
        merged = []
        i = j = inversions = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, inversion_count = merge_sort(arr)
    return inversion_count
