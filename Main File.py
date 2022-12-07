import turtle
import f
import g

Data1 = []
Data2 = []
Data2Calc = []
Data3 = []

ListOfInputs, IntType = [1, 2], 0

while IntType not in ListOfInputs:
    try:
        IntType = int(input("Enter [1] to load previous data, Enter [2] to key in new data : "))
    except ValueError:
        continue

if IntType == 1:
    outfile = open("PrevData.txt", 'r')
    for lines in outfile:
        items = lines.split()

        if items[0] == "Type":
            Type = int(items[1])
        if items[0] == "Length":
            Length = float(items[1])
        if items[0] == "DistOfSup":
            DistOfSup = float(items[1])
        if items[0] == '1':
            Data1.append([float(items[1]), float(items[2])])
        if items[0] == '2':
            Data2.append([float(items[1]), float(items[2]), float(items[3]), float(items[4])])
        if items[0] == '3':
            Data3.append([float(items[1]), float(items[2]), int(items[3])])
        if items[0] == '-1':
            continue


elif IntType == 2:
    outfile = open("PrevData.txt", 'w').close()
    outfile = open("PrevData.txt", 'w')
    print()

    print("Types of Beams : ")
    print("[1] Simply Supported Beam")
    print("[2] Over-hanging Beam")
    print("[3] Cantilever Beam")
    ListOfBeams, Type = [1, 2, 3], 0

    while Type not in ListOfBeams:
        try:
            Type = int(input("Enter 1, 2 or 3 to Select : "))
            print(f"Type {Type}", file=outfile)
        except ValueError:
            continue
    print()

    Error = True
    while Error:
        try:
            Length = -1
            while Length <= 0:
                Length = float(input("Enter length of beam : "))
                print(f"Length {Length}", file=outfile)
            Error = False
        except ValueError:
            continue

    if Type == 2:
        Error = True
        while Error:
            try:
                DistOfSup = float(input("Enter distance of movable support from left end : "))
                print(f"DistOfSup {DistOfSup}", file=outfile)
                Error = False
            except ValueError:
                continue

        while True:
            if DistOfSup > Length or DistOfSup < 0:
                Error = True
                while Error:
                    try:
                        DistOfSup = float(input("Enter distance of movable support from left end : "))
                        Error = False
                    except ValueError:
                        continue
            else:
                break

    while True:
        print()
        print("Types of Loads : ")
        print("[1] Concentrated Loads")
        print("[2] Distributed Loads")
        print("[3] Bending Moment")

        ListOfLoads, Load = [1, 2, 3, -1], 0

        while Load not in ListOfLoads:
            try:
                Load = int(input("Enter 1, 2 or 3 to Select, -1 if None : "))

            except ValueError:
                continue
        print(f"{Load}", end=' ', file=outfile)
        Error = True
        while Error:
            try:
                if Load == 1:
                    M = float(input("Enter magnitude of load : "))
                    while True:
                        D = float(input("Enter distance from left end of beam : "))
                        if D <= Length:
                            break
                        else:
                            continue
                    Data1.append([M, D])
                    print(f"{M} {D}", file=outfile)
                    Error = False
                elif Load == 2:
                    M1 = float(input("Enter left magnitude of load distribution : "))
                    M2 = float(input("Enter right magnitude of load distribution : "))
                    while True:
                        D1 = float(input("Enter distance of left magnitude from left end of beam : "))
                        D2 = float(input("Enter distance of right magnitude from left end of beam (Larger than left distance) : "))
                        if D1 < D2 and D1 < Length and D2 <= Length:
                            break
                        else:
                            continue
                    Data2.append([M1, M2, D1, D2])
                    print(f"{M1} {M2} {D1} {D2}", file=outfile)

                    Error = False

                elif Load == 3:
                    M = float(input("Enter magnitude of load : "))
                    D = float(input("Enter distance from left end of beam : "))
                    O = 0
                    while O not in [1, 2]:
                        O = int(input("[1] for clockwise, [2] for anti-clockwise : "))

                    Data3.append([M, D, O])
                    print(f"{M} {D} {O}", file=outfile)
                    Error = False
                else:
                    break

            except ValueError:
                continue
        if Load == -1:
            break


try:
    for i in range(len(Data2)):
        Data2Calc.append(f.CalcData2(Data2[i][0], Data2[i][1], Data2[i][2], Data2[i][3]))
except NameError:
    pass

try:  # draws all the loads and beams
    if Type == 1:
        L, R = f.reaction(Type, Length, Data1, Data2Calc, Data3)
        g.border()
        g.beam(Type, L, R, Length)
        g.load2(Length, Data2)
        g.load1(Length, Data1)
        g.load3(Length, Data3)

    elif Type == 2:
        L, R = f.reaction(Type, Length, Data1, Data2Calc, Data3, DistOfSup)
        g.border()
        g.beam(Type, L, R, Length, DistOfSup)
        g.load2(Length, Data2)
        g.load1(Length, Data1)
        g.load3(Length, Data3)

    elif Type == 3:
        g.border()
        g.beam(Type, 0, 0, 0, 0)
        g.load2(Length, Data2)
        g.load1(Length, Data1)
        g.load3(Length, Data3)
except NameError:
    print("There are no saved data. Please re-run the program and key in the new data.")

g.border()

try: # draws the shear and moment graphs
    if Type == 1:
        ShearList, MomentList = f.IntShear(Data1, Data2, Data3)
        path, maxval = g.shearGraph(Type, Length, ShearList, L, R)
        Val = f.moment(path)
        g.momentGraph(Val, MomentList, Length, maxval)
    elif Type == 2:
        ShearList, MomentList = f.IntShear(Data1, Data2, Data3)
        path, maxval = g.shearGraph(Type, Length, ShearList, L, R, DistOfSup)
        Val = f.moment(path)
        g.momentGraph(Val, MomentList, Length, maxval)
    else:
        ShearList, MomentList = f.IntShear(Data1, Data2, Data3)
        path, maxval = g.shearGraph(Type, Length, ShearList)
        Val = f.moment(path)
        g.momentGraph(Val, MomentList, Length, maxval)
except NameError:
    pass


outfile.close()
turtle.done()
