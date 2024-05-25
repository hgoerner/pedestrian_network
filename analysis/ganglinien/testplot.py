import matplotlib
matplotlib.use('Qt5Agg')  # Set backend to Qt5Agg
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()  # This will create an interactive window if run in a Python script