# Shortest Path Problem using Genetic Algorithm

![Genetic Algorithm Simulation](https://github.com/jaymordevera/shortest-path-problem-using-genetic-algorithm/blob/main/outputs/SPPGA.gif)

## Overview

Genetic Algorithm (GA) is an optimization and search technique based on the principles of genetics and natural selection. We apply the basic methods in GA to one of network optimization problems called *shortest path problem*.

The idea is simple we want to determine the shortest path from the starting point to the end goal.

## The Problem

Suppose we have $N$ points and $M$ obstacles. They are positioned in a way such that no two objects overlap. Our goal is to find the path with minimum distance from the source point to the destination point while avoiding collisions with any obstacles. 

Note that as $N$ and $M$ increase, the total number of possible paths increases as well. Stochastic methods like GA are great in handling problems with very large yet finite solution space.

## Instructions
1. Make sure you have [Python 3.10](https://www.python.org/downloads/) or above.
2. Open [config.py](config.py#L9-L17) to modify the GA parameters to your liking.
3. Run [main.py](main.py) to simulate GA.

## References
1. [genetic-algorithm-shortest-path by rofe-dl](https://github.com/rofe-dl/genetic-algorithm-shortest-path)
2. [genetic-algorithm-path-planning by Yaaximus](https://github.com/Yaaximus/genetic-algorithm-path-planning)
