"""
Parameters Section

Description: This contains the parameters of the Genetic Algorithm (GA). You may change them as you please.

Author: Jay De Vera (jaymordevera)
"""

# Genetic Algorithm Parameteters
GENERATION = 25
POPULATION_SIZE = 20
MUTATION_RATE = 0.5
CROSSOVER_RATE = 0.5

# Objects Parameteters
POINTS = 30
OBSTACLES = 15



"""
Tools Section

Description: This contains the functions generating and validating points, obstacles, genetic operators, etc.

Author: Jay De Vera (jaymordevera)
"""

from random import randint
from shapely.geometry import LineString, Polygon # Use `pip install shapely` if the module is not found.


def init_obstacles(num_of_obstacles=OBSTACLES):
    """Generate random obstacles
    
    Args:
        num_of_obstacles (int, optional): Number of obstacles to be generated. Defaults to config.OBSTACLES.
        
    Return:
        obstacles (list): List of corner coordinates of the rectangles
    """

    rectangles = []
    for i in range(num_of_obstacles):
        x, y = randint(20,70), randint(20,70) # To ensure that the obstacles are near the center
        w, h = randint(5, 20), randint(5,20)
        
        rectangles.append([(x,y), (x,y+h), (x+w, y+h), (x+w,y)]) # Corners: Lower Left, Lower Right, Top Left, Top Right
    
    return rectangles
     

def init_points(obstacles, num_of_points=POINTS):
    """Generate random points
    
    Args:
        rectangles (list, required): Coordinates of the corners of the obstacles
        num_of_points (int, optional): Number of points to be generated. Defaults to config.POINTS.
        
    Return:
        points (list): List of valid points
    """

    points = [(0,0)]
    
    for i in range(num_of_points-2):
        x, y = randint(10,90), randint(10,90)
        
        while not valid_point([x,y], obstacles):
            x, y = randint(10,90), randint(10,90)
        
        points.append((x,y))
    
    points.append((100,100))
    
    return points


def valid_point(point, obstacles):
    """Check if the point is within or not any obstacles
    
    Args:
        points (list, required): A generated point
        rectangles (list, optional): List of generated obstacles
        
    Return:
        isValid (bool): True - No points are within any obstacles. False - Otherwise.
    """
    x, y = point[0], point[1]
    padding = 10
    isValid = True
    
    for rect in obstacles:
        if rect[0][0] - padding <= x <= rect[3][0] + padding and rect[0][1] - padding <= y <= rect[1][1] + padding:
            isValid = False
            
    return isValid


def path_obstacle_matrix(points, obstacles):
    """Generate an adjacency matrix to check connection of points
        
        Args:
            points (list, required): List of generated points
            obstacles (list, optional): List of generated obstacles
            
        Return:
            adj_mat (list): An adjacency matrix.
    """
    
    # Function to check if a path overlaps to any obstacles
    def do_overlap(path):
        line = LineString(path)
        
        for rect in obstacles:
            poly = Polygon(rect)
            if line.intersects(poly):
                return 0
        
        return 1  

    adj_mat = [[-1]*len(points) for _ in range(len(points))]
    
    for i in range(len(points)):
        for j in range(len(points)):
            line = [points[i], points[j]]
            adj_mat[i][j] = do_overlap(line)
    
    return adj_mat


# Initializing Global Variables
def init_global():
    _obstacles = init_obstacles()
    _points = init_points(_obstacles)
    _valid_paths = path_obstacle_matrix(_points, _obstacles)
    
    return _points, _obstacles, _valid_paths


_points, _obstacles, _valid_paths = init_global()