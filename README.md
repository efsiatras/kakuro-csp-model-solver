#  Modelling and Solving Kakuro Puzzles as CSP
Kakuro (also known as Kakkuro or Kakoro) is a logic puzzle often regarded as the mathematical counterpart to a crossword puzzle.

In this work, we model Kakuro puzzles as a **Constraint Satisfaction Problem (CSP)** and solve them using various algorithms. Our objective is to evaluate the performance of different CSP algorithms during the puzzle-solving process.

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

The **kakuro.py** file was developed specifically for this project; it contains the CSP model for Kakuro as well as the main function.

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

## License
This project is available under the MIT License.
