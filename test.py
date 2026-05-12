import random
import time

def counting_sort(arr, max_val):
    """自實作 Counting Sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * (max_val + 1)

    # 1. 計算頻率
    for num in arr:
        count[num] += 1

    # 2. 累加位置
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # 3. 為了確保穩定性，從後往前放置 (downto)
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output

def counting_sort_for_radix(arr, exp):
    """供 Radix Sort 使用的位數 Counting Sort"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 依據目前的位數 (exp) 計算頻率
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 將排序結果寫回原陣列
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """自實作 Radix Sort (Base 10)"""
    max_val = max(arr)
    exp = 1
    # 依序對個位、十位、百位...進行排序
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

if __name__ == "__main__":
    # 產生 1,000,000 個 16-bit 整數 (範圍 0 ~ 65535)
    print("正在產生 1M 個 16-bit 整數資料...")
    data = [random.randint(0, 65535) for _ in range(1000000)]

    # 1. 測量 Python 內建 sorted()
    data_timsort = data.copy()
    start_time = time.time()
    sorted_timsort = sorted(data_timsort)
    timsort_time = time.time() - start_time
    print(f"Timsort (Python內建) 花費時間: {timsort_time:.4f} 秒")

    # 2. 測量自實作 Counting Sort
    data_counting = data.copy()
    start_time = time.time()
    sorted_counting = counting_sort(data_counting, 65535)
    counting_time = time.time() - start_time
    print(f"Counting Sort 花費時間:       {counting_time:.4f} 秒")

    # 3. 測量自實作 Radix Sort
    data_radix = data.copy()
    start_time = time.time()
    radix_sort(data_radix)
    radix_time = time.time() - start_time
    print(f"Radix Sort 花費時間:          {radix_time:.4f} 秒")