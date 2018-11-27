# import pygal
# import pandas as pd
# from .models import Statistiques

# class LineChart():

#     def __init__(self, **kwargs):
#         self.chart = pygal.Line(**kwargs)
#         self.chart.title = 'Evolution de la population entre 1968 et 2015'

#     def get_data(self):
#         filtre = Statistiques.objects.values_list("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop").filter(codgeo='39230')
#         data = [el for el in filtre[0]]
#         return data

#     def generate(self):
#         # year = ["1968", "1975", "1982", "1990", "1999", "2010", "2015"]
#         chart_data = self.get_data()
        
#         # Add data to chart
#         for el in chart_data:
#             self.chart.add(el)

#         # Return the rendered SVG
#         return self.chart.render(is_unicode=True)