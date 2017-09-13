
class PrintSummary:

    def __init__(self, print_data):
        self.print_data = print_data

    def print(self):
        data = self.print_data

        print(
            """
Обобщение
---------
    Общ брой продажби: {}
    Обща сума продажби: {}
    Средна цена на продажба: {}
    Начало на период на данни: {}
    Край на период на данни: {}
            """.format(data[0], data[1], data[2], data[3], data[4])
        )


class PrintTopFive:

    def __init__(self, print_data, query):
        self.print_data = print_data
        self.query = query

    def print(self):
        QUERIES = {
            'category': 'Сума на продажби по категории',
            'city': 'Сума на продажби по градове',
            'hour': 'Часове с най-голяма сума продажби'
        }
        data = self.print_data
        top_category = sorted(data, key=data.get, reverse=True)[:5]  # Sorting our categories

        # Indentation of colons
        indent = []
        max_length = 0
        for cat in top_category:
            cat = str(cat)
            length = len(cat)
            if length > max_length:
                max_length = length
        for cat in top_category:
            cat = str(cat)
            length = len(cat)
            indent.append(max_length - length)

        # Bar charts with '*'
        chart_bars = []
        max_bar = 30
        max_value = data[top_category[0]]
        for key in top_category:
            value = data[key]
            bar = int(max_bar * (value / max_value))
            chart_bars.append(bar)

        print(
            """
{} (top 5)
{}
    {}{} :{} {} $
    {}{} :{} {} $
    {}{} :{} {} $
    {}{} :{} {} $
    {}{} :{} {} $
            """.format(
                    QUERIES[self.query],
                    len(QUERIES[self.query],) * '-',
                    top_category[0], ' ' * indent[0], '*' * chart_bars[0], data[top_category[0]],
                    top_category[1], ' ' * indent[1], '*' * chart_bars[1], data[top_category[1]],
                    top_category[2], ' ' * indent[2], '*' * chart_bars[2], data[top_category[2]],
                    top_category[3], ' ' * indent[3], '*' * chart_bars[3], data[top_category[3]],
                    top_category[4], ' ' * indent[4], '*' * chart_bars[4], data[top_category[4]]
                )
        )
