#! /usr/bin/env python3
#
# Copyright (c) 2021, Gabriel Linder <linder.gabriel@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
#

import atexit
import logging
import os
import subprocess
from time import sleep


def _write_autogroup(n):
    while True:
        try:
            with open('/proc/self/autogroup', 'w') as f:
                f.write(str(n))
            break
        except FileNotFoundError:
            # no autogroup support in kernel
            break
        except BlockingIOError:
            # race condition at exit
            sleep(.1)


atexit.register(_write_autogroup, 0)


def _run(cmd):
    try:
        r = subprocess.run(cmd.split(' '))
        r.check_returncode()
    except Exception:
        logging.warning(f'Error while running: {cmd}', exc_info=True)


def ionice():
    _run(f'ionice -c 3 -p {os.getpid()}')


def sched_idle():
    _run(f'chrt -i -p 0 {os.getpid()}')


def nice():
    os.nice(19)
    _write_autogroup(19)


def install():
    ionice()
    sched_idle()
    nice()


if __name__ == '__main__':
    install()
    _run('sched-idle -d')
