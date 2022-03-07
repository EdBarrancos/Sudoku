#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <stdarg.h>

#define ARG_NUM 1

#define CLEAR(var) var[0] = '\0'
#define FALSE 0
#define TRUE 1

#define RED "\033[0;31m"
#define NC "\033[0m" 

int tst(int h,int g[9][9],int x,int y,int kind,int array_passage);
int tst_lines(int g[9][9],int y,int x);
int tst_collums(int g[9][9],int y,int x);
int tst_squares(int g[9][9],int x,int y,int x_s,int y_s);

void throw_error(const char *fmt, ...){
  va_list args;
  va_start(args, fmt);

  fflush(stdout);

  fprintf(stderr, RED);
  vfprintf(stderr, fmt, args);
  fprintf(stderr, "\n");
  if (errno)
    fprintf(stderr, "\t%s\n", strerror(errno));
  fprintf(stderr, NC);

  exit(0);

  va_end(args);
}

void parse_args(int *debug, int argc, char *argv[]){
    if(argc > (ARG_NUM + 1)){
        throw_error("Invalid Number of Arguments");
        return;
    }

    *debug = FALSE;

    for(int i = 1; i < argc; i++){
        if(strcmp(argv[i], "-d") == 0)
            *debug = TRUE;
    }      
}


int main(int argc, char *argv[])
{
    int debug;

    parse_args(&debug, argc, argv);

    int r;
    int last_r = 0;
    int x,y;
    int x_s,y_s;
    int runs = 0;

    int sudoku[9][9] = {9,2,0,0,0,0,3,0,0,
                        0,5,0,0,4,0,0,2,0,
                        0,0,0,0,0,6,0,0,0,

                        0,0,0,4,0,0,0,1,0,
                        3,0,0,0,0,5,6,8,0,
                        0,0,0,0,8,3,0,0,4,

                        6,8,0,1,3,0,0,0,0,
                        0,0,4,0,0,0,1,0,0,
                        0,1,9,0,0,0,5,0,0};

    printf("Please, input the sudoku table that needs solving:");
    printf("\n");
    

    /*Main loop that will only stop when the sudoku is solved*/
    do{
        r = 0;
        /*We can test, at least at first, a "house" at a time instead a big for loop for all like no galo*/

        /*A for loop too test all*/
        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if (sudoku[y][x] == 0){
                    
                    sudoku[y][x] = tst(sudoku[y][x],sudoku,x,y,0,0);
                    
                    if (sudoku[y][x] != 0){
                        printf("x:%d, y:%d, value:%d\n",x,y,sudoku[y][x]);
                    }
                }
            }
        }

        if(runs == 0){
            printf("\n");
        }

        /*Test lines*/
        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if(sudoku[y][x] == 0){
                    
                    sudoku[y][x] = tst_lines(sudoku,y,x);
                    
                    if (sudoku[y][x] != 0){
                        printf("x:%d, y:%d, value:%d\n",x,y,sudoku[y][x]);
                    }
                }
            }
        }
        if(runs == 0){
            printf("\n");
        }

        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if (sudoku[y][x] == 0){
                    
                    sudoku[y][x] = tst(sudoku[y][x],sudoku,x,y,0,0);
                    
                    if (sudoku[y][x] != 0){
                        printf("x:%d, y:%d, value:%d\n",x,y,sudoku[y][x]);
                    }
                }
            }
        }
        if(runs == 0){
            printf("\n");
        }

        /*Test collums*/
        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if(sudoku[y][x] == 0){
                    
                    sudoku[y][x] = tst_collums(sudoku,y,x);
                    
                    if (sudoku[y][x] != 0){
                        printf("x:%d, y:%d, value:%d\n",x,y,sudoku[y][x]);
                    }
                }
            }
        }

        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if (sudoku[y][x] == 0){
                    
                    sudoku[y][x] = tst(sudoku[y][x],sudoku,x,y,0,0);
                    
                    if (sudoku[y][x] != 0){
                        printf("x:%d, y:%d, value:%d\n",x,y,sudoku[y][x]);
                    }
                }
            }
        }

        /*printf("Testing squares now:\n\n");*/
        for(y = 0;y < 9; y++){
            for(x = 0; x < 9;x++){
                if (sudoku[y][x] == 0){
                    for(y_s = 0;y_s < 9;y_s = y_s + 3){
                        if ((y == y_s) || (y == y_s+1) || (y == y_s+2)){
                            break;
                        }
                    }
                    for(x_s = 0;x_s < 9;x_s = x_s + 3){
                        if ((x == x_s) || (x == x_s+1) || (x == x_s+2)){
                            break;
                        }
                    }
                    if((y == 1) && (x == 4)){
                        printf("Testing squares x:%d, y:%d, value:%d, x_s:%d, y_s:%d\n\n",x,y,sudoku[y][x],x_s,y_s);
                    }
                    sudoku[y][x] = tst_squares(sudoku,x,y,x_s,y_s);
                    if(runs == 0){
                        printf("Tested squares x:%d, y:%d, value:%d, x_s:%d, y_s:%d\n",x,y,sudoku[y][x],x_s,y_s);
                    }
                }
            }
        }

        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if (sudoku[y][x] == 0){
                    
                    sudoku[y][x] = tst(sudoku[y][x],sudoku,x,y,0,0);
                }
            }
        }

        for(y = 0;y < 9;y++){
            for(x = 0;x < 9;x++){
                if (sudoku[y][x] != 0){
                    r++;
                }
            }
        }

        if (r == last_r){
            break;
        }
        last_r = r;
        runs++;
    }while(r != 81);/*r != 81*/

    for(y = 0;y <= 8;y++){
        printf("%d|%d|%d| |%d|%d|%d| |%d|%d|%d",sudoku[y][0],sudoku[y][1],sudoku[y][2],sudoku[y][3],sudoku[y][4],sudoku[y][5],sudoku[y][6],sudoku[y][7],sudoku[y][8]);
        printf("\n");
        if((y == 2) || (y == 5)){
            printf("\n");
        }
    }

    return 0;
}

