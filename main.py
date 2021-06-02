import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print("Population mean : ", mean)
print("Standard Deviation : ", std_dev)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    
mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_means(30)
    mean_list.append(set_of_means)



sampling_mean = statistics.mean(mean_list)
sampling_std_deviation = statistics.stdev(mean_list)

std_1_dev_start, std_1_dev_end = sampling_mean-sampling_std_deviation, mean+sampling_std_deviation
std_2_dev_start, std_2_dev_end = sampling_mean-(2*sampling_std_deviation), mean+(2*sampling_std_deviation)
std_3_dev_start, std_3_dev_end = sampling_mean-(3*sampling_std_deviation), mean+(3*sampling_std_deviation)

print("std 1: ", std_1_dev_start,", ", std_1_dev_end)
print("std 1: ", std_2_dev_start,", ", std_2_dev_end)
print("std 1: ", std_3_dev_start,", ", std_3_dev_end)

fig = ff.create_distplot([mean_list], ["READING TIME"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0, 1], mode="lines", name="Sampling Mean"))

fig.add_trace(go.Scatter(x=[std_1_dev_start, std_1_dev_start], y=[0, 1], mode="lines", name="1 std_dev start"))
fig.add_trace(go.Scatter(x=[std_1_dev_end, std_1_dev_end], y=[0, 1], mode="lines", name="1 std_dev end"))

fig.add_trace(go.Scatter(x=[std_2_dev_start, std_2_dev_start], y=[0, 1], mode="lines", name="2 std_dev start"))
fig.add_trace(go.Scatter(x=[std_2_dev_end, std_2_dev_end], y=[0, 1], mode="lines", name="2 std_dev end"))

fig.add_trace(go.Scatter(x=[std_3_dev_start, std_3_dev_start], y=[0, 1], mode="lines", name="3 std_dev start"))
fig.add_trace(go.Scatter(x=[std_3_dev_end, std_3_dev_end], y=[0, 1], mode="lines", name="3 std_dev end"))

fig.show()

z_score = (sampling_mean - mean)/sampling_std_deviation
print(f"Z Score : {z_score}")