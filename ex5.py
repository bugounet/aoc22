from dataclasses import dataclass
from typing import List
stacks = [
    ["H","R","B","D","Z","F","L","S"],
    ["T", "B", "M", "Z", "R"],
    ["Z", "L", "C", "H", "N", "S"],
    ["S", "C", "F", "J"], 
    ["P","G","H","W","R","Z","B"],
    ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    ["M", "Z", "R"],
    ['M', 'C', 'L', 'G', 'V', 'R', 'T'],
]
instructions = [
    "move 6 from 1 to 7",
    "move 2 from 2 to 4",
    "move 2 from 7 to 4",
    "move 6 from 4 to 3",
    "move 1 from 5 to 1",
    "move 3 from 8 to 3",
    "move 15 from 3 to 4",
    "move 6 from 5 to 9",
    "move 14 from 4 to 2",
    "move 3 from 2 to 7",
    "move 1 from 2 to 7",
    "move 9 from 9 to 1",
    "move 3 from 2 to 1",
    "move 7 from 6 to 7",
    "move 1 from 6 to 8",
    "move 2 from 9 to 1",
    "move 9 from 2 to 3",
    "move 8 from 3 to 9",
    "move 1 from 1 to 4",
    "move 1 from 8 to 6",
    "move 1 from 6 to 2",
    "move 5 from 9 to 8",
    "move 2 from 9 to 1",
    "move 1 from 4 to 2",
    "move 17 from 1 to 9",
    "move 1 from 3 to 1",
    "move 3 from 2 to 3",
    "move 2 from 4 to 5",
    "move 12 from 7 to 3",
    "move 16 from 9 to 2",
    "move 5 from 7 to 5",
    "move 2 from 1 to 2",
    "move 1 from 3 to 6",
    "move 1 from 4 to 6",
    "move 1 from 7 to 3",
    "move 1 from 6 to 3",
    "move 7 from 3 to 4",
    "move 5 from 8 to 3",
    "move 1 from 6 to 7",
    "move 7 from 3 to 4",
    "move 6 from 3 to 1",
    "move 2 from 4 to 8",
    "move 1 from 5 to 2",
    "move 10 from 4 to 5",
    "move 3 from 5 to 2",
    "move 2 from 8 to 9",
    "move 5 from 2 to 8",
    "move 1 from 3 to 5",
    "move 2 from 5 to 8",
    "move 12 from 5 to 7",
    "move 1 from 4 to 2",
    "move 5 from 9 to 4",
    "move 1 from 2 to 5",
    "move 6 from 1 to 3",
    "move 6 from 3 to 5",
    "move 10 from 7 to 4",
    "move 2 from 7 to 3",
    "move 4 from 7 to 6",
    "move 1 from 9 to 5",
    "move 12 from 2 to 1",
    "move 1 from 8 to 7",
    "move 3 from 7 to 4",
    "move 4 from 4 to 8",
    "move 7 from 5 to 3",
    "move 1 from 2 to 4",
    "move 10 from 1 to 5",
    "move 2 from 1 to 2",
    "move 4 from 6 to 7",
    "move 8 from 8 to 3",
    "move 5 from 4 to 9",
    "move 12 from 3 to 8",
    "move 4 from 3 to 8",
    "move 2 from 9 to 2",
    "move 3 from 5 to 4",
    "move 1 from 3 to 5",
    "move 1 from 7 to 6",
    "move 14 from 4 to 6",
    "move 6 from 5 to 9",
    "move 8 from 2 to 8",
    "move 3 from 5 to 7",
    "move 21 from 8 to 4",
    "move 16 from 4 to 9",
    "move 8 from 6 to 2",
    "move 4 from 6 to 1",
    "move 1 from 4 to 6",
    "move 2 from 4 to 8",
    "move 3 from 1 to 8",
    "move 2 from 4 to 6",
    "move 1 from 6 to 2",
    "move 3 from 8 to 4",
    "move 2 from 2 to 5",
    "move 2 from 5 to 7",
    "move 1 from 8 to 9",
    "move 1 from 4 to 9",
    "move 1 from 1 to 6",
    "move 3 from 6 to 3",
    "move 3 from 2 to 3",
    "move 1 from 4 to 6",
    "move 3 from 6 to 7",
    "move 10 from 9 to 7",
    "move 1 from 4 to 7",
    "move 6 from 8 to 3",
    "move 1 from 6 to 8",
    "move 2 from 2 to 5",
    "move 1 from 2 to 1",
    "move 1 from 8 to 9",
    "move 1 from 2 to 8",
    "move 1 from 1 to 9",
    "move 7 from 9 to 1",
    "move 1 from 8 to 5",
    "move 7 from 1 to 7",
    "move 3 from 5 to 8",
    "move 3 from 7 to 2",
    "move 1 from 8 to 4",
    "move 1 from 2 to 4",
    "move 2 from 4 to 6",
    "move 5 from 3 to 1",
    "move 9 from 7 to 2",
    "move 6 from 3 to 8",
    "move 8 from 2 to 7",
    "move 2 from 6 to 4",
    "move 2 from 1 to 7",
    "move 2 from 1 to 4",
    "move 24 from 7 to 4",
    "move 4 from 8 to 9",
    "move 2 from 7 to 5",
    "move 1 from 5 to 2",
    "move 1 from 3 to 8",
    "move 4 from 2 to 8",
    "move 13 from 9 to 2",
    "move 2 from 8 to 6",
    "move 3 from 9 to 6",
    "move 26 from 4 to 2",
    "move 1 from 5 to 7",
    "move 2 from 6 to 2",
    "move 2 from 4 to 1",
    "move 7 from 2 to 1",
    "move 15 from 2 to 6",
    "move 8 from 2 to 8",
    "move 4 from 6 to 8",
    "move 9 from 2 to 9",
    "move 13 from 6 to 7",
    "move 6 from 1 to 9",
    "move 2 from 2 to 4",
    "move 4 from 1 to 6",
    "move 3 from 8 to 3",
    "move 1 from 4 to 9",
    "move 2 from 6 to 7",
    "move 1 from 4 to 3",
    "move 3 from 3 to 2",
    "move 14 from 7 to 4",
    "move 5 from 9 to 5",
    "move 9 from 8 to 5",
    "move 7 from 9 to 6",
    "move 2 from 5 to 6",
    "move 2 from 9 to 2",
    "move 10 from 5 to 1",
    "move 1 from 3 to 1",
    "move 2 from 8 to 1",
    "move 1 from 9 to 2",
    "move 1 from 7 to 5",
    "move 4 from 2 to 1",
    "move 1 from 9 to 8",
    "move 3 from 4 to 1",
    "move 1 from 8 to 6",
    "move 12 from 1 to 5",
    "move 1 from 1 to 6",
    "move 1 from 7 to 5",
    "move 4 from 6 to 9",
    "move 2 from 2 to 4",
    "move 1 from 9 to 6",
    "move 1 from 1 to 5",
    "move 2 from 9 to 7",
    "move 10 from 6 to 5",
    "move 1 from 6 to 7",
    "move 20 from 5 to 1",
    "move 1 from 7 to 9",
    "move 2 from 9 to 1",
    "move 3 from 5 to 1",
    "move 2 from 8 to 4",
    "move 2 from 8 to 7",
    "move 1 from 5 to 9",
    "move 1 from 8 to 4",
    "move 22 from 1 to 7",
    "move 5 from 4 to 8",
    "move 1 from 5 to 9",
    "move 19 from 7 to 4",
    "move 2 from 9 to 1",
    "move 1 from 5 to 9",
    "move 10 from 1 to 8",
    "move 1 from 9 to 1",
    "move 1 from 8 to 3",
    "move 8 from 4 to 7",
    "move 1 from 5 to 6",
    "move 3 from 4 to 5",
    "move 1 from 5 to 9",
    "move 11 from 7 to 4",
    "move 4 from 4 to 9",
    "move 1 from 6 to 2",
    "move 1 from 3 to 9",
    "move 5 from 9 to 4",
    "move 5 from 7 to 9",
    "move 23 from 4 to 2",
    "move 17 from 2 to 7",
    "move 2 from 2 to 8",
    "move 4 from 4 to 7",
    "move 1 from 4 to 5",
    "move 2 from 5 to 2",
    "move 5 from 8 to 9",
    "move 5 from 2 to 7",
    "move 9 from 7 to 5",
    "move 11 from 9 to 2",
    "move 1 from 4 to 3",
    "move 5 from 8 to 7",
    "move 3 from 8 to 5",
    "move 2 from 1 to 3",
    "move 2 from 3 to 9",
    "move 1 from 5 to 8",
    "move 5 from 7 to 5",
    "move 15 from 5 to 4",
    "move 2 from 8 to 1",
    "move 2 from 5 to 1",
    "move 4 from 4 to 1",
    "move 1 from 8 to 7",
    "move 8 from 2 to 1",
    "move 4 from 2 to 8",
    "move 2 from 7 to 4",
    "move 5 from 8 to 6",
    "move 5 from 7 to 9",
    "move 4 from 6 to 5",
    "move 7 from 4 to 8",
    "move 1 from 6 to 1",
    "move 1 from 3 to 1",
    "move 2 from 5 to 1",
    "move 7 from 1 to 5",
    "move 5 from 1 to 3",
    "move 4 from 7 to 9",
    "move 4 from 3 to 9",
    "move 2 from 9 to 7",
    "move 6 from 9 to 2",
    "move 1 from 4 to 1",
    "move 1 from 3 to 5",
    "move 1 from 2 to 5",
    "move 5 from 9 to 4",
    "move 4 from 4 to 6",
    "move 1 from 8 to 9",
    "move 8 from 4 to 3",
    "move 7 from 7 to 3",
    "move 5 from 1 to 3",
    "move 11 from 5 to 9",
    "move 1 from 7 to 6",
    "move 2 from 3 to 5",
    "move 1 from 3 to 1",
    "move 3 from 6 to 2",
    "move 2 from 5 to 1",
    "move 2 from 1 to 2",
    "move 3 from 1 to 5",
    "move 5 from 9 to 2",
    "move 2 from 6 to 8",
    "move 2 from 3 to 8",
    "move 4 from 9 to 7",
    "move 3 from 5 to 2",
    "move 2 from 1 to 8",
    "move 1 from 9 to 8",
    "move 1 from 9 to 2",
    "move 4 from 7 to 9",
    "move 11 from 8 to 7",
    "move 1 from 8 to 2",
    "move 6 from 9 to 7",
    "move 3 from 7 to 1",
    "move 13 from 2 to 7",
    "move 24 from 7 to 1",
    "move 2 from 2 to 6",
    "move 1 from 8 to 3",
    "move 1 from 9 to 3",
    "move 5 from 2 to 4",
    "move 1 from 2 to 5",
    "move 1 from 6 to 2",
    "move 1 from 6 to 3",
    "move 1 from 2 to 4",
    "move 3 from 7 to 3",
    "move 2 from 1 to 7",
    "move 2 from 3 to 8",
    "move 2 from 7 to 8",
    "move 9 from 3 to 2",
    "move 3 from 4 to 8",
    "move 1 from 5 to 1",
    "move 9 from 2 to 1",
    "move 3 from 4 to 9",
    "move 1 from 7 to 8",
    "move 6 from 3 to 9",
    "move 2 from 1 to 5",
    "move 15 from 1 to 3",
    "move 13 from 3 to 9",
    "move 11 from 1 to 4",
    "move 5 from 4 to 1",
    "move 6 from 3 to 6",
    "move 4 from 4 to 8",
    "move 6 from 1 to 4",
    "move 1 from 5 to 2",
    "move 1 from 2 to 1",
    "move 3 from 4 to 2",
    "move 2 from 8 to 5",
    "move 2 from 4 to 2",
    "move 9 from 9 to 3",
    "move 9 from 3 to 5",
    "move 2 from 9 to 4",
    "move 5 from 2 to 6",
    "move 1 from 1 to 8",
    "move 1 from 4 to 1",
    "move 10 from 9 to 2",
    "move 9 from 2 to 4",
    "move 10 from 4 to 1",
    "move 3 from 1 to 3",
    "move 4 from 1 to 2",
    "move 5 from 2 to 4",
    "move 2 from 5 to 2",
    "move 4 from 1 to 7",
    "move 10 from 5 to 4",
    "move 2 from 2 to 4",
    "move 1 from 9 to 2",
    "move 2 from 3 to 5",
    "move 1 from 3 to 5",
    "move 3 from 6 to 7",
    "move 8 from 4 to 9",
    "move 6 from 6 to 1",
    "move 4 from 9 to 5",
    "move 2 from 9 to 1",
    "move 1 from 2 to 6",
    "move 6 from 5 to 2",
    "move 3 from 7 to 9",
    "move 4 from 8 to 2",
    "move 1 from 7 to 9",
    "move 1 from 5 to 3",
    "move 2 from 7 to 4",
    "move 1 from 7 to 1",
    "move 14 from 1 to 9",
    "move 1 from 1 to 9",
    "move 1 from 3 to 8",
    "move 3 from 2 to 5",
    "move 2 from 4 to 2",
    "move 6 from 8 to 1",
    "move 1 from 2 to 1",
    "move 5 from 1 to 9",
    "move 1 from 1 to 7",
    "move 2 from 8 to 5",
    "move 1 from 5 to 4",
    "move 1 from 6 to 1",
    "move 8 from 2 to 7",
    "move 2 from 6 to 1",
    "move 9 from 9 to 5",
    "move 11 from 4 to 8",
    "move 4 from 7 to 4",
    "move 6 from 4 to 6",
    "move 1 from 7 to 4",
    "move 6 from 6 to 7",
    "move 1 from 5 to 9",
    "move 6 from 8 to 9",
    "move 8 from 9 to 5",
    "move 1 from 4 to 5",
    "move 15 from 9 to 3",
    "move 3 from 1 to 4",
    "move 6 from 7 to 2",
    "move 3 from 4 to 9",
    "move 2 from 7 to 3",
    "move 1 from 7 to 3",
    "move 1 from 7 to 2",
    "move 2 from 8 to 1",
    "move 3 from 8 to 5",
    "move 2 from 1 to 7",
    "move 8 from 3 to 6",
    "move 3 from 6 to 5",
    "move 1 from 6 to 1",
    "move 10 from 5 to 7",
    "move 6 from 5 to 4",
    "move 4 from 2 to 4",
    "move 6 from 5 to 1",
    "move 6 from 1 to 8",
    "move 2 from 9 to 2",
    "move 2 from 9 to 7",
    "move 6 from 3 to 7",
    "move 1 from 3 to 5",
    "move 1 from 1 to 9",
    "move 2 from 8 to 1",
    "move 2 from 5 to 4",
    "move 3 from 3 to 7",
    "move 10 from 4 to 6",
    "move 1 from 9 to 7",
    "move 12 from 7 to 3",
    "move 12 from 3 to 8",
    "move 2 from 1 to 5",
    "move 1 from 1 to 3",
    "move 13 from 8 to 1",
    "move 7 from 7 to 1",
    "move 13 from 6 to 9",
    "move 1 from 7 to 4",
    "move 6 from 5 to 3",
    "move 3 from 4 to 3",
    "move 6 from 3 to 1",
    "move 10 from 9 to 4",
    "move 2 from 7 to 6",
    "move 8 from 1 to 9",
    "move 3 from 2 to 9",
    "move 1 from 3 to 5",
    "move 1 from 3 to 5",
    "move 1 from 1 to 4",
    "move 6 from 9 to 3",
    "move 2 from 6 to 7",
    "move 4 from 9 to 5",
    "move 4 from 1 to 6",
    "move 1 from 2 to 4",
    "move 6 from 1 to 4",
    "move 3 from 9 to 3",
    "move 3 from 6 to 8",
    "move 3 from 8 to 7",
    "move 5 from 5 to 1",
    "move 1 from 3 to 9",
    "move 1 from 9 to 5",
    "move 1 from 3 to 2",
    "move 2 from 5 to 1",
    "move 1 from 6 to 9",
    "move 1 from 6 to 3",
    "move 2 from 9 to 7",
    "move 2 from 8 to 1",
    "move 1 from 3 to 2",
    "move 1 from 2 to 5",
    "move 1 from 7 to 1",
    "move 7 from 7 to 9",
    "move 12 from 1 to 9",
    "move 1 from 5 to 2",
    "move 1 from 7 to 1",
    "move 13 from 4 to 7",
    "move 1 from 9 to 4",
    "move 5 from 7 to 3",
    "move 4 from 9 to 1",
    "move 8 from 7 to 9",
    "move 3 from 2 to 3",
    "move 4 from 3 to 7",
    "move 5 from 4 to 6",
    "move 3 from 9 to 4",
    "move 10 from 1 to 5",
    "move 3 from 4 to 7",
    "move 16 from 9 to 2",
    "move 3 from 9 to 2",
    "move 6 from 5 to 3",
    "move 4 from 6 to 2",
    "move 1 from 4 to 6",
    "move 2 from 6 to 8",
    "move 1 from 5 to 2",
    "move 1 from 5 to 8",
    "move 7 from 7 to 2",
    "move 16 from 2 to 1",
    "move 1 from 5 to 1",
    "move 10 from 2 to 8",
    "move 14 from 8 to 5",
    "move 2 from 2 to 6",
    "move 1 from 2 to 5",
    "move 2 from 2 to 1",
    "move 8 from 1 to 7",
    "move 4 from 1 to 7",
    "move 2 from 1 to 7",
    "move 5 from 3 to 2",
    "move 1 from 1 to 6",
    "move 2 from 2 to 5",
    "move 4 from 1 to 7",
    "move 1 from 2 to 8",
    "move 1 from 2 to 8",
    "move 3 from 6 to 7",
    "move 10 from 7 to 5",
    "move 1 from 2 to 8",
    "move 27 from 5 to 9",
    "move 1 from 5 to 6",
    "move 1 from 6 to 4",
    "move 1 from 4 to 3",
    "move 3 from 3 to 7",
    "move 4 from 3 to 6",
    "move 2 from 6 to 4",
    "move 3 from 8 to 1",
    "move 2 from 6 to 1",
    "move 12 from 7 to 8",
    "move 2 from 3 to 9",
    "move 1 from 9 to 2",
    "move 1 from 2 to 8",
    "move 2 from 1 to 2",
    "move 6 from 3 to 8",
    "move 1 from 7 to 4",
    "move 15 from 9 to 5",
    "move 7 from 9 to 4",
    "move 1 from 2 to 1",
    "move 16 from 8 to 2",
    "move 8 from 5 to 2",
    "move 24 from 2 to 9",
    "move 3 from 1 to 2",
    "move 24 from 9 to 1",
    "move 5 from 5 to 9",
    "move 3 from 4 to 1",
    "move 1 from 7 to 6",
    "move 1 from 6 to 3",
    "move 1 from 3 to 2",
    "move 3 from 2 to 3",
    "move 1 from 5 to 6",
    "move 1 from 2 to 7",
]

