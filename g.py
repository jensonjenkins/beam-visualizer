import turtle
import math
import f

def border():
    T = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(1000, 800)  # sets the turtle window to 1000 x 800 pixels
    T.speed(0)

    T.penup()
    T.goto(-382, 358)
    T.pendown()

    T.forward(764)
    T.right(90)
    T.forward(712)
    T.right(90)
    T.forward(764)
    T.right(90)
    T.forward(712)
    T.right(90)

    T.penup()
    T.goto(-382, 120.66)
    T.pendown()

    T.forward(764)

    T.penup()
    T.goto(-382, -116.66)
    T.pendown()

    T.forward(764)
    T.hideturtle()

def load1(length, data1):  # draws the point loads on the beam
    templist1 = []

    if len(data1) > 0:
        T = turtle.Turtle()
        T.speed(0)
        T.right(90)
        T.penup()


        for i in range(len(data1)):
            templist1.append(abs(data1[i][0]))
        for i in range(len(data1)):
            T.goto((data1[i][1] / length) * 500 - 250, 230)
            T.pendown()

            T.stamp()
            T.goto((data1[i][1] / length) * 500 - 250, (data1[i][0]/max(templist1)) * 100 + 230)
            T.write(f"{data1[i][0]} kN")
            T.penup()
            T.hideturtle()


def load2(length, data2):  # draws the distributed loads on the beam
    templist1 = []
    if len(data2) > 0:  # [M1, M2, D1, D2]
        T = turtle.Turtle()
        T.speed(0)
        T.right(90)
        T.penup()
        for i in range(len(data2)):
            templist1.append(data2[i][0])
            templist1.append(data2[i][1])

        for i in range(len(data2)):
            T.color("black" , "#baffc4")
            
            T.goto((data2[i][2] / length) * 500 - 250, 230)
            T.pendown()
            
            T.begin_fill()
            T.goto((data2[i][2] / length) * 500 - 250, (data2[i][0] / max(templist1)) * 100 + 230)
            T.write(f"{data2[i][0]} kN/m")
            T.penup()
            T.goto((data2[i][2] / length) * 500 - 250, 230)
            T.stamp()

            T.goto((data2[i][3] / length) * 500 - 250, 230)
            T.pendown()
            T.stamp()
            
            T.goto((data2[i][3] / length) * 500 - 250, (data2[i][1] / max(templist1)) * 100 + 230)
            T.write(f"{data2[i][1]} kN/m")
            
            T.goto((data2[i][2] / length) * 500 - 250, (data2[i][0] / max(templist1)) * 100 + 230)
            T.end_fill()
            T.penup()
            T.hideturtle()

def load3(length, data3):  # draws the moment on the beam

    templist = []

    if len(data3) > 0:  # [M, D, O]
        T = turtle.Turtle()
        T.speed(0)
        T.penup()
        for i in range(len(data3)):
            templist.append(data3[i][0])
        for i in range(len(data3)):
            if data3[i][2] == 1:
                T.goto((data3[i][1] / length) * 500 - 250, 212.5 + data3[i][0]/max(templist) * 75)
                T.pendown()
                T.circle(-1 * data3[i][0]/max(templist) * 75, 200)
                T.stamp()
                T.penup()
                T.goto((data3[i][1] / length) * 500 - 250, data3[i][0]/max(templist) * 75 + 217.5)
                T.pendown()
                T.write(f"{data3[i][0]} kNm")
                T.penup()
                T.setheading(0)
            elif data3[i][2] == 2:
                T.goto((data3[i][1] / length) * 500 - 250, 212.5 - data3[i][0]/max(templist) * 75)
                T.pendown()
                T.circle(data3[i][0]/max(templist) * 75, 200)
                T.stamp()
                T.penup()
                T.goto((data3[i][1] / length) * 500 - 250, data3[i][0] / max(templist) * 75 + 217.5)
                T.pendown()
                T.write(f"{data3[i][0]} kNm")
                T.penup()
                T.setheading(0)

        T.hideturtle()


