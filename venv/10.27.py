import random

num_duplications = 0

for x in range(10000):
    birthdays = []

    i = 1
    while i <= 23:
        days = random.randint(1, 365)
        i += 1
        birthdays.append(days)

    withoutdup = set(birthdays)

    if len(withoutdup) != len(birthdays):
        num_duplications += 1
    else:
        continue

probability = (num_duplications / 10000) * 100

print(f"{probability:.2f}%")
