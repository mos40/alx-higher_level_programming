#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Definition of a singly linked list node
 * @n: Integer value stored in the node
 * @next: Pointer to the next node in the list
 *
 * Description: This structure defines a node in a singly linked list
 * for a Holberton project.
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* Function prototypes */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
