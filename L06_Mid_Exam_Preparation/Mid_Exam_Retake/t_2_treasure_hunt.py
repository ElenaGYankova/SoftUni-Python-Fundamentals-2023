initial_chest = input().split('|')

data = input().split()
while data[0] != 'Yohoho!':
    command = data[0]
    
    if command == 'Loot':
        for treasure in data[1::]:
            if treasure not in initial_chest:
                initial_chest.insert(0, treasure)
                
    elif command == 'Drop':
        index = int(data[1])
        if 0 <= index < len(initial_chest):
            initial_chest.append(initial_chest.pop(index))
            
    elif command == 'Steal':
        count = int(data[1])
        stolen_items = []
        
        if count <= len(initial_chest):
            stolen_items = initial_chest[-count::]
            for iteration in range(count):
                initial_chest.pop()
        else:
            stolen_items = initial_chest.copy()
            initial_chest.clear()
        print(', '.join(stolen_items))
    data = input().split()

if initial_chest:
    average_sum = 0
    for jewels in initial_chest:
        average_sum += len(jewels)
    print(f"Average treasure gain: {average_sum/len(initial_chest):.2f} pirate credits.")
else:
    print('Failed treasure hunt.')
