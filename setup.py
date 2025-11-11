"""
Setup configuration for Algorithmic Toolkit package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="algorithmic-toolkit",
    version="1.0.0",
    author="Algorithmic Toolkit Team",
    author_email="contact@algorithmic-toolkit.com",
    description="A comprehensive package for search algorithms and game implementations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/algorithmic-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    install_requires=[
        "networkx>=2.5",
        "matplotlib>=3.3.0",
        "pygments>=2.7.0",  # For syntax highlighting
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "nbsphinx>=0.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "algorithmic-toolkit=algorithmic_toolkit.cli:main",
        ],
    },
    keywords=[
        "algorithms",
        "search",
        "graph",
        "dfs",
        "bfs",
        "ucs",
        "networkx",
        "wumpus-world",
        "prolog",
        "artificial-intelligence",
        "education",
        "learning",
    ],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/algorithmic-toolkit/issues",
        "Source": "https://github.com/yourusername/algorithmic-toolkit",
        "Documentation": "https://algorithmic-toolkit.readthedocs.io/",
    },
)