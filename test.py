from collections import Counter
import numpy as np
import random

def analyze_colors():
    color_data = {
        "Monday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", 
                   "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        "Tuesday": ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED",
                    "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
        "Wednesday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", 
                      "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
        "Thursday": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", 
                     "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
        "Friday": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", 
                   "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
    }

    all_colors = [color for colors in color_data.values() for color in colors]
    color_counts = Counter(all_colors)

    mean_occurrence = np.mean(list(color_counts.values()))
    mean_color = min(color_counts, key=lambda color: abs(color_counts[color] - mean_occurrence))
    
    most_worn_color = color_counts.most_common(1)[0][0]
    
    sorted_counts = sorted(color_counts.items(), key=lambda x: x[1])
    median_color = sorted_counts[len(sorted_counts) // 2][0]
    
    variance = np.var(list(color_counts.values()))
    
    prob_red = color_counts["RED"] / sum(color_counts.values())
    
    return mean_color, most_worn_color, median_color, variance, prob_red

def recursive_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, right)
    else:
        return recursive_search(arr, target, left, mid - 1)

def binary_to_decimal():
    binary_number = ''.join(str(random.randint(0, 1)) for _ in range(4))
    return binary_number, int(binary_number, 2)

def fibonacci_sum(n=50):
    a, b = 0, 1
    sum_fib = 0
    for _ in range(n):
        sum_fib += a
        a, b = b, a + b
    return sum_fib

if __name__ == "__main__":
    mean_color, most_worn_color, median_color, variance, prob_red = analyze_colors()
    binary_number, decimal_value = binary_to_decimal()
    sum_fib_50 = fibonacci_sum()
    
    print(f"Mean Color: {mean_color}")
    print(f"Most Worn Color: {most_worn_color}")
    print(f"Median Color: {median_color}")
    print(f"Variance of Colors: {variance:.2f}")
    print(f"Probability of Picking Red: {prob_red:.2%}")
    print(f"Random 4-Digit Binary: {binary_number} (Base 10: {decimal_value})")
    print(f"Sum of First 50 Fibonacci Numbers: {sum_fib_50}")
