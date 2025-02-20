import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col=["date"])

# Clean data
df = df[(df.value < np.percentile(df.value,97.5)) & (df.value > np.percentile(df.value,2.5))]


def draw_line_plot():
   
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df.index, df["value"])

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.figure(figsize=(15,6))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar_grp = df_bar.groupby([df_bar.index.year, df_bar.index.month])["value"].mean().unstack()

    df_bar_grp.columns = pd.to_datetime(df_bar_grp.columns, format='%m').month_name()
    
    
    # Draw bar plot

    fig = plt.figure(figsize=(10, 6))


    ax = df_bar_grp.plot(kind='bar', ax=fig.gca())
    ax.set_title("Average Daily Page Views per Month")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, plot = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x="year", y= "value",data = df_box, ax=plot[0], palette="bright", flierprops=dict(marker='o', markersize=5))
    plot[0].set_title("Year-wise Box Plot (Trend)")
    plot[0].set_xlabel("Year")
    plot[0].set_ylabel("Page Views")


    sns.boxplot(x="month", y= "value",data = df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=plot[1], palette="bright", flierprops=dict(marker='o', markersize=5))
    plot[1].set_title("Month-wise Box Plot (Seasonality)")
    plot[1].set_xlabel("Month")
    plot[1].set_ylabel("Page Views")

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
