from rose.common import obstacles, actions

driver_name = "Ziv"

def noChoiceBeCareful(frontNextObstacle, sideAction):
    if frontNextObstacle == obstacles.TRASH or frontNextObstacle == obstacles.BIKE or frontNextObstacle == obstacles.BARRIER: 
        if sideAction == None:                               #    The position of the vehicle does not change in this function
            return actions.RIGHT                             #    The purpose of the function is to prevent an accident with obstacles
        else:                                                #    If there is an obstacle and there is no preferred direction due to the location of the vehicle we will turn right- does not matter
            return sideAction                                #    If the function gets value in SIDEACTION there is because it is better to turn only because of the location of the vehicle
    else:                                                    #   
        return actions.NONE                                  #     The last option does not exist and there is no way to get more points so we will continue on the current path



def middleChoice(x, y, frontNextObstacle, world):            #    LOOK PIC1 IN BOTTOM
    right2NextObstacle = world.get((x + 1, y - 2))           #    This function refers to the case I am in the middle lane   
    left2NextObstacle = world.get((x - 1, y - 2))            #    In the middle lane we perform a test for both lanes  
    if right2NextObstacle == obstacles.PENGUIN:              #    The first test we get as a value in the function and it tests the obstacle before                                                          
        return actions.RIGHT                                 #    test for right and left lanes we will check if there is an object in two places before
    elif left2NextObstacle == obstacles.PENGUIN:             #    In case there is a penguin or element that could add another score to us                                                 
        return actions.LEFT                                  #    The elements that add a score are penguin crack and water                                                                    
    else:                                                    #    And therefore we have treated them in function only                                                         
        if frontNextObstacle == obstacles.CRACK:             #    Prioritization is determined by the score of the following elements according to the guide                                       
            return actions.JUMP                              #    A penguin has the most point value so I will check if it is on the sides if true we want to change lanes                                              
        elif right2NextObstacle == obstacles.CRACK:          #    If no penguin is found in front of us or on the sides we will look to check the next element with the most points                                                                 
            return actions.RIGHT                             #    The function refers only to elements that have a scoring value                                                               
        elif left2NextObstacle == obstacles.CRACK:                                                                                           
            return actions.LEFT                                                                
        else:                                                                                                                                 
            if frontNextObstacle == obstacles.WATER:                                                                                                     
                return actions.BRAKE                                                                                                               
            elif right2NextObstacle == obstacles.WATER:                                                                 
                return actions.RIGHT                                                                                                                       
            elif left2NextObstacle == obstacles.WATER:                                                             
                return actions.LEFT                                                                                                                                             
            else:                                                   # If we did not specify an element with added value in our tests
                return noChoiceBeCareful(frontNextObstacle, None)   # we will look to see if we will not lose a score in faults in other elements.


def edgeView(x, y, frontNextObstacle, sideValue, world):        #    I use this function to test the forward and middle lanes
    middleLaneView = world.get((x + sideValue, y - 2))          #    Paths lower than 0 or greater than 6 cannot be checked
    sideAction = ''                                             #    It is not possible to cross lane number three so that there will be no accident
    if sideValue == 1 :                                         #    The SIDEVALUE variable has a positive or negative value
        sideAction = actions.RIGHT                              #    A positive value signifies that we are in the right lane and want to check straight and left
    else:                                                       #    A negative value represents that we are in the left lane and we want to check straight and right
        sideAction = actions.LEFT                               #    I chose to use the Y-2 because it takes a whole turn to respond and I can take things I locate before on the sides
                                                                #    I did not choose to test further than Y-2 to be able to have more obstacles before and it is ineffective
    if middleLaneView == obstacles.PENGUIN:                     #    To check right from the vehicle position I add +1 to X and to check left I subtract -1 from X
        return sideAction                                       #    SIDEVALUE is the value that should be added or subtracted from X depending on the location of the vehicle
    elif frontNextObstacle == obstacles.CRACK:                  #    SIDEVALUE gets the value from the previous function that checked the position of the vehicle
        return actions.JUMP                                     #    The order of priority is determined by the highest score possible
    elif middleLaneView == obstacles.CRACK:                     #    The function is a modular function and knows how to answer the test on the right and left side
        return sideAction                                       #    OBSTACLE and ACTIONS are directories that come from the game file
    elif frontNextObstacle == obstacles.WATER:                  #    SIDEACTION This is the direction we want to turn to - it is a variable that contains within it the function we need to return
        return actions.BRAKE                                    #    I wrote this to avoid unnecessary lines of code performing the same test with a single variable
    elif middleLaneView == obstacles.WATER:                     # 
        return sideAction                                       #
    else:                                                       #
        return noChoiceBeCareful(frontNextObstacle, sideAction) #   If there is no way to get more points I want not to lose points by collision

                                                                #    I am now checking the location of the vehicle
