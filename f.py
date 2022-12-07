
def CalcData2(M1, M2, D1, D2):  # simplifies the distributed load into 1 magnitude and 1 distance
    ResMag = (1/2)*(M1 + M2)*(D2 - D1)
    DistRes = (((1/6)*(M1-M2)*(D2-D1)**2 + (1/2)*M2*((D2-D1)**2))/ResMag) + D1
    return [ResMag, DistRes]

def reaction(Type, length, data1, data2calc, data3, support = 1):
    if Type == 1:  # calculates the reaction forces on each support for simply supported beam
        SumL, SumR = 0, 0
        for i in range(len(data1)):
            SumL += data1[i][0]*data1[i][1]
            SumR += data1[i][0]*(length - data1[i][1])

        for i in range(len(data2calc)):
            SumL += data2calc[i][0] * data2calc[i][1]
            SumR += data2calc[i][0] * (length - data2calc[i][1])

        for i in range(len(data3)):
            if data3[i][2] == 1:
                tempVal = data3[i][0]
                SumL += tempVal
                SumR -= tempVal
            else:
                tempVal = data3[i][0]
                SumL -= tempVal
                SumR += tempVal


        ReactionL = SumR/length
        ReactionR = SumL/length
        return ReactionL, ReactionR

    elif Type == 2:  # calculates the reaction forces on each support for overhanging beam
        SumL, SumR = 0, 0
        for i in range(len(data1)):
            SumL += data1[i][0] * data1[i][1]
            if data1[i][1] < support:
                SumR += data1[i][0] * (support - data1[i][1])
            else:
                SumR -= data1[i][0] * (data1[i][1] - support)

        for i in range(len(data2calc)):
            SumL += data2calc[i][0] * data2calc[i][1]
            if data2calc[i][1] < support:
                SumR += data2calc[i][0] * (support - data2calc[i][1])
            else:
                SumR -= data2calc[i][0] * (data2calc[i][1] - support)

        for i in range(len(data3)):
            if data3[i][2] == 1:
                tempVal = data3[i][0]
                SumL += tempVal
                SumR -= tempVal
            else:
                tempVal = -1 * data3[i][0]
                SumL -= tempVal
                SumR += tempVal

        ReactionR = SumL/support
        ReactionL = SumR/support

        return ReactionL, ReactionR
    elif Type == 3:
        SumL = 0
        for i in range(len(data1)):
            SumL += data1[i][0]

        for i in range(len(data2calc)):
            SumL += data2calc[i][0]

        ReactionR = SumL / length
        print(Type)
        print(ReactionR)
        return SumL, ReactionR


def IntShear(data1, data2, data3):  # Integration function
    temp1, temp2, temp3 = [], [], []
    for i in range(len(data1)):  # Flips the data type 1 so that each index starts with the distance
        dataN = data1[i][::-1]  # This will help with sorting based on distance
        temp1.append(dataN)
        dataN.append(1)  # this is to mark that the load is a point load
    for i in range(len(data2)):
        m = (data2[i][0] - data2[i][1]) / (data2[i][2] - data2[i][3])
        # finds the gradient of 2 endpoints of the distributed force

        c = data2[i][0] - m * data2[i][2]  # finds the c (intersection point with the y-axis)
        for j in range(1, 101):  # splits the distribution into 100 parts
            x = data2[i][2] + (data2[i][3] - data2[i][2]) * (j/100)  # finds the current tiny slice of distance x
            y = m * x + c  # calculates the y value for the given x
            A = y * (x - (data2[i][2] + (data2[i][3] - data2[i][2]) * ((j - 1)/100)))
            # calculates the area of the tiny rectangular slice

            temp2.append([(data2[i][2] + (j / 100) * (data2[i][3] - data2[i][2])), abs(A), 2])
            # appends the coordinates into a list, the 2 at the end is a distributed load
    for i in range(len(data3)):
        if data3[i][2] == 2:
            temp3.append([data3[i][1], data3[i][0], 3])
        else:
            temp3.append([data3[i][1], -data3[i][0], 3])

    temp1.extend(temp2)
    temp1.sort()

    return temp1, temp3


def moment(path):  # Integrates the shear function
    Val = []
    for i in range(1, len(path)):
        if path[i][1] == 1:
            for j in range(1, 101):  # divides each difference of point into 100 parts
                # so if it appears as if the moment graph has stopped, just give it a while, it will continue.

                A = path[i][0][1] * (1 / 100) * (path[i][0][0] - path[i - 1][0][0])  # area of the small slice
                Val.append([(path[i - 1][0][0] + (j / 100) * (path[i][0][0] - path[i - 1][0][0])), A, 0])
                # x value is the distance, y value (A) is the value of the small area slice, 0 is just a marker

        elif path[i][1] == 2:  # if current load is distributed and previous load is a point load
            if path[i - 1][1] == 1:
                for j in range(1, 101):
                    A = path[i][0][1] * (1 / 100) * (path[i][0][0] - path[i-1][0][0])
                    Val.append([(path[i - 1][0][0] + (j / 100) * (path[i][0][0] - path[i-1][0][0])), A, 0])

            else:  # if current load is distributed and previous load is also distributed
                A = path[i][0][1] * (path[i][0][0] - path[i-1][0][0])
                Val.append([path[i][0][0], A, 0])

    return Val













