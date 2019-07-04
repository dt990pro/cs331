import numpy as np
import sys

def read(str):
    file = np.loadtxt(str, dtype=int, delimiter=',')
    c = file[1][0]
    w = file[1][1]
    return file

def check_die(x):
    try:
        if (x == None):
            return None
    except ValueError:
        0

    if (x[0][0] == 0):
        if (x[1][0] < x[1][1]):
            return None
    else:
        if (x[1][0] == 0):
            if (x[0][0] < x[0][1]):
                return None
        else:
            if (x[1][0] < x[1][1] or x[0][0] < x[0][1]):
                return None

    return x

def move(x):
    case = x.copy()
    ### ship locates at bottom
    if (case[0][2] == 0):
        ### move c
        case = x.copy()
        if (case[1][0] >= 1):
            case[1][0] -= 1
            case[0][0] += 1
            case[0][2] = 1
            case[1][2] = 0
            case1 = case
        else:
            case1 = None

        ### move w
        case = x.copy()
        if (case[1][1] >= 1):
            case[1][1] -= 1
            case[0][1] += 1
            case[0][2] = 1
            case[1][2] = 0
            case2 = case
        else:
            case2 = None

        ### move cc
        case = x.copy()
        if (case[1][0] >= 2):
            case[1][0] -= 2
            case[0][0] += 2
            case[0][2] = 1
            case[1][2] = 0
            case3 = case
        else:
            case3 = None

        ### move ww
        case = x.copy()
        if (case[1][1] >= 2):
            case[1][1] -= 2
            case[0][1] += 2
            case[0][2] = 1
            case[1][2] = 0
            case4 = case
        else:
            case4 = None

        ### move cw
        case = x.copy()
        if (case[1][1] >= 1 and case[1][0] >= 1):
            case[1][1] -= 1
            case[0][1] += 1
            case[1][0] -= 1
            case[0][0] += 1
            case[0][2] = 1
            case[1][2] = 0
            case5 = case
        else:
            case5 = None

    ### ship locates at top
    else:
        ### move c
        case = x.copy()
        if (case[0][0] >= 1):
            case[0][0] -= 1
            case[1][0] += 1
            case[0][2] = 0
            case[1][2] = 1
            case1 = case
        else:
            case1 = None

        ### move w
        case = x.copy()
        if (case[0][1] >= 1):
            case[0][1] -= 1
            case[1][1] += 1
            case[0][2] = 0
            case[1][2] = 1
            case2 = case
        else:
            case2 = None

        ### move cc
        case = x.copy()
        if (case[0][0] >= 2):
            case[0][0] -= 2
            case[1][0] += 2
            case[0][2] = 0
            case[1][2] = 1
            case3 = case
        else:
            case3 = None

        ### move ww
        case = x.copy()
        if (case[0][1] >= 2):
            case[0][1] -= 2
            case[1][1] += 2
            case[0][2] = 0
            case[1][2] = 1
            case4 = case
        else:
            case4 = None

        ### move cw
        case = x.copy()
        if (case[0][1] >= 1 and case[0][0] >= 1):
            case[0][1] -= 1
            case[1][1] += 1
            case[0][0] -= 1
            case[1][0] += 1
            case[0][2] = 0
            case[1][2] = 1
            case5 = case
        else:
            case5 = None

    #print((case1, case2, case3, case4, case5))
    case1 = check_die(case1)
    case2 = check_die(case2)
    case3 = check_die(case3)
    case4 = check_die(case4)
    case5 = check_die(case5)
    #print((case1, case2, case3, case4, case5))
    return case1, case2, case3, case4, case5

def check_win(x, goal):
    for i in x:
        if ((i == goal).all()):
            return True, i
    return False, 0

