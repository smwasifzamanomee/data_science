import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Set interactive backend to pop up the window
matplotlib.use('TkAgg')

# Load the data
df = pd.read_csv(
    'https://raw.githubusercontent.com/pandas-dev/'
    'pandas/main/pandas/tests/io/data/csv/iris.csv'
)

# Generate Andrews curves plot
pd.plotting.andrews_curves(df, 'Name')

# Show the plot in a new window
plt.show()

np.random.seed(5)
x = np.cumsum(np.random.normal(loc=1, scale=5, size=50))
s = pd.Series(x)

s.plot()

plt.show()


a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([1, 2, 3, 4, 5, 6])


plt.plot(a, b)


plt.show()


# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#     }
# )

# df.to_excel("out.xlsx")

# result = pd.read_excel('out.xlsx')


# print(result)
# print(df["Sex"].describe())

# df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
# df.to_excel('myfile.xlsx')  
# file = pd.ExcelFile('out.xlsx')  
# # ----------------
# print(file)
# # -----------
# print(file.parse())
