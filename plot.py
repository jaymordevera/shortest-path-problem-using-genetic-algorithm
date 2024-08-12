"""
Plot File

Description: This contains the functions for plotting the population.

Author: Jay De Vera (jaymordevera)
"""

import config
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.patches as patches
from ga import fitness_function

def plot_obstacles(obstacles=config._obstacles):
    """Plot all generated obstacles

    Args:
        obstacles (list): List of corner coordinates of the rectangles
    """

    hasLegend = False
    for rect in obstacles:
        x, y = [], []
        
        for corner in rect:
            x.append(corner[0])
            y.append(corner[1])
    
        plt.fill(x,y, 'b', hatch='/') if hasLegend else plt.fill(x,y, 'b', hatch='/', label='Obstacles')
        hasLegend = True


def plot_points(points=config._points):
    """Plot all generated points

    Args:
        points (list): List of the generated points
    """
    x, y = [], []
    
    # Separate start and goal points
    start, goal = points[0], points[-1]
    for i in range(1, len(points)-1):
        x.append(points[i][0])
        y.append(points[i][1])
    
    plt.plot(x, y, 'o', color='black')
    
    # Annotate each point with its index
    #for i, (x, y) in enumerate(points):
    #    plt.text(x+3, y+3, f'{i}', fontsize=11, ha='right', va='top')
    
    plt.plot(start[0], start[1], color='green', marker='s', label='Start')
    plt.plot(goal[0], goal[1], color='red', marker='s', label='Goal')


def plot_chromosome(chromosome, points=config._points):
    """Plot a chromosome

    Args:
        chromosome (list): List of 1s and 0s
    """
    
    point1 = 0
    x, y = [points[0][0]], [points[0][1]]
    
    for i in range(len(chromosome)):
        if chromosome[i]:
            x.append(points[i][0])
            y.append(points[i][1])
            
    plt.plot(x,y, color='black')
    

def simulation(all_solution):
    """Simulate the genetic algorithm

    Args:
        parameters (list): List of population
    """
    fig, ax = plt.subplots(figsize=(8,5))
    
    # Function for animation
    def plot_path(solution):
        ax.clear()
        plot_obstacles()
        plot_points()
        plot_chromosome(solution[0])
        plt.title("Shortest Path Problem using Genetic Algorithm")
        plt.legend()
        plt.annotate(f'Generation: {solution[1]}, Fitness Score: {round(fitness_function(solution[0]), 4)}', (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
    
    # Creating animation
    anim = FuncAnimation(fig, plot_path, frames=all_solution)
    
    # Save the animation as GIF 
    my_writer = PillowWriter(fps=5)
    anim.save('outputs\SPPGA.gif', writer=my_writer, dpi=300)
    
    plt.show()
    

def convergence(_average_fitness):
    plt.figure(2)
    
    x = range(len(_average_fitness))
    y = _average_fitness
    
    # Plotting
    plt.plot(x,y, color='black', linewidth=1, marker='o')
    plt.title("Convergence of Genetic Algorithm")
    plt.xlabel("Generation")
    plt.ylabel("Average Fitness Score")
    
    # Save Figure
    plt.savefig("outputs\convergence.png", dpi=300)
    
    plt.show()
    