def beam(type, L, R,  length=0, support=0):  # draws the beam itself (type 1, 2, 3 corresponds to the input)
    if type == 1:
        T = turtle.Turtle()
        T.speed(0)
        T.penup()
        T.color("#24475F", "#779EB7")
        T.begin_fill()
        T.goto(-250, 230)
        T.pendown()
        T.forward(500)
        T.right(90)
        T.forward(35)
        T.right(90)
        T.forward(500)
        T.right(90)
        T.forward(35)
        T.end_fill()
        T.goto(-250, 195)
        T.stamp()
        T.goto(-250, 170)

        T.write(f"{L:5.2f} kN")
        T.penup()
        T.goto(250, 195)
        T.pendown()
        T.stamp()
        T.goto(250, 170)

        T.write(f"{R:5.2f} kN")

        T.hideturtle()

    elif type == 2:
        T = turtle.Turtle()
        T.speed(0)
        T.penup()
        T.color("#24475F", "#779EB7")
        T.begin_fill()
        T.goto(-250, 230)
        T.pendown()
        T.forward(500)
        T.right(90)
        T.forward(35)
        T.right(90)
        T.forward(500)
        T.right(90)
        T.forward(35)
        T.end_fill()
        T.goto(-250, 195)
        T.stamp()
        T.goto(-250, 170)
        T.write(f"{L:5.2f} kN")
        T.penup()

        T.goto((support / length) * 500 - 250, 195)
        T.pendown()
        T.stamp()
        T.write(f"{support} m")
        T.goto((support / length) * 500 - 250, 170)
        T.write(f"{R:5.2f} kN")
        T.penup()
        T.goto(250, 195)
        T.pendown()
        T.write(f"{length} m")

        T.hideturtle()

    else:
        T = turtle.Turtle()
        T.speed(0)
        T.penup()
        T.color("#24475F", "#779EB7")
        T.begin_fill()
        T.goto(-250, 230)
        T.pendown()
        T.forward(500)
        T.right(90)
        T.forward(35)
        T.right(90)
        T.forward(500)
        T.right(90)
        T.forward(35)
        T.end_fill()

        T.color("black", "grey")
        T.goto(250, 230)
        T.begin_fill()
        T.left(180)
        T.fd(90)
        T.left(90)
        T.fd(35)
        T.left(90)
        T.fd(190)
        T.left(90)
        T.fd(35)
        T.left(90)
        T.fd(190)
        T.end_fill()
        T.hideturtle()

def shearGraph(type, length, data, L = 0, R = 0, DistOfSup = 1):  # draws the shear graph itself
    T = turtle.Turtle()
    T.speed(0)
    T.penup()
    T.goto(-250, 99)
    T.pendown()
    T.left(90)
    T.stamp()
    T.write("Shear Force (kN)")
    T.goto(-250, -99)
    T.penup()
    T.goto(-270, 0)
    T.write("0 kN")
    T.goto(-250, 0)
    T.pendown()
    
    T.goto(250, 0)
    T.right(90)
    T.stamp()
    T.penup()
    T.goto(250, -16)
    T.write("Distance along beam (m)")
    T.goto(-250, 0)
    T.pd()

    if type == 1:  # draws for the simply supported beam
        path = []
        data.insert(0, [0, -L, 1])  # inserts the value of the left reaction force as a starting point
        emp = []
        for i in range(len(data)):
            emp.append(abs(L - data[i][1]))  # takes the maximum displacement from x-axis to scale into proportion

        for i in range(len(data)):
            if data[i][2] == 2:  # draws the graph for distributed loads
                if data[i-1][2] == 1:
                    T.fd(-250 + (data[i][0] / length) * 500 - (-250 + (data[i - 1][0] / length) * 500))
                if data[i - 1][1] != -L and data[i-1][2] != 1:
                    L -= data[i - 1][1]  # subtracts the current value with each iterated force
                T.goto(-250 + (data[i][0]/length)*500, ((L - data[i][1])/ max(emp)) * 90)
                path.append([T.pos(), 2])
                # each path.append is to keep track of the turtles position in order to be able to draw the moment graph

            else:  # draws the graph for point loads
                if i == 0:
                    try:
                        T.goto(-250 + (data[i][0] / length) * 500, (L/max(emp)) * 90)
                        T.write(f"{L:5.2f}kN")
                        path.append([T.pos(), 1])

                    except ZeroDivisionError:  # accounts for point load graphs jumping vertically
                        pass
                else:
                    if data[i - 1][1] != -L and data[i-1][2] == 2:
                        L -= data[i - 1][1]
                    T.fd(-250 + (data[i][0] / length) * 500 - (-250 + (data[i-1][0] / length) * 500))
                    T.write(f"{L:5.2f}kN")
                    path.append([T.pos(), 1])
                    L -= data[i][1]  # subtracts the current value with each iterated force
                    T.goto(-250 + (data[i][0] / length) * 500, (L/max(emp)) * 90)
                    path.append([T.pos(), 1])

        T.forward(250 - (-250 + (data[-1][0]/length)*500))  # goes fully forward from current point to the end
        T.write(f"{L:5.2f}kN")
        path.append([T.pos(), 1])

        T.hideturtle()
        return path, max(emp)

    elif type == 2:  # draws for the overhanging beam
        data.insert(0, [0, -L, 1])
        data.append([DistOfSup, -R, 1])
        data.sort()
        emp = []
        path = []
        for i in range(len(data)):
            emp.append(abs(L - data[i][1]))

        for i in range(len(data)):
            if data[i][2] == 2:
                if data[i-1][2] == 1:
                    T.fd(-250 + (data[i][0] / length) * 500 - (-250 + (data[i - 1][0] / length) * 500))
                    path.append([T.pos(), 2])
                if data[i - 1][1] != -L and data[i-1][2] != 1:
                    L -= data[i - 1][1]
                T.goto(-250 + (data[i][0]/length)*500, ((L - data[i][1])/ max(emp)) * 90)
                path.append([T.pos(), 2])

            else:
                if i == 0:
                    T.goto(-250 + (data[i][0] / length) * 500, (L/max(emp)) * 90)
                    T.write(f"{L:5.2f}kN")
                    path.append([T.pos(), 1])
                else:
                    if data[i - 1][1] != -L and data[i-1][2] == 2:
                        L -= data[i - 1][1]
                    T.fd(-250 + (data[i][0] / length) * 500 - (-250 + (data[i-1][0] / length) * 500))
                    T.write(f"{L:5.2f}kN")
                    path.append([T.pos(), 1])
                    L -= data[i][1]
                    T.goto(-250 + (data[i][0] / length) * 500, (L/max(emp)) * 90)
                    path.append([T.pos(), 1])

        T.forward(250 - (-250 + (data[-1][0] / length) * 500))
        T.write(f"{L:5.2f}kN")
        path.append([T.pos(), 1])
        T.hideturtle()
        return path, max(emp)

    else:   # draws for the cantilever beam
        data.insert(0, [0, 0, 1])
        Max = 0
        for i in range(len(data)):
            Max += data[i][1]
        for i in range(len(data)):  # the max function is rather different since the graph starts from 0 downwards
            if data[i][2] == 1:
                Max += data[i][1]
        path = []
        for i in range(len(data)):
            if data[i][2] == 2:
                if data[i - 1][2] == 1:
                    T.fd(-250 + (data[i][0] / length) * 500 - (-250 + (data[i - 1][0] / length) * 500))
                    path.append([T.pos(), 2])
                if data[i - 1][1] != 0 and data[i - 1][2] != 1:
                    L -= data[i - 1][1]
                T.goto(-250 + (data[i][0] / length) * 500, ((L - data[i][1]) / Max) * 90)
                path.append([T.pos(), 2])
            else:
                if i == 0:
                    T.goto(-250 + (data[i][0] / length) * 500, (L / Max) * 90)
                    path.append([T.pos(), 1])
                else:
                    if data[i - 1][1] != -L and data[i-1][2] == 2:
                        L -= data[i - 1][1]
                    T.fd(-250 + (data[i][0] / length) * 500 - (-250 + (data[i - 1][0] / length) * 500))
                    T.write(f"{L:5.2f}kN")
                    path.append([T.pos(), 1])
                    L -= data[i][1]
                    T.goto(-250 + (data[i][0] / length) * 500, (L / Max) * 90)         
                    path.append([T.pos(), 1])

        T.forward(250 - (-250 + (data[-1][0] / length) * 500))
        T.write(f"{L:5.2f}kN")
        path.append([T.pos(), 1])
        T.hideturtle()
        return path, Max


