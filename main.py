"""
Main File

Description: Execute to visualize genetic algorithm

Author: Jay De Vera (jaymordevera)
"""

# Import files and libraries
import config
import plot
import ga
import matplotlib.pyplot as plt
from random import randint

def main():
    # Initiate global variables
    config.init_global()

    # Storing Data
    generated_solutions, average_fitness = [], []

    # Genetic Algorithm Implementation
    population = ga.init_population()

    for gen in range(config.GENERATION):
        selected_parents = ga.select_parents(population)
        
        num_of_parents = len(selected_parents)
        num_of_child = config.POPULATION_SIZE-num_of_parents
        
        curr_population = selected_parents.copy()
        
        while num_of_child != 0:
            m, f = randint(0, num_of_parents-1), randint(0, num_of_parents-1)
            mother, father = selected_parents[m], selected_parents[f]
            
            non_mutated_offspring = ga.crossover_operator(mother, father)
            offspring = ga.mutation_operator(non_mutated_offspring)

            if ga.is_chromosome_valid(offspring):
                curr_population.append(offspring)
                num_of_child -= 1
        
        population = curr_population.copy()
        
        # Best Fitness Score
        ranked = ga.rank_population(population)
        generated_solutions.append((ranked[0][0], gen))
        
        # Average Fitness Score
        total = 0
        for i in ranked:
            total += i[1]
        average_fitness.append(total/config.POPULATION_SIZE)

    # Simulation
    plot.simulation(generated_solutions)
    
    # Convergence Plot
    plot.convergence(average_fitness)


if __name__ == '__main__':
    main()