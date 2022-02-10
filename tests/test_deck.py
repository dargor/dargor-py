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

import random as rn
from typing import MutableSequence, TypeVar

from dargor.deck import deck

T = TypeVar('T')


def sample(population: MutableSequence[T]) -> MutableSequence[T]:
    rn.seed(42)
    return rn.sample(population, 13)


def test_deck() -> None:

    l = list(range(30))
    h = deck(list(range(30)))

    assert l[10] == h[10]
    assert l[-10] == h[-10]

    assert l[10:] == h[10:]
    assert l[-10:] == h[-10:]

    assert l[:10] == h[:10]
    assert l[:-10] == h[:-10]

    assert l[1:10] == h[1:10]
    assert l[-1:10] == h[-1:10]
    assert l[1:-10] == h[1:-10]

    assert l[100:] == h[100:]
    assert l[-100:] == h[-100:]

    assert l[:100] == h[:100]
    assert l[:-100] == h[:-100]

    assert sample(l) == sample(h)