def check_visited(case1, case2, case3, case4, case5, visited):
    cases = []

    check = True
    try:
        if (case1 == None):
            check = False
    except ValueError:
        for i in visited:
            if ((case1 == i).all()):
                check = False
                break
    if (check == True):
        cases.append(case1)

    check = True
    try:
        if (case2 == None):
            check = False
    except ValueError:
        for i in visited:
            if ((case2 == i).all()):
                check = False
                break
    if (check == True):
        cases.append(case2)

    check = True
    try:
        if (case3 == None):
            check = False
    except ValueError:
        for i in visited:
            if ((case3 == i).all()):
                check = False
                break
    if (check == True):
        cases.append(case3)

    check = True
    try:
        if (case4 == None):
            check = False
    except ValueError:
        for i in visited:
            if ((case4 == i).all()):
                check = False
                break
    if (check == True):
        cases.append(case4)

    check = True
    try:
        if (case5 == None):
            check = False
    except ValueError:
        for i in visited:
            if ((case5 == i).all()):
                check = False
                break
    if (check == True):
        cases.append(case5)

    return cases

def bfs(start, goal):
    idx = 0
    array = []
    parent = None
    count = 1

    ### loop
    queue = []              # init a queue
    queue.append(start)     # with start
    visited = []
    while (queue):
        #print('queue = ', queue)
        node = queue.pop(0)
        
        #print('==', node)
        # if None
        try:
            if (node == None):
                continue
        except ValueError:
            visited.append(node)
            case1, case2, case3, case4, case5 = move(node)
            # if visited
            cases = check_visited(case1, case2, case3, case4, case5, visited)
            #print('cases = ', cases)
                

        # get ADJs
        if (idx == 0):
            #--------current node   parent      ADJs
            layer = (node,          int(-1),    cases)
        else:
            #--------current node   parent      ADJs
            layer = (node,          parent,     cases)

        # update graph
        array.append(layer)
        
        # check if win
        win, x = check_win(array[idx][2], goal)
        ### win
        if (win):
            print('win')
            #print(x)
            #print(idx)
            #print('len = ', len(visited))
            return idx, array, count
        ### not win
        else:
            # add queue
            for i in array[idx][2]:
                check = True
                try:
                    if (i == None):
                        print('in')
                        continue
                except ValueError:
                    for j in queue:
                        if ((i == j).all()):
                            check = False
                            break

                    if (check):
                        queue.append(i)
                        count += 1

            # get parent
            parent = node.copy()

        idx += 1
        #print(idx)
        #print('---------------')

    # not win
    return -1, array, count

def h(node):
    if (node[1][2] == 1):
        cost = (node[1][0] + node[1][1] - 2) * 2 + 1
    else:
        cost = (node[1][0] + node[1][1]) * 2 + 1
    return cost


def get_lowest_g_n(open):
    low = open[0][2]
    temp = open[0]
    #print('-', open)
    for i in open:
        if (low > i[2]):
            temp = i
    return temp

def A_start_get_ADJs(node, closed):
    case1, case2, case3, case4, case5 = move(node)
    temp = []
    for i in closed:
        temp.append(i[0])
    cases = check_visited(case1, case2, case3, case4, case5, temp)

    return cases

def A_start(start, goal):
    open = []           # store nodes that need to be considered
    closed = []         # store nodes that need not to be considered
    idx = 0
    count = 1

    ### add start
    open.append((start, -1, h(start) + idx))
    while (open):
        node = get_lowest_g_n(open)
        #print('node = ', node)
        ### add to closed
        closed.append(node)
        ### remove from open
        target = 0
        for x in range(len(open)):
            if ((open[x][0] == node[0]).all()):
                target = x
                break
        del open[x]

        ### path found
        for i in closed:
            if ((i[0] == goal).all()):
                print('win')
                return True, closed, count

        ### adjancents
        idx += 1
        cases = A_start_get_ADJs(node[0], closed)
        #print('case = ', cases)
        for i in cases:
            # in closed
            check = False
            for j in closed:
                if ((j[0] == i).all()):
                    check = True
                    break
            if (check == True):
                continue
            else:
                # in open
                inopen = False
                for k in open:
                    if ((k[0] == i).all()):
                        inopen = True
                        break
                if (inopen == False):
                    # compute F score and parent and add to open
                    open.append((i, node[0], h(i) + idx))
                    count += 1
                else:
                    # redundant
                    0
        
        #print('open = ', open)
        #print(idx)
        #print('-----\n')

    return False, closed, count

