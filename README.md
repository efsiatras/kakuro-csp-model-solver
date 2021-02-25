#  Modelling Kakuro as CSP and Solving Kakuro Puzzles
**Kakuro** or Kakkuro or Kakoro is a kind of logic puzzle that is often referred to as a mathematical transliteration of the crossword.

We model Kakuro as a **CSP** and solve Kakuro puzzles with various algorithms. Our goal is to show how different algorithms for CSP behave during the solution of these puzzles.

## Algorithms for CSP
The algorithms tested are combinations of:
- BT (Backtracking-Search)
- FC (Forward-Checking)
- MAC (Maintaining-Arc-Consistency)
- MRV (Minimum-Remaining-Values)
- LCV (Least-Constraining-Value)

## Usage
`$ python3 kakuro.py`

## Implementation
The **csp.py**, **search.py** and **utils.py** files are modified files of [aimacode/aima-python](https://github.com/aimacode/aima-python).

The **kakuro.py** file is written by me and it's the modelization of Kakuro as a CSP and the main function. 

## Kakuro Puzzles
The Kakuro puzzles are taken from [here](https://www.kakuroconquest.com/) and [here](https://www.menneske.no/kakuro/eng/).

## Runtime and Number of Assignments
| Easy, 4x3 Puzzle     | Average Runtime (seconds) | Average Number of Assignments |
| -------------------- | ------------------------- | ----------------------------- |
| BT + FC + MRV        | 0.00099                   | 20                            |
| BT + MAC + MRV       | 0.00099                   | 15                            |
| BT + FC + MRV + LCV  | 0.00096                   | 15                            |
| BT + MAC + MRV + LCV | 0.00401                   | 33                            |

| Easy, 6x6 Puzzle     | Average Runtime (seconds) | Average Number of Assignments |
| -------------------- | ------------------------- | ----------------------------- |
| BT + FC + MRV        | 0.00697                   | 72                            |
| BT + MAC + MRV       | 0.00797                   | 46                            |
| BT + FC + MRV + LCV  | 0.00697                   | 74                            |
| BT + MAC + MRV + LCV | 0.01395                   | 46                            |

| Easy, 14x14 Puzzle   | Average Runtime (seconds) | Average Number of Assignments |
| -------------------- | ------------------------- | ----------------------------- |
| BT + FC + MRV        | 2.02458                   | 10027                         |
| BT + MAC + MRV       | 0.20046                   | 214                           |
| BT + FC + MRV + LCV  | 1.33246                   | 4949                          |
| BT + MAC + MRV + LCV | 0.19248                   | 215                           |

| Intermediate, 5x7 Puzzle | Average Runtime (seconds) | Average Number of Assignments |
| ------------------------ | ------------------------- | ----------------------------- |
| BT + FC + MRV            | 0.41786                   | 1053                          |
| BT + MAC + MRV           | 0.50165                   | 45                            |
| BT + FC + MRV + LCV      | 0.38500                   | 862                           |
| BT + MAC + MRV + LCV     | 0.43480                   | 45                            |

| Hard, 6x6 Puzzle     | Average Runtime (seconds) | Average Number of Assignments |
| -------------------- | ------------------------- | ----------------------------- |
| BT + FC + MRV        | 2.02458                   | 10027                         |
| BT + MAC + MRV       | 0.20046                   | 214                           |
| BT + FC + MRV + LCV  | 1.33246                   | 4949                          |
| BT + MAC + MRV + LCV | 0.19248                   | 215                           |
