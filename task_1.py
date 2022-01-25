def direction(facing, turn):
    compass_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    try:
        facing_index = compass_directions.index(facing)
        index_should_be_added = int(turn / 45)
        if (turn % 45 != 0) and (-1080 <= turn <= 1080):
            raise ArithmeticError("Turn value must be divided by 45 without remainder.")
        if (turn > 1080) or (turn < -1080):
            raise OverflowError("Turn value must be between -1080 and 1080.")
    except ValueError:
        print("\nNo such facing in compass directions.\n")
    index_final = facing_index + index_should_be_added
    if abs(index_final) > len(compass_directions) - 1:
        index_final = (facing_index + index_should_be_added) % len(compass_directions)
    facing_final = compass_directions[index_final]

    return facing_final


print(direction("N", 0))
