import math as m

plots = []
houses = []


# # of circular plots, # of circular houses, # of square houses
lst1 = [int(x) for x in input().split()]

# radius of the circular plots
lst2 = [int(x) for x in input().split()]
plots = lst2

# radius of the circular houses
lst3 = [int(x) for x in input().split()]
houses = lst3

# side length of the square houses
lst4 = [int(x) for x in input().split()]

# get the radius of a circle that is required to fit a square with side lengths "side"
for side in lst4:
    radius = (side * m.sqrt(2)) / 2
    houses.append(radius)

plots.sort()
houses.sort()

# can we fill the smallest plot with the smallest house?
# if so fill it 
# if not can we fill the next smallest plot with the smallest house
# then keep doing that

hp = 0 # house pointer
pp = 0 # plot pointer

filledPlots = 0

for plot in plots:
    # if we are past the hp array then exit loop
    # check if we can fill in this plot with the current house
    # if so:
        # filledPlots++ # we count this plot as filled
        # hp++ # we move onto the next house
        # continue # we move onto the next plot
    # otherwise 
        # check if we can fill this plot with the next smallest house
    
    if hp >= len(houses): # if we have no more homes break
        break

    if plot > houses[hp]:
        filledPlots += 1
        hp += 1




        
print(filledPlots)





