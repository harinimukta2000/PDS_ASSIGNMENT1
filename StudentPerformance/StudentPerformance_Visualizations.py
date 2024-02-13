import pandas as pds
import matplotlib.pyplot as mtlib
import seaborn as sb

# Load the dataset
df = pds.read_csv('/content/drive/MyDrive/StudentPerformance/Student_Clean.csv')

# Task 1: Visualization 1 - Heatmap visualization using seaborn
mtlib.figure(figsize=(10, 8))
sb.heatmap(data=df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
mtlib.title('Correlation Heatmap')
mtlib.savefig('/content/drive/MyDrive/StudentPerformance/heatmap.png')
mtlib.show()


# Task 2: Visualization 2- Pie Chart visualization 
avg_scr = df.groupby('gender')['reading score'].mean()
labels = avg_scr.index
sizes = avg_scr.values
mtlib.figure(figsize=(8, 6))
mtlib.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#CD5C5C','#32CD32'])
mtlib.title('Average Reading Scores by Gender')
mtlib.savefig('/content/drive/MyDrive/StudentPerformance/pie_chart.png')
mtlib.show()

# Task 3: Visualization 3 - Barplot of Parental Education Levels
mtlib.figure(figsize=(10, 6))
sb.countplot(data=df, x='parental level of education', hue='test preparation course')
mtlib.title('Barplot of Parental Education Levels by Test Preparation Course')
mtlib.xlabel('Parental Education Level')
mtlib.ylabel('Count')
mtlib.xticks(rotation=45, ha='right')
mtlib.savefig('/content/drive/MyDrive/StudentPerformance/countplot.png')
mtlib.show()

# Task 4: Visualization 4 - Scatter Plot of Writing vs. Reading Scores
mtlib.figure(figsize=(8, 6))
sb.scatterplot(data=df, x='reading score', y='writing score', hue='gender')
mtlib.title('Scatter Plot of Writing vs. Reading Scores')
mtlib.xlabel('Reading Score')
mtlib.ylabel('Writing Score')

mtlib.savefig('/content/drive/MyDrive/StudentPerformance/Scatterplot.png')
mtlib.show()

# Task 5: Visualization 5 - Barplot
mtlib.bar(df["gender"].unique(),df["gender"].value_counts())
mtlib.xlabel("gender")
mtlib.ylabel("count")
mtlib.title("Barplot")
mtlib.savefig('/content/drive/MyDrive/StudentPerformance/Barplot.png')
mtlib.show()
