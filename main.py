import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
performance = df["reading score"].tolist()

mean = statistics.mean(performance)
print("Mean is:", mean)

median = statistics.median(performance)
print("Median is:", median)

mode = statistics.mode(performance)
print("Mode is:", mode)

sd = statistics.stdev(performance)
print("Std Dev is:", sd)

first_sd_start, first_sd_end = mean-sd, mean+sd
second_sd_start, second_sd_end = mean-(2*sd), mean+(2*sd)
third_sd_start, third_sd_end = mean-(3*sd), mean+(3*sd)

list_1_sd = [result for result in performance if result > first_sd_start and result < first_sd_end]
first_sd_percent = len(list_1_sd)*100/len(performance)
print("{}% data lies in 1st sd".format(first_sd_percent))

list_2_sd = [result for result in performance if result > second_sd_start and result < second_sd_end]
second_sd_percent = len(list_2_sd)*100/len(performance)
print("{}% data lies in 2nd sd".format(second_sd_percent))

list_3_sd = [result for result in performance if result > third_sd_start and result < third_sd_end]
third_sd_percent = len(list_3_sd)*100/len(performance)
print("{}% data lies in 3rd sd".format(third_sd_percent))

fig = ff.create_distplot([performance], ["Reading Score"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.05], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start, first_sd_start], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_sd_end, first_sd_end], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x=[second_sd_start, second_sd_start], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_sd_end, second_sd_end], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 2"))

fig.add_trace(go.Scatter(x=[third_sd_start, third_sd_start], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_sd_end, third_sd_end], y=[0, 0.05], mode="lines", name="STANDARD DEVIATION 3"))

fig.show()