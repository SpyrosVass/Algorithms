# -*- coding: utf-8 -*-

import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys

"""
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')
"""
#μεταβλήτες ερωτήματος 1
def drawCircle(xc, yc, x, y, azx, azy):
    azx.append(xc+x)
    azy.append(yc+y)
    azx.append(xc-x)
    azy.append(yc+y)
    azx.append(xc+x)
    azy.append(yc-y)
    azx.append(xc-x)
    azy.append(yc-y)
    azx.append(xc+y)
    azy.append(yc+x)
    azx.append(xc-y)
    azy.append(yc+x)
    azx.append(xc+y)
    azy.append(yc-x)
    azx.append(xc-y)
    azy.append(yc-x)
    return azx, azy

def circleBres(xc, yc, r):
    azx = []
    azy = []
    x = 0
    y = r
    d = 3 - 2 * r
    
    azx, azy = drawCircle(xc, yc, x, y, azx, azy)
    
    while (y >= x):
        
        x = x + 1
        
        if (d > 0):
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        azx, azy = drawCircle(xc, yc, x, y, azx, azy)
   
    plt.gca().set_aspect('equal', adjustable='box')     
    plt.plot(azx , azy , color='orange')        
    plt.show()

def bresenham(x0,y0,x1, y1):
    case = 0
    azx = []
    azy = []
    dx = abs(x1 - x0) 
    dy = abs(y1 - y0) 
    incr1 = 2 * dy 
    d = 2 * dy - dx 
    if (x0 > x1):
        x0 , x1 = x1 , x0
        y0 , y1 = y1 , y0

    if (y0 > y1):
        y0 , y1 = y1 , y0
        case = 1
        
    if (dy > dx):
        x0 , y0 = y0 , x0
        x1 , y1 = y1 , x1
        dx , dy = dy , dx
        incr1 = 2 * dy 
        d = 2 * dy - dx
        if (case == 0):
            case = 2
        elif (case == 1):
            case = 3

    azx.append(x0)
    azy.append(y0)
    x , y = x0 , y0
    while (x < x1):
        x = x + 1 
        d = d + incr1	
        if (d >= 0):
            y = y + 1 
            d = d - 2 * dx  	
        azx.append(x)
        azy.append(y)
       
    cases(case, azx, azy)



def cases(case, azx, azy):
    plt.gca().set_aspect('equal', adjustable='box')
    if (case == 0):
        plt.plot(azx , azy)        
        plt.show()
    elif (case == 1):
        azy.reverse()
        plt.plot(azx , azy)        
        plt.show()
    elif (case == 2):
        plt.plot(azy , azx)        
        plt.show()
    else:
        azy.reverse()
        plt.plot(azy , azx)        
        plt.show()
    

def inputcheck():
    while (True):
       temp = input(": ")
       if (temp == 'e'):
           sys.exit("Simulation ended.")
       try:
          x = int(temp)
       except:
          print("Please enter an integer.")
          x = "error"
       if (isinstance(x, int)):
           print("ΟΚ")
           break
    return x

def inputcheck1():
    while (True):
       temp = input(": ")
       if (temp == 'e'):
           sys.exit("Simulation ended.")
       try:
          x = int(temp)
       except:
          print("Please enter the integer 1, 2 or 3.")
          x = "error"
       if (isinstance(x, int)):
           if ((x == 1) or (x == 2) or (x == 3)):
               print("ΟΚ")
               break
           else:
               print("Please enter 1, 2 or 3.") 
    return x
#μεταβλήτες ερωτήματος 2
first_time2 = True
first_time3 = True
first_time_reg =True
x_min = 1.0
y_min = 1.0
x_max = 1.0
y_max = 1.0
#μεταβλήτες ερωτήματος 3

def draw(ax1, ay1, ax2, ay2):
    plt.plot(ax1 , ay1 , color='orange')
    plt.plot(ax2 , ay2 , color='orange')
    for i in ax1:
        x = (ax1, ax2)
        y = (ay1, ay2)
        plt.plot(x, y, color='green')
    plt.pause(1)
    plt.draw()
    
def draw1(ax1, ay1, ax2, ay2, ax, ay):
    plt.plot(ax, ay, color='purple')
    for i in ax1:
        x = (ax1, ax2)
        y = (ay1, ay2)
        plt.plot(x, y, color='green')
    plt.pause(1)
    plt.draw()
    
    
