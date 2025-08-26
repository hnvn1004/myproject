# test_complex.py
import random

# Hàm tính factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Hàm tạo danh sách ngẫu nhiên
def generate_numbers(count, start=1, end=50):
    return [random.randint(start, end) for _ in range(count)]

# Hàm tính tổng số chẵn và lẻ
def even_odd_summary(numbers):
    summary = {"even": 0, "odd": 0}
    for n in numbers:
        if n % 2 == 0:
            summary["even"] += 1
        else:
            summary["odd"] += 1
    return summary

# Hàm in báo cáo
def report(numbers):
    print("Danh sách số:", numbers)
    print("Tổng số:", sum(numbers))
    print("Số lớn nhất:", max(numbers))
    print("Số nhỏ nhất:", min(numbers))
    summary = even_odd_summary(numbers)
    print("Số chẵn:", summary["even"], "| Số lẻ:", summary["odd"])
    print("Các số nguyên tố trong danh sách:")
    primes = [n for n in numbers if is_prime(n)]
    print(primes)
    print("Factorial của các số <= 5 trong danh sách:")
    for n in numbers:
        if n <= 5:
            print(f"{n}! =", factorial(n))

# Main program
if __name__ == "__main__":
    nums = generate_numbers(10)
    report(nums)
