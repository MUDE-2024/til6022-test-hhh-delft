import testbook

@testbook.testbook('test.ipynb', execute=True)
def test_func(tb):
    func = tb.ref("foo")

    assert func(2) == 3
