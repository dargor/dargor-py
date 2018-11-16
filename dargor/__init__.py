#
# Copyright (c) 2018, Gabriel Linder <linder.gabriel@gmail.com>
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

from .logger import logging

import asyncio
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    logging.debug('asyncio: using uvloop')
except ImportError:
    logging.debug('asyncio: using default loop')

import sys
import traceback

from pygments import highlight
from pygments.lexers import Python3TracebackLexer
from pygments.formatters import Terminal256Formatter


def excepthook(exc_type, exc_value, exc_traceback):
    tb = ''.join(traceback.format_exception(exc_type,
                                            exc_value,
                                            exc_traceback))
    lexer = Python3TracebackLexer(stripall=True, tabsize=4)
    formatter = Terminal256Formatter(style='vim', bg='dark')
    logging.error(highlight(tb, lexer, formatter).strip())
    print('\x07', end='', flush=True)


sys.excepthook = excepthook


def asyncio_exception_handler(loop, context):
    try:
        e = context['exception']
        excepthook(type(e), e, e.__traceback__)
    except KeyError:
        logging.error(context)
    loop.default_exception_handler(context)


asyncio.get_event_loop().set_exception_handler(asyncio_exception_handler)


# leave here alone
__version__ = '0.0.11'
