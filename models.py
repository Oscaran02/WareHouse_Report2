from datetime import datetime
import matplotlib.pyplot as plt
import pandas


class report:
    def __init__(self, start_date, end_date, country):
        self.df = None

        # Dates are set as date format if they have something different from 0
        if str(start_date) == "0" or str(end_date) == "0":
            self.start_date = str(start_date)
            self.end_date = str(end_date)
        else:
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
            self.end_date = datetime.strptime(end_date, "%d/%m/%Y")

        self.country = country

    # Method to get the data from Excel file and return a dataframe
    def get_data_from_excel(self):
        # TODO make a better filter, get all data here
        self.df = pandas.read_excel("uploads/data.xlsx",
                                    header=0,
                                    usecols="B,AI:AK,AM,AO,AP",
                                    parse_dates=['Fecha ingreso'],
                                    decimal=",",
                                    engine="openpyxl"
                                    )

    # Method to graph the data in local python
    def graphing_statistics(self):
        # Graphing statistics
        fig, ax = plt.subplots(figsize=(15, 8))
        plt.barh(["Foto", "Registro Datos", "Bodega", "Transito"], self.df[0:4])
        ax.set_ylabel('Categoria')
        ax.set_xlabel('Tiempo (minutos)')
        ax.set_title("Tiempo promedio en bodega\n")
        ax.grid(axis='x', color='gray', linestyle='dashed')
        plt.show()
        # TODO grafica de tiempo en bodega

    # Groups the data grouped by country
    def group_by_country(self):
        self.df = self.df[self.df["País"] == self.country]

    # returns dataframe with the data grouped by dates given in the parameter
    def group_by_dates(self):
        # If one of the dates is 0, it means that the user didn't select a date, so we will use the entire dataframe
        if self.start_date == "0" or self.end_date == "0":
            pass
        else:
            self.df = self.df[self.start_date <= self.df["Fecha ingreso"]]
            self.df = self.df[self.end_date >= self.df["Fecha ingreso"]]

    # Filters the dataframe
    def filter_data(self):
        self.group_by_country()
        self.group_by_dates()

    # Returns the average times in the warehouse a
    def average_per_column(self):
        # TODO only average the data in the warehouse, not all the data
        return self.df.mean(axis=0, skipna=True, numeric_only=True)

    def set_data(self):
        self.get_data_from_excel()
        self.filter_data()
        #ESTOY EN LA NEW BRANCH