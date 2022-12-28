from sort import merge_sort

max_cal = 0
calories = []

with open('input.txt') as all_calories:
  elf = 0
  for cals in all_calories:
    cal = cals.strip()
    if cal != '':
      elf += int(cal)
    elif cal == '':
      calories.append(int(elf))
      if elf > max_cal:
        max_cal = elf
      elf = 0
  print("Task 1:", max_cal, "\n\n")

print("Task 2:")
calories = merge_sort(calories)
print("Most Calories:", calories[len(calories) - 1])
print("Second Most Calories:", calories[len(calories) - 2])
print("Third Most Calories", calories[len(calories) - 3])
Total = calories[len(calories) - 1] + calories[len(calories) -
                                               2] + calories[len(calories) - 3]

print("Total:", Total)
