➡️Array / String Inputs

1. Is the array sorted?
- Yes → Think: Binary Search, Two Pointers, or Prefix Sums.
- No → Move to structural/intent-based decisions.



2. What's the intent of the problem?


- Optimization (Max/Min, count of ways, min cost)

    - Interdependent choices? → Use Dynamic Programming (Top-Down or Bottom-Up).

    - Independent decisions? → Consider a Greedy approach (with proof of correctness).

    - Feasibility / Existence Check

    - Use Backtracking, DFS with pruning, or Binary Search on Answer.


- Does it involve String Manipulation?

    - Prefix/Suffix logic? → Trie, Rolling Hash, or Z-Algorithm.

    - Sequential manipulation? → Stack, Monotonic Stack, or Deque.

    - Frequent lookups / duplicates / uniqueness

    - Use Hash Maps, Hash Sets, or Counting Arrays.

    - Sliding window behavior

    - Use Two Pointers, Deque, or Counting Hash Map.

    - Frequent Min/Max retrieval

    - Use Heap, Monotonic Queue, or Segment Tree (for range queries).





➡️ Graph Inputs

1. Pathfinding / Traversals

Shortest path / fewest steps → BFS (Unweighted), Dijkstra (Weighted).

Exhaustive exploration / component discovery → DFS, Union-Find.

2. Cycle Detection / Topological Order

Use DFS with visited tracking, Kahn’s Algorithm, or Disjoint Sets.

3. Optimization on graphs

Minimum Spanning Tree? → Kruskal, Prim.

Connectivity? → Tarjan's Algorithm, Bridge Finding, etc.

➡️ Tree Inputs (Typically Binary Trees)

1. Traversals / Depth Calculations

Level-order traversal / Lowest Common Ancestor → Use BFS / DFS with depth tracking.

Recursive divide-and-conquer logic → Postorder traversal is your friend.

2. Balancing / Ordering Constraints

Use BST properties, AVL / Red-Black trees, or Segment Trees if mutable.

➡️ Linked List Inputs

1. Cycle detection → Fast/Slow Pointers
2. Structural changes

Reversal? → Track prev, curr, next pointers.

Head/edge cases? → Use a dummy node strategy.
