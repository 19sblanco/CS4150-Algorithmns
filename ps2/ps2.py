D = None
memo = None
MAX_DISTANCE = 1000
MAX = None
INFINITY = 100000 # for the sake of this problem, this value is inifinity


"""
determine the minimum total that can be reached by + or -
each D[i] such that your total never goes below 0 and by the
end of the array you end up with a height of 0
"""
def minWall():
    global memo

    # fill base cases
    for i in range(MAX_DISTANCE):
        memo[len(D)][i] = INFINITY
    memo[len(D)][0] = 0


    # todo: make sure base cases work
    for i in range(len(D) -1, -1, -1): # loop over D backwards
        for h in range(MAX_DISTANCE):
            height = h
            distance = D[i]

            if height + distance >= MAX_DISTANCE: # dont consider values beyond our limit
                go_down = memo[i+1][h-D[i]]
                memo[i][h] = max(height, go_down)
                
            elif height < distance:
                go_up = memo[i+1][height + distance]
                memo[i][h] = max(height, go_up)
                
            else:
                go_down = memo[i+1][h-D[i]]
                go_up = memo[i+1][height + distance]
                minwall = min(go_down, go_up)
                memo[i][h] = max(h, minwall)
            
            
            
    
    return memo[0][0]



def main():
    N = int(input())
    distances = input().split()
    global memo
    global D
    
    D = [int(x) for x in distances]
    memo = [ [0]*(MAX_DISTANCE) for i in range(N+1)]

    print(minWall())



main()