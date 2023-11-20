import itertools
import more_itertools



def eager_group(it, key=None):
    return map(lambda x: (x[0], tuple(x[1])), itertools.groupby(iterable=it, key=key))


def mylog(msg):
    #print(f'LOG {msg}')
    pass


def generic_join(i1, i2, join_type='outer', key=None):
    nothing = None

    assert join_type in ('left', 'right', 'inner', 'outer')

    if key is None:
        key = lambda x: x

    grouped1 = itertools.groupby(i1, key=key)
    grouped2 = more_itertools.peekable(eager_group(i2, key=key))

    for key1, items1 in grouped1:
        mylog(f'advancing left to {key1}')
        key2, items2 = grouped2.peek((nothing, nothing))
        mylog(f'peeking right {key2} {items2}')
        while key2 is not nothing and key2 <= key1:
            mylog(f'while body {key1} {key2}')

            if key2 == key1:
                mylog(f'key1 {key1} == key2 {key2}')
                mylog('cross')

                for pair in itertools.product(items1, items2):
                    mylog(f'yield {pair}')
                    yield pair
                mylog('endcross')

            elif key2 < key1:
                mylog(f'key2 {key2} < key1 {key1}')
                if join_type in ('right', 'outer'):
                    for value in items2:
                        yield nothing, value

            next(grouped2, (nothing, nothing))
            mylog(f'advancing 2')
            key2, items2 = grouped2.peek((nothing, nothing))
            mylog(f'peeking {key2} {items2}')

        mylog(f'out of while {key1} {key2}')
        if key2 is nothing or key2 > key1:
            if join_type in ('left', 'outer'):
                for value in items1:
                    yield value, nothing


    for key2, items2 in grouped2:
        for value in items2:
            if join_type in ('right', 'outer'):
                yield nothing, value


