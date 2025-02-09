import testbook

@testbook.testbook('/path/to/notebook.ipynb', execute=True)
def test_func(tb):
    func = tb.ref("func")

    assert func(2) == 3
