
def test_maze1():

    assert do_maze1([0,3,0,1,-3])==5

def test_maze2():

    assert do_maze2([0,3,0,1,-3])==10

    
def do_maze1(maze):

    spot=0
    
    steps=0
    while spot in range(0,len(maze)):

        steps+=1
        jump = maze[spot]
        maze[spot]+=1

        spot+=jump
        

    return steps


def do_maze2(maze):

    spot=0
    steps=0
    while spot in range(0,len(maze)):

        steps+=1
        jump = maze[spot]

        if (jump>=3):
            maze[spot]-=1
        else:
            maze[spot]+=1

        spot+=jump
                

    return steps
    
if __name__=='__main__':

    maze=[int(x) for x in open("input.txt").readlines()]

    print(do_maze1(maze))

    maze=[int(x) for x in open("input.txt").readlines()]
    #print(len(maze))
    print(do_maze2(maze))
