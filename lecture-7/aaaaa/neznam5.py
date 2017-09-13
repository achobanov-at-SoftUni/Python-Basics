data = [6, 28, 354, 89, 12]


def get_chart(data_values):
    """
    Return a list of chart strings for each data point in data_values
    :param data_values:
    :type data_values:
    :return:
    :rtype:
    """
    max_value = max(data_values)
    max_chart_width = 40
    value_per_star = max_value / max_chart_width

    return ['*' * int(value / value_per_star) for value in data_values]