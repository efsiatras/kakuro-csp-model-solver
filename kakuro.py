from csp import *
from time import time
from itertools import permutations


######### Kakuro puzzles

# Given, 4x3
kakuro_given4x3 = [
	['*', '*', '*', [6, ''], [3, '']],
	['*', [4, ''], [3, 3], '_', '_'],
	[['', 10], '_', '_', '_', '_'],
	[['', 3], '_', '_', '*', '*']
	]

#Given, 5x7
kakuro_given5x7 = [
	['*', [17, ''], [28, ''], '*', [42, ''], [22, '']],
	[['', 9], '_', '_', [31, 14], '_', '_'],
	[['', 20], '_', '_', '_', '_', '_'],
	['*', ['', 30], '_', '_', '_', '_'],
	['*', [22, 24], '_', '_', '_', '*'],
	[['', 25], '_', '_', '_', '_', [11, '']],
	[['', 20], '_', '_', '_', '_', '_'],
	[['', 14], '_', '_', ['', 17], '_', '_']
	]

# Given, 14x14
kakuro_given14x14 = [
    ['*', '*', '*', '*', '*', [4, ''], [24, ''], [11, ''], '*', '*', '*', [11, ''], [17, ''], '*', '*'],
    ['*', '*', '*', [17, ''], [11, 12], '_', '_', '_', '*', '*', [24, 10], '_', '_', [11, ''], '*'],
    ['*', [4, ''], [16, 26], '_', '_', '_', '_', '_', '*', ['', 20], '_', '_', '_', '_', [16, '']],
    [['', 20], '_', '_', '_', '_', [24, 13], '_', '_', [16, ''], ['', 12], '_', '_', [23, 10], '_', '_'],
    [['', 10], '_', '_', [24, 12], '_', '_', [16, 5], '_', '_', [16, 30], '_', '_', '_', '_', '_'],
    ['*', '*', [3, 26], '_', '_', '_', '_', ['', 12], '_', '_', [4, ''], [16, 14], '_', '_', '*'],
    ['*', ['', 8], '_', '_', ['', 15], '_', '_', [34, 26], '_', '_', '_', '_', '_', '*', '*'],
    ['*', ['', 11], '_', '_', [3, ''], [17, ''], ['', 14], '_', '_', ['', 8], '_', '_', [7, ''], [17, ''], '*'],
    ['*', '*', '*', [23, 10], '_', '_', [3, 9], '_', '_', [4, ''], [23, ''], ['', 13], '_', '_', '*'],
    ['*', '*', [10, 26], '_', '_', '_', '_', '_', ['', 7], '_', '_', [30, 9], '_', '_', '*'],
    ['*', [17, 11], '_', '_', [11, ''], [24, 8], '_', '_', [11, 21], '_', '_', '_', '_', [16, ''], [17, '']],
    [['', 29], '_', '_', '_', '_', '_', ['', 7], '_', '_', [23, 14], '_', '_', [3, 17], '_', '_'],
    [['', 10], '_', '_', [3, 10], '_', '_', '*', ['', 8], '_', '_', [4, 25], '_', '_', '_', '_'],
    ['*', ['', 16], '_', '_', '_', '_', '*', ['', 23], '_', '_', '_', '_', '_', '*', '*'],
    ['*', '*', ['', 6], '_', '_', '*', '*', ['', 15], '_', '_', '_', '*', '*', '*', '*']
    ]

# Easy, 6x6
kakuro_intermediate6x6 = [
	['*', [11, ''], [16, ''], [30, ''], '*', [24, ''], [11, '']],
	[['', 24], '_', '_', '_', ['', 9], '_', '_'],
	[['', 16], '_', '_', '_', [14, 17], '_', '_'],
	['*', '*', [22, 20], '_', '_', '_', '*'],
	['*', [3, 24], '_', '_', '_', [10, ''], [13, '']],
	[['', 7], '_', '_', ['', 19], '_', '_', '_'],
	[['', 11], '_', '_', ['', 7], '_', '_', '_']
	]

