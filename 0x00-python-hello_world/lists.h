#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h> /* for malloc, free */

/* singly linked list node */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* function prototype */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
