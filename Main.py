from Algorithms import *
from Graph import *
from Tools import *

#from webapp import *

#wishlist = getwishlist(wishlist)

#wishlist = ['top', 'running_shoes','sneakers']
# print(wishlist)
# print(length)
visitedA = True
visitedB = True
visitedC = True
visitedD = True
visitedE = True
storeA = False
length = 0
wishlist = []
print("Items in stock today:")
print("sneakers, running_shoes, boots, heels, top, bottoms, sweater, coat, scarf")
    
while input != 'ok':
    item = input("What do you want to shop for today? (Type OK once you're done): ")
    if item == 'ok' or item == 'OK':
        for i in range(5):
            print("\n")
        
        print("Welcome to ShopperMapper!")
        print("Here's your Shopping List:", wishlist, end="\n")
        
        break
    else:
        wishlist.append(item)
        
wishlength = len(wishlist)

#StoreA:  Sneakers + Running Shoes
#StoreB: Boots + Heels
#StoreC: Top
#StoreD: Bottoms
#StoreE: Sweater, Coat, Scarf
for i in range (wishlength):
    if (wishlist[i] == 'sneakers' or wishlist[i] == 'running_shoes'):
        print("You will be going to store A to get your", wishlist[i])
        if visitedA == True:
            visitedA = False
            storeA = True
    if (wishlist[i] == 'boots' or wishlist[i] == 'heels'):
        print("You will be going to store B to get your", wishlist[i])
        if visitedB == True:
            visitedB = False
            length = length + 1
    if (wishlist[i] == 'top'):
        print("You will be going to store C to get your", wishlist[i])
        if visitedC == True:
            visitedC = False
            length = length + 1
    if (wishlist[i] == 'bottoms'):
        print("You will be going to store D to get your", wishlist[i])
        if(visitedD == True):
            visitedD = False
            length = length + 1
    if (wishlist[i] == 'sweater' or wishlist[i] == 'coat' or wishlist[i] == 'scarf'):
        print("You will be going to store E to get your", wishlist[i])
        if visitedE == True:
            visitedE = False
            length = length + 1    
print("\n")
def draw_square_grid_example():
    g = SquareGrid(14, 29)
    g.walls = DIAGRAM1_WALLS  # long list, [(21, 0), (21, 2), ...]
    came_from, cost_so_far = a_star_search(diagram4, A, Z)
    draw_grid(count, g, width=3, path=reconstruct_path(came_from, start=A, goal=Z))  #to display @@@@



def a_star_search_example():
    print()


def checkdistance(A, Z):
    g = SquareGrid(14, 29)
    g.walls = DIAGRAM1_WALLS  # long list, [(21, 0), (21, 2), ...]
    came_from, cost_so_far = a_star_search(diagram4, A, Z)
    return distance(count, g, width=3, path=reconstruct_path(came_from, start=A, goal=Z))  #to display @@@@

