class Analysis:
    def __init__(self, data):
        self.data = data

    def st_dev(self, col: str) -> float:
        """Стандартное отклонение"""
        return round(self.data[col].std(), 2)

    def mean(self, col: str) -> float:
        """Среднее значение"""
        return round(self.data[col].mean(), 2)

    def percent(self, *args: str) -> float:
        """Сколько первый столбец занимает % от суммы всех"""
        return self.data[args[0]] / sum([*[self.data[arg] for arg in args]]) * 100

    def correlation(self, y: str, *args: str) -> str:
        """Вычисление квадрата корреляции (доли вариации т.н. степень зависимости переменных друг от друга)
        между y и множеством x-ов. Берется наибольшая доля вариации среди передаваемых аргументов.
        """
        res = []
        for arg in args:
            res.append(self.data[arg].corr(self.data[y]) ** 2)

        return f'Наибольшая доля вариации обнаружена между "{y}" и "{args[res.index(max(res))]}": {round(max(res), 2)}'
