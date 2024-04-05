
week_data = {}

day_data = {}
for z in range(1, 6):
    day_data[z] = 'null'

for y in week_list:
    week_data[y] = day_data

for x in range(1, 20):
    course_data[x] = week_data