# this is a test code for lib.py
# test every functions in lib.py
import lib


# is file being read
def test_read_file():
    file = (
        "https://gist.githubusercontent.com/"
        "seankross/a412dfbd88b3db70b74b/raw/"
        "5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    data_frame = lib.read_file(file)
    assert data_frame != []


def test_findMin():
    file = (
        "https://gist.githubusercontent.com/"
        "seankross/a412dfbd88b3db70b74b/raw/"
        "5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    data_frame = lib.read_file(file)
    assert data_frame.describe()["mpg"]["min"] == lib.findMin(data_frame["mpg"])


def test_findMax():
    file = (
        "https://gist.githubusercontent.com/"
        "seankross/a412dfbd88b3db70b74b/raw/"
        "5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    data_frame = lib.read_file(file)
    assert data_frame.describe()["mpg"]["max"] == lib.findMax(data_frame["mpg"])


def test_calcMean():
    file = (
        "https://gist.githubusercontent.com/"
        "seankross/a412dfbd88b3db70b74b/raw/"
        "5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    data_frame = lib.read_file(file)
    assert round(data_frame.describe()["mpg"]["mean"], 3) == lib.calcMean(
        data_frame["mpg"]
    )


def test_visulize_figure():
    pass


if __name__ == "__main":
    # test_read_file()
    test_findMin()
    test_findMax()
    test_calcMean()
    test_visulize_figure()
