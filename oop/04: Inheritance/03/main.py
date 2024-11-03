def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    for i in range(0, len(dragons)):
        describe(dragons[i])
        to_get_fired = dragons[i::]
        for j in range(0, len(dragons), i + 1):
            dragons[i].breathe_fire(3, 3, to_get_fired)


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        is_x_within = x_1 <= self.pos_x <= x_2 or x_2 <= self.pos_x <= x_1
        is_y_within = y_1 <= self.pos_y <= y_2 or y_2 <= self.pos_y <= y_1

        return is_x_within and is_y_within


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("====================================")

        unit_got_hit = []
        # Calculate the boundaries of the fire area
        x_min = min(x - self.__fire_range, x + self.__fire_range)
        x_max = max(x - self.__fire_range, x + self.__fire_range)
        y_min = min(y - self.__fire_range, y + self.__fire_range)
        y_max = max(y - self.__fire_range, y + self.__fire_range)

        for unit in units:
            if unit.in_area(x_min, y_min, x_max, y_max):
                unit_got_hit.append(unit)
                print(f"{unit.name} is hit by the fire")

        return unit_got_hit


main()
