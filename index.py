import json
import csv
import pandas as pd
import matplotlib.pyplot as plt

class IDataConverter:
    def convert(self, data: dict) -> pd.DataFrame:
        pass

class JsonToDataFrameConverter(IDataConverter):
    def convert(self, data: dict) -> pd.DataFrame:
        # Convertir datos JSON a formato pandas DataFrame
        df = pd.DataFrame.from_dict(data)
        return df

class JsonToCsvConverter(IDataConverter):
    def convert(self, data: dict) -> pd.DataFrame:
        # Convertir datos JSON a formato CSV
        df = pd.DataFrame.from_dict(data)
        df.to_csv('data.csv', index=False)
        return df

class IPlotter:
    def plot(self, data: pd.DataFrame):
        pass

class MatplotlibPlotter(IPlotter):
    def plot(self, data: pd.DataFrame):
        # Graficar datos utilizando la librería matplotlib
        plt.plot(data['date'], data['cases'])
        plt.xlabel('Fecha')
        plt.ylabel('Casos')
        plt.title('Casos de COVID-19')
        plt.show()

class CsvPlotter(IPlotter):
    def plot(self, data: pd.DataFrame):
        # Graficar datos utilizando la librería csv
        with open('data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['date'], row['cases'])

class CovidDataService:
    def __init__(self, data_converter: IDataConverter, plotter: IPlotter):
        self.data_converter = data_converter
        self.plotter = plotter

    def getCountriesData(self) -> dict:
        # Descargar datos de países en formato JSON
        data = {
            'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
            'cases': [10, 15, 20, 30, 40]
        }
        return data

    def getCountriesHistoryData(self) -> dict:
        # Descargar datos de historial de países en formato JSON
        data = {
            'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
            'cases': [5, 10, 15, 25, 35]
        }
        return data

    def plotCountriesData(self):
        data = self.getCountriesData()
        df = self.data_converter.convert(data)
        self.plotter.plot(df)

    def plotCountriesHistoryData(self):
        data = self.getCountriesHistoryData()
        df = self.data_converter.convert(data)
        self.plotter.plot(df)

class Main:
    def main(self):
        data_converterDataFrame = JsonToDataFrameConverter()
        data_converterCsv = JsonToCsvConverter()
        plotter = MatplotlibPlotter()
        csv_plotter = CsvPlotter()
        serviceMatplotlib = CovidDataService(data_converterDataFrame, plotter)
        seviceCsv = CovidDataService(data_converterCsv, csv_plotter)

        # Generar gráfico de datos de países
        seviceCsv.plotCountriesData()
        serviceMatplotlib.plotCountriesData()

        # Generar gráfico de historial de países
        seviceCsv.plotCountriesHistoryData()
        serviceMatplotlib.plotCountriesHistoryData()

if __name__ == '__main__':
    Main().main()