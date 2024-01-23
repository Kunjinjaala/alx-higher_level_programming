#include "Python.h"
/*
 * File: 103-python.c
 */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
        Py_ssize_t size, alloc, count;
        const char *type;
        PyListObject *list = (PyListObject *)p;
        PyVarObject *var = (PyVarObject *)p;

        size = var->ob_size;
        alloc = list->allocated;

        fflush(stdout);

        printf("[*] Python list info\n");
        if (strcmp(p->ob_type->tp_name, "list") != 0)
        {
                printf("  [ERROR] Invalid List Object\n");
                return;
        }

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", alloc);

        for (count = 0; count < size; count++)
        {
                type = list->ob_item[i]->ob_type->tp_name;
                printf("Element %ld: %s\n", count, type);
                if (strcmp(type, "bytes") == 0)
                        print_python_bytes(list->ob_item[count]);
                else if (strcmp(type, "float") == 0)
                        print_python_float(list->ob_item[count]);
        }
}
