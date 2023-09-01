#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
void ValueBoard();                 // done
void players();                    // done
void ladder();                     // done
int dice();                        // done
int check(int index1, int index2); // done
void welcome();                    // done

static int index1 = 0, index2 = 0;
static int flag1 = 0, flag2 = 0;
void main()
{
    welcome();
    players();
    getch();
}

void welcome()
{
    system("cls");
    char st0[200] = {"\t\t\t\t\t\t   |\t\tWelcome To Snake and Ladder Game            |\n\t\t\t\t\t\t   |\t\t\t\t\t\t\t    |\n"};
    char st1[100] = {"\t\t\t\t\t\t   |   -P1- is the player 1\t\t                    |\n"};
    char st2[100] = {"\t\t\t\t\t\t   |   -P2- is the player 2\t\t                    |\n"};
    char st3[100] = {"\t\t\t\t\t\t   |   -S- indicates Snake\t\t                    |\n"};
    char st4[100] = {"\t\t\t\t\t\t   |   -L- indicates Ladder\t\t                    |\n"};
    char st5[200] = {"\t\t\t\t\t\t   |   **If P1 and P2 are on the same block then,           |\n\t\t\t\t\t\t   |   -P- indicates both players\t                    |\n"};
    char st6[100]={"\t\t\t\t\t\t   |    Enter any key to Start the Game\t\t            |\n"};
    int i, j, k;
    printf("\t\t\t\t\t\t    ____________________\n");

    for (j = 0; j < strlen(st0); j++)
    {
        printf("%c", st0[j]);
        usleep(1500);
    }
    for (j = 0; j < strlen(st1); j++)
    {
        printf("%c", st1[j]);
        usleep(1500);
    }
    for (j = 0; j < strlen(st2); j++)
    {
        printf("%c", st2[j]);
        usleep(1500);
    }
    for (j = 0; j < strlen(st3); j++)
    {
        printf("%c", st3[j]);
        usleep(1500);
    }
    for (j = 0; j < strlen(st4); j++)
    {
        printf("%c", st4[j]);
        usleep(1500);
    }
    for (j = 0; j < strlen(st5); j++)
    {
        printf("%c", st5[j]);
        usleep(1500);
    }
    for (j = 0; j < strlen(st6); j++)
    {
        printf("%c", st6[j]);
        usleep(1500);
    }
    printf("\t\t\t\t\t\t   |____________________|\n");
    getch();
}

void ladder()
{
    flag1 = 0, flag2 = 0;
    if (index1 == 74)
    {
        index1 += 18;
        flag1 = 1;
    }
    if (index2 == 74)
    {
        index2 = 92;
        flag2 = 1;
    }
    if (index1 == 62)
    {
        index1 = 81;
        flag1 = 1;
    }
    if (index2 == 62)
    {
        index2 = 81;
        flag2 = 1;
    }
    if (index1 == 13)
    {
        index1 = 46;
        flag1 = 1;
    }
    if (index2 == 13)
    {
        index2 = 46;
        flag2 = 1;
    }
    if (index1 == 50)
    {
        index1 += 19;
        flag1 = 1;
    }
    if (index2 == 50)
    {
        index2 += 19;
        flag2 = 1;
    }
}

