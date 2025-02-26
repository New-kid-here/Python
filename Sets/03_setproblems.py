set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

set3 = {10, 20, 30, 40, 50, 60}

set3.difference_update({10, 20, 30})
print(set3)