int tst_squares(int g[9][9],int x,int y,int x_s,int y_s){

    int h[9][9] = {0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0};

    int counter = 0,kind_tst = 1;

    int y_c,x_c;

    int y_list = -1;

    int square_nbr;

    if((x == 4) && (y == 1)){
        printf("y:%d, y_s:%d\n\n",y,y_s);
    }

    for(y_c = 0;y_c < 3;y_c++){
        for(x_c = 0;x_c < 3;x_c++){
            y_list++;

            if((x == 4) && (y == 1)){
                printf("\nY-list:%d, x:%d, y:%d\n\n",y_list,x_c,y_c);
            }

            if (g[y_s+y_c][x_s+x_c] == 0){
                for(counter = 0;counter < 9;counter++){
                    h[y_list][counter] = tst(g[y_s+y_c][x_s+x_c],g,x_s+x_c,y_s+y_c,kind_tst,counter);

                    if((x == 4) && (y == 1)){
                        printf("In the middle of square testing\n");
                        printf("List form x:%d, y:%d\n",x_s+x_c,y_s+y_c);
                        printf("pos on list:%d, nbr of list:%d, value:%d\n\n",counter+1,y_list,h[y_list][counter]);
                    }

                }
            }
        }
    }

    if ((x == 4) && (y == 1)){
        printf("y:%d, y_s:%d\n",y,y_s);
    }

    /*Find the square number*/
    if (y == y_s){
        if (x == x_s){
            square_nbr = 0;
        }
        else if (x == (x_s+1)){
            square_nbr = 1;
        }
        else if (x == (x_s+2)){
            square_nbr = 2;
        }
    }
    else if (y == (y_s+1)){
        if (x == x_s){
            square_nbr = 3;
        }
        else if (x == (x_s+1)){
            square_nbr = 4;
        }
        else if (x == (x_s+2)){
            square_nbr = 5;
        }
    }
    else if (y == (y_s+2)){
        if (x == x_s){
            square_nbr = 6;
        }
        else if (x == (x_s+1)){
            square_nbr = 7;
        }
        else if (x == (x_s+2)){
            square_nbr = 8;
        }
    }

    if((x == 4) && (y == 1)){
        printf("square number:%d, y:%d, y_s:%d\n\n",square_nbr,y,y_s);
    }

    /*Cross the lists*/
    for(y_list = 0;y_list < 9;y_list++){
        if (y_list != square_nbr){
            for(x_c = 0;x_c < 9;x_c++){
                if (h[y_list][x_c] == h[square_nbr][x_c]){
                    h[square_nbr][x_c] = 0;
                }
            }
        }
    }

    /*See if we got a conclusion*/
    counter = 0;
    for(x_c = 0;x_c <= 8;x_c++){
        if (h[square_nbr][x_c] != 0){
            counter++;
        }
    }
    if (counter == 1){
        for(x_c = 0;x_c <= 8;x_c++){
            if (h[square_nbr][x_c] != 0){
                return h[square_nbr][x_c];
            }
        }
    }
    else{
        return 0;
    }
}

int tst_collums(int g[9][9],int y,int x){
    /*This time i'll do it the new way*/

    int h[9][9] = {0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0};

    int counter,kind_tst = 1;

    int y_c,x_c;

    /*Fill the lists*/
    for(y_c = 0;y_c <= 8; y_c++){
        if (g[y_c][x] == 0){
            for(counter = 0;counter <= 8;counter++){
                h[y_c][counter] = tst(g[y_c][x],g,x,y_c,kind_tst,counter);
            }
        }
    }


    /*Cross the lists*/
    for(y_c = 0;y_c <= 8;y_c++){
        if (y_c != y){
            for(x_c = 0;x_c <= 8;x_c++){
                if (h[y][x_c] != 0){
                    if (h[y][x_c] == h[y_c][x_c]){
                        h[y][x_c] = 0;
                    }
                }
            }
        }
    }

    /*See if we got a conclusion*/
    counter = 0;
    for(x_c = 0;x_c <= 8;x_c++){
        if (h[y][x_c] != 0){
            counter++;
        }
    }

    if (counter == 1){
        for(x_c = 0;x_c <= 8;x_c++){
            if (h[y][x_c] != 0){
                return h[y][x_c];
            }
        }
    }
    else{
        return 0;
    }
}

