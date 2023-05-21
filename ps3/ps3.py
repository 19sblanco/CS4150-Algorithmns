values = [] 

k = None
N = None

mV0Memo = None
mV1Memo = None
mV_1Memo = None
negInfinity = -1000000

"""
returns the greatest value that you can get out of artGallery
by closing k doors where you can't close door 0
"""
def maxValue0(r):
    if r > N:
        return

    for i in range(k):
        if i > N - r:
            mV_1Memo[r][i] = negInfinity
            
        elif i == N - r:
            mV0Memo[r][i] = values[r][0] + mV0Memo[r+1][i-1]
        else:
            close1 = values[r][0] + mV0Memo[r+1][i-1]
            closeNeither = values[r][0] + values[r][1] + mV_1Memo[r+1][i]
            mV0Memo[r][i] = max(close1, closeNeither)



"""
returns the greatest value that you can get out of artGallery
by closing k doors where you can't close door 1
"""
def maxValue1(r):
    if r > N:
        return
    
    for i in range(k):
        if i > N - r:
            mV1Memo[r][i] = negInfinity
            
        elif i == N - r:
            mV1Memo[r][i] = values[r][1] + mV1Memo[r+1][i-1]

        else:
            close0 = values[r][1] + mV1Memo[r+1][i-1]
            closeNeither = values[r][0] + values[r][1] + mV_1Memo[r+1][i]
            mV1Memo[r][i] = max(close0, closeNeither)


"""
returns the greaters value that you can get out of artGallery
by closing k doors where you don't have to close a particular door
"""
def maxValue_1(r):
    if r > N:
        return

    for i in range(k):
        if i > N - r:
           mV_1Memo[r][i] = negInfinity

        elif i == N - r:
            close0 = values[r][1] + mV1Memo[r+1][i-1]
            close1 = values[r][0] + mV0Memo[r+1][i-1]
            mV_1Memo[r][i] = max(close0, close1)

        else:
            close0 = values[r][1] + mV1Memo[r+1][i-1]
            close1 = values[r][0] + mV0Memo[r+1][i-1]
            closeNeither = values[r][0] + values[r][1] + mV_1Memo[r+1][i]
            mV_1Memo[r][i] = max(close0, close1, closeNeither)

"""
returns the greatest value that you can get out of artGallery
by closing k doors
"""
def maxValue(N):
    for r in range(N-1, -1 , -1):
        maxValue_1(r)
        maxValue0(r)
        maxValue1(r)
        
    print(mV_1Memo[0][k-1])



def main():
    global k, N, values, mV0Memo, mV1Memo, mV_1Memo

    N, k = input().split()

    N, k = int(N), int(k) + 1

    for i in range(N):
        temp = input().split()
        values.append([int(temp[0]), int(temp[1])])


    mV0Memo = [ [0]*int(k) for i in range(N+1)]
    mV1Memo = [ [0]*int(k) for i in range(N+1)]
    mV_1Memo = [ [0]*int(k) for i in range(N+1)]

    maxValue(N)
    

main()
