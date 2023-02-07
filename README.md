# ma1008-miniproject

1. How to run the program
Upon running the program, the user will be prompted to input 1 or 2 (just the number) to
indicate whether the input data is manually keyed in or loaded from a previously saved
file (“PrevData.txt”). If the file is empty the program will come to an end, prompting the
user to rerun it and then manually input the data.


2. Capabilities
The program is capable of running any sort of combination of forces on any type of beam
and drawing the forces on the beam, the respective shear graph, and moment graph. It
is also capable of overlapping distributed forces and linearly varying distributed
forces. Other than the turtle visuals, the program is able to run values from a text file or
through the user’s input.


3. Data file format
Text Document (.txt) → filename: PrevData.txt
The first line is always the type of the beam starting with “Type” followed by a space and
the integer corresponding to the beam (e.g. Type 2). The second line is always the
length of the beam followed by a space and the value of the beam’s length (e.g. Length
10.0). The third line depends on the type. If the beam is an overhanging beam, there will
be a line starting with “DistOfSup” followed by a space and the distance of the right
support’s value (e.g. DistOfSup 6.0). The following lines contain the actual load type and
its corresponding magnitudes and positions separated by spaces. A concentrated load
will start with “1”, distributed loads with “2”, and “3” for bending moments. For a
concentrated load, the first value after “1” is the magnitude followed by the position (e.g.
1 8.0 8.0). For a distributed load, the values after “2” are the magnitude of the left end
load, the position of the left magnitude, the magnitude of the right end load, and the
position of the right load respectively (e.g. 2 1.0 9.0 5.0 8.0). For a bending moment, the
values after “3” are the magnitude, position, and an integer value 1 or 2 representing its
clockwise or counterclockwise orientation (e.g. 3 10.0 7.0 2). The file is then ended with
a -1 to mark the end of the file.


4. Strengths
● Able to compute a combination of force types, position, and magnitude.
● Able to compute the shear and moment graph for all types of forces and beams.
○ Including but not limited to distributed varying loads, overlapping distributed
varying loads, and point loads within distributed loads.
● Labeled values for forces on the shear graph.
● Labeled support reaction forces on beam and magnitude of forces on beam.
● Forces on the force diagram are scaled within each type.
● Both graphs perfectly align with the force diagram on the top.


5. Limitations
● Moment graph unlabeled
● Values of position for all graphs are unlabeled
● The bending moment represented on the moment graph can be inconsistent and a bit
faulty at times.
● Due to the nature of the moment graph algorithm, it may take a while for the graph to
render. When it looks like it may have stopped, it is doing 100 iterations on the same
spot.


6. Submitted Files
● f.py consists of the calculating functions
● g.py consists of the functions responsible for drawing the graphs
● Main File.py is where everything comes together. This is the file to run.


PDF file containing the diagrams of the program output:
[MA1008 Mini Project Report.pdf](https://github.com/jensonjenkins/ma1008-miniproject/files/10677989/MA1008.Mini.Project.Report.pdf)