def whatLane(x, y, frontNextObstacle, world):                   #    I took care not to cross the white line so as not to have an accident with the other driver
    if x == 1 or x == 4:                                        #    1 and 4 are the means paths from which I perform a test to both sides
        return middleChoice(x, y, frontNextObstacle, world)     #    So I created a separate function for this test
    elif x == 0 or x == 3:                                      #    0 and 3 are the left lanes no matter where the vehicle is placed
        return edgeView(x, y, frontNextObstacle, 1, world)      #    From this point I can check what is in front of me and in the middle lane
    elif x == 2 or x == 5:                                      #    2 and 5 are the right lanes no matter where the vehicle is placed
        return edgeView(x, y, frontNextObstacle, -1, world)     #    From this point I can check what is in front of me and in the middle lane


def isPenguinAhead(x, y, world):                                #    In this function I check if there is a penguin in front of me that it is ideal to start with 
    frontNextObstacle = world.get((x, y - 1))                   #    From the situation only more possibilities develop according to the following situations
    if frontNextObstacle == obstacles.PENGUIN:                  #    If there is no penguin found in front of me   
        return actions.PICKUP                                   #    I want to check where my vehicle is located to know how to perform the following tests 
    else:                                                       #    **** I preferred to set this variable from now  *************************************************************
        return whatLane(x, y, frontNextObstacle, world)         #    **** and move it between all the following functions so as not to set it multiple times - more efficient ****
                                                                #    *************************************************************************************************************

def drive(world):                                #  /|                             
    x = world.car.x                              # /   -----------|   It starts from here
    y = world.car.y                              # \   -----------|   To keep order I divided the function into several functions to make it easy to read and understand
    return isPenguinAhead(x, y, world)           #  \|                I pass on important values to the following functions


#PIC 1 
#    X0      X1      X2            X3      X4      X5           Demo for the MIDDLEVIEW function        
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|        C = car                      
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|        ! = test we want to perform    
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|                                                                    
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|                                                 
#|...!...|...1...|...!...|||||||...3...|...4...|...5...|                                                            
#|...0...|...!...|...2...|||||||...3...|...4...|...5...|                                        
#|...0...|...C...|...2...|||||||...3...|...4...|...5...|   

#PIC 2 
#    LEFT SIDE X = 0             RIGHT SIDE x = 2  
#    X0      X1      X2            X0      X1      X2           Demo for the EDGEVIEW function        
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|        C = car                      
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|        ! = test we want to perform    
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|                                                                    
#|...0...|...1...|...2...|||||||...3...|...4...|...5...|                                                 
#|...0...|...!...|...2...|||||||...3...|...!...|...5...|                                                            
#|...!...|...1...|...2...|||||||...3...|...4...|...!...|                                        
#|...C...|...0...|...2...|||||||...3...|...4...|...C...|  


#               66          66666           \\
#             66          6     66           \\     ()                   
#           66  66666     6      66           \\                 *************************************************
#           66  6   666   66       66           \\               ****    to win your best driver              ****                                                          
#            666      66   6      66             \\              ****                  and 100% on long run   ****                                     
#             66     66    66     66       ()     \\             *************************************************                                                      
#              66666666     666666                 \\                                             
#   
