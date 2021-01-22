def calculate(days):
    if days > 14 and days <= 30:
        return days * 50
    if days > 30 and days <= 60:
        return days * 80
    if days > 60:
        return days * 100