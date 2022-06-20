import bisect

"""
Defining a class for the problem structure that we will solve with a search.
The Problem class is an abstract class from which we make inheritance to define the basic
characteristics of every problem we want to solve
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """Given a state, return a dictionary of {action : state} pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once.

        :param state: given state
        :return:  dictionary of {action : state} pairs reachable
                  from this state
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """Given a state, return a list of all actions possible
        from that state

        :param state: given state
        :return: list of actions
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """Given a state and action, return the resulting state

        :param state: given state
        :param action: given action
        :return: resulting state
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares
        the state to self.goal, as specified in the constructor. Implement
        this method if checking against a single self.goal is not enough.

        :param state: given state
        :return: is the given state a goal state
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from state1
        via action, assuming cost c to get up to state1. If the problem is such
        that the path doesn't matter, this function will only look at state2.
        If the path does matter, it will consider c and maybe state1 and action.
        The default method costs 1 for every step in the path.

        :param c: cost of the path to get up to state1
        :param state1: given current state
        :param action: action that needs to be done
        :param state2: state to arrive to
        :return: cost of the path after executing the action
        :rtype: float
        """
        return c + 1

    def value(self):
        """For optimization problems, each state has a value.
        Hill-climbing and related algorithms try to maximize this value.

        :return: state value
        :rtype: float
        """
        raise NotImplementedError


"""
Definition of the class for node structure of the search.
The class Node is not inherited
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create node from the search tree,  obtained from the parent by
        taking the action

        :param state: current state
        :param parent: parent state
        :param action: action
        :param path_cost: path cost
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node.

        :param problem: given problem
        :return: list of available nodes in one step
        :rtype: list(Node)
        """
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Return a child node from this node

        :param problem: given problem
        :param action: given action
        :return: available node  according to the given action
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Return the sequence of actions to go from the root to this node.

        :return: sequence of actions
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Return the sequence of states to go from the root to this node.

        :return: list of states
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node.

        :return: list of states from the path
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """We want the queue of nodes at breadth_first_search or
    astar_search to not contain states-duplicates, so the nodes that
    contain the same condition we treat as the same. [Problem: this can
    not be desirable in other situations.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Definitions of helper structures for storing the list of generated, but not checked nodes
"""


class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): Last In First Out Queue (stack).
        FIFOQueue(): First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Adds the item into the queue

        :param item: given element
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Adds the items into the queue

        :param items: given elements
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Returns the first element of the queue

        :return: first element
        """
        raise NotImplementedError

    def __len__(self):
        """Returns the number of elements in the queue

        :return: number of elements in the queue
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Check if the queue contains the element item

        :param item: given element
        :return: whether the queue contains the item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """A queue in which the minimum (or maximum) element is returned first
     (as determined by f and order). This structure is used in
     informed search"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: sorting function, if order is min, returns the element
                      with minimal f (x); if the order is max, then returns the
                      element with maximum f (x).
        :param f: function f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


"""
Uninformed graph search
The main difference is that here we do not allow loops,
i.e. repetition of states
"""


def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
     If two paths reach a state, only use the best one.

    :param problem: given problem
    :param fringe: empty queue
    :return: Node
    """
    closed = {}
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    """Search the shallowest nodes in the search tree first.

    :param problem: given problem
    :return: Node
    """
    return graph_search(problem, FIFOQueue())


# ['SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'SvrtiDesno', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'ProdolzhiPravo', 'SvrtiLevo', 'ProdolzhiPravo', 'ProdolzhiPravo']

def convertToTuple(list_to_convert):
    converted_to_tuple = list()
    for x, y in list_to_convert:
        converted_to_tuple.append(tuple((x, y)))
    return tuple(converted_to_tuple)


def convertToList(tuple_to_convert):
    converted_to_list = list()
    for x, y in tuple_to_convert:
        converted_to_list.append([x, y])
    return converted_to_list


def prodolzhiPravo(snake, green_apples, red_apples):
    """prodolzhi pravo funkcija vo site 4 nasoki odnosno orientacii na zmijata
    Gore, Dole, Levo , Desno"""
    snake_temp = snake[:]
    green_apples_temp = green_apples[:]
    first_pos_snake = snake_temp[0]
    second_pos_snake = snake_temp[1]
    temp_snake = []
    temp_green_apples = []

    first_pos_x, first_pos_y = first_pos_snake[0], first_pos_snake[1]
    second_pos_x, second_pos_y = second_pos_snake[0], second_pos_snake[1]

    # Prodolzi pravo od momentalnata nasoka nadole
    if first_pos_x == second_pos_x and first_pos_y == second_pos_y - 1:
        if first_pos_y > 0 and [first_pos_x, first_pos_y - 1] != [first_pos_x, first_pos_y] and \
                (first_pos_x, first_pos_y - 1) not in red_apples \
                and [first_pos_x, first_pos_y - 1] not in snake_temp:
            new_first_post = [first_pos_x, first_pos_y - 1]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x, first_pos_y - 1] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x, first_pos_y - 1])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Prodolzi pravo od momentalnata nasoka nagore
    if first_pos_x == second_pos_x and first_pos_y == second_pos_y + 1:
        if first_pos_y < 9 and [first_pos_x, first_pos_y + 1] != [first_pos_x, first_pos_y] \
                and (first_pos_x, first_pos_y + 1) not in red_apples\
                and [first_pos_x, first_pos_y + 1] not in snake_temp:
            new_first_post = [first_pos_x, first_pos_y + 1]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x, first_pos_y + 1] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x, first_pos_y + 1])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Prodolzi pravo od momentalnata nasoka nalevo
    if first_pos_y == second_pos_y and first_pos_x == second_pos_x - 1:
        if first_pos_x > 0 and [first_pos_x - 1, first_pos_y] != [first_pos_x, first_pos_y] \
                and (first_pos_x - 1, first_pos_y) not in red_apples\
                and [first_pos_x - 1, first_pos_y] not in snake_temp:
            new_first_post = [first_pos_x - 1, first_pos_y]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x - 1, first_pos_y] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x - 1, first_pos_y])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Prodolzi pravo od momentalnata nasoka nadesno
    if first_pos_y == second_pos_y and first_pos_x == second_pos_x + 1:
        if first_pos_x < 9 and [first_pos_x + 1, first_pos_y] != [first_pos_x, first_pos_y] \
                and (first_pos_x + 1, first_pos_y) not in red_apples\
                and [first_pos_x + 1, first_pos_y] not in snake_temp:
            new_first_post = [first_pos_x + 1, first_pos_y]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x + 1, first_pos_y] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x + 1, first_pos_y])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    return temp_snake, temp_green_apples


def svrtiLevo(snake, green_apples, red_apples):
    snake_temp = snake[:]
    green_apples_temp = green_apples[:]
    first_pos_snake = snake_temp[0]
    second_pos_snake = snake_temp[1]
    temp_snake = []
    temp_green_apples = []
    first_pos_x, first_pos_y = first_pos_snake[0], first_pos_snake[1]
    second_pos_x, second_pos_y = second_pos_snake[0], second_pos_snake[1]

    # Svrti levo od momentalnata nasoka nadole:
    if first_pos_x == second_pos_x and first_pos_y == second_pos_y - 1:
        if first_pos_x < 9 and [first_pos_x + 1, first_pos_y] != [first_pos_x, first_pos_y] \
                and (first_pos_x + 1, first_pos_y) not in red_apples\
                and [first_pos_x + 1, first_pos_y] not in snake_temp:
            new_first_post = [first_pos_x + 1, first_pos_y]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x + 1, first_pos_y] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x + 1, first_pos_y])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Svrti levo od momentalnata nasoka nagore:
    if first_pos_x == second_pos_x and first_pos_y == second_pos_y + 1:
        if first_pos_x > 0 and [first_pos_x - 1, first_pos_y] != [first_pos_x, first_pos_y] \
                and (first_pos_x - 1, first_pos_y) not in red_apples\
                and [first_pos_x - 1, first_pos_y] not in snake_temp:
            new_first_post = [first_pos_x - 1, first_pos_y]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x - 1, first_pos_y] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x - 1, first_pos_y])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Svrti levo od momentalnata nasoka nalevo:
    if first_pos_y == second_pos_y and first_pos_x == second_pos_x - 1:
        if first_pos_y > 0 and [first_pos_x, first_pos_y - 1] != [first_pos_x, first_pos_y] \
                and (first_pos_x, first_pos_y - 1) not in red_apples\
                and [first_pos_x, first_pos_y - 1] not in snake_temp:
            new_first_post = [first_pos_x, first_pos_y - 1]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x, first_pos_y - 1] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x, first_pos_y - 1])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Svrti levo od momentalnata nasoka nadesno:
    if first_pos_y == second_pos_y and first_pos_x == second_pos_x + 1:
        if first_pos_y < 9 and [first_pos_x, first_pos_y + 1] != [first_pos_x, first_pos_y] \
                and (first_pos_x, first_pos_y + 1) not in red_apples\
                and [first_pos_x, first_pos_y + 1] not in snake_temp:
            new_first_post = [first_pos_x, first_pos_y + 1]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x, first_pos_y + 1] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x, first_pos_y + 1])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    return temp_snake, temp_green_apples


def svrtiDesno(snake, green_apples, red_apples):
    snake_temp = snake[:]
    green_apples_temp = green_apples[:]
    first_pos_snake = snake_temp[0]
    second_pos_snake = snake_temp[1]
    temp_snake = []
    temp_green_apples = []
    first_pos_x, first_pos_y = first_pos_snake[0], first_pos_snake[1]
    second_pos_x, second_pos_y = second_pos_snake[0], second_pos_snake[1]

    # Svrti desno od momentalnata nasoka nadole:
    if first_pos_x == second_pos_x and first_pos_y == second_pos_y - 1:
        if first_pos_x > 0 and [first_pos_x - 1, first_pos_y] != [first_pos_x, first_pos_y] \
                and (first_pos_x - 1, first_pos_y) not in red_apples\
                and [first_pos_x - 1, first_pos_y] not in snake_temp:
            new_first_post = [first_pos_x - 1, first_pos_y]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x - 1, first_pos_y] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x - 1, first_pos_y])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Svrti desno od momentalnata nasoka nagore:
    if first_pos_x == second_pos_x and first_pos_y == second_pos_y + 1:
        if first_pos_x < 9 and [first_pos_x + 1, first_pos_y] != [first_pos_x, first_pos_y] \
                and (first_pos_x + 1, first_pos_y) not in red_apples\
                and [first_pos_x + 1, first_pos_y] not in snake_temp:
            new_first_post = [first_pos_x + 1, first_pos_y]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x + 1, first_pos_y] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x + 1, first_pos_y])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Svrti desno od momentalnata nasoka nalevo:
    if first_pos_y == second_pos_y and first_pos_x == second_pos_x + 1:
        if first_pos_y > 0 and [first_pos_x, first_pos_y - 1] != [first_pos_x, first_pos_y] \
                and (first_pos_x, first_pos_y - 1) not in red_apples\
                and [first_pos_x, first_pos_y - 1] not in snake_temp:
            new_first_post = [first_pos_x, first_pos_y - 1]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x, first_pos_y - 1] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x, first_pos_y - 1])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    # Svrti desno od momentalnata nasoka nadesno:
    if first_pos_y == second_pos_y and first_pos_x == second_pos_x - 1:
        if first_pos_y < 9 and [first_pos_x, first_pos_y + 1] != [first_pos_x, first_pos_y] \
                and (first_pos_x, first_pos_y + 1) not in red_apples\
                and [first_pos_x, first_pos_y + 1] not in snake_temp:
            new_first_post = [first_pos_x, first_pos_y + 1]
            temp_snake = snake_temp[:-1]
            temp_snake.insert(0, new_first_post)
            if [first_pos_x, first_pos_y + 1] in green_apples:
                temp_snake.append(snake_temp[-1])
                green_apples_temp.remove([first_pos_x, first_pos_y + 1])
                temp_green_apples = green_apples_temp[:]
            else:
                temp_green_apples = green_apples_temp[:]
        else:
            temp_snake = snake_temp[:]
            temp_green_apples = green_apples_temp[:]

    return temp_snake, temp_green_apples

class Snake(Problem):
    def __init__(self, red_apples, initial, goal=None):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = dict()
        #[()]
        snake_position = list(state[0])
        green_apples = list(state[1])
        if len(green_apples) == 0:
            successors["""[]"""] = (tuple(snake_position), tuple(green_apples))
        else:
            green_apples_list = convertToList(green_apples)
            snake_position_list = convertToList(snake_position)
            new_snake_position, new_green_apples = prodolzhiPravo(snake_position_list, green_apples_list, self.red_apples)
            # [()] != [()]
            if green_apples_list != new_snake_position:
                new_snake_position = convertToTuple(new_snake_position)
                new_green_apples = convertToTuple(new_green_apples)
                successors['ProdolzhiPravo'] = (new_snake_position, new_green_apples)
            new_snake_position, new_green_apples = svrtiDesno(snake_position_list, green_apples_list, self.red_apples)
            if green_apples_list != new_snake_position:
                new_snake_position = convertToTuple(new_snake_position)
                new_green_apples = convertToTuple(new_green_apples)
                successors['SvrtiDesno'] = (new_snake_position, new_green_apples)
            new_snake_position, new_green_apples = svrtiLevo(snake_position_list, green_apples_list, self.red_apples)
            if green_apples_list != new_snake_position:
                new_snake_position = convertToTuple(new_snake_position)
                new_green_apples = convertToTuple(new_green_apples)
                successors['SvrtiLevo'] = (new_snake_position, new_green_apples)
        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        possible = self.successor(state)
        return possible[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        green_apples = state[1]
        return len(green_apples) == 0


if __name__ == '__main__':
    n = int(input())
    green_apples = [tuple(map(int, input().split(','))) for _ in range(n)]
    m = int(input())
    red_apples = [tuple(map(int, input().split(','))) for _ in range(m)]
    snake_position = ((0, 7), (0, 8), (0, 9))
    snake = Snake(tuple(red_apples), (snake_position, tuple(green_apples)))
    result = breadth_first_graph_search(snake)
    print(result.solution())