def redraw(ax1, ay1, ax2, ay2, A, top, bottom):
    plt.plot(ax1 , ay1 , color='orange')
    plt.plot(ax2 , ay2 , color='orange')
    plt.plot(A[0] , A[1] , marker='o' , color='blue')
    for i in ax1:
        x = (ax1, ax2)
        y = (ay1, ay2)
        plt.plot(x, y, color='green') 
    i = 0
    while (i < top):
        x = (ax1[i], ax2[i])
        y = (ay1[i], ay2[i])
        plt.plot(x, y, color='red')
        i = i + 1
    i = 9
    while (i > bottom):
        x = (ax1[i], ax2[i])
        y = (ay1[i], ay2[i])
        plt.plot(x, y, color='red')
        i = i - 1
    plt.pause(1)
    plt.draw()

def redraw1(ax1, ay1, ax2, ay2, A, top, bottom, ax, ay):
    plt.plot(ax, ay, color='purple')
    plt.plot(A[0] , A[1] , marker='o' , color='blue')
    for i in ax1:
        x = (ax1, ax2)
        y = (ay1, ay2)
        plt.plot(x, y, color='green') 
    i = 0
    while (i < top):
        x = (ax1[i], ax2[i])
        y = (ay1[i], ay2[i])
        plt.plot(x, y, color='red')
        i = i + 1
    i = 9
    while (i > bottom):
        x = (ax1[i], ax2[i])
        y = (ay1[i], ay2[i])
        plt.plot(x, y, color='red')
        i = i - 1
    plt.pause(1)
    plt.draw()
    
    
    
def calc(A,ax1,ay1,ax2,ay2):
    top = 0
    bottom = 9
    middle = round((bottom+top)/2)
    while (bottom > (top + 1)):
        v1 = (ax2[middle]-ax1[middle], ay2[middle]-ay1[middle])
        v2 = (ax2[middle]-x, ay2[middle]-y)
        xp = v1[0]*v2[1] - v1[1]*v2[0]
        if xp >= 0:
            top = middle
        elif xp < 0:
            bottom = middle
        middle = round((bottom+top)/2)
        redraw(ax1, ay1, ax2, ay2, A, top, bottom)
    
 

def calc1(A, ax1, ay1, ax2, ay2, ax, ay):
    top = 0
    bottom = 9
    middle = round((bottom+top)/2)
    while (bottom > (top + 1)):
        xdiff = (ax1[middle] - ax2[middle], ax[0] - ax[1])
        ydiff = (ay1[middle] - ay2[middle], ay[0] - ay[1])

        div = det(xdiff, ydiff)
       
        azx = (ax1[middle], ax2[middle])
        azy = (ay1[middle], ay2[middle])

        d = (det(azx, azy), det(ax, ay))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
    
        if y >= A[1]:
            top = middle
        elif y < A[1]:
            bottom = middle
        middle = round((bottom+top)/2)
        redraw1(ax1, ay1, ax2, ay2, A, top, bottom, ax, ay)
        
        
def det(a, b):
    return a[0] * b[1] - a[1] * b[0] 

        
def find_point(x0, y0, x1, y1, y):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    m = dy / dx 
    b = y1 - (m * x1)
    x = (y - b) / m
    return x
    
       
def inputcheck2():
    while (True):
       temp = input(": ")
       if (temp == 'e'):
           sys.exit("Simulation ended.")
       try:
          x = float(temp)
       except:
          print("Please enter an float from 0 to 100")
          x = "error"
       if (isinstance(x, float)):
           if ((x >= 0) and (x <= 100)):
               print("ΟΚ")
               break
           else:
               print("The value should be from 0 to 100") 
    return x
#μεταβλήτες ερωτήματος 4
first_time = True
line_start = []
line_end =[]
INSIDE = 0  #0000 
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000 

def computeCode(x, y): 
    code = INSIDE 
    if x < x_min:      # to the left of rectangle 
        code |= LEFT 
    elif x > x_max:    # to the right of rectangle 
        code |= RIGHT 
    if y < y_min:      # below the rectangle 
        code |= BOTTOM 
    elif y > y_max:    # above the rectangle 
        code |= TOP 
  
    return code 


