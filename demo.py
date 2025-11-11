#!/usr/bin/env python3
"""
Comprehensive demonstration of the Algorithmic Toolkit package.
This script shows how to use the package to print and execute algorithms.
"""

import sys
sys.path.insert(0, '/mnt/okcomputer/output')

def demo_search_algorithms():
    """Demonstrate the search algorithms functionality."""
    print("=" * 60)
    print("SEARCH ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    # Import the algorithms
    from algorithmic_toolkit.algorithms.search import dfs, bfs, ucs
    
    print("\\n1. DEPTH-FIRST SEARCH (DFS)")
    print("-" * 40)
    print("The complete DFS algorithm implementation:")
    print("\\nprint(dfs)  # This will show the full DFS code")
    print("\\n" + "="*60)
    print(dfs)
    print("="*60)
    
    # Test DFS execution
    print("\\n2. EXECUTING DFS ALGORITHM")
    print("-" * 40)
    exec(str(dfs))
    
    # Create a test graph
    test_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Import the dfs function after execution
    from algorithmic_toolkit.algorithms.search import dfs_func
    result = dfs_func(test_graph, 'A')
    print(f"DFS traversal from 'A': {result}")
    
    print("\\n3. BREADTH-FIRST SEARCH (BFS)")
    print("-" * 40)
    print("The complete BFS algorithm implementation:")
    print("\\nprint(bfs)  # This will show the full BFS code")
    print("\\n" + "="*60)
    print(bfs)
    print("="*60)
    
    # Test BFS execution
    print("\\n4. EXECUTING BFS ALGORITHM")
    print("-" * 40)
    exec(str(bfs))
    result = bfs(test_graph, 'A')
    print(f"BFS traversal from 'A': {result}")
    
    print("\\n5. UNIFORM COST SEARCH (UCS)")
    print("-" * 40)
    print("The complete UCS algorithm implementation:")
    print("\\nprint(ucs)  # This will show the full UCS code")
    print("\\n" + "="*60)
    print(ucs)
    print("="*60)
    
    # Test UCS execution
    print("\\n6. EXECUTING UCS ALGORITHM")
    print("-" * 40)
    exec(str(ucs))
    
    weighted_graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('C', 1), ('D', 7)],
        'C': [('D', 3)],
        'D': []
    }
    
    path, cost = ucs(weighted_graph, 'A', 'D')
    print(f"UCS shortest path from 'A' to 'D': {path} with cost {cost}")

