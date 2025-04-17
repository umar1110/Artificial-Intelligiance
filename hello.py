import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

# Dataset
load_times = [110, 140, 170, 190, 205, 215, 225, 235, 245, 255,
              265, 275, 285, 295, 305, 315, 325, 335, 345, 355,
              365, 375, 385, 395, 405, 415, 425, 435, 445, 455,
              465, 475, 485, 495, 505, 515, 525, 535, 545, 555,
              590, 610, 640, 690, 710, 740, 790, 840, 890, 1150]

# Create DataFrame
df = pd.DataFrame({'Load Time (ms)': load_times})

# Save to Excel
excel_file = 'web_page_load_times.xlsx'
df.to_excel(excel_file, index=False, sheet_name='Data')

# Create histogram bins
bins = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
bin_labels = ['100-200', '200-300', '300-400', '400-500', '500-600',
              '600-700', '700-800', '800-900', '900-1000', '1000-1100', '1100+']

# Add histogram data
hist_data = pd.cut(df['Load Time (ms)'], bins=bins, labels=bin_labels[:-1], right=False)
hist_counts = hist_data.value_counts().sort_index()

# Write histogram data to Excel
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
    hist_counts.to_excel(writer, sheet_name='Histogram Data', header=['Frequency'])
    
    # Create chart
    workbook = writer.book
    worksheet = writer.sheets['Histogram Data']
    
    chart = BarChart()
    chart.type = "col"
    chart.title = "Distribution of Web Page Load Times (50 Samples)"
    chart.y_axis.title = "Frequency"
    chart.x_axis.title = "Page Load Time (ms)"
    
    data = Reference(worksheet, min_col=2, min_row=1, max_row=len(hist_counts)+1)
    categories = Reference(worksheet, min_col=1, min_row=2, max_row=len(hist_counts)+1)
    
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)
    
    worksheet.add_chart(chart, "D2")

print(f"Excel file '{excel_file}' created successfully!")