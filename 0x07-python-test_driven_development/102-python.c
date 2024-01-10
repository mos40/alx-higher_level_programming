#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Invalid string object\n");
        return;
    }

    // Ensure the Python GIL is held
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    // Convert the Python object to a C string
    const char *c_str = PyUnicode_AsUTF8(p);

    if (c_str == NULL) {
        fprintf(stderr, "Error converting Unicode to UTF-8\n");
        PyGILState_Release(gstate);
        return;
    }

    // Print the C string
    printf("String: %s\n", c_str);

    // Release the Python GIL
    PyGILState_Release(gstate);
}
