def open_or_senior(data):
    results = list()
    for i in data:
        if i[0] < 55 or i[1] <= 7:
            results.append("Open")
        else:
            results.append("Senior")
    return results
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))