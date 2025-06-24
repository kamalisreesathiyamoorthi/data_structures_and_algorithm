class SortingAlgorithms:

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            swap = False
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap = True
            if not swap:
                break
        return arr

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def merge(self, arr, start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i = j = 0
        k = start
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def merge_sort(self, arr, start, end):
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(arr, start, mid)
            self.merge_sort(arr, mid + 1, end)
            self.merge(arr, start, mid, end)

    def partition(self, arr, start, end):
        pivot = arr[start]
        i = start
        j = end
        while i < j:
            while i <= end and arr[i] <= pivot:
                i += 1
            while j >= start and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[j] = arr[j], arr[start]
        return j

    def quick_sort(self, arr, start, end):
        if start < end:
            q = self.partition(arr, start, end)
            self.quick_sort(arr, start, q - 1)
            self.quick_sort(arr, q + 1, end)

    def max_heapify(self, arr, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest, n)

    def build_max_heap(self, arr, n):
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(arr, i, n)

    def heap_sort(self, arr):
        n = len(arr)
        self.build_max_heap(arr, n)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.max_heapify(arr, 0, i)
        return arr


# ✅ Example usage
if __name__ == "__main__":
    arr = [90, 98, 78, 35, 45, -100, 9, -12, 23, 41, 100]

    sorter = SortingAlgorithms()

    # Uncomment any one to test:
    # sorter.bubble_sort(arr)
    # sorter.selection_sort(arr)
    # sorter.insertion_sort(arr)
    # sorter.merge_sort(arr, 0, len(arr) - 1)
    # sorter.quick_sort(arr, 0, len(arr) - 1)
    sorter.heap_sort(arr)

    print("Sorted array:", arr)
