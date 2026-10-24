# Artificial Intelligence Laboratory (AI Lab) Experiments

A curated repository containing source code implementations, algorithms, and execution outputs for all Artificial Intelligence Lab experiments.

---

## 👨‍🎓 Student Details
- **Student Name:** *[Your Name]*
- **Registration / Roll No:** *[Your Roll / Registration Number]*
- **Department:** Computer Science & Engineering / Artificial Intelligence & Data Science
- **Semester:** 3rd / 5th Semester
- **Course:** Artificial Intelligence Laboratory
- **Submission Date:** October 2026

---

## 📚 List of Experiments

| Exp No. | Experiment Title | Source Code | Output Log |
| :---: | :--- | :---: | :---: |
| **01** | Breadth First Search (BFS) Traversal | [bfs.py](file:///Exp-01-Breadth-First-Search/bfs.py) | [output.txt](file:///Exp-01-Breadth-First-Search/output.txt) |
| **02** | Depth First Search (DFS) Traversal | [dfs.py](file:///Exp-02-Depth-First-Search/dfs.py) | [output.txt](file:///Exp-02-Depth-First-Search/output.txt) |
| **03** | Hill Climbing Optimization Algorithm | [hill_climbing.py](file:///Exp-03-Hill-Climbing/hill_climbing.py) | [output.txt](file:///Exp-03-Hill-Climbing/output.txt) |
| **04** | A* Search Algorithm | [a_star.py](file:///Exp-04-A-Star-Algorithm/a_star.py) | [output.txt](file:///Exp-04-A-Star-Algorithm/output.txt) |
| **05** | Min-Max Adversarial Search Algorithm | [min_max.py](file:///Exp-05-Min-Max-Algorithm/min_max.py) | [output.txt](file:///Exp-05-Min-Max-Algorithm/output.txt) |
| **06** | Alpha-Beta Pruning Optimization | [alpha_beta_pruning.py](file:///Exp-06-Alpha-Beta-Pruning/alpha_beta_pruning.py) | [output.txt](file:///Exp-06-Alpha-Beta-Pruning/output.txt) |
| **07** | 8-Queens Problem (Backtracking) | [eight_queens.py](file:///Exp-07-8-Queens-Problem/eight_queens.py) | [output.txt](file:///Exp-07-8-Queens-Problem/output.txt) |
| **08** | Water Jug Problem (State-Space Search) | [water_jug.py](file:///Exp-08-Water-Jug-Problem/water_jug.py) | [output.txt](file:///Exp-08-Water-Jug-Problem/output.txt) |
| **09** | Tic-Tac-Toe Game (Adversarial Agent) | [tic_tac_toe.py](file:///Exp-09-Tic-Tac-Toe-Game/tic_tac_toe.py) | [output.txt](file:///Exp-09-Tic-Tac-Toe-Game/output.txt) |
| **10** | Travelling Salesman Problem (TSP) | [travelling_salesman.py](file:///Exp-10-Travelling-Salesman-Problem/travelling_salesman.py) | [output.txt](file:///Exp-10-Travelling-Salesman-Problem/output.txt) |

---

## 🛠️ Experiment Summaries & Methodology

### 1. Breadth First Search (BFS)
- **Concept:** Explores the graph layer by layer using a FIFO Queue.
- **Data Structure:** `collections.deque` and visited `set`.
- **Time Complexity:** $O(V + E)$

### 2. Depth First Search (DFS)
- **Concept:** Traverses down the deepest branch before backtracking using recursion / LIFO Stack.
- **Time Complexity:** $O(V + E)$

### 3. Hill Climbing Algorithm
- **Concept:** Local search heuristic that iteratively moves to an immediate neighbor with higher evaluation value.
- **Objective Function:** $f(x) = -(x - 3)^2 + 9$ (Global maximum at $x=3$).

### 4. A* Search Algorithm
- **Concept:** Best-first search combining past path cost $g(n)$ and estimated heuristic cost $h(n)$ via $f(n) = g(n) + h(n)$.
- **Data Structure:** Priority Queue (`heapq`).

### 5. Min-Max Algorithm
- **Concept:** Decision rule used in two-player zero-sum games where the Maximizer maximizes the minimum payoff possible for the adversary.

### 6. Alpha-Beta Pruning
- **Concept:** Optimization for Min-Max that eliminates branches that cannot influence the final decision ($\alpha \ge \beta$).

### 7. 8-Queens Problem
- **Concept:** Constraint satisfaction problem solved using recursive backtracking to place 8 non-attacking queens on an $8 \times 8$ chessboard.

### 8. Water Jug Problem
- **Concept:** State-space exploration with operations (Fill, Empty, Pour) using BFS to reach the target volume with minimal steps.

### 9. Tic-Tac-Toe Game
- **Concept:** Classic 2-player board game state evaluation with victory checks along rows, columns, and diagonals. Includes both an interactive mode and demonstration mode.

### 10. Travelling Salesman Problem (TSP)
- **Concept:** Finds the minimum-cost Hamiltonian cycle visiting every city once and returning to the origin city using permutation search.

---

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd ai-lab-experiments
   ```

2. **Ensure Python 3 is installed:**
   ```bash
   python --version
   ```

3. **Run any experiment directly:**
   ```bash
   # Run Experiment 1 (BFS)
   python Exp-01-Breadth-First-Search/bfs.py

   # Run Experiment 4 (A*)
   python Exp-04-A-Star-Algorithm/a_star.py

   # Run Experiment 7 (8-Queens)
   python Exp-07-8-Queens-Problem/eight_queens.py

   # Run Experiment 9 (Tic-Tac-Toe Demo)
   python Exp-09-Tic-Tac-Toe-Game/tic_tac_toe.py --demo
   ```

---

## 📋 Evaluation Compliance Checklist
- [x] Source code provided for all lab experiments
- [x] Validated execution outputs provided in dedicated text files
- [x] Standard folder structure with documentation
- [x] Public GitHub repository ready for evaluation