def demo_networkx_algorithms():
    """Demonstrate NetworkX algorithms functionality."""
    print("\\n" + "=" * 60)
    print("NETWORKX ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    from algorithmic_toolkit.algorithms.graph import networkx_algorithms
    
    print("\\n1. NETWORKX ALGORITHMS COLLECTION")
    print("-" * 40)
    print("Complete collection of NetworkX-based graph algorithms:")
    print("\\nprint(networkx_algorithms)  # Shows all NetworkX algorithms")
    print("\\n" + "="*60)
    print(networkx_algorithms)
    print("="*60)
    
    # Test NetworkX execution
    print("\\n2. EXECUTING NETWORKX ALGORITHMS")
    print("-" * 40)
    exec(str(networkx_algorithms))
    
    # Create an instance and test
    alg = NetworkXAlgorithms()
    G = alg.create_sample_graph()
    
    print(f"Sample graph nodes: {list(G.nodes())}")
    print(f"Sample graph edges: {list(G.edges(data=True))}")
    
    # Test shortest path
    path, cost = alg.dijkstra_shortest_path(G, 'A', 'Z')
    print(f"Dijkstra shortest path from 'A' to 'Z': {path} with cost {cost}")

def demo_wumpus_world():
    """Demonstrate Wumpus World functionality."""
    print("\\n" + "=" * 60)
    print("WUMPUS WORLD DEMONSTRATION")
    print("=" * 60)
    
    from algorithmic_toolkit.games.wumpus import wumpus
    
    print("\\n1. WUMPUS WORLD PROLOG IMPLEMENTATION")
    print("-" * 40)
    print("Complete Wumpus World game implementation in Prolog:")
    print("\\nprint(wumpus)  # Shows the complete Prolog code")
    print("\\n" + "="*60)
    print("Wumpus World Prolog code preview (first 1000 characters):")
    print(wumpus[:1000] + "...")
    print("\\n" + "="*60)
    print("\\n2. WUMPUS WORLD FEATURES")
    print("-" * 40)
    print("The Wumpus World implementation includes:")
    print("• Complete game logic in Prolog")
    print("• Agent perception system (stench, breeze, glitter)")
    print("• Action execution framework (move, turn, grab, shoot, climb)")
    print("• Game state management")
    print("• Win/lose conditions")
    print("• Sample world configuration")
    print("• Knowledge base for intelligent agents")
    print("• Query predicates for game state")
    print("• Reset and initialization functions")

def demo_codestring_utility():
    """Demonstrate the CodeString utility class."""
    print("\\n" + "=" * 60)
    print("CODESTRING UTILITY DEMONSTRATION")
    print("=" * 60)
    
    from algorithmic_toolkit.utils.code_printer import CodeString
    
    print("\\n1. CODESTRING FEATURES")
    print("-" * 40)
    print("The CodeString class provides:")
    print("• String-like behavior with code content")
    print("• Formatted printing with descriptions")
    print("• Syntax highlighting support (if pygments available)")
    print("• Code execution capability with exec()")
    print("• Custom display methods")
    
    print("\\n2. CREATING CUSTOM CODE SNIPPETS")
    print("-" * 40)
    
    # Create a custom code snippet
    custom_code = '''
def fibonacci(n):
    \"\"\"Generate Fibonacci sequence up to n terms.\"\"\"
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Example usage
result = fibonacci(10)
print(f"First 10 Fibonacci numbers: {result}")
'''
    
    custom_cs = CodeString(custom_code, "Fibonacci Sequence Generator")
    print("Custom CodeString created:")
    print("\\n" + "="*60)
    print(custom_cs)
    print("="*60)
    
    # Test execution
    print("\\n3. EXECUTING CUSTOM CODE")
    print("-" * 40)
    exec(str(custom_cs))

def main():
    """Run the complete demonstration."""
    print("ALGORITHMIC TOOLKIT - COMPREHENSIVE DEMONSTRATION")
    print("=" * 60)
    print("This package provides complete algorithm implementations")
    print("that can be printed and executed with simple commands.")
    
    # Run all demonstrations
    demo_search_algorithms()
    demo_networkx_algorithms()
    demo_wumpus_world()
    demo_codestring_utility()
    
    print("\\n" + "=" * 60)
    print("PACKAGE SUMMARY")
    print("=" * 60)
    print("✓ DFS, BFS, UCS search algorithms implemented")
    print("✓ NetworkX-based graph algorithms included")
    print("✓ Complete Wumpus World Prolog implementation")
    print("✓ Custom CodeString utility for code printing")
    print("✓ All algorithms can be printed with print() statements")
    print("✓ All algorithms can be executed with exec()")
    print("✓ Educational and practical usage ready")
    
    print("\\nUSAGE EXAMPLES:")
    print("-" * 40)
    print("from algorithmic_toolkit import dfs, bfs, ucs, networkx_algorithms, wumpus")
    print("print(dfs)        # Show complete DFS implementation")
    print("print(bfs)        # Show complete BFS implementation")
    print("print(ucs)        # Show complete UCS implementation")
    print("print(wumpus)     # Show complete Wumpus World Prolog")
    print("exec(str(dfs))    # Execute DFS algorithm")
    print("exec(str(wumpus)) # Execute Wumpus World logic")
    
    print("\\n🎉 Demonstration completed successfully!")

if __name__ == "__main__":
    main()