def is_equal(current, start):
    if (current[0][0] != start[0][0]):
        return False
    elif (current[0][1] != start[0][1]):
        return False
    elif (current[0][2] != start[0][2]):
        return False
    else:
        return True

def output_path(path, mode, name):
    file = open(name, 'w')
    for i in path:
        print('--------')
        print(i)
        file.write('--------\n')
        file.write(str(i) + '\n')

    file.close()

    print('output done')
    return

def get_path(closed, start, goal, mode, name):
    path = []

    if (mode == 'astar'):
        # start from the last
        current = closed[len(closed) - 1][0].copy()

        while (is_equal(current, start) == False):
            # update parent
            for i in range(len(closed)):
                if ((current == closed[i][0]).all()):
                    # add current to path
                    path.append(current)
                    current = closed[i][1].copy()

    elif (mode == 'bfs'):
        # start from the last
        path.append(goal)
        current = closed[len(closed) - 1][0].copy()

        while (is_equal(current, start) == False):
            # update parent
            for i in range(len(closed)):
                for j in closed[i][2]:
                    
                    if ((current == j).all()):
                        # add current to path
                        path.append(current)
                        current = closed[i][0].copy()

    path.append(start)
    path.reverse()
    print('solution moves = ', len(path) - 1)
    output_path(path, mode, name)
    return

def evaluation(case):   
    y=len(case)
    for i in range(y):
        for x in range(6):
            if (case[i][x]<0):
                case[i]=None
                break

    res = []
    for val in case:
        if val != None :
            res.append(val)
    
    case=res[:]
	#print(case)
    y=len(case)
	#print(y)
    for i in range(y):
        if (case[i][0]>0 and case[i][1]>case[i][0] ):
            case[i]=None
        if(case[i]!=None):
            if (case[i][3]>0 and case[i][4]>case[i][3]):
                case[i]=None
    res = []
    for val in case:
        if val != None :
            res.append(val)
    return res

def move_action(state): 

	case=[]
	if(state[5]==1):
		S=state[:]
		S[0]=S[0]+1
		S[3]=S[3]-1
		S[2]=1
		S[5]=0
		case.append(S)	
		# remove chick from right to left

		S=state[:]
		S[1]=S[1]+1
		S[4]=S[4]-1
		S[2]=1
		S[5]=0
		case.append(S)	

		# remove wolf from right to left

		S=state[:]
		S[0]=S[0]+2
		S[3]=S[3]-2
		S[2]=1
		S[5]=0
		case.append(S)	
	    # remove  two chick from right to left

		S=state[:]
		S[1]=S[1]+2
		S[4]=S[4]-2
		S[2]=1
		S[5]=0
		case.append(S)	

	    # remove  two chick from right to left

		S=state[:]
		S[0]=S[0]+1
		S[3]=S[3]-1
		S[1]=S[1]+1
		S[4]=S[4]-1
		S[2]=1
		S[5]=0
		case.append(S)

	    # remove  two chick from right to left


	if(state[5]==0):

		S=state[:]
		S[0]=S[0]-1
		S[3]=S[3]+1
		S[2]=0
		S[5]=1
		case.append(S)   # remove chick from right to left

		S=state[:]
		S[1]=S[1]-1
		S[4]=S[4]+1
		S[2]=0
		S[5]=1
		case.append(S)   # # remove wolf from right to left

		S=state[:]
		S[0]=S[0]-2
		S[3]=S[3]+2
		S[2]=0
		S[5]=1
		case.append(S)   # remove  two chick from right to left

		S=state[:]
		S[1]=S[1]-2
		S[4]=S[4]+2
		S[2]=0
		S[5]=1
		case.append(S)   # remove  two chick from right to left

		S=state[:]
		S[0]=S[0]-1
		S[3]=S[3]+1
		S[1]=S[1]-1
		S[4]=S[4]+1
		S[2]=0
		S[5]=1
		case.append(S)   # remove  two chick from right to left
	# print(case)
	return case

class Node:
    def __init__(self,l,r,p,child,depth=0):
    	self.parent = p
    	self.left = l
    	self.right = r
    	self.children = child
    	self.d = depth

def move1(state):
	case=[]
	case=move_action(state)
	allow_action=[] 
	allow_action=evaluation(case)

	return allow_action

