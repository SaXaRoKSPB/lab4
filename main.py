all_things = {'в':(3, 25), 
              'п':(2, 15), 
              'б':(2, 15), 
              'а':(2, 20), 
              'и':(1, 5), 
              'н':(1, 15), 
              'т':(3, 20),
              'о':(1, 25),
              'ф':(1, 15),
              'д':(1, 10), 
              'к':(2, 20),
              'р':(2, 20),               
             }
sum_value = 0

for item in all_things:
    thing = all_things[item]
    sum_value += thing[1]

ans = 15
max_place = 8
things_place = []
things_value = []

for item in all_things:
    thing = all_things[item]
    things_place.append(thing[0])
    things_value.append(thing[1])

sum_place = len(things_value)
table = [[0 for counter1 in range(max_place + 1)] 
         for counter2 in range(sum_place + 1)]

for line in range (sum_place + 1):
    for column in range (max_place + 1):
        if line == 0 or column == 0:                
            table[line][column] = 0
        else:
            if things_place[line-1] <= column:
                table[line][column] = max(things_value[line-1] + 
                                          table[line-1][column-things_place[line-1]], table[line-1][column])
            else:
                table[line][column] = table[line-1][column]

now_sum_place = max_place
items_list = []
res = table[sum_place][max_place]

for line in range(sum_place, 0, -1):
    if res <= 0:
        break
    if res != table[line-1][now_sum_place]:
        items_list.append([things_place[line - 1], things_value[line - 1]])
        res -= things_value[line - 1]
        now_sum_place -= things_place[line - 1]

selected_stuff = []

for search in items_list:
    for key, things_value in all_things.items():
        if things_value[0] == search[0] and things_value[1] == search[1]:
            if not(key in selected_stuff):
                ans += things_value[1]
                sum_value -= things_value[1]
                selected_stuff.append(key)
                break     

ans -= sum_value
ans_table = [['' for counter1 in range (2)] for counter2 in range (4)]
line = 0
column = 0

for item in selected_stuff:
    thing = all_things[item]
    sum_place_item = thing[0]
    while sum_place_item != 0:
        if column != 1:
            ans_table[line][column] = f'[{str(item)}],'
        else:
            ans_table[line][column] = f'[{str(item)}]'
            print(ans_table[line][column-1], ans_table[line][column])
        if column != 1:
            column += 1
        else:
            line += 1
            column -=1
        sum_place_item -= 1

print (f'Итоговые очки выживания: {ans}')