# Hard, 8x8
kakuro_hard8x8 = [
	['*', [28, ''], [15, ''], '*', [9, ''], [15, ''], '*', [9, ''], [12, '']],
	[['', 10], '_', '_', [15, 6], '_', '_', [10, 4], '_', '_'],
	[['', 38], '_', '_', '_', '_', '_', '_', '_', '_'],
	[['', 17], '_', '_', '_', ['', 4], '_', '_', [27, ''], '*'],
	[['', 13], '_', '_', [7, ''], [17, 19], '_', '_', '_', [15, '']],
	['*', ['', 8], '_', '_', '_', '*', [16, 3], '_', '_'],
	['*', [11, ''], [4, 4], '_', '_', [3, 24], '_', '_', '_'],
	[['', 44], '_', '_', '_', '_', '_', '_', '_', '_'],
	[['', 3], '_', '_', ['', 6], '_', '_', ['', 10], '_', '_']
	]


######### Kakuro class implementation

class Kakuro(CSP):

	""" Constructor method given the kakuro puzzle to be solved as argument """
	def __init__(self, kakuro_puzzle):
		variables = [] # A list of variables; each is atomic

		domains = {} # A dict of {var:[possible_value, ...]} entries

		neighbors = {} # A dict of {var:[var,...]} that for each variable lists
        			   # the other variables that participate in constraints.

		self.puzzle = kakuro_puzzle

		for i in range(len(kakuro_puzzle)): # Index for each line
			for j in range(len(kakuro_puzzle[i])): # Index for each cell in each line
				# Find empty cells
				if kakuro_puzzle[i][j] == "_": 
					var = "X" + str(i) + "," + str(j)
					variables.append(var) # Add variable var

					domains[var] = list(map(str, list(range(1, 10)))) # Add domain of variable var

				# Find slash cells
				if kakuro_puzzle[i][j] != '_' and kakuro_puzzle[i][j] != '*':

					# Sum of cells down
					if kakuro_puzzle[i][j][0] != "":
						hidden_var = "C_d" + str(i) + "," + str(j)
						variables.append(hidden_var) # Add hidden variable to convert n-ary sum constraint to binary

						cell_counter = 0
						for m in range(i + 1, len(kakuro_puzzle)):
							if kakuro_puzzle[m][j] != "_":
								break

							nei = "X" + str(m) + "," + str(j)

							if hidden_var not in neighbors:
								neighbors[hidden_var] = []
							neighbors[hidden_var].append(nei)

							if nei not in neighbors:
								neighbors[nei] = []
							neighbors[nei].append(hidden_var)

							cell_counter += 1

						perms = list(map("".join, permutations('123456789', cell_counter)))
						domains[hidden_var] = [perm for perm in perms if sum(int(x) for x in perm) == kakuro_puzzle[i][j][0]]

					# Sum of cells right
					if kakuro_puzzle[i][j][1] != "":
						hidden_var = "C_r" + str(i) + "," + str(j)
						variables.append(hidden_var) # Add hidden variable to convert n-ary constraint of sum to binary

						cell_counter = 0
						for k in range(j + 1, len(kakuro_puzzle[i])):
							if kakuro_puzzle[i][k] != "_":
								break

							nei = "X" + str(i) + "," + str(k)

							if hidden_var not in neighbors:
								neighbors[hidden_var] = []
							neighbors[hidden_var].append(nei)

							if nei not in neighbors:
								neighbors[nei] = []
							neighbors[nei].append(hidden_var)

							cell_counter += 1

						perms = list(map("".join, permutations('123456789', cell_counter)))
						domains[hidden_var] = [perm for perm in perms if sum(int(x) for x in perm) == kakuro_puzzle[i][j][1]]
						
		CSP.__init__(self, variables, domains, neighbors, self.kakuro_constraint)

	""" A function that returns true if neighbors A, B satisfy 
		kakuro's constraints when they have values A = a, B = b """
	def kakuro_constraint(self, A, a, B, b):
		if A[0] == "X" and B[0] == "C":
			X_i = int(A[1 : A.index(",")])
			X_j = int(A[A.index(",") + 1 :])

			C_i = int(B[3 : B.index(",")])
			C_j = int(B[B.index(",") + 1 :])

			if B[2] == "d":
				ind = X_i - C_i - 1 # Index of character to be checked
				hidden_var = "C_d" + str(C_i) + "," + str(C_j)

				if b[ind] == a: #and sum(int(x) for x in b) == self.sums[hidden_var]:
					return True

			else: # B[2] == "r":
				ind = X_j - C_j - 1 # Index of character to be checked
				hidden_var = "C_r" + str(C_i) + "," + str(C_j)

				if b[ind] == a: #and sum(int(x) for x in b) == self.sums[hidden_var]:
					return True

		elif A[0] == "C" and B[0] == "X":
			C_i = int(A[3 : A.index(",")])
			C_j = int(A[A.index(",") + 1 :])

			X_i = int(B[1 : B.index(",")])
			X_j = int(B[B.index(",") + 1 :])

			if A[2] == "d":
				ind = X_i - C_i - 1 # Index of character to be checked
				hidden_var = "C_d" + str(C_i) + "," + str(C_j)

				if a[ind] == b:# and sum(int(x) for x in a) == self.sums[hidden_var]:
					return True

			else: # A[2] == "r":
				ind = X_j - C_j - 1 # Index of character to be checked
				hidden_var = "C_r" + str(C_i) + "," + str(C_j)

				if a[ind] == b:# and sum(int(x) for x in a) == self.sums[hidden_var]:
					return True

		return False

	def display(self, assignment=None):
		for i in range(len(self.puzzle)): # Index for each line
			line = ""
			for j in range(len(self.puzzle[i])): # Index for each cell in each line
				if self.puzzle[i][j] == '*':
					line += " * \t"
				elif self.puzzle[i][j] == "_": 
					var = "X" + str(i) + "," + str(j)
					if assignment != None:
						if var in assignment:
							line += " " + assignment[var] + " \t"
						else:
							line += " _ \t"
					else:
						line += " _ \t"
				else:
					sum1 = str(self.puzzle[i][j][0]) if self.puzzle[i][j][0] else " "
					sum2 = str(self.puzzle[i][j][1]) if self.puzzle[i][j][1] else " "
					line += sum1 + "\\" + sum2 + "\t"
			print(line)
			print()