def dfs(start,goal,name):
    stack=[]
    visited=[]
    status=start[:]
    stack.append(Node(status[:3],status[3:],None,None,0))
    current_node = stack[0]
    visited.append(status)
    has_solution = True
    count = 1
    while len(stack) > 0:
        if current_node.left+current_node.right == goal:
            break
        temp_index = False
        current_node.children = move1(current_node.left+current_node.right)
        for c in current_node.children:
            if c in visited:
                continue
            else:
                temp_index = True
                stack.append(Node(c[:3],c[3:],current_node,None,current_node.d+1))
                visited.append(c)
                count += 1
        if temp_index == False:
            del stack[len(stack)-1]
        if len(stack)-1 == 0:
            has_solution = False
            break

        current_node = stack[len(stack)-1]

    if has_solution:
        file = open(name, 'w')
        print('expanded nodes ', count)
        print('solution nodes ', current_node.d)
        while current_node is not None:
            print(current_node.left+current_node.right)
            file.write(str(current_node.left+current_node.right) + '\n')
            current_node = current_node.parent
        file.close()
    else:
        print("No solution")

def iddfs(start,goal,name):
    limit_value = 2;
    has_solution = True
    count = 0
    while True:
        current_depth = 0
        stack=[]
        visited=[]
        status=start[:]
        stack.append(Node(status[:3],status[3:],None,None,0))
        current_node = stack[0]
        visited.append(status)
        count += 1
        while current_depth <= limit_value:
            if current_node.left+current_node.right == goal:
                has_solution = True
                break
            temp_index = False
            temp = move1(current_node.left+current_node.right)
            if current_node.d + 1 <= limit_value:
                for c in temp:
                    if c in visited:
                        continue
                    else:
                        temp_index = True
                        stack.append(Node(c[:3],c[3:],current_node,None,current_node.d+1))
                        visited.append(c)
                        count += 1
            if temp_index == False:
                del stack[len(stack)-1]
            if len(stack) == 0:
                has_solution = False
                break
            else:
                current_node = stack[len(stack)-1]
			#print(current_node.d)
            current_depth = current_node.d
        #print("-----------")
        if current_node.left+current_node.right == goal or (has_solution == False and limit_value >=1000):
            break
        # print(limit_value)
        limit_value = limit_value + 1
    if has_solution:
        file = open(name, 'w')
        print('expanded nodes ', count)
        print('solution node ', current_node.d)
        while current_node is not None:
            print(current_node.left+current_node.right)
            file.write(str(current_node.left+current_node.right) + '\n')
            current_node = current_node.parent
        file.close()
    else: 
        print("No solution")

def readfile(i):
	f=open(i,"r")
	left_inital=f.readline()
	right_goal=f.readline()
	first_line=left_inital.split('\n')
	second_line=right_goal.split('\n')
	nums_l=first_line[0].split(',')
	nums_r=second_line[0].split(',')
	first=[]
	second=[]
	
	for i in range(3):
		first.append(int(nums_l[i]))
	#print(str(first))

	for i in range(3):
		second.append(int(nums_r[i]))
	#print(str(second))
	
	inital_state=first+second

	return inital_state

def main():
    a=sys.argv[1]
    b=sys.argv[2]
    mode=sys.argv[3]
    name=sys.argv[4]

    if (mode == 'bfs'):
        start = read(a)
        goal = read(b)
        print(mode)
        status, array, count = bfs(start, goal)
        if (status):
            print('expanded ', count, ' nodes')
            get_path(array, start, goal, mode, name)
        else:
            print('no solution found')

    elif (mode == 'astar'):
        start = read(a)
        goal = read(b)
        print(mode)
        status, closed, count = A_start(start, goal)
        if (status):
            print('expanded ', count, ' nodes')
            get_path(closed, start, goal, mode, name)
        else:
            print('no solution found')

    elif (mode == 'dfs'):
        inital_state=readfile(a)
        goal=readfile(b)
        dfs(inital_state, goal, name)

    elif (mode == 'iddfs'):
        inital_state=readfile(a)
        goal=readfile(b)
        iddfs(inital_state, goal, name)

    else:
        print('command err')

    return

main()