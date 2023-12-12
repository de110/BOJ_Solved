#include <iostream>
#include <cstring>

using namespace std;

typedef struct stack
{
    int point;
    int value[10000]{0};
} stack;

void push(stack *A, int data)
{
    A->point++;
    A->value[A->point] = data;
}

int pop(stack *A)
{
    if (A->point == -1)
    {
        printf("%d\n", A->point);
        return A->point;
    }
    else
    {
        int tmp = A->value[A->point];
        A->value[A->point--] = 0;
        printf("%d\n", tmp);
        return tmp;
    }
}

int size(stack *A)
{
    if (A->point == -1)
    {
        printf("0\n");
        return 0;
    }
    else
    {
        printf("%d\n", A->point + 1);
        return A->point + 1;
    }
}

int empty(stack *A)
{
    if (A->point == -1)
    {
        printf("1\n");
        return 1;
    }
    else
    {
        printf("0\n");
        return 0;
    }
}

int top(stack *A)
{
    printf("%d\n", A->value[A->point]);
    return A->point;
}

int main()
{
    int N, tmp;
    scanf("%d", &N);
    stack A;
    A.point = -1;

    char s[6];

    while (N--)
    {
        scanf("%s", s);
        if (strcmp(s, "push") == 0)
        {
            scanf("%d", &tmp);
            push(&A, tmp);
        }
        else if (strcmp(s, "pop") == 0)
            pop(&A);
        else if (strcmp(s, "size") == 0)
            size(&A);
        else if (strcmp(s, "empty") == 0)
            empty(&A);
        else if (strcmp(s, "top") == 0)
            top(&A);
    }
}