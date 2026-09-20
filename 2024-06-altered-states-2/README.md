# Jane Street Puzzle June 2024

This repository contains a Python solution to the Jane Street Puzzle of June 2024, which challenges solvers to place U.S. state names within a 5x5 grid following certain rules.

Before reading further, you should consider attempting the puzzle yourself, and thinking about the rules.

Puzzle Link: [Jane Street Puzzles - Altered States 2](https://www.janestreet.com/puzzles/altered-states-2-index/)

## Puzzle Overview

"Altered States 2" challenges solvers to score as many points as possible by arranging the names of U.S. states in a 5x5 grid of letters. State's names are spelled out using King’s moves, and you are allowed to alter the name of each state by one letter. Each state in your grid contributes a score equal to its population in the
[2020 census](https://en.wikipedia.org/wiki/2020_United_States_census#State_rankings), and certain special-grid-citations are possible.

## Solution Approach

The code solution here implements a niave--but surprisingly high scoring--search approach for constructing high scoring grids.

We start with an initial grid, and randomly alter `temp` number of characters. If the resulting grid admits a higher score than the previous grid, the search is restarted. Otherwise, we try again, allowing the search to run `ANNEALING_TIME` iterationsand, if a higher scoring grid has not been seen, the search ends and the highest scoring observed grid is returned. Importantly, `temp` is a time varying parameter, begining as a large integer that decays to `1` as the current loop interation approaches the `ANNEALING_TIME`. This stocastic search scheme is sometimes refered to as __simulated anealing__. 

## Repository Structure

- `main.py`: The main search script.
- `states.json`: JSON file with state names and their respective populations.
- `/results`: Folder where results are temporarily stored.
- `/results/bests`: Folder containing the best solutions found during the my personal trial.

## Installation

No additional libraries are required beyond the Python Standard Library. The code is compatible with Python 3.6 and above.

## Usage Instructions

To run the search algorithm, execute the following command from the terminal:
```sh
python3 main.py
```
Top scoring grids will be saved to the results folder.

## Expected Output

The script outputs the progression of the score and states during the optimization process. When a new high score is achieved, it prints the current best grid and the corresponding states. All high scores and their grids are saved to the `/results` directory in JSON format.

The highest scoring grid I found was 
```
LMYWK
AISER
HCNST
FOIAO
LGRNH
```
which scores `242536477` total points from 26 states! __California, Texas, Florida, New York, Illinois, Ohio, Maine, West Virginia, Idaho, Kansas, Arkansas, Iowa, Utah, Oregon, Louisiana, Alabama, Minnesota, Colorado, Wisconsin, Missouri, Indiana, Arizona, Virginia, New Jersey, Michigan, and Georgia__.
(approximately 73% of the toal population in 2020). This submission also achives three special-grid-citations
- 20S - over 20 states
- 200M - over 200 million population
- C2C - unbroken coast to cost state chain.

## Performance
Depending on the users configuration, the search script may run for a few hours before terminating. However, it is lightwaight to the extent that five concurrent searches were able to be carried out on a 36GB 2023 MacBook Pro without degrading search speed.