######### Solution of Kakuro Puzzle: Given, 4x3
print("Kakuro puzzle: Given, 4x3\n")

# BT + FC + MRV
Kakuro_problem = Kakuro(kakuro_given4x3)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV
Kakuro_problem = Kakuro(kakuro_given4x3)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_given4x3)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_given4x3)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.")


######### Solution of Kakuro Puzzle: Given, 5x7
print("\n\nKakuro puzzle: Given, 5x7\n")

# BT + FC + MRV
Kakuro_problem = Kakuro(kakuro_given5x7)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV
Kakuro_problem = Kakuro(kakuro_given5x7)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_given5x7)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_given5x7)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.")


######### Solution of Kakuro Puzzle: Given, 14x14
print("\n\nKakuro puzzle: Given, 14x14\n")

# BT + FC + MRV
Kakuro_problem = Kakuro(kakuro_given14x14)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV
Kakuro_problem = Kakuro(kakuro_given14x14)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_given14x14)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_given14x14)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.")


######### Solution of Kakuro Puzzle: Intermediate, 6x6
print("\n\nKakuro puzzle: Intermediate, 6x6\n")

# BT + FC + MRV
Kakuro_problem = Kakuro(kakuro_intermediate6x6)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV
Kakuro_problem = Kakuro(kakuro_intermediate6x6)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_intermediate6x6)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_intermediate6x6)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")


######### Solution of Kakuro Puzzle: Hard, 8x8
print("\n\nKakuro puzzle: Hard, 8x8\n")

# BT + FC + MRV
Kakuro_problem = Kakuro(kakuro_hard8x8)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=forward_checking)
total_time = time() - start_time
Kakuro_problem.display(assignments)
print("\tHeuristic algorithms: BT + FC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV
Kakuro_problem = Kakuro(kakuro_hard8x8)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + FC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_hard8x8)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=forward_checking)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + FC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.\n")

# BT + MAC + MRV + LCV
Kakuro_problem = Kakuro(kakuro_hard8x8)
start_time = time()
assignments = backtracking_search(Kakuro_problem, select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)
total_time = time() - start_time
print("\tHeuristic algorithms: BT + MAC + MRV + LCV")
print("\tSolved in", total_time, "seconds.")
print("\tMade", Kakuro_problem.nassigns, "assignments.")