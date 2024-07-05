import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns


class  Plotter:

    """
    Allows the use to visualise the data

    Parameter:
        dataframe (df):
            Dataframe from which information will be use to create the plots.
    
    Methods:
        missing_values_plot:
            Creates a density plot of missing values for all columns of a selected dataframe
        hist_plot:
            Creates a histogram from provided data
        plot_qq: Creates a quantile-quantile plot from provided data.

    
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

    def hist_plot(self, dataframe, column, bins_size=10, title ="", xlabel="", ylabel="", kde_option = False):
        """
        This function:
            Creates a histogram from provided data.

        Prameters:
            Dataframe (df):
                Where the desired data is store.
            Column (str):
                Name of the dataframe column to create the histogram from.
            bin_size (str):
                Number of bins the histagram will show.
            title (str):
                Title of the histogram.
            xlabel (str):
                Name of the x-axis.
            ylabel (str):
                Name of the y-axis.
            kde_option (bool):
                cComputes a kernel density estimate to smooth the distribution and show on the plot as a line.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=dataframe, x=column, bins= bins_size, kde=kde_option)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, axis="y") 
        plt.show()

    def plot_qq(self, dataframe, column, scale_option=1):
        """
        This function:
                Creates a quantile-quantile plot from provided data.

        Prameters:
            Dataframe_column (df):
                Dataframe wich contains the data to plot.
            column (df):
                Column of the dataframe use to generate the plot.
            Scale_option (int):
                Scale parameter for distribution.
        """
        qqplot(dataframe[column], scale=scale_option ,line='q')
        pyplot.show()