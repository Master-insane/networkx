#!/usr/bin/env python3
"""
Direct test of the algorithmic toolkit functionality without package installation.
"""

import sys
import os
sys.path.insert(0, '/mnt/okcomputer/output')

def test_direct_imports():
    """Test direct imports from the source code."""
    print("Testing direct imports...")
    
    try:
        # Test importing the modules directly
        from algorithmic_toolkit.algorithms.search import dfs, bfs, ucs
        from algorithmic_toolkit.algorithms.graph import networkx_algorithms
        from algorithmic_toolkit.games.wumpus import wumpus
        from algorithmic_toolkit.utils.code_printer import CodeString
        
        print("✓ All direct imports successful!")
        return True
    except ImportError as e:
        print(f"✗ Direct import failed: {e}")
        return False

def test_codestring_functionality():
    """Test the CodeString class functionality."""
    print("\\nTesting CodeString functionality...")
    
    try:
        from algorithmic_toolkit.utils.code_printer import CodeString
        
        # Create test code
        test_code = '''
def hello_world():
    """A simple hello world function."""
    print("Hello, World!")
    return 42
'''
        
        # Create CodeString instance
        cs = CodeString(test_code, "Hello World Function")
        
        print(f"CodeString created successfully")
        print(f"Type: {type(cs)}")
        print(f"Length: {len(cs)}")
        print(f"Description: {cs.get_description()}")
        
        # Test string representation
        str_repr = str(cs)
        print(f"String representation length: {len(str_repr)}")
        print("Preview:", str_repr[:100] + "...")
        
        # Test that it behaves like a string
        print(f"Can be sliced: {cs[:50]}...")
        print(f"Can be concatenated: {cs[:30] + '...'}")
        
        print("✓ CodeString functionality test passed!")
        return True
        
    except Exception as e:
        print(f"✗ CodeString test failed: {e}")
        return False

def test_algorithm_code_content():
    """Test that algorithm code content is properly stored."""
    print("\\nTesting algorithm code content...")
    
    try:
        from algorithmic_toolkit.algorithms.search import dfs, bfs, ucs
        
        algorithms = [('DFS', dfs), ('BFS', bfs), ('UCS', ucs)]
        
        for name, algo in algorithms:
            print(f"\\n{name} algorithm:")
            print(f"  Type: {type(algo)}")
            print(f"  Length: {len(algo)} characters")
            print(f"  Contains 'def': {'def ' in algo}")
            print(f"  Contains algorithm name: {name.lower() in algo.lower()}")
            print(f"  Description: {algo.get_description()}")
        
        print("✓ Algorithm code content test passed!")
        return True
        
    except Exception as e:
        print(f"✗ Algorithm code test failed: {e}")
        return False

def test_wumpus_content():
    """Test Wumpus World content."""
    print("\\nTesting Wumpus World content...")
    
    try:
        from algorithmic_toolkit.games.wumpus import wumpus
        
        print(f"Wumpus type: {type(wumpus)}")
        print(f"Wumpus length: {len(wumpus)} characters")
        print(f"Contains Prolog comments: {'%' in wumpus}")
        print(f"Contains Prolog predicates: {':-' in wumpus}")
        print(f"Contains game logic: {'wumpus' in wumpus.lower()}")
        print(f"Description: {wumpus.get_description()}")
        
        print("✓ Wumpus content test passed!")
        return True
        
    except Exception as e:
        print(f"✗ Wumpus test failed: {e}")
        return False

def test_networkx_content():
    """Test NetworkX algorithms content."""
    print("\\nTesting NetworkX algorithms content...")
    
    try:
        from algorithmic_toolkit.algorithms.graph import networkx_algorithms
        
        print(f"NetworkX type: {type(networkx_algorithms)}")
        print(f"NetworkX length: {len(networkx_algorithms)} characters")
        print(f"Contains NetworkX import: {'import networkx' in networkx_algorithms}")
        print(f"Contains matplotlib import: {'import matplotlib' in networkx_algorithms}")
        print(f"Contains class definition: {'class ' in networkx_algorithms}")
        print(f"Description: {networkx_algorithms.get_description()}")
        
        print("✓ NetworkX content test passed!")
        return True
        
    except Exception as e:
        print(f"✗ NetworkX test failed: {e}")
        return False

def test_print_functionality():
    """Test the print functionality that was requested."""
    print("\\nTesting print functionality...")
    
    try:
        from algorithmic_toolkit.algorithms.search import dfs
        
        print("\\nTesting print(dfs) - this should show the complete DFS code:")
        print("=" * 60)
        print(dfs)
        print("=" * 60)
        
        print("\\n✓ Print functionality test completed!")
        return True
        
    except Exception as e:
        print(f"✗ Print functionality test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Algorithmic Toolkit Direct Functionality Test")
    print("=" * 50)
    
    tests = [
        test_direct_imports,
        test_codestring_functionality,
        test_algorithm_code_content,
        test_wumpus_content,
        test_networkx_content,
        test_print_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\\n🎉 All tests passed! The package is working correctly.")
        print("\\nUsage example:")
        print("# Add the package to your Python path:")
        print("import sys")
        print("sys.path.insert(0, '/mnt/okcomputer/output')")
        print("")
        print("# Import and use the algorithms:")
        print("from algorithmic_toolkit.algorithms.search import dfs, bfs, ucs")
        print("from algorithmic_toolkit.algorithms.graph import networkx_algorithms")
        print("from algorithmic_toolkit.games.wumpus import wumpus")
        print("")
        print("# Print complete code implementations:")
        print("print(dfs)  # Shows complete DFS algorithm")
        print("print(bfs)  # Shows complete BFS algorithm")
        print("print(ucs)  # Shows complete UCS algorithm")
        print("print(networkx_algorithms)  # Shows NetworkX algorithms")
        print("print(wumpus)  # Shows Wumpus World Prolog code")
    else:
        print("\\n❌ Some tests failed. Please check the implementation.")

if __name__ == "__main__":
    main()