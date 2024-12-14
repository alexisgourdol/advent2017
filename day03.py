from typing import NamedTuple, List, Tuple
from itertools import cycle


class Directions:
    RIGHT = (1, 0)
    UP = (0, 1)
    LEFT = (-1, 0)
    DOWN = (0, -1)


class Point(NamedTuple):
    x: int
    y: int
    val: int


class Grid:
    input_value: int = None
    points: List[Point] = []
    curr_x_min: int = (None,)
    curr_x_max: int = (None,)
    curr_y_min: int = (None,)
    curr_y_min: int = (None,)
    cursor_position: Point = None
    direction_gen = cycle(
        [Directions.RIGHT, Directions.UP, Directions.LEFT, Directions.DOWN]
    )
    cursor_dir: Tuple = None

    def __init__(
        self,
        input_value,
        points,
        curr_x_min,
        curr_x_max,
        curr_y_min,
        curr_y_max,
        cursor_position,
    ) -> None:

        self.input_value = input_value
        # get 1st direction : RIGHT
        self.cursor_dir = next(self.direction_gen)
        self.points = points
        self.curr_x_min = curr_x_min
        self.curr_x_max = curr_x_max
        self.curr_y_min = curr_y_min
        self.curr_y_max = curr_y_max
        self.cursor_position = cursor_position

    def __repr__(self):
        return "Test()"

    def __str__(self):
        return f"""Grid - curr_x_min:{self.curr_x_min} - curr_x_max:{self.curr_x_max} - curr_y_min:{self.curr_y_min} - curr_y_max:{self.curr_y_max}
        - cursor_dir: {self.cursor_dir} - cursor_position: {self.cursor_position=} - input_value: {self.input_value=}
        - l5points: {self.points[-5:]}"""

    def move_cursor(self, val):
        if val > 1:
            new_x = self.cursor_position.x + self.cursor_dir[0]
            new_y = self.cursor_position.y + self.cursor_dir[1]
            self.points.append(Point(new_x, new_y, val))
            self.cursor_position = Point(new_x, new_y, 0)

            # if you hit a bound, get new direction and increase the bound
            if new_x == self.curr_x_min:
                # print(f"X_MIN HIT - Changing {self.curr_x_min=} to {self.curr_x_min -1=}")
                self.cursor_dir = next(self.direction_gen)
                self.curr_x_min -= 1
            if new_x == self.curr_x_max:
                # print(f"X_MAX HIT - Changing {self.curr_x_max=} to {self.curr_x_max +1=}")
                self.cursor_dir = next(self.direction_gen)
                self.curr_x_max += 1
            if new_y == self.curr_y_min:
                # print(f"Y_MIN HIT - Changing {self.curr_y_min=} to {self.curr_y_min -1=}")
                self.cursor_dir = next(self.direction_gen)
                self.curr_y_min -= 1
            if new_y == self.curr_y_max:
                # print(f"Y_MAX HIT - Changing {self.curr_y_max=} to {self.curr_y_max +1=}")
                self.cursor_dir = next(self.direction_gen)
                self.curr_y_max += 1
        return self

    def move_all(self):
        for val in range(1, self.input_value + 1):
            self.move_cursor(val)


def compute_manhattan_distance(g: Grid) -> int:
    target = [point for point in g.points if point.val == g.input_value]
    if target:
        return abs(target[0].x) + abs(target[0].y)
    else:
        return ValueError("point not found to compute")


def main():
    g = Grid(23, [Point(0, 0, 1)], -1, 1, -1, 1, Point(0, 0, 0))
    g.move_all()
    print(g)
    print("_" * 50)

    input_grid = Grid(277678, [Point(0, 0, 1)], -1, 1, -1, 1, Point(0, 0, 0))
    input_grid.move_all()
    print(input_grid)
    print(f"part 1 : {compute_manhattan_distance(input_grid)}")
    print("_" * 50)


if __name__ == "__main__":
    main()
