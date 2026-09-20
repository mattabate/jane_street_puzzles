import json
import random
import time
import tqdm


SIZE = 5
SAVE_FILE = f"results/bests_{int(time.time())}.json"

with open("states.json") as f:
    JSON_POPULATION: list[list] = json.load(f)


def get_kings_moves(pos: tuple[int, int]) -> list[tuple[int, int]]:
    """Get the possible moves for a king on a chess board.

    Args:
        pos (tuple[int, int]): the position of the king on the board

    Returns:
        list[tuple[int, int]]: a list of possible next positions for the king
    """
    moves = []
    for i in range(-1, 2):
        x = pos[0] + i
        for j in range(-1, 2):
            if 0 == i == j:  # the king must move
                continue
            y = pos[1] + j
            if 0 <= x < SIZE and 0 <= y < SIZE:
                moves.append((x, y))

    return moves


def iterate(index, starting: list[tuple[int, int]], grid: list[str], word: str):
    surviving = []
    for s in starting:
        km = get_kings_moves(s)
        for move in km:
            if grid[move[0]][move[1]] == word[index]:
                surviving.append(move)

    return surviving


def word_possible_at_point(start: tuple[int, int], grid: list[str], word: str):
    current_letter = grid[start[0]][start[1]]
    extra_life = True

    if current_letter == word[0]:
        starting = [start]
    elif current_letter != word[0]:
        extra_life = False
        starting = get_kings_moves(start)

    for i in range(1, len(word)):
        new_starting = iterate(i, starting, grid, word)
        if not new_starting:
            if extra_life:
                extra_life = False
                new_starting = []
                for s in starting:
                    new_starting += get_kings_moves(s)
            else:
                return False
        starting = new_starting
    else:
        return True


def process(grid: list[str]) -> tuple[int, list[str]]:
    """Return the score and states found in a grid.

    Args:
        grid (list[str]): the grid to process

    Returns:
        tuple[int, list[str]]: the score and states found in the grid

    HACK: Score here is an underapproximation of true score since
    # word_possible_at_point does not alway identify all words
    """
    score = 0
    states = []
    for state, population in JSON_POPULATION:
        possible = False
        for i in range(SIZE):
            for j in range(SIZE):
                if word_possible_at_point((i, j), grid, state):
                    possible = True
                    score += population
                    states.append(state)
                    break
            if possible:
                break
    return score, states


def flip_random(grid: list[str], num_flips: int) -> list[str]:
    """Randomly flip some number of letters in the grid.

    Args:
        grid (list[str]): the grid to flip
        num_flips (int): the number of letters to randomize

    Returns:
        list[str]: the new grid"""
    new_grid = grid.copy()
    for _ in range(num_flips):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        random_letter = chr(random.randint(65, 90))
        new_grid[x] = new_grid[x][:y] + random_letter + new_grid[x][y + 1 :]
    return new_grid


if __name__ == "__main__":
    # states_i_care_about = [
    #     "CALIFORNIA",
    #     "ARIZONA",
    #     "TEXAS",
    #     "LOUISIANA",
    #     "MISSISSIPPI",
    #     "ALABAMA",
    #     "FLORIDA",
    # ]

    IMPT_LETTERS = "UDLFXBRMOSTPAZ"
    # letters i dont care about
    # [G, H, J, K, Q, V, W, Y]

    # # mix up letters to make grid
    grid: list[str] = ["".join(random.sample(IMPT_LETTERS, SIZE)) for _ in range(SIZE)]

    best_grids = []

    ANNEALING_TIME = 50000
    MAX_TEMP = 10
    MIN_TEMP = 1

    intial_score, _ = process(grid)
    best_score = intial_score
    best_grid = grid.copy()

    t0 = time.time()
    temp = MAX_TEMP
    delta_temp = MAX_TEMP - MIN_TEMP
    while True:
        for i in tqdm.tqdm(range(ANNEALING_TIME)):
            new_grid = flip_random(best_grid, temp)

            score, states = process(new_grid)
            if score > best_score:
                best_score = score
                best_grid = new_grid
                print()
                print("------------------")
                print(json.dumps(best_grid, indent=4))
                print(states)
                print("new best score:", "\033[93m", best_score, "\033[0m")

                best_grids.append((best_score, len(states), best_grid, states))
                with open(SAVE_FILE, "w") as f:
                    json.dump(best_grids, f, indent=4)
                break

            # flips == 25 when tries = 0 and flips = 2 when tries = annealing_time
            temp = int(MAX_TEMP - (i / ANNEALING_TIME) * delta_temp)
            if i > ANNEALING_TIME:
                break
        else:
            break

    print("fin", "time:", time.time() - t0, "seconds")
