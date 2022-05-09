from collections import deque
from maze import maze
from index import Node, MazeProblem
import maze


def breath_first_search(problem):
    node = Node(problem.init)
    if problem.goal_test(node.position):
        # Return solution
        return node.solution()
    frontier, explored = deque([node]), set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.position)

        for child in node.expand(problem):
            if child.position not in explored and child not in frontier:
                if problem.goal_test(child.position):
                    return child.solution()
                frontier.append(child)
    return None

# if __name__ == "__main__":
#     init = (0, 9)
#     goal = (9, 0)
#     problem = MazeProblem(init, goal, maze.maze5)
#     solution = breath_first_search(problem)
#     print("solution: ", solution)