@dataclass
class Instruction:
    from_stack: int
    to_stack: int
    number_of_crates: int

    @classmethod
    def read_input(cls, input):
        number_of_crates = int(input.split(" from ")[0].split("move ")[1])
        from_stack = int(input.split(" from ")[1].split(" to ")[0]) - 1
        to_stack = int(input.split(" to ")[1]) - 1
        return cls(number_of_crates=number_of_crates, from_stack=from_stack, to_stack=to_stack)

    def __str__(self):
        return f"move {self.number_of_crates} from {self.from_stack+1} to {self.to_stack+1}"

class CateMover9000(Instruction):
    def transform_stacks(self, stacks) -> List[List[str]]:
        for _ in range(self.number_of_crates):
            crate = stacks[self.from_stack].pop()
            stacks[self.to_stack].append(crate)
        return stacks


class CateMover9001(Instruction):
    def transform_stacks(self, stacks) -> List[List[str]]:
        fifo = []
        for _ in range(self.number_of_crates):
            crate = stacks[self.from_stack].pop()
            fifo.append(crate)
        for _ in range(self.number_of_crates):
            crate = fifo.pop()
            stacks[self.to_stack].append(crate)
        return stacks



def print_stacks(stacks):
    max_height = 0
    for stack in stacks:
        max_height = max(max_height, len(stack))
    
    for i in reversed(range(max_height)):
        line = ""
        for stack in stacks:
            if len(stack) > i:
                line += f"[{stack[i]}]"
            else:
                line += f"[ ]"
        print(line)
    print("".join([f" {i} " for i in range(1, len(stacks)+1)]))

# print_stacks(stacks)
# for input in instructions:
#     stacks = CateMover9000.read_input(input).transform_stacks(stacks)
# print_stacks(stacks)

# for stack in stacks:
#     print(stack[-1])

    
#part 2
print_stacks(stacks)
for input in instructions:
    stacks = CateMover9001.read_input(input).transform_stacks(stacks)
print_stacks(stacks)

for stack in stacks:
    print(stack[-1])
