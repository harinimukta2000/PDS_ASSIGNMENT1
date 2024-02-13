# Load the cleaned data from a CSV file
cleaned_data = pd.read_csv("/content/drive/MyDrive/Frailty/Frailty_clean_data.csv")

# Extract weight data for two groups based on frailty
fr_h1 = cleaned_data[cleaned_data['Frailty'] == 1]['Height']
fr_h0 = cleaned_data[cleaned_data['Frailty'] == 0]['Height']

# Define the path to the text file
txt_file = '/content/drive/MyDrive/Frailty/FrailtyAnalysis.txt'

# Open the text file for writing results
with open(txt_file, 'w') as result_file:
    # Calculate the t-statistic and p-value for a Student's t-test
    result = stat.ttest_ind(fr_h1, fr_h0)
    t_stat = result.statistic
    p_val = result.pvalue

    # Write the results to the text file
    result_file.write("Student's t test t_statistic: " + str(t_stat) + "\n")
    result_file.write("Student's t test p_value: " + str(p_val) + "\n")

    alpha = 0.05
    if p_val < alpha:
        result_file.write("Based on the statistical analysis, we have strong evidence to conclude that there is a significant difference in grip strength between the two groups.")
    else:
        result_file.write("According to the statistical analysis, we do not have sufficient evidence to assert a significant difference in grip strength between the two groups.")

