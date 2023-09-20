"""
Main cli or app entry point
"""
import lib


def descriptive_summary(data_frame, data):
    """
    this function return a descriptive statistics from the dataset
    """
    dict_discript = {
        "minimum": lib.findMin(data),
        "maximum": lib.findMax(data),
        "mean": lib.calcMean(data),
    }
    lib.visulize_figure(data_frame)
    return dict_discript
