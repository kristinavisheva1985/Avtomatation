def bank(x, y):
    for _ in range(y):
        x += x * 0.1
    return x 

amount = 5000
year = 3
final_amount = bank(amount, year)
print(f"Сумма на счету через {year} лет: {final_amount}")
