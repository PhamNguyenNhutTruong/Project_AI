from math import sqrt
from maze import maze, maze3
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

        if current_node not in closed_list:
            closed_list.append(current_node)

        # Check if we found the goal
        if problem.goal_test(current_node.position):
            return current_node.solution(), closed_list

        # Expand children
        children = current_node.expand(problem)

        # Check len children
        if len(children) == 0:
            return None

        # Loop throught list children
        for child in children:
            flag = False
            for closed_child in closed_list:
                if child == closed_child:
                    flag = True
            # Don't append child exist in explored
            if flag:
                continue

            # Create the f, g, h values
            child.g = current_node.g + 1
            # child.h = sqrt(
            #     ((child.position[0] - problem.goal[0]) ** 2)
            #     + ((child.position[1] - problem.goal[1]) ** 2)
            # )
            child.h = abs((child.position[0] - problem.goal[0])) + abs(
                (child.position[1] - problem.goal[1])
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
            if child not in open_list:
                open_list.append(child)
    return None, None


if __name__ == "__main__":
    init = (5, 8)
    goal = (8, 7)
    problem = MazeProblem(init, goal, maze3)

    solution,explored = a_start(problem)
    print(solution)
    print("=======================================================================")
    print(explored)