int tst_lines(int g[9][9],int y,int x){

    int h[9][9] = {0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0};

    int counter,kind_tst = 1;

    int y_c,x_checker,x_c;

    int y_list;

    /*Fill the lists*/
    for(x_c = 0;x_c <= 8; x_c++){
        if (g[y][x_c] == 0){
            for(counter = 0;counter <= 8;counter++){
                h[x_c][counter] = tst(g[y][x_c],g,x_c,y,kind_tst,counter);
            }
        }
    }


    /*Cross the lists*/
    for(y_c = 0;y_c <= 8;y_c++){
        if (y_c != x){
            for(x_c = 0;x_c <= 8;x_c++){
                if (h[x][x_c] != 0){
                    if (h[x][x_c] == h[y_c][x_c]){
                        h[x][x_c] = 0;
                    }
                }
            }
        }
    }

    /*See if we got a conclusion*/
    counter = 0;
    for(x_c = 0;x_c <= 8;x_c++){
        if (h[x][x_c] != 0){
            counter++;
        }
    }
    if (counter == 1){
        for(x_c = 0;x_c <= 8;x_c++){
            if (h[x][x_c] != 0){
                return h[x][x_c];
            }
        }
    }
    else{
        return 0;
    }
}

int tst(int h,int g[9][9],int x,int y,int kind,int array_passage){
    int h_l[9] = {1,2,3,4,5,6,7,8,9};
    int h_c[9] = {1,2,3,4,5,6,7,8,9};
    int h_q[9] = {1,2,3,4,5,6,7,8,9};
    int h_f[9] = {0,0,0,0,0,0,0,0,0};

    int x_t,y_t,h_t;

    int y_s,x_s,n_s,s[3][3] = {1,2,3,4,5,6,7,8,9};

    int t;

    /*Lets test the lines*/

    for(x_t = 0;x_t < 9;x_t++){
        for(h_t = 1;h_t != 10;h_t++){
            if(h_t == g[y][x_t]){
                h_l[h_t-1] = 0;
            }
        }
    }

    /*Lets test the collums now*/

    for(y_t = 0;y_t < 9;y_t++){
        for(h_t = 1;h_t != 10;h_t++){
            if(h_t == g[y_t][x]){
                h_c[h_t-1] = 0;
            }
        }
    }

    /*Lets figure out the square that h is in*/

    if(y <= 2){
        y_s = 0;
    }
    else if((y > 2) && (y <= 5)){
        y_s = 1;
    }
    else if((y > 5) && (y <= 8)){
        y_s = 2;
    }

    if(x <= 2){
        x_s = 0;
    }
    else if((x > 2) && (x <= 5)){
        x_s = 1;
    }
    else if((x > 5) && (x <= 8)){
        x_s = 2;
    }

    n_s = s[y_s][x_s];

    /*Test the squares*/
    /*square number 1*/
    if(n_s == 1){
        for(y_t = 0;y_t <= 2;y_t++){
            for(x_t = 0;x_t <= 2;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 2){
        for(y_t = 0;y_t <= 2;y_t++){
            for(x_t = 3;x_t <= 5;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 3){
        for(y_t = 0;y_t <= 2;y_t++){
            for(x_t = 6;x_t <= 8;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 4){
        for(y_t = 3;y_t <= 5;y_t++){
            for(x_t = 0;x_t <= 2;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 5){
        for(y_t = 3;y_t <= 5;y_t++){
            for(x_t = 3;x_t <= 5;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 6){
        for(y_t = 3;y_t <= 5;y_t++){
            for(x_t = 6;x_t <= 8;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 7){
        for(y_t = 6;y_t <= 8;y_t++){
            for(x_t = 0;x_t <= 2;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 8){
        for(y_t = 6;y_t <= 8;y_t++){
            for(x_t = 3;x_t <= 5;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }

    else if(n_s == 9){
        for(y_t = 6;y_t <= 8;y_t++){
            for(x_t = 6;x_t <= 8;x_t++){
                for(h_t = 1;h_t != 10;h_t++){
                    if(h_t == g[y_t][x_t]){
                        h_q[h_t-1] = 0;
                    }
                }
            }
        }
    }
    /*n_s is the number of the square, with that I know the coordinate of  the corner of the square*/


    /*Agr eu tenho que fazer uma gespecie de cross*/

    for(x_t = 0;x_t != 9;x_t++){
        if((h_l[x_t] == h_c[x_t]) && (h_l[x_t] == h_q[x_t]) && (h_l[x_t] == h_q[x_t])){
            h_f[x_t] = h_l[x_t];
        }
    }

    t = 0;
    for(x_t = 0;x_t < 9;x_t++){
        if(h_f[x_t] != 0){
            t++;
        }
    }
    if (kind == 0){
        if(t == 1){
            for(x_t = 0;x_t < 9;x_t++){
                if(h_f[x_t] != 0){
                    return h_f[x_t];
                }
            }
        }
        else{
            return 0;
        }
    }
    else if (kind == 1){
        return h_f[array_passage];
    }
}
