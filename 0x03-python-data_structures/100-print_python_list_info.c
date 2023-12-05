#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print list info
 *
 * @p: python list
 *
 * Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int allocate, i, size;
	PyObject *obj;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;
	printtf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
