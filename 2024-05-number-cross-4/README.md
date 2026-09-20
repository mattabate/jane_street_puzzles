# Jane Street Puzzle May 2024

This repository contains a Python solution to the Jane Street Puzzle of May 2024. Before reading further, you should consider attempting the puzzle yourself, and thinking about the rules.

Puzzle Link: [Jane Street Puzzles - Number Cross 4](https://www.janestreet.com/puzzles/number-cross-4-index/)

## Puzzle Rules Overview - Number Cross 4

Solvers are provided an 11x11 grid which is pre-partitioned into connected regions.  The task involves placing digits (0-9) in certain cells, and shading others, adhering to a set of strategic rules:

- Adjacent cells must contain the same digit if they are in the same region and different digits if they are in different regions.  Shading cells alters the configuration of regions, however, shading must be "sparse," meaning no two shaded cells may share an edge.

- Each row of the grid includes a clue that relates to the numbers formed by concatenating consecutive groups of unshaded cells. Numbers must be at least two digits long and may not begin with a '0'.

## Solution Approach - Apologies for the Messy Repo

Jane Street's puzzles often require reducing a large search space down to a reasonable search problem; however, this one was particularly difficult to reduce. I first calculated the set of possibilities for the ninth row using `1_row_9.py`, discovering there were just under 1000 possible.  Then the eighth row using `2_row_8.py`, merging the possible sets as I went to ensure there existed a solution.  My approach was very brute force, but it led to the following solution.

```
11122233444
13332x3444x
1331x734449
133x100411x
13x144x4181
1444x444889
74444x74888
7714177x989
77111779999
x1144x79992
444443x3992
```

Needless to say, the code project is messy. See what you can do, and feel free to contact me for usage instructions.

## Contact Information
  
Email: <mabate13@gmail.com>