void ValueBoard()
{
    system("cls");
    char snake1[200]={"\t\t\t\t\t\t     |\t\tSnake 1- Mouth is at 99 and Tail is at 40             |\n"};
    char snake2[200]={"\t\t\t\t\t\t     |\t\tSnake 2- Mouth is at 89 and Tail is at 53             |\n"};
    char snake3[200]={"\t\t\t\t\t\t     |\t\tSnake 3- Mouth is at 76 and Tail is at 58             |\n"};
    char snake4[200]={"\t\t\t\t\t\t     |\t\tSnake 4- Mouth is at 43 and Tail is at 18             |\n"};
    char lad1[200]={"\t\t\t\t\t\t     |\t\tLadder 1 is at 74 to 92                               |\n"};
    char lad2[200]={"\t\t\t\t\t\t     |\t\tLadder 2 is at 62 to 81                               |\n"};
    char lad3[200]={"\t\t\t\t\t\t     |\t\tLadder 3 is at 13 to 46                               |\n"};
    char lad4[200]={"\t\t\t\t\t\t     |\t\tLadder 4 is at 50 to 69                               |\n"};
    printf("\t\t\t\t\t\t      ______________________\n");
    printf("\t\t\t\t\t\t     |                                                                |\n");
    printf("%s",snake1);
    printf("%s",snake2);
    printf("%s",snake3);
    printf("%s",snake4);
    printf("%s",lad1);
    printf("%s",lad2);
    printf("%s",lad3);
    printf("%s",lad4);
    printf("\t\t\t\t\t\t     |______________________|\n\n");
    
    int board[10][10], i, j, x = 100, y = 81;
    printf("\t\t\t\t\t\t ______________________________\n");
    printf("\t\t\t\t\t\t|                                                                                        |\n");

    

    for (i = 0; i < 10; i++)
    {
        for (j = 0; j < 10; j++)
        {
            if (i % 2 == 0)
            {
                board[i][j] = x--;
            }
            else
            {
                board[i][j] = y++;
            }
        }
        if (i % 2 == 0)
            x -= 10;
        else
            y -= 30;
    }
    
    ladder();
    int s1 = 0, s2 = 0, s3 = 0, s4 = 0;
    // system("cls");
    for (i = 0; i < 10; i++)
    {
        printf("\t\t\t\t\t\t");
        for (j = 0; j < 10; j++)
        {
            if(j==0)
            printf("|\t");
            if (index1 == index2 && index1 == board[i][j])
            {
                printf("\e[46m*P*\e[0m\t");
            }
            else if (index1 == board[i][j] && index1 != 99 && index1 != 89 && index1 != 76 && index1 != 43)
            {
                printf("\e[44m*P1*\e[0m\t");
            }
            else if (board[i][j] == index2)
            {
                printf("\e[45m*P2*\e[0m\t");
            }
            else if (board[i][j] == 99 || board[i][j] == 40)
            {
                if (index1 == 99)
                {
                    index1 = 40;
                    s1 = 1;
                }
                if (index2 == 99)
                {
                    index2 = 40;
                    s1 = 1;
                }
                printf("\e[31m-S1-\e[0m\t");
            }
            else if (board[i][j] == 74 || board[i][j] == 92)
            {
                printf("\e[34m-L1-\e[0m\t");
            }
            else if (board[i][j] == 62 || board[i][j] == 81)
            {
                printf("\e[35m-L2-\e[0m\t");
            }
            else if (board[i][j] == 89 || board[i][j] == 53)
            {
                if (index1 == 89)
                {
                    index1 = 53;
                    s2 = 1;
                }
                if (index2 == 89)
                {
                    index2 = 53;
                    s2 = 1;
                }
                printf("\e[30m-S2-\e[0m\t");
            }
            else if (board[i][j] == 76 || board[i][j] == 58)
            {
                if (index1 == 76)
                {
                    index1 = 58;
                    s3 = 1;
                }
                if (index2 == 76)
                {
                    index2 = 58;
                    s3 = 1;
                }
                printf("\e[32m-S3-\e[0m\t");
            }
            else if (board[i][j] == 13 || board[i][j] == 46)
            {
                printf("\e[36m-L3-\e[0m\t");
            }
            else if (board[i][j] == 50 || board[i][j] == 69)
            {
                printf("\e[31m-L4-\e[0m\t");
            }
            else if (board[i][j] == 43 || board[i][j] == 18)
            {
                if (index1 == 43)
                {
                    index1 = 18;
                    s4 = 1;
                }
                if (index2 == 43)
                {
                    index2 = 18;
                    s4 = 1;
                }
                printf("\e[33m-S4-\e[0m\t");
            }
            else
                printf(" %d\t", board[i][j]);

            if(j==9)
            printf(" |");     
        }
        // printf("\t\t\t\t\t\t|                                                                            |");
        printf("\n\t\t\t\t\t\t|                                                                                        |\n");
    }
    printf("\t\t\t\t\t\t|______________________________|\n");
    if (flag2 == 1)
    {
        printf("PLAYER 2 You Stepped On Ladder \2\2\2\n\n");
        sleep(3);
        system("cls");
        ValueBoard();
    }
    if (flag1 == 1)
    {
        printf("PLAYER 1 You Stepped On Ladder \2\2\2\n\n");
        sleep(3);
        system("cls");
        ValueBoard();
    }
    if (s1 == 1)
    {
        printf("You are bitten by snake!!! \nYou were at 99 and now you are at 40 :(\n\n");
        sleep(3);
        system("cls");
        ValueBoard();
    }
    if (s2 == 1)
    {
        printf("You are bitten by snake!!!  \nYou were at 89 and now you are at 53 :(\n\n");
        sleep(3);
        system("cls");
        ValueBoard();
    }
    if (s3 == 1)
    {
        printf("You are bitten by snake!!!  \nYou were at 76 and now you are at 58 :(\n\n");
        sleep(3);
        system("cls");
        ValueBoard();
    }
    if (s4 == 1)
    {
        printf("You are bitten by snake!!! \nYou were at 43 and now you are at 13 :(\n\n");
        sleep(3);
        system("cls");
        ValueBoard();
    }
}

