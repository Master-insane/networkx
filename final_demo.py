#!/usr/bin/env python3
"""
Final demonstration of the Algorithmic Toolkit package.
This script shows the main functionality: printing complete algorithm code.
"""

import sys
sys.path.insert(0, '/mnt/okcomputer/output')

def main():
    """Demonstrate the core functionality of the package."""
    print("ALGORITHMIC TOOLKIT - FINAL DEMONSTRATION")
    print("=" * 60)
    print("This package allows you to print complete algorithm implementations")
    print("using simple print() statements, as requested.")
    print("\\n" + "=" * 60)
    
    # Import all the algorithms
    from algorithmic_toolkit.algorithms.search import dfs, bfs, ucs
    from algorithmic_toolkit.algorithms.graph import networkx_algorithms
    from algorithmic_toolkit.games.wumpus import wumpus
    
    print("\\n1. DEPTH-FIRST SEARCH (DFS)")
    print("-" * 40)
    print("print(dfs)  # Shows complete DFS algorithm")
    print("\\n" + "="*60)
    print(dfs)
    print("="*60)
    
    print("\\n2. BREADTH-FIRST SEARCH (BFS)")
    print("-" * 40)
    print("print(bfs)  # Shows complete BFS algorithm")
    print("\\n" + "="*60)
    print(bfs)
    print("="*60)
    
    print("\\n3. UNIFORM COST SEARCH (UCS)")
    print("-" * 40)
    print("print(ucs)  # Shows complete UCS algorithm")
    print("\\n" + "="*60)
    print(ucs)
    print("="*60)
    
    print("\\n4. NETWORKX GRAPH ALGORITHMS")
    print("-" * 40)
    print("print(networkx_algorithms)  # Shows NetworkX algorithms")
    print("\\n" + "="*60)
    print(networkx_algorithms)
    print("="*60)
    
    print("\\n5. WUMPUS WORLD PROLOG")
    print("-" * 40)
    print("print(wumpus)  # Shows complete Wumpus World Prolog code")
    print("\\n" + "="*60)
    print("Wumpus World Prolog code (first 1000 characters):")
    print(wumpus[:1000] + "...")
    print("="*60)
    
    print("\\n" + "=" * 60)
    print("PACKAGE SUCCESSFULLY CREATED!")
    print("=" * 60)
    print("✅ All requested features implemented:")
    print("  • print(dfs) - Complete DFS algorithm code")
    print("  • print(bfs) - Complete BFS algorithm code") 
    print("  • print(ucs) - Complete UCS algorithm code")
    print("  • print(networkx_algorithms) - NetworkX algorithms")
    print("  • print(wumpus) - Complete Wumpus World Prolog code")
    print("\\n📦 Package ready for GitHub publishing!")
    print("\\n🚀 Usage instructions:")
    print("1. Add to Python path: sys.path.insert(0, '/mnt/okcomputer/output')")
    print("2. Import: from algorithmic_toolkit import dfs, bfs, ucs, networkx_algorithms, wumpus")
    print("3. Print algorithms: print(dfs), print(bfs), etc.")
    print("4. Execute code: exec(str(dfs)), exec(str(wumpus)), etc.")

if __name__ == "__main__":
    main()