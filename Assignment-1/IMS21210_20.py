coords = {'x': 0, 'y': 0}

input_commands = eval(input('Enter commands in dictionary: '))

for command in input_commands:
    if command == 'up':
        coords['y'] = coords['y']+input_commands[command]
    elif command == 'down':
        coords['y'] = coords['y'] - input_commands[command]
    elif command == 'left':
        coords['x'] = coords['x'] - input_commands[command]
    elif command == 'right':
        coords ['x'] = coords['x'] + input_commands[command]
    else:
        raise ValueError('Enter appropriate command')

print(coords)