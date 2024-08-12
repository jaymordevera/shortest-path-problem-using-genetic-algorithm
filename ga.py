"""
Genetic Algorithm File

Description: This file contains the functions to simulate genetic algorithm.

Author: Jay De Vera (jaymordevera)
"""

import config
from math import sqrt
from random import randint, uniform


def is_chromosome_valid(chromosome):
    """Check whether the choromosome creates a valid path or not

    Args:
        chromosome (list): The chromosome to validate
    """
    prev_visited = 0
    num_of_gene = config.POINTS
    isPathValid = config._valid_paths
    
    for i in range(1, num_of_gene):
        if chromosome[i]:
            if isPathValid[prev_visited][i]:
                prev_visited = i
            else:
                return False
    
    return True


def generate_chromosome(isPathValid=config._valid_paths, num_of_gene=config.POINTS):
    """Generates a chromosome for the initial population

    Args:
        isPathValid (list, optional): Adjacency matrix created by the generated points and obstacles
        num_of_gene (int, optional): Length of a chromosome. Defaults to config.POINTS
    """
    
    chromosome = [-1]*num_of_gene
    chromosome[0], chromosome[-1] = 1, 1 # Start and Goal points are always visited
    
    isValid = False
    while not isValid:
        for i in range(1, num_of_gene-1):
            gene = 0 if uniform(0,1) > 0.5 else 1
            chromosome[i] = gene
            
        isValid = is_chromosome_valid(chromosome)

    return chromosome
    

def init_population(num_of_pop=config.POPULATION_SIZE):
    """Generate the initial population
    
    Args:
        num_of_pop (int, optional): Defaults to config.POPULATION_SIZE
    
    Return:
        population (list): List of valid chromosomes, duplicates may be allowed
    """
    
    population = []
    for _ in range(num_of_pop):
        population.append(generate_chromosome())
        
    return population
    
    
def fitness_function(chromosome):
    """Returns the fitness cost of a chromosome

    Args:
        chromosome (list, required): List of visited points
    Return:
        total_distance(float): Total distance travelled
    """
    
    # Returns distance between two points
    def distance(p1, p2):
        return sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    
    
    points = config._points
    prev_point = points[0]
    total_distance = 0
    
    for i in range(1, len(chromosome)):
        curr_point = points[i]
        
        if i < len(chromosome)-1:
            total_distance += distance(prev_point, curr_point) if chromosome[i] else 0
            prev_point = curr_point
        else:
            total_distance += distance(prev_point, curr_point)
            
    return total_distance        


def rank_population(population):
    """Ranks the population based on their fitness value
    
    Args:
        population (list, required): List of chromosomes to be evaluated in the population
    Return:
        chromosome_to_fitness (list): Sorted list of 2-tuple (path, score) from lowest to highest
    """
    
    fitness_score = []
    
    for chromosome in population:
        fitness_score.append((chromosome, fitness_function(chromosome)))
        
    chromosome_to_fitness = sorted(fitness_score, key=lambda x: x[1])
    
    return chromosome_to_fitness

    
def select_parents(population):
    """Select parents based on fitness function cost
    
    Args:
        population (list, required): List of chromosomes to produce offsprings
    """
    
    chromosome_to_fitness = rank_population(population)
    
    num_to_keep = config.POPULATION_SIZE//2
    
    half_population = chromosome_to_fitness[:num_to_keep]
    
    selected_parents = [chromosome[0] for chromosome in half_population]
    
    return selected_parents
    

def crossover_operator(parent1, parent2):
    """Create a new offspring from parent1 and parent2

    Args:
        parent1 (list): Father
        parent2 (list): Mother
    Return:
        offspring (list): Newly generated element of the solution space
    """
    
    split_site = randint(2, len(parent1)-2)
    
    if uniform(0,1) > 0.5:
        parent = parent1
    else:
        parent = parent2
    
    return parent1[:split_site] + parent2[split_site:] if uniform(0,1) > 0.5 else parent


def mutation_operator(offspring):
    """Mutate an offspring

    Args:
        offspring (list): The chromosome to mutate
    """
    
    mutated_offspring = offspring.copy()
    
    if uniform(0,1) < config.MUTATION_RATE:
        isValid = False
        
        tries = 100
        while not isValid and tries != 0:
            flip_site = randint(1, len(offspring)-2)
            mutated_offspring[flip_site] = abs(offspring[flip_site]-1)
            
            isValid = is_chromosome_valid(mutated_offspring)
            tries -= 1
        
    
    return mutated_offspring