def cohenSutherlandClip(x1, y1, x2, y2): 
  
    # Compute region codes for P1, P2 
    code1 = computeCode(x1, y1) 
    code2 = computeCode(x2, y2) 
    accept = False
  
    while True: 
  
        # If both endpoints lie within rectangle 
        if code1 == 0 and code2 == 0: 
            accept = True
            break
  
        # If both endpoints are outside rectangle 
        elif (code1 & code2) != 0: 
            break
  
        # Some segment lies within the rectangle 
        else: 
  
            # Line Needs clipping 
            # At least one of the points is outside,  
            # select it 
            x = 1.0
            y = 1.0
            if code1 != 0: 
                code_out = code1 
            else: 
                code_out = code2 
  
            # Find intersection point 
            # using formulas y = y1 + slope * (x - x1),  
            # x = x1 + (1 / slope) * (y - y1) 
            if code_out & TOP: 
                
                # point is above the clip rectangle 
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1) 
                y = y_max 
  
            elif code_out & BOTTOM: 
                  
                # point is below the clip rectangle 
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1) 
                y = y_min 
  
            elif code_out & RIGHT: 
                  
                # point is to the right of the clip rectangle 
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1) 
                x = x_max 
  
            elif code_out & LEFT: 
                  
                # point is to the left of the clip rectangle 
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1) 
                x = x_min 
  
            # Now intersection point x,y is found 
            # We replace point outside clipping rectangle 
            # by intersection point 
            if code_out == code1: 
                x1 = x 
                y1 = y 
                code1 = computeCode(x1,y1) 
  
            else: 
                x2 = x 
                y2 = y 
                code2 = computeCode(x2, y2) 
  
    if accept: 
        print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2))
        plt.plot([x1,x2], [y1,y2],'k-')
