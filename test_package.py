#!/usr/bin/env python3
"""
Test script to verify the algorithmic_toolkit package functionality.
"""

def test_imports():
    """Test that all modules can be imported correctly."""
    print("Testing imports...")
    try:
        from algorithmic_toolkit import dfs, bfs, ucs, networkx_algorithms, wumpus
        print("✓ All imports successful!")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_code_printing():
    """Test that code printing works correctly."""
    print("\\nTesting code printing...")
    
    from algorithmic_toolkit import dfs, bfs, ucs, networkx_algorithms, wumpus
    
    # Test DFS
    print("\\n=== Testing DFS ===")
    print(f"DFS type: {type(dfs)}")
    print(f"DFS length: {len(dfs)} characters")
    print("DFS preview:", str(dfs)[:200] + "...")
    
    # Test BFS
    print("\\n=== Testing BFS ===")
    print(f"BFS type: {type(bfs)}")
    print(f"BFS length: {len(bfs)} characters")
    print("BFS preview:", str(bfs)[:200] + "...")
    
    # Test UCS
    print("\\n=== Testing UCS ===")
    print(f"UCS type: {type(ucs)}")
    print(f"UCS length: {len(ucs)} characters")
    print("UCS preview:", str(ucs)[:200] + "...")
    
    # Test NetworkX algorithms
    print("\\n=== Testing NetworkX ===")
    print(f"NetworkX type: {type(networkx_algorithms)}")
    print(f"NetworkX length: {len(networkx_algorithms)} characters")
    print("NetworkX preview:", str(networkx_algorithms)[:200] + "...")
    
    # Test Wumpus World
    print("\\n=== Testing Wumpus World ===")
    print(f"Wumpus type: {type(wumpus)}")
    print(f"Wumpus length: {len(wumpus)} characters")
    print("Wumpus preview:", str(wumpus)[:200] + "...")
    
    print("\\n✓ Code printing tests completed!")

def test_algorithm_execution():
    """Test that algorithms can be executed."""
    print("\\nTesting algorithm execution...")
    
    from algorithmic_toolkit import dfs, bfs, ucs
    
    # Test DFS execution
    print("\\n=== Testing DFS Execution ===")
    try:
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
        
        result = dfs(test_graph, 'A')
        print(f"DFS result: {result}")
        print("✓ DFS execution successful!")
    except Exception as e:
        print(f"✗ DFS execution failed: {e}")
    
    # Test BFS execution
    print("\\n=== Testing BFS Execution ===")
    try:
        exec(str(bfs))
        
        result = bfs(test_graph, 'A')
        print(f"BFS result: {result}")
        print("✓ BFS execution successful!")
    except Exception as e:
        print(f"✗ BFS execution failed: {e}")
    
    # Test UCS execution
    print("\\n=== Testing UCS Execution ===")
    try:
        exec(str(ucs))
        
        # Create a weighted test graph
        weighted_graph = {
            'A': [('B', 2), ('C', 4)],
            'B': [('C', 1), ('D', 7)],
            'C': [('D', 3)],
            'D': []
        }
        
        path, cost = ucs(weighted_graph, 'A', 'D')
        print(f"UCS result: path={path}, cost={cost}")
        print("✓ UCS execution successful!")
    except Exception as e:
        print(f"✗ UCS execution failed: {e}")

def test_networkx_algorithms():
    """Test NetworkX algorithms execution."""
    print("\\nTesting NetworkX algorithms...")
    
    from algorithmic_toolkit import networkx_algorithms
    
    try:
        exec(str(networkx_algorithms))
        
        # Create an instance and test basic functionality
        alg = NetworkXAlgorithms()
        G = alg.create_sample_graph()
        
        print(f"Graph nodes: {list(G.nodes())}")
        print(f"Graph edges: {list(G.edges())}")
        
        # Test shortest path
        path, cost = alg.dijkstra_shortest_path(G, 'A', 'Z')
        print(f"Shortest path from A to Z: {path}, cost: {cost}")
        
        print("✓ NetworkX algorithms execution successful!")
    except Exception as e:
        print(f"✗ NetworkX execution failed: {e}")

def test_codestring_functionality():
    """Test the CodeString utility class."""
    print("\\nTesting CodeString functionality...")
    
    from algorithmic_toolkit.utils import CodeString
    
    # Create a test CodeString
    test_code = """
def test_function():
    print("This is a test function")
    return 42
"""
    
    cs = CodeString(test_code, "Test Function")
    
    print(f"CodeString type: {type(cs)}")
    print(f"CodeString length: {len(cs)}")
    print(f"CodeString description: {cs.get_description()}")
    print("CodeString content preview:", str(cs)[:100] + "...")
    
    # Test display method (will show syntax highlighting if pygments available)
    print("\\nTesting display method:")
    try:
        cs.display()
        print("✓ CodeString display successful!")
    except Exception as e:
        print(f"CodeString display failed: {e}")
    
    print("✓ CodeString functionality tests completed!")

def main():
    """Run all tests."""
    print("Algorithmic Toolkit Package Test Suite")
    print("=" * 50)
    
    # Run tests
    success = test_imports()
    if success:
        test_code_printing()
        test_algorithm_execution()
        test_networkx_algorithms()
        test_codestring_functionality()
        
        print("\\n" + "=" * 50)
        print("All tests completed!")
        print("\\nQuick usage example:")
        print("from algorithmic_toolkit import dfs, bfs, ucs, networkx_algorithms, wumpus")
        print("print(dfs)  # Shows complete DFS implementation")
        print("print(bfs)  # Shows complete BFS implementation")
        print("print(ucs)  # Shows complete UCS implementation")
        print("print(networkx_algorithms)  # Shows NetworkX algorithms")
        print("print(wumpus)  # Shows Wumpus World Prolog code")
    else:
        print("Package import failed. Please check installation.")

if __name__ == "__main__":
    main()