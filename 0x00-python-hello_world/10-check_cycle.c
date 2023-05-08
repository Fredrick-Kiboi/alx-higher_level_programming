#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @head: pointer to the head of the list
 *
 * Return: 1 if the list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *head)
{
    listint_t *slow_ptr = head;
    listint_t *fast_ptr = head;

    while (fast_ptr && fast_ptr->next)
    {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;

        if (slow_ptr == fast_ptr)
        {
            return (1);
        }
    }

    return (0);
}
