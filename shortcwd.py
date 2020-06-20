import contextlib
import os
import re
import subprocess
import sys


# Main API -------------------------------------------------------------------------------------------------------------

class ShortCWDError(Exception):
    pass


@contextlib.contextmanager
def shortcwd():
    source = os.getcwd()
    if sys.platform.startswith('win') and len(source) > 3:
        target = create(source)
        os.chdir(target)
        yield target
        os.chdir(source)
        delete(target)
    else:
        yield source


# Low-level functions --------------------------------------------------------------------------------------------------

def create(source):
    output = ''
    for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        success, output = subst(drive, source)
        if success:
            return drive + ':\\'
    else:
        raise ShortCWDError('Failed to create mount point: %s' % output)


def delete(drive):
    success, output = subst(drive[0])
    if not success:
        raise ShortCWDError('Failed to unmount drive %r: %s' % (drive, output))


def drives():
    success, output = subst()
    if not success:
        raise ShortCWDError('Failed to enumerate drives: %s' % output)
    for line in output.splitlines():
        match = re.match(r'([A-Z])[\s\\:=>]+(.+)', line)
        if match:
            yield match.groups()


def subst(drive=None, source=None):
    if drive and source:
        cmd = 'subst %s: "%s"' % (drive, source)
    elif drive:
        cmd = 'subst %s: /D' % drive
    else:
        cmd = 'subst'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    return proc.returncode == 0, output
