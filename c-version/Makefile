CC := gcc
FLAGS = 

all: sudoku

C_FILES := soduku_solver_old.c

debug: FLAGS = -d
debug: all

sudoku: $(C_FILES)
	$(CC) $(FLAGS) -o $@ $^

clean:
	rm sudoku

run:
	./sudoku