def momentGraph(Val, MomentList, length, maxval):  # draws the moment graph
    T = turtle.Turtle()
    T.speed(0)
    T.penup()
    T.goto(-250, -140.66)
    T.pendown()
    T.left(90)
    T.stamp()
    T.write("Bending Moment (kN-m)")
    T.goto(-250, -140.66 - 197.67)
    T.penup()
    T.goto(-285, -239.5)
    T.write("0 kN-m")
    T.goto(-250, -239.5)
    T.pendown()
    
    T.goto(250, -239.5)
    T.right(90)
    T.stamp()
    T.write("Distance along beam (m)")
    T.goto(-250, -239.5)

    Y = 0
    scale = 0
    MaxList = []
    MomentVal = []

    for i in range(len(Val)):
        scale += Val[i][1]
    for i in range(len(MomentList)):
        MomentVal.append([MomentList[i][0], MomentList[i][1]/maxval * scale])

    #  specifically for including the bending moment into the graph since it was excluded previously

    for i in range(len(Val)):
        Y += Val[i][1]
        MaxList.append(abs(Y))
    for i in range(len(MomentVal)):
        Y += MomentVal[i][1]
        MaxList.append(abs(Y))
    try:
        value = max(MaxList)
    except ValueError:
        pass

    Y = 0
    for i in range(len(MomentVal)):
        Val.append([(MomentVal[i][0] / length * 500) - 250, MomentVal[i][1], 3])
    Val.sort()
    
    for i in range(len(Val)):  # draws the actual graph excluding the bending moment
        try:
            if Val[i][2] == 3:
                Y += Val[i][1]
                T.goto(Val[i][0], Y / value * 90 - 239.5)
            else:
                Y += Val[i][1]
                T.goto(Val[i][0], Y / value * 90 - 239.5)
        except ZeroDivisionError:
            pass

    T.hideturtle()

