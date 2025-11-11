#!/usr/bin/env python3
"""
Simple test to verify basic functionality.
"""

import sys
sys.path.insert(0, '/mnt/okcomputer/output')

def test_basic_import():
    """Test basic import functionality."""
    print("Testing basic imports...")
    
    try:
        # Test importing the CodeString class
        from algorithmic_toolkit.utils.code_printer import CodeString
        print("✓ CodeString import successful!")
        
        # Test creating a simple CodeString
        test_code = "def hello(): print('Hello World!')"
        cs = CodeString(test_code, "Test Function")
        
        print(f"✓ CodeString creation successful!")
        print(f"Content: {cs}")
        print(f"Description: {cs.get_description()}")
        
        return True
        
    except Exception as e:
        print(f"✗ Basic import failed: {e}")
        return False

def test_search_algorithms():
    """Test search algorithms."""
    print("\\nTesting search algorithms...")
    
    try:
        # Test importing search algorithms
        from algorithmic_toolkit.algorithms.search import dfs, bfs, ucs
        
        print("✓ Search algorithms import successful!")
        print(f"DFS length: {len(dfs)} characters")
        print(f"BFS length: {len(bfs)} characters")
        print(f"UCS length: {len(ucs)} characters")
        
        # Test printing DFS
        print("\\nDFS Algorithm Preview:")
        print("=" * 50)
        print(str(dfs)[:500] + "...")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"✗ Search algorithms test failed: {e}")
        return False

def test_wumpus():
    """Test Wumpus World."""
    print("\\nTesting Wumpus World...")
    
    try:
        from algorithmic_toolkit.games.wumpus import wumpus
        
        print("✓ Wumpus import successful!")
        print(f"Wumpus length: {len(wumpus)} characters")
        
        # Test printing Wumpus
        print("\\nWumpus World Prolog Preview:")
        print("=" * 50)
        print(str(wumpus)[:500] + "...")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"✗ Wumpus test failed: {e}")
        return False

def main():
    """Run simple tests."""
    print("Simple Functionality Test")
    print("=" * 30)
    
    tests = [
        test_basic_import,
        test_search_algorithms,
        test_wumpus
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\\n" + "=" * 30)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\\n🎉 All simple tests passed!")
        print("\\nThe package is ready to use!")
        print("\\nUsage example:")
        print("import sys")
        print("sys.path.insert(0, '/mnt/okcomputer/output')")
        print("from algorithmic_toolkit.algorithms.search import dfs")
        print("print(dfs)  # This will print the complete DFS algorithm!")

if __name__ == "__main__":
    main()