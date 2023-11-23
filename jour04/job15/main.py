numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded_numbers = [int(num + 0.5) if num % 1 != 0.5 else round(num) for num in numbers]

n = len(rounded_numbers)
i = 0
while i < n:
    j = i + 1
    while j < n:
        if rounded_numbers[j] < rounded_numbers[i]:
            temp = rounded_numbers[i]
            rounded_numbers[i] = rounded_numbers[j]
            rounded_numbers[j] = temp
        j += 1
    i += 1

print("Liste arrondie et triée :", rounded_numbers)
