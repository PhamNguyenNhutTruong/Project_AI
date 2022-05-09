from math import sqrt
from maze import maze
from index import Node, MazeProblem


def a_start(problem):
    start_node = Node(problem.init)

    # open_list: frontier, closed_list: explored
    open_list, closed_list = [start_node], []

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Check if we found the goal
        if problem.goal_test(current_node.position):
            return current_node.solution()

        # Loop throught list children

        for child in current_node.expand(problem):
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            # Create the f, g, h values
            child.g = current_node.g + 1
            child.h = sqrt(
                ((child.position[0] - problem.goal[0]) ** 2)
                + ((child.position[1] - problem.goal[1]) ** 2)
            )
            child.f = child.g + child.h

            # Child is already in the open list
            if len(
                [
                    open_node
                    for open_node in open_list
                    if open_node == child and child.g > open_node.g
                ]
            ):
                continue

            # Add the child to the open list
            open_list.append(child)


# if __name__ == "__main__":
#     init = (0, 0)
#     goal = (9, 9)
#     problem = MazeProblem(init, goal, maze)

#     solution = a_start(problem)
#     print(solution)