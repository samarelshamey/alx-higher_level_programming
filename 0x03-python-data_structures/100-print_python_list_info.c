#include <stdio.h>
#include <python.h>
#include <stdlib.h>
/**
 * print_python_list_info - printing python info
 *
 * @p: python list
 * Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int element;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elemet = 0; element <  Py_SIZE(p); element++)
		printf("Element %d: %s\n", element, Py_TYPE(PyList_GetItem(p, element))->tp_name);
}
