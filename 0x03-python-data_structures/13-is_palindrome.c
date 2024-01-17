#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
*is_palindrome -  checks if a singly linked list is a palindrome
*
*@head: head of list
*
*Return: 1 if it is a palindrome or 0 if it is not
*/

int is_palindrome(listint_t **head)
{
	listint_t *next;
	listint_t *prev;
	listint_t *slow;
	listint_t *fast;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	prev = NULL;
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
