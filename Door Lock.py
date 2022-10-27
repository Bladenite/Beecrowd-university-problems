count = 0
number_of_pins, ideal_height = map(int, input().split())
pins = [int(pin) for pin in input().split()]

while pins != []:

    movement = ideal_height - pins[0]
    pins[0] += movement
    pins[1] += movement

    if pins[1] == ideal_height:
        pins.pop(1)
    pins.pop(0)

    count += abs(movement)

print(count)
