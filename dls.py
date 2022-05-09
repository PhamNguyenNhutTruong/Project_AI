from index import Node, MazeProblem
from maze import maze


def depth_limit_search(problem, limit):
    node = Node(problem.init)
    return recursive_dls(node, problem, limit)


def recursive_dls(node, problem, limit):
    if problem.goal_test(node.position):
        return node.solution()
    elif limit == 0:
        return 0  # cutoff
    else:
        cutoff_occurred = False
        for action in problem.actions(node.position):
            child = Node(action, node)
            result = recursive_dls(child, problem, limit - 1)
            if result == 0:
                cutoff_occurred = True
            elif result != -1:
                return result
        if cutoff_occurred:
            return 0
        else:
            return -1  # Failure


def iterative_deepening_search(problem):
    depth = 0
    while True:
        print(depth)
        solution = depth_limit_search(problem, depth)
        if solution != 0 and solution != -1:
            return solution
        if depth > 100:
            return None
        depth += 1


# if __name__ == "__main__":
#     init = (0, 0)
#     goal = (9, 9)
#     problem = MazeProblem(init, goal, maze)
#     solution = iterative_deepening_search(problem)
#     print(solution)