totaldistance = 0
for i in range (length):
    shortestdist = 500
    count = i + 1
    counter = 1
    dist = 0
    distB, distC, distD, distE = 0,0,0,0
    
    
    if count == 1: #Step1
        A = (1,4)
        Z = (7,0)
        bestA = A
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedB == False:
            distB = dist
            shortestdist = distB
            bestA = A
        else:
            A = bestA
            
        A = (8,8)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedC == False:
            distC = dist
            shortestdist = distC
            bestA = A
        else:
            A = bestA
            
        A = (6,12)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedD == False:
            distD = dist
            shortestdist = distD
            bestA = A
        else:
            A = bestA
            
        A = (12,24)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedE == False:
            distE = dist
            shortestdist = distE
            bestA = A
        else:
            A = bestA
        
        if bestA == (1,4): #b
            visitedB = True
            shortestdist = distB
        elif bestA == (8,8): #c 
            visitedC = True
            shortestdist = distC
        elif bestA == (6,12): #d
            visitedD = True
            shortestdist = distD
        elif bestA == (12,0): #e 
            visitedE = True
            shortestdist = distE
        
    elif count == 2: #Step2
        Z = bestA 
        A = (1,4) #b
        bestA = A
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedB == False:
            distB = dist
            shortestdist = distB
            bestA = A
        else:
            A = bestA
            
        A = (8,8)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedC == False:
            distC = dist
            shortestdist = distC
            bestA = A
        else:
            A = bestA
            
        A = (6,12)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedD == False:
            distD = dist
            shortestdist = distD
            bestA = A
        else:
            A = bestA
            
        A = (12,24)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedE == False:
            distE = dist
            shortestdist = distE
            bestA = A
        else:
            A = bestA
            
        if bestA == (1,4): #b
            visitedB = True
            shortestdist = distB
        elif bestA == (8,8): #c 
            visitedC = True
            shortestdist = distC
        elif bestA == (6,12): #d
            visitedD = True
            shortestdist = distD
        elif bestA == (12,24): #e 
            visitedE = True
            shortestdist = distE
        
    elif count == 3:
        Z = bestA 
        A = (1,4) #b
        bestA = A
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedB == False:
            distB = dist
            shortestdist = distB
            bestA = A
        else:
            A = bestA
            
        A = (8,8)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedC == False:
            distC = dist
            shortestdist = distC
            bestA = A
        else:
            A = bestA
            
        A = (6,12)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedD == False:
            distD = dist
            shortestdist = distD
            bestA = A
        else:
            A = bestA
            
        A = (12,24)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedE == False:
            distE = dist
            shortestdist = distE
            bestA = A
        else:
            A = bestA
            
        if bestA == (1,4): #b
            visitedB = True
            shortestdist = distB
        elif bestA == (8,8): #c 
            visitedC = True
            shortestdist = distC
        elif bestA == (6,12): #d
            visitedD = True
            shortestdist = distD
        elif bestA == (12,24): #e 
            visitedE = True
            shortestdist = distE    

    elif count == 4:
        Z = bestA 
        A = (1,4) #b
        bestA = A
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedB == False:
            distB = dist
            shortestdist = distB
            bestA = A
        else:
            A = bestA
            
        A = (8,8)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedC == False:
            distC = dist
            shortestdist = distC
            bestA = A
        else:
            A = bestA
            
        A = (6,12)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedD == False:
            distD = dist
            shortestdist = distD
            bestA = A
        else:
            A = bestA
            
        A = (12,24)
        dist = checkdistance(A, Z)
        if dist < shortestdist and visitedE == False:
            distE = dist
            shortestdist = distE
            bestA = A
        else:
            A = bestA
            
        if bestA == (1,4): #b
            visitedB = True
            shortestdist = distB
        elif bestA == (8,8): #c 
            visitedC = True
            shortestdist = distC
        elif bestA == (6,12): #d
            visitedD = True
            shortestdist = distD
        elif bestA == (12,24): #e 
            visitedE = True
            shortestdist = distE

    
    totaldistance = totaldistance + shortestdist
     
    print('Step:', count)
    if storeA == True:
        print("Here in Store A, you can shop for Sneakers and Running shoes!")
        storeA = False
    
    if __name__ == '__main__':
        
        draw_square_grid_example()
          
            
        if bestA == (1,4): #b
            print("Here in Store B, you can shop for Boots and Heels!")
        elif bestA == (8,8): #c 
            print("Here in Store C, you can shop for Tops!")
        elif bestA == (6,12): #d
            print("Here in Store D, you can shop for Bottoms!")
        elif bestA == (12,24): #e 
            print("Here in Store E, you can shop for Coats, Scarves and Sweaters!")
        
        if (i == length - 1):
            distancesaved = 90 - totaldistance #A D E B C 
            percentsaved = (distancesaved*100)/90   
            print("\n")
            print("Congratulations! You have saved %d mins with ShopperMapper!" %distancesaved)
            print("Total time savings: %d" %percentsaved, end="%.")

print("\n")
print("Thank you for using ShopperMapper! Have a fantastic day!")