int dice()
{
    srand(time(0));
    int p = rand() % 7;
    if (p != 0)
        return p;
    else
    {
        while (p == 0)
        {
            p = rand() % 7;
        }
        return p;
    }
}

int check(int index1, int index2)
{
    if (index1 == 100)
    {
        printf("\n\n\t\t\t\t\t\t\t\t\t\tPlayer 1 WON  \2\2\2\n");
        return 1;
    }
    if (index2 == 100)
    {
        printf("\n\n\t\t\t\t\t\t\t\t\t\tPlayer 2 WON  \2\2\2\n");
        return 1;
    }
    return 0;
}

void players()
{
    int p1, p2, i, j;
    // index1 = 50;
    // ValueBoard();
    while (index1 < 100 && index2 < 100)
    {
        system("cls");
        ValueBoard();
        printf("Player 1 Enter Any Key to Roll the Dice\n");
        getch();
        p1 = dice();
        if (p1 == 6)
        {
            printf("Rolled Dice is: 6\nSo You get Another chance to Roll the Dice\n");
            printf("Player 1 Enter Any Key to Roll the Dice Again\n");
            getch();
            srand(time(0));
            p1 += dice();
            printf("Rolled Dice: %d\n", p1 - 6);
            sleep(1);
        }
        printf("total Rolled Dice: %d\n", p1);
        if(index1+p1 >100)
        {
            printf("You cannot move :| \n");
        }
        else
        {
            index1 += p1;
        }
        
        printf("PLAYER 1 IS AT %d\n", index1);

        sleep(2);
        system("cls");
        ValueBoard();

        if (check(index1, index2) == 1)
        {
            exit(0);
        }

        printf("Player 2 Enter Any Key to Roll the Dice\n");
        getch();
        p2 = dice();
        if (p2 == 6)
        {
            printf("Rolled Dice is: 6\nSo You get Another chance to Roll the Dice\n");
            printf("Player 2 Enter Any Key to Roll the Dice Again\n");
            getch();
            srand(time(0));
            p2 += dice();
            printf("Rolled Dice: %d\n", p2 - 6);
            sleep(1);
        }

        printf("Total Rolled Dice: %d\n", p2);
        if(index2+p2 >100)
        {
            printf("You cannot move :| \n");
        }
        else
        {
            index2 += p2;
        }
        printf("PLAYER 2 IS AT %d\n", index2);

        sleep(2);
        if (check(index1, index2) == 1)
        {
            exit(0);
        }
        
    }
}
