# Algorithmic Toolkit

A comprehensive Python package that provides easy access to various search algorithms and game implementations through simple print statements.

## Features

- **Search Algorithms**: DFS, BFS, UCS with complete implementations
- **Graph Algorithms**: NetworkX-based algorithms for graph analysis
- **Game Implementations**: Complete Wumpus World in Prolog
- **Code Printing**: Print complete source code with simple `print()` statements
- **Educational Focus**: Perfect for learning and teaching algorithms

## Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/yourusername/algorithmic-toolkit.git
```

### From Local Source

```bash
git clone https://github.com/yourusername/algorithmic-toolkit.git
cd algorithmic-toolkit
pip install -e .
```

### Using requirements.txt

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from algorithmic_toolkit import dfs, bfs, ucs, networkx_algorithms, wumpus

# Print complete DFS algorithm code
print(dfs)

# Print complete BFS algorithm code  
print(bfs)

# Print complete UCS algorithm code
print(ucs)

# Print NetworkX-based graph algorithms
print(networkx_algorithms)

# Print Wumpus World Prolog implementation
print(wumpus)
```

## Detailed Usage

### Search Algorithms

The package provides three fundamental search algorithms:

#### Depth-First Search (DFS)
```python
from algorithmic_toolkit import dfs

# Access the complete DFS implementation
print(dfs)

# Use the code in your projects
exec(str(dfs))

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

result = dfs(graph, 'A')
print("DFS traversal:", result)
```

#### Breadth-First Search (BFS)
```python
from algorithmic_toolkit import bfs

print(bfs)

# The BFS implementation includes:
# - Basic BFS traversal
# - BFS with level information
# - BFS shortest path finding
# - BFS all paths finding
```

#### Uniform Cost Search (UCS)
```python
from algorithmic_toolkit import ucs

print(ucs)

# The UCS implementation includes:
# - Basic UCS path finding
# - UCS with all paths
# - UCS with heuristic support
```

### NetworkX Graph Algorithms

```python
from algorithmic_toolkit import networkx_algorithms

print(networkx_algorithms)

# The NetworkX implementation includes:
# - Graph creation and visualization
# - Shortest path algorithms (Dijkstra, Bellman-Ford)
# - Minimum spanning tree
# - Topological sort
# - Centrality measures
# - Graph analysis (diameter, radius, clustering)
# - And much more...
```

### Wumpus World Game

```python
from algorithmic_toolkit import wumpus

print(wumpus)

# The Wumpus World implementation includes:
# - Complete game logic in Prolog
# - Agent perception system
# - Action execution framework
# - Game state management
# - Win/lose conditions
```

## Package Structure

```
algorithmic_toolkit/
├── __init__.py                 # Package initialization
├── algorithms/                 # Search algorithms
│   ├── __init__.py
│   ├── search.py              # DFS, BFS, UCS implementations
│   └── graph.py               # NetworkX algorithms
├── games/                     # Game implementations
│   ├── __init__.py
│   └── wumpus.py              # Wumpus World Prolog
└── utils/                     # Utility modules
    ├── __init__.py
    └── code_printer.py        # CodeString class for printing
```

## Advanced Features

### CodeString Class

The package uses a custom `CodeString` class that:
- Maintains code content as a string
- Provides formatted printing when used with `print()`
- Supports syntax highlighting (if pygments is available)
- Allows code execution with `exec()`

```python
from algorithmic_toolkit.utils import CodeString

# Create custom code snippets
my_code = CodeString("""
def hello_world():
    print("Hello, World!")
    return "Success"
""", "Sample Hello World Function")

print(my_code)  # Prints with description
print(my_code.get_code())  # Gets raw code
my_code.display()  # Displays with syntax highlighting
```

### Educational Applications

This package is ideal for:
- **Computer Science Education**: Teaching search algorithms
- **AI Coursework**: Demonstrating pathfinding and game AI
- **Programming Workshops**: Code examples and demonstrations
- **Self-Study**: Learning algorithm implementations

## Examples

### Complete Search Example

```python
from algorithmic_toolkit import dfs, bfs, ucs

# Execute DFS, BFS, and UCS on the same graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS traversal
exec(str(dfs))
dfs_result = dfs(graph, 'A')
print("DFS:", dfs_result)

# BFS traversal  
exec(str(bfs))
bfs_result = bfs(graph, 'A')
print("BFS:", bfs_result)

# UCS on weighted graph
exec(str(ucs))
weighted_graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}
ucs_result = ucs(weighted_graph, 'A', 'D')
print("UCS path and cost:", ucs_result)
```

### Graph Analysis Example

```python
from algorithmic_toolkit import networkx_algorithms

exec(str(networkx_algorithms))

# Create and analyze a graph
alg = NetworkXAlgorithms()
G = alg.create_sample_graph()

# Find shortest path
path, cost = alg.dijkstra_shortest_path(G, 'A', 'Z')
print(f"Shortest path from A to Z: {path}, cost: {cost}")

# Calculate centrality measures
centrality = alg.betweenness_centrality(G)
print("Betweenness centrality:", centrality)

# Visualize the graph
alg.visualize_graph(G, "Sample Graph")
```

## Requirements

- Python 3.6+
- NetworkX 2.5+
- Matplotlib 3.3.0+
- Pygments 2.7.0+ (optional, for syntax highlighting)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
git clone https://github.com/yourusername/algorithmic-toolkit.git
cd algorithmic-toolkit
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Code Style

```bash
black algorithmic_toolkit/
flake8 algorithmic_toolkit/
mypy algorithmic_toolkit/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by educational needs in AI and algorithms courses
- Built with NetworkX for graph algorithms
- Uses Pygments for syntax highlighting
- Designed for educational and research purposes

## Support

If you find this package helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 📖 Contributing documentation
- 🔧 Submitting improvements

## Changelog

### Version 1.0.0 (Initial Release)
- DFS, BFS, UCS search algorithms
- NetworkX-based graph algorithms
- Complete Wumpus World Prolog implementation
- Code printing functionality
- Educational examples and documentation