if __name__=='__main__':
    print("Welcome to our program.")
    while True:
        print("Menu :")
        print("Enter 1 for Bresenham algorithm for construction of lines and circles.")
        print("Enter 2 for displacement,resizing and rotation transformations for spatial data points in 2 and 3 dimensions.")
        print("Enter 3 for binary geometric search algorithms on a flat area or a line.")
        print("Enter 4 for line cutting algorithms on a flat area based on the Cohen – Sutherland technique.")
        print("Enter 5 for exiting the program.")
        choice1 = input("Input:")
        while choice1 != '1' and choice1 != '2' and choice1 != '3'and choice1 != '4'and choice1 != '5':
            print("Input must be 1,2,3,4 or 5, please try again")
            choice1 = input("Input:")
            
        if choice1 == '1':
            while (True):
                print("Menu for Bresenham algorithm for construction of lines and circles:")
                print ("Enter 1 for line simulation.\nEnter 2 for circle simulation\nEnter 3 to return at the first menu\n(Enter e to exit in any input)")
                ques = inputcheck1()
            
                if (ques == 1):
                    print ("Enter the coordinates for the first point.")
                    print ("x")
                    x0 = inputcheck()
                    print ("\ny")
                    y0 = inputcheck()
                    print ("\nEnter the coordinates for the second point.")
                    print ("x")
                    x1 = inputcheck()
                    print ("\ny")
                    y1 = inputcheck()
                    bresenham(x0, y0, x1, y1)
                elif (ques == 2):
                    print ("Enter the coordinates for the circle center.")
                    print ("x")
                    xc = inputcheck()
                    print ("\ny")
                    yc = inputcheck()
                    print ("Enter the value of the radius.")
                    r = inputcheck()
                    circleBres(xc, yc, r)
                elif (ques == 3):
                    break
            
        elif choice1 == '2':
            while True:
               print("Menu for displacement,resizing and rotation transformations for spatial data points in 2 and 3 dimensions.:")
               print("Enter 1 for 2d shape.")
               print("Enter 2 for 3d shape.")
               print("Enter 3 for returning to the main menu.")
               choice = input("Input:")
               while choice != '1' and choice != '2' and choice != '3':
                   print("Input must be 1,2 or 3, please try again")
                   choice = input("Input:")
                
               if choice == '1':
                   while True:
                      print("Menu for 2d shape:")
                      print("Enter 1 for adding spatial point.")
                      print("Enter 2 for deleting spatial point.")
                      print("Enter 3 for displacement of shape.")
                      print("Enter 4 for resizing of shape.")
                      print("Enter 5 for rotation of shape.")
                      print("Enter 6 for returning to previous menu.")
                
                      choice2 = input("Input:")
            
                      while choice2 != '1' and choice2 != '2' and choice2 != '3' and choice2 != '4' and choice2 != '5' and choice2 != '6':
                           print("Input must be 1,2,3,4,5 or 6, please try again")
                           choice2 = input("Input:")
                      if choice2 == '1':
                          print("adding spatial point")
                          try:
                            inx = float(input("x:"))
                            iny = float(input("y:"))
                          except:
                            print("wrong spatial point entry")
                          else:
                            if first_time2 == True:
                                twodpoints = np.array([[inx], [iny],[1]])
                                print(twodpoints[0:2, :])
                                first_time2 = False
                                plt.scatter(twodpoints[0], twodpoints[1])
                                plt.axis('equal')
                                plt.show()
                            else:
                                helper = np.array([[inx], [iny],[1]])
                                twodpoints = np.append(twodpoints, helper, axis=1)
                                print(twodpoints[0:2, :])
                                plt.scatter(twodpoints[0], twodpoints[1])
                                plt.axis('equal')
                                plt.show()
                      elif choice2 == '2':
                          if first_time2 == True or twodpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("spatial point deletion")
                              counter = 1
                              print(twodpoints.shape[1])
                              for x in range(twodpoints.shape[1]):
                                 print(counter,": x=",twodpoints[0, x],", y=",twodpoints[1, x])
                                 counter += 1
                              print("Enter spatial point number you wish to delete")
                              try:
                                 del_choice = int(input("Input:"))
                                 assert(del_choice > 0 and del_choice <= twodpoints.shape[1])
                              except:
                                 print("wrong spatial point input")
                              else:
                                 twodpoints = np.delete(twodpoints, del_choice-1 , 1)
                                 print(twodpoints[0:2, :])
                                 plt.scatter(twodpoints[0], twodpoints[1])
                                 plt.axis('equal')
                                 plt.show()
                      elif choice2 == '3':
                          if first_time2 == True or twodpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("displacement of shape")
                              try:
                                 print("Enter distance dx.")
                                 dx = float(input("dx="))
                                 print("Enter distance dy.")
                                 dy = float(input("dy="))
                              except:
                                 print("wrong distance input")
                              else:
                                 twoddistance = np.array([[1,0,dx],[0,1,dy],[0,0,1]])
                                 print(twoddistance)
                                 twodpoints = np.dot(twoddistance,twodpoints)
                                 print(twodpoints[0:2, :])
                                 plt.scatter(twodpoints[0], twodpoints[1])
                                 plt.axis('equal')
                                 plt.show()
                      elif choice2 == '4':
                          if first_time2 == True or twodpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("resizing of shape")
                              try:
                                 print("Enter resizing Sx.")
                                 Sx = float(input("Sx="))
                                 print("Enter resizing Sy.")
                                 Sy = float(input("Sy="))
                              except:
                                 print("wrong resizing input")
                              else:
                                 twodgradation = np.array([[Sx,0,0],[0,Sy,0],[0,0,1]])
                                 print(twodgradation)
                                 twodpoints = np.dot(twodgradation,twodpoints)
                                 print(twodpoints[0:2, :])
                                 plt.scatter(twodpoints[0], twodpoints[1])
                                 plt.axis('equal')
                                 plt.show()
                      elif choice2 == '5':
                          if first_time2 == True or twodpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("rotation of shape")
                              try:
                                 print("Enter angle of incidence θ.")
                                 theta = float(input("θ="))
                              except:
                                 print("wrong angle of incidence input")
                              else:
                                 twodrotation = np.array([[math.cos(theta),-math.sin(theta),0],[math.sin(theta),math.cos(theta),0],[0,0,1]])
                                 print(twodrotation)
                                 twodpoints = np.dot(twodrotation,twodpoints)
                                 print(twodpoints[0:2, :])
                                 plt.scatter(twodpoints[0], twodpoints[1])
                                 plt.axis('equal')
                                 plt.show()
                      elif choice2 == '6':
                          break
                
               elif choice == '2':
                    while True:
                      print("Menu for 3d shape:")
                      print("Enter 1 for adding spatial point.")
                      print("Enter 2 for deleting spatial point.")
                      print("Enter 3 for displacement of shape.")
                      print("Enter 4 for resizing of shape.")
                      print("Enter 5 for rotation of shape.")
                      print("Enter 6 for returning to previous menu.")
                
                      choice2 = input("Input:")
            
                      while choice2 != '1' and choice2 != '2' and choice2 != '3' and choice2 != '4' and choice2 != '5' and choice2 != '6':
                           print("Input must be 1,2,3,4,5 or 6, please try again")
                           choice2 = input("Input:")
                      if choice2 == '1':
                          
                          print("adding spatial point")
                          try:
                            inx = float(input("x:"))
                            iny = float(input("y:"))
                            inz = float(input("z:"))
                          except:
                            print("wrong spatial point entry")
                          else:
                            if first_time3 == True:
                              threedpoints = np.array([[inx], [iny], [inz],[1]])
                              print(threedpoints[0:3, :])        
                              first_time3 = False
                              fig = plt.figure()
                              ax = fig.add_subplot(111,projection='3d')
                              ax.scatter(threedpoints[0], threedpoints[1],threedpoints[2])
                              plt.show()
                            else:
                              helper = np.array([[inx], [iny], [inz],[1]])
                              threedpoints = np.append(threedpoints, helper, axis=1)
                              print(threedpoints[0:3, :])
                              fig = plt.figure()
                              ax = fig.add_subplot(111,projection='3d')               
                              ax.scatter(threedpoints[0], threedpoints[1],threedpoints[2])
                              plt.show()
                      elif choice2 == '2':
                          if first_time3 == True or threedpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("spatial point deletion")
                              counter = 1
                              print(threedpoints.shape[1])
                              for x in range(threedpoints.shape[1]):              
                                 print(counter,": x=",threedpoints[0, x],", y=",threedpoints[1, x],", z=",threedpoints[2, x])           
                                 counter += 1
                              print("Enter spatial point number you wish to delete")
                              try:
                                 del_choice = int(input("Input:"))
                                 assert(del_choice > 0 and del_choice <= threedpoints.shape[1])
                              except:
                                 print("wrong spatial point input")
                              else:
                                 threedpoints = np.delete(threedpoints, del_choice-1 , 1)
                                 print(threedpoints[0:3, :])
                                 fig = plt.figure()
                                 ax = fig.add_subplot(111,projection='3d')               
                                 ax.scatter(threedpoints[0], threedpoints[1],threedpoints[2])
                                 plt.show()
                      elif choice2 == '3':
                          if first_time3 == True or threedpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("displacement of shape")
                              try:
                                 print("Enter distance dx.")
                                 dx = float(input("dx="))
                                 print("Enter distance dy.")
                                 dy = float(input("dy="))
                                 print("Enter distance dz.")
                                 dz = float(input("dz="))
                              except:
                                 print("wrong distance input")
                              else:
                                 threeddistance = np.array([[1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]])
                                 print(threeddistance)
                                 threedpoints = np.dot(threeddistance,threedpoints)
                                 print(threedpoints[0:3, :])
                                 fig = plt.figure()
                                 ax = fig.add_subplot(111,projection='3d')               
                                 ax.scatter(threedpoints[0], threedpoints[1],threedpoints[2])
                                 plt.show()
                      elif choice2 == '4':
                          if first_time3 == True or threedpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("resizing of shape")
                              try:
                                 print("Enter resizing Sx.")
                                 Sx = float(input("Sx="))
                                 print("Enter resizing Sy.")
                                 Sy = float(input("Sy="))
                                 print("Enter resizing Sz.")
                                 Sz = float(input("Sz="))
                              except:
                                 print("wrong resizing input")
                              else:
                                 threedgradation = np.array([[Sx,0,0,0],[0,Sy,0,0],[0,0,Sz,0],[0,0,0,1]])
                                 print(threedgradation)
                                 threedpoints = np.dot(threedgradation,threedpoints)
                                 print(threedpoints[0:3, :])
                                 fig = plt.figure()
                                 ax = fig.add_subplot(111,projection='3d')               
                                 ax.scatter(threedpoints[0], threedpoints[1],threedpoints[2])
                                 plt.show()
                      elif choice2 == '5':
                          if first_time3 == True or threedpoints.shape[1] == 0:
                              print("there are no spatial points")
                          else:
                              print("rotation of shape")
                              print("Choose the rotation axis")
                              print("Enter 1 for zz'")
                              print("Enter 2 for xx'")
                              print("Enter 3 for yy'")
                              choice2 = input("Input:")
                              if choice2 == '1' or choice2 == '2' or choice2 == '3':
                                try:
                                   print("Enter angle of incidence θ.")
                                   theta = float(input("θ="))
                                except:
                                   print("wrong angle of incidence input")
                                else:
                                   if choice2 == '1':
                                     threedrotation = np.array([[math.cos(theta),-math.sin(theta),0,0],[math.sin(theta),math.cos(theta),0,0],[0,0,1,0],[0,0,0,1]])
                                   elif choice2 == '2':
                                     threedrotation = np.array([[1,0,0,0],[0,math.cos(theta),-math.sin(theta),0],[0,math.sin(theta),math.cos(theta),0],[0,0,0,1]])
                                   elif choice2 == '3':
                                     threedrotation = np.array([[math.cos(theta),0,math.sin(theta),0],[0,1,0,0],[-math.sin(theta),0,math.cos(theta),0],[0,0,0,1]])
                                   print(threedrotation)
                                   threedpoints = np.dot(threedrotation,threedpoints)
                                   print(threedpoints[0:3, :])
                                   fig = plt.figure()
                                   ax = fig.add_subplot(111,projection='3d')               
                                   ax.scatter(threedpoints[0], threedpoints[1],threedpoints[2])
                                   plt.show()
                              else:
                                print("wrong axis input")
                      elif choice2 == '6':
                          break
               elif choice == '3': 
                    break
        elif choice1 == '3':
            ax1 = [0,0,0,0,0,0,0,0,0,0]
            ay1 = [100,93,84,62,55,37,24,18,7,0]
            ax2 = [100,100,100,100,100,100,100,100,100,100]
            ay2 = [100,88,81,66,50,42,30,15,10,0]
    
            #first
            while (True):
                print ("Binary geometric search algorithms on a flat area or a line:")
                print ("Enter 1 for strip simulation.\nEnter 2 for line simulation\nEnter 3 to return at the first menu\n(Enter e to exit in any input)")
                ques = inputcheck1()
    
                if (ques == 1):
                    draw(ax1, ay1, ax2, ay2)
    
                    print ("Enter the coordinates for the your point.")
                    print ("x")
                    x = inputcheck2()
                    print ("\ny")
                    y = inputcheck2()
                    A = (x,y)
            
                    redraw(ax1, ay1, ax2, ay2, A, 0, 9)
                    calc(A ,ax1,ay1,ax2,ay2)
                elif (ques == 2):
                    x0 = 30
                    y0 = 0
                    x1 = 70
                    y1 = 100
    
                    ax = [x0, x1]
                    ay = [y0, y1]
    
                     #ax1.pop(0)
                     #ax1.pop(-1)
                     #ay1.pop(0)
                     #ay1.pop(-1)
                     #ax2.pop(0)
                     #ax2.pop(-1)
                     #ay2.pop(0)
                     #ay2.pop(-1)
    
                    draw1(ax1, ay1, ax2, ay2, ax, ay)
    
                    print ("Enter the y coordinate to create a point in the purple line.")
                    print ("y")
                    y = inputcheck2()
    
                    x = find_point(x0, y0, x1, y1, y)
                    A = (x,y)
    
                    redraw1(ax1, ay1, ax2, ay2, A, 0, 9, ax, ay)
    
                    calc1(A, ax1, ay1, ax2, ay2, ax, ay)
                elif (ques == 3):
                    break
        elif choice1 == '4':
            while True:
               print("Line cutting algorithms on a flat area based on the Cohen – Sutherland technique.:")
               print("Enter 1 to define a rectangle.")
               print("Enter 2 to add a line.")
               print("Enter 3 to delete all lines.")
               print("Enter 4 to run Cohen–Sutherland algorithm.")
               print("Enter 5 for returning to previous menu.")
               
               choice = input("input:")
               while choice != '1' and choice != '2' and choice != '3'and choice != '4'and choice != '5':
                   print("Input must be 1,2,3,4 or 5, please try again")
                   choice = input("input:")
                
               if choice == '1':
                   print("Rectangle input.")
                   try:
                     x_min = float(input("x min:"))
                     y_min = float(input("y min:"))
                     x_max = float(input("x max:"))
                     y_max = float(input("y max:"))
                     assert(x_max > x_min and y_max > y_min)
                   except:
                     print("wrong rectangle input")
                   else:
                     plt.plot([x_min,x_max],[y_max,y_max],'r')
                     plt.plot([x_min,x_min],[y_max,y_min],'r')
                     plt.plot([x_min,x_max],[y_min,y_min],'r')
                     plt.plot([x_max,x_max],[y_max,y_min],'r')
                     first_time_reg = False
                     if first_time == False:
                        for x in range(line_start.shape[1]):
                           plt.plot([line_start[0,x],line_end[0,x]], [line_start[1,x],line_end[1,x]],'ko-')
                     plt.axis('equal')
                     plt.show()
               elif choice == '2':
                   print("Add line")
                   try:
                     x1 = float(input("x1:"))
                     y1 = float(input("y1:"))
                     x2 = float(input("x2:"))
                     y2 = float(input("y2:"))
                   except:
                     print("wrong point entry")
                   else:
                       if first_time == True:
                            line_start = np.array([[x1], [y1]])
                            print(line_start)
                            line_end = np.array([[x2], [y2]])
                            print(line_end)
                            first_time = False
                            plt.plot([line_start[0],line_end[0]], [line_start[1],line_end[1]],'ko-')
                            if first_time_reg == False:
                                plt.plot([x_min,x_max],[y_max,y_max],'r')
                                plt.plot([x_min,x_min],[y_max,y_min],'r')
                                plt.plot([x_min,x_max],[y_min,y_min],'r')
                                plt.plot([x_max,x_max],[y_max,y_min],'r')
                            plt.axis('equal')
                            plt.show()
                       else:
                            helper = np.array([[x1], [y1]])
                            line_start = np.append(line_start, helper, axis=1)
                            print(line_start)
                            
                            helper = np.array([[x2], [y2]])
                            line_end = np.append(line_end, helper, axis=1)
                            print(line_end)
                            
                            for x in range(line_start.shape[1]):
                               plt.plot([line_start[0,x],line_end[0,x]], [line_start[1,x],line_end[1,x]],'ko-')
                            if first_time_reg == False:
                                plt.plot([x_min,x_max],[y_max,y_max],'r')
                                plt.plot([x_min,x_min],[y_max,y_min],'r')
                                plt.plot([x_min,x_max],[y_min,y_min],'r')
                                plt.plot([x_max,x_max],[y_max,y_min],'r')
                            plt.axis('equal')
                            plt.show()
               elif choice == '3':
                   if first_time == True or line_start.shape[1] == 0:
                     print("there are no lines")
                   else:
                     print("Deleting lines...")
                 
                     line_start = np.array([[], []])
                     line_end = np.array([[], []])
                     print(line_start)
                     print(line_end)
                     if first_time_reg == False:
                                plt.plot([x_min,x_max],[y_max,y_max],'r')
                                plt.plot([x_min,x_min],[y_max,y_min],'r')
                                plt.plot([x_min,x_max],[y_min,y_min],'r')
                                plt.plot([x_max,x_max],[y_max,y_min],'r')
                                plt.axis('equal')
                                plt.show()
                     else:
                        plt.axis('equal')
                        plt.show()
               elif choice == '4':
                   if first_time_reg == True:
                     print("no rectangle is defined")
                   elif first_time == True or line_start.shape[1] == 0:
                     print("There are no lines")
                   else:
                     print("Implementation of Cohen–Sutherland algorithm.")
                     for x in range(line_start.shape[1]):
                        cohenSutherlandClip(line_start[0,x], line_start[1,x],line_end[0,x], line_end[1,x])
                     plt.plot([x_min,x_max],[y_max,y_max],'r')
                     plt.plot([x_min,x_min],[y_max,y_min],'r')
                     plt.plot([x_min,x_max],[y_min,y_min],'r')
                     plt.plot([x_max,x_max],[y_max,y_min],'r')
                     plt.axis('equal')
                     plt.show()
               elif choice == '5':
                   break
        elif choice1 == '5':
            break
    print("The program has ended.")