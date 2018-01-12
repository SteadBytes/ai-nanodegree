# Implementing Search

## Nodes
Each state is a **node** consisting of:
* Current State
* Action to reach node
* Cost to node
* Pointer to Parent node

A **Path** is a sequence of nodes,  traversed by follwing the parent pointers on each node.

## Frontier
* Operations:
    * Remove best item
    * Add in new items
    * Membership test
* Implementation:
    * Priority Queue
* Representation:
    * Set
* Build:
    * Hash Table
    * Tree

## Explored
* Operations:
    * Add new members
    * Membership test
* Representation:
    * Single Set
* Build:
    * Hash Table
    * Tree