# Cachy-datastructure
# ⚡ Cachy: Memory Pool Data Structure

A memory-optimized cache data structure utilizing a localized **Memory Pool** and custom **Nodes** backed by NumPy arrays.

## 📦 Project Structure
* `cachy/node.py`: Defines the contiguous block node elements using NumPy.
* `cachy/memory_pool.py`: Manages allocation and lifecycle of the cache blocks.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* NumPy

### Code Usage Example
```python
import numpy as np
from cachy.node import Node

# Creating a cachy node holding 10 integer slots
my_node = Node(size=10, data_type=np.int32)
print(my_node.cachy_node)
