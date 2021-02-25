class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0

        for i in instructions:
            if i == 'L':
                idx = (idx + 3) % 4
            elif i == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

            # after one cycle:
            # robot returns into initial position
            # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0

# input: string of commands -> output: boolean of whether the robot changes direction

# use numbers from 0 to 3 to mark the directions: north=0, east=1, south=2, west=3.  In the array directions we could store corresponding coordinates changes ie. directions[0] is to go north, directions[1] is to go east, directions[2] is to go south, and directions[3] is to go west.

# the initial robot position is in the center x = y = 0, facing north idx = 0

# now everything is ready to iterate over the instructions.
# after one cycle we have everything to decide.  It's a limit cycle trajectory if the robot is back to the center x = y = 0 or if the robot doesn't face north: idx != 0.
