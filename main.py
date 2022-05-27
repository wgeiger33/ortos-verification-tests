import matplotlib.pyplot as plt
import pandas as pd


def formatter(dataframe):
    dataframe = dataframe.drop(axis=0, index=0)
    dataframe.reset_index()


def plotter(dataframe, graphtitle):
    plt.plot(dataframe['Extension'], dataframe['Load'])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Extension')
    plt.ylabel('Load')
    plt.title(graphtitle)
    plt.show()


for x in range(1, 4):
    file_path = "C:/Users/wgeig/Downloads/Nylon no stiffy.is_flex_RawData-selected/Specimen_RawData_"
    add_on_string = str(x) + ".csv"
    full_file_path = file_path + add_on_string
    instron_nylon_no_stiffy = pd.read_table(full_file_path, sep=',', header=5)

    formatter(instron_nylon_no_stiffy)
    graph_name = 'instron_nylon_no_stiffy_' + str(x)
    plotter(instron_nylon_no_stiffy, graph_name)

for x in range(1, 5):
    file_path = "C:/Users/wgeig/Downloads/Nylon 1kn.is_flex_RawData-selected/Specimen_RawData_"
    add_on_string = str(x) + ".csv"
    full_file_path = file_path + add_on_string
    instron_nylon_with_stiffy = pd.read_table(full_file_path, sep=',', header=5)

    formatter(instron_nylon_with_stiffy)
    graph_name = 'instron_nylon_with_stiffy_' + str(x)
    plotter(instron_nylon_with_stiffy, graph_name)
