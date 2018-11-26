import pygal
import pandas as pd
from .models import Statistiques

class PopLineChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Line(**kwargs)
        self.chart.title = 'Evolution de la population entre 1968 et 2015'

    def get_data(self):
        data = list(Statistiques.objects.values_list("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop").filter(codgeo='39038'))
        return data

    def generate(self):
        # year = ["1968", "1975", "1982", "1990", "1999", "2010", "2015"]
        chart_data = self.get_data()
        
        # Add data to chart
        # self.chart.x_labels = map(str, year)
        self.chart.add("population", [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)