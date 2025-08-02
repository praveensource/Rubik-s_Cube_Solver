import copy
import random
import tkinter as tk
import time

# ---------------------- Cube Representation --------------------- #
class Cube:
    def __init__(self):
        self.faces = {
            'U': ['W'] * 9,
            'D': ['Y'] * 9,
            'F': ['G'] * 9,
            'B': ['B'] * 9,
            'L': ['O'] * 9,
            'R': ['R'] * 9,
        }

    def copy(self):
        new_cube = Cube()
        new_cube.faces = copy.deepcopy(self.faces)
        return new_cube

    def is_solved(self):
        return all(face.count(face[0]) == 9 for face in self.faces.values())

    def __str__(self):
        return '\n'.join(f"{f}: {self.faces[f]}" for f in "UDFBLR")

# ---------------------- Move Definitions ---------------------- #
edge_map = {
    'U': [('B', 0), ('R', 0), ('F', 0), ('L', 0)],
    'D': [('F', 2), ('R', 2), ('B', 2), ('L', 2)],
    'F': [('U', 2), ('R', 3), ('D', 0), ('L', 1)],
    'B': [('U', 0), ('L', 3), ('D', 2), ('R', 1)],
    'L': [('U', 3), ('F', 3), ('D', 3), ('B', 1)],
    'R': [('U', 1), ('B', 3), ('D', 1), ('F', 1)],
}

row_col_map = {
    0: [0, 1, 2],
    1: [2, 5, 8],
    2: [6, 7, 8],
    3: [0, 3, 6]
}

def rotate_face(face):
    return [face[6], face[3], face[0],
            face[7], face[4], face[1],
            face[8], face[5], face[2]]

def rotate_face_ccw(face):
    return [face[2], face[5], face[8],
            face[1], face[4], face[7],
            face[0], face[3], face[6]]

def rotate_face_180(face):
    return [face[8], face[7], face[6],
            face[5], face[4], face[3],
            face[2], face[1], face[0]]

def apply_move(cube, move):
    face = move[0]
    direction = move[1:] if len(move) > 1 else ''

    if direction == "'":
        cube.faces[face] = rotate_face_ccw(cube.faces[face])
    elif direction == "2":
        cube.faces[face] = rotate_face_180(cube.faces[face])
    else:
        cube.faces[face] = rotate_face(cube.faces[face])

    edges = edge_map[face]
    buffer = []

    for e in edges:
        buf = [cube.faces[e[0]][i] for i in row_col_map[e[1]]]
        buffer.append(buf)

    if direction == "'":
        buffer = buffer[1:] + [buffer[0]]
    elif direction == "2":
        buffer = buffer[2:] + buffer[:2]
    else:
        buffer = [buffer[-1]] + buffer[:-1]

    for idx, e in enumerate(edges):
        for j, pos in enumerate(row_col_map[e[1]]):
            cube.faces[e[0]][pos] = buffer[idx][j]

    return cube

# ---------------------- Solver Engine ---------------------- #
MOVES = ['U', "U'", 'U2', 'D', "D'", 'D2', 'F', "F'", 'F2',
         'B', "B'", 'B2', 'L', "L'", 'L2', 'R', "R'", 'R2']

MAX_DEPTH = 14

def dfs(cube, depth, path, visited):
    if cube.is_solved():
        return path
    if depth == 0:
        return None

    cube_key = str(cube.faces)
    if cube_key in visited:
        return None
    visited.add(cube_key)

    for move in MOVES:
        new_cube = cube.copy()
        apply_move(new_cube, move)
        result = dfs(new_cube, depth - 1, path + [move], visited)
        if result:
            return result

    return None

def solve(cube):
    for depth in range(1, MAX_DEPTH + 1):
        visited = set()
        result = dfs(cube, depth, [], visited)
        if result:
            return result
    return None

# ---------------------- GUI Visualizer ---------------------- #
COLOR_MAP = {
    'W': 'white',
    'Y': 'yellow',
    'G': 'green',
    'B': 'blue',
    'O': 'orange',
    'R': 'red'
}

FACE_POS = {
    'U': (3, 0),
    'L': (0, 3), 'F': (3, 3), 'R': (6, 3), 'B': (9, 3),
    'D': (3, 6)
}

class CubeVisualizer:
    def __init__(self, cube):
        self.cube = cube
        self.root = tk.Tk()
        self.root.title("Rubik's Cube Solver")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='gray')
        self.canvas.pack()
        self.tile_size = 30
        self.draw_cube()

    def draw_face(self, face, face_id):
        start_x, start_y = FACE_POS[face_id]
        for i in range(3):
            for j in range(3):
                color = COLOR_MAP[face[i * 3 + j]]
                x = (start_x + j) * self.tile_size
                y = (start_y + i) * self.tile_size
                self.canvas.create_rectangle(x, y, x + self.tile_size, y + self.tile_size,
                                             fill=color, outline='black')

    def draw_cube(self):
        self.canvas.delete("all")
        for face_id in self.cube.faces:
            self.draw_face(self.cube.faces[face_id], face_id)
        self.root.update()

    def animate_solution(self, solution):
        for move in solution:
            apply_move(self.cube, move)
            self.draw_cube()
            time.sleep(1)

    def start(self, solution):
        self.draw_cube()
        self.root.after(1000, lambda: self.animate_solution(solution))
        self.root.mainloop()

# ---------------------- CLI + Visual Demo ---------------------- #
def scramble(cube, moves=5):
    sequence = [random.choice(MOVES) for _ in range(moves)]
    for move in sequence:
        apply_move(cube, move)
    return sequence

if __name__ == "__main__":
    cube = Cube()
    print("Initial Solved Cube:")
    print(cube)

    scramble_seq = scramble(cube, moves=5)
    print("\nScramble Moves:", scramble_seq)
    print("\nScrambled Cube:")
    print(cube)

    solution = solve(cube)
    if solution:
        print("\nSolution Moves:", solution)
        visualizer = CubeVisualizer(cube)
        visualizer.start(solution)
    else:
        print("\n No solution found within depth limit.")
        print("\n Try changing MAX_DEPTH and MOVES.")
