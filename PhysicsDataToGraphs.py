import plotly.express as px

with open("./Output/PhysicsData.txt", "r") as f:
    Data = f.read().replace("h above earth: ", "").replace("w: ", "").replace("mass ratio: ", "").\
        replace("Best dV2 delta: ", "").replace("Best dV1 percentage: ", "").replace("Max height: ", "").split("\n")

h = []
w_m = []
dv2delta = []
dv1percent = []
max_heights = []

num = 0
for i in range(len(Data)):
    print("Line: " + str(i))
    if num == 0 and i != len(Data) - 1:
        print("Is 1.")
        tmp = Data[i].split(" ")
        h.append(float(tmp[0]))
        w_m.append(tmp[1] + " m/s " + tmp[2] + " m0/me")
    elif num == 1:
        print("Is 2.")
        dv2delta.append(float(Data[i]))
    elif num == 2:
        print("Is 3.")
        dv1percent.append(float(Data[i]))
    elif num == 3:
        print("Is 4.")
        max_heights.append(float(Data[i]))

    if num >= 3:
        num = 0
    else:
        num += 1


fig = px.scatter(x=h, y=dv1percent, color=w_m, size=h)
fig.write_html("./Output/DataGraphs.html")
