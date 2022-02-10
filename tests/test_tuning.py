#
# Copyright (c) 2022, Gabriel Linder <linder.gabriel@gmail.com>
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

import gc

from dargor.tuning import disable_gc


def test_disable_gc() -> None:
    assert gc.isenabled()
    with disable_gc():
        assert not gc.isenabled()
    assert gc.isenabled()


def test_inception() -> None:
    assert gc.isenabled()
    with disable_gc():
        assert not gc.isenabled()
        with disable_gc():
            assert not gc.isenabled()
        assert not gc.isenabled()
    assert gc.isenabled()
