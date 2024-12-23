def total_calc(bill_amount, tip_percent):
    total = bill_amount + ((bill_amount / 100) * tip_percent)
    return total

print(total_calc(100, 10))  # 110.0