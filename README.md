# Sudoku

A small project to try to make a program to solve sudoku puzzles

It started a few years ago as a introductory project in order to learn a bit of C

I wanted to make a cleaner version in Python

**Author:** Eduardo Barrancos

## Index

## C Version

[sudoku_solver_old.c](c-version/soduku_solver_old.c) was an old project to make a Sudoku solver using C

Due to my lack of inexperience it is not the best program efficiency wise neither cleaness wise, but, at the time, I gave it my best shot.

### Usage

To insert the puzzle intended to be solved open [the c file](c-version/soduku_solver_old.c) and change the "sudoku" matrix. All blank spaces should have '0' instead.

Then, inside the [c-version folder](c-version)

```cd c-version/```

run the *"make"* command to compile or *"make debug"* to compile and debug

```make```

```make debug```

*"make run"* to compile and run.

```make run```

The *"make clean"* can be used to clean the binary file.

```make clean```

## Python Version

The [Python Updated version](python-version/src/main.py) of the Sudoku Solver.

### Usage

On the [python-version folder](python-version):

```cd python-version/```

Run the Command:

```python3 src/main.py path/to/input/file [path/to/output/file] [flag]```

If no output file is provided, the program will print the solution on the console

The output will be in the same format as the one in the input. *Either in a matrix set up or all in a single line*

Regarding the Input *Empty Cells in the puzzle should have 0's or other characters besides digits* *Please Leave no spaces between Cells*

#### Available Flags

Each flag also activates the properties of the ones above

**Example**: The *-e* flag prints the errors and the step-by-step changes

##### -v

Only Visualize the step-by-step changes made by the algorithm

##### -e

Also prints the Error Logs

##### -d

Also prints the Debug Logs

##### -i

Also prints the Info Logs

#### Testing

To test the program run the command:

```python3 tests/testing.py [flag]```

It will run all the tests in the [input folder](python-version/tests/inputs), comparing the results to the files in the [output folder](python-version/tests/outputs).

##### Adding More Tests

Add a file in the [input folder](python-version/tests/inputs) with the intended sudoku puzzle. *Empty Cells in the puzzle should have 0's or other characters besides digits* *Please Leave no spaces between Cells*

Then add a file to the [output folder](python-version/tests/outputs) with the same name as the first.
