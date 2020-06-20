shortcwd
========

This package helps avoid ``MAX_PATH`` issues on Windows by mounting the current directory on a new drive letter.

The ``shortcwd`` module exposes a context manager that calls the ``SUBST`` DOS command.
On non-Windows platforms it does nothing.


Usage
-----

Use pip to install::

    pip install --user shortcwd

Use ``shortcwd.shortcwd()`` as a context manager::

    import os
    import shortcwd

    print(os.getcwd())
    with shortcwd.shortcwd():
        print(os.getcwd())
    print(os.getcwd())

Output::

    C:\Users\Barney\shortcwd
    A:\
    C:\Users\Barney\shortcwd
