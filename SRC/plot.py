import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class  Plotter:

    """
    Allows the use to visualise the data

    Parameter:
        dataframe (df):
            Dataframe from which information will be use to create the plots.
    
    Methods:
        missing_values_plot:
            Creates a density plot of missing values for all columns of a selected dataframe


    """
    
    def __init__(self, dataframe):
        self.dataframe = dataframe



    def missing_values_plot(self):
        """
        This function:
            Creates a barplot based on the based on the proprotion of missing data per column, which the plot fucntion calculates.
        """
        plt.figure(figsize=(12,8))
        sns.displot(
            data= self.dataframe.isnull().melt(value_name="missing"),
            y="variable",
            hue="missing",
            multiple="fill",
            aspect=1.05
    )