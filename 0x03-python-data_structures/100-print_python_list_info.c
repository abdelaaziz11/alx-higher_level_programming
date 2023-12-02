#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - shows some info about Python lists
 * @p: object
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int size, alloc, i;

	i = 0;
	PyObject *obj;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	while (i < size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
