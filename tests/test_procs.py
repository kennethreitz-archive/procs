from procs import Process


def test_single_proc():
    ls = Process('ls')
    ls.run()
    assert ls.returncode == 0
    assert ls.stdout == 'file1 file2 file3'

