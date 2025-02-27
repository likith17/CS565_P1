# Battleship AI: Fleet Maneuvering and Navigation  

## Overview  
This project implements AI-based search algorithms for fleet maneuvering and navigation in a **grid-based maritime environment**. The system performs **four missions**, each requiring a different search strategy.

## Missions Implemented  

### Mission 1: Counting Battleships (Enemy Fleet Detection)  
- **Algorithm Used:** Depth First Search (DFS)  
- **Task:** Identify and count distinct enemy fleets in a **2D maritime grid**, where:  
  - `'1'` represents **battleships**  
  - `'0'` represents **open water**  
- **Output:** The total number of **connected battleship clusters**.  

---

### Mission 2: Navigating the Grid (Finding a Safe Path)  
- **Algorithm Used:** Breadth First Search (BFS)  
- **Task:** Determine the shortest path through **open water (`0`)**, avoiding **battleships (`1`)**.  
- **Movement:** **8-directional** (up, down, left, right, and diagonals).  
- **Output:** The **minimum number of moves** required to escape. If no path exists, return `"Alert!!!"`.

---

### Mission 3: Crossing Treacherous Waters (Minimizing Effort)  
- **Algorithm Used:** Uniform Cost Search (UCS)  
- **Task:** Navigate through a **grid of elevation values**, where **higher values** indicate **difficult terrain**.  
- **Objective:** Find the **easiest route** by **minimizing the maximum elevation difference** between any two adjacent cells.  
- **Output:** The **least effort path cost**.

---

### Mission 4: Fleet Maneuvering (Arranging Battleships)  
- **Algorithm Used:** A* Search (A\*)  
- **Task:** Rearrange a **2x3 grid** of battleships to match the **target formation**:  




All the references used to implement the missions:

https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

https://favtutor.com/blogs/breadth-first-search-python

https://www.geeksforgeeks.org/find-the-level-of-given-node-in-an-undirected-graph/

https://www.reddit.com/r/leetcode/comments/125tvft/how_do_i_start_with_bfs_on_matrix/?rdt=35620

https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm

https://www.geeksforgeeks.org/depth-first-search-dfs-for-artificial-intelligence/

https://www.geeksforgeeks.org/uniform-cost-search-ucs-in-ai/

https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/

https://en.wikipedia.org/wiki/A*_search_algorithm

https://www.geeksforgeeks.org/a-search-algorithm/#

https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html