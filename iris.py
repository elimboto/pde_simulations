import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue='species', height=2.5)
textstr = 'Created at www.tssfl.com'
plt.gcf().text(0.36, 0.985, textstr, fontsize=14, color='green')
plt.show()
