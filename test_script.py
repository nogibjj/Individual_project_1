"""
Test goes here

"""
import lib
import descriptive_script as dscr


def testScript():
    file = (
        "https://gist.githubusercontent.com/"
        "seankross/a412dfbd88b3db70b74b/raw/"
        "5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    data_frame = lib.read_file(file)
    print(data_frame.describe())
    data = data_frame["mpg"]
    summar = dscr.descriptive_summary(data_frame, data)
    # print("this is summary", summar)

    # assert min
    assert summar["minimum"] == data_frame.describe()["mpg"]["min"]
    # assert max
    assert summar["maximum"] == data_frame.describe()["mpg"]["max"]

    # assert mean
    assert summar["mean"] == round(data_frame.describe()["mpg"]["mean"], 3)


if __name__ == "__main__":
    testScript()
