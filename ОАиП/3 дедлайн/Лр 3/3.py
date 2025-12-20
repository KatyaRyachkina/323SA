def binary_search(arr: list, target: int, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50, 60, 70]
    print(binary_search(my_list, 40))
    print(binary_search(my_list, 99))
