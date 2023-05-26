fire_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
print("Cells: ")

for fire in fire_cells:
    fire_type = fire.split(" = ")
    if fire_type[0] == "High" and 80 < int(fire_type[1]) <= 125:
        if int(fire_type[1]) <= water:
            total_fire += int(fire_type[1])
            water -= int(fire_type[1])
            effort += int(fire_type[1]) * 0.25
            print(f" - {int(fire_type[1])}")
    elif fire_type[0] == "Medium" and 50 < int(fire_type[1]) <= 80:
        if int(fire_type[1]) <= water:
            total_fire += int(fire_type[1])
            water -= int(fire_type[1])
            effort += int(fire_type[1]) * 0.25
            print(f" - {int(fire_type[1])}")
    elif fire_type[0] == "Low" and 0 < int(fire_type[1]) <= 50:
        if int(fire_type[1]) <= water:
            total_fire += int(fire_type[1])
            water -= int(fire_type[1])
            effort += int(fire_type[1]) * 0.25
            print(f" - {int(fire_type[1])}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


'''
fires_with_cells = input()
water = int(input())
effort = 0
total_fire = 0
put_out_cells = []
cells_list = fires_with_cells.split("#")
for i in range(len(cells_list)):
    if water <= 0:
        break
    current_cell = cells_list[i]
    current_cell_list = current_cell.split(" ")
    current_fire_type = current_cell_list[0]
    current_water_needed = int(current_cell_list[-1])
    if (current_fire_type == "High") and (81 <= current_water_needed <= 125):
        cell_is_valid = True
    elif (current_fire_type == "Medium") and (51 <= current_water_needed <= 80):
        cell_is_valid = True
    elif (current_fire_type == "Low") and (1 <= current_water_needed <= 50):
        cell_is_valid = True
    else:
        cell_is_valid = False
    if cell_is_valid:
        if water >= current_water_needed:
            water -= current_water_needed
            effort += current_water_needed * 0.25
            total_fire += current_water_needed
            put_out_cells.append(current_water_needed)
print("Cells:")
for j in range(len(put_out_cells)):
    cell_value = put_out_cells[j]
    print(f"- {cell_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
'''
