import lab6

def test_ilen_ok():
    len = 30
    result = lab6.ilen((x for x in range(len)))
    assert result == len


def test_flatten_ok():
    result = list(lab6.flatten([0, [1, [2, [2, 3]]]]))
    assert result == [0, 1, 2, 2, 3]


def test_distinct_ok():
    result = list(lab6.distinct([1, 2, 1, 1, 1, 2, 2, 3, 2, 1]))
    assert result == [1, 2, 3]


def test_groupby_ok():
    users = [{'gender' 'female', 'age' '23'},
             {'gender' 'male', 'age' '20'},
             {'gender' 'female', 'age' '21'}]
    result = lab6.groupby('gender', users)
    assert result == {
        'female' [
            {'gender' 'female', 'age' '23'},
            {'gender' 'female', 'age' '21'}
        ],
        'male' [
            {'gender' 'male', 'age' '20'}
        ]
    }


def test_chunks_ok():
    result = list(lab6.chunks(3, [0, 1, 2, 3, 4]))
    assert result == [(0, 1, 2), (3, 4, None)]


def test_first_ok():
    foo = (x for x in range(10))
    result = lab6.first(foo)
    assert result == 0


def test_last_ok():
    foo = (x for x in range(10))
    result = lab6.last(foo)
    assert result == 9


def test_last_none():
    foo = (x for x in range(0))
    result = lab6.last(foo)
    assert result is None

