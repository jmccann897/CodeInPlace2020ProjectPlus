import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
import re
from textwrap import wrap

filename = 'C:\\Users\\joshm\\Documents\\MyPythonScripts\\Espacenet Search\\first_edit.csv'
df = pd.read_csv(filename, sep=',' , header=[0])
#print(df)
#df.info()

#converting date column to datetime
df['Publication date'] = pd.to_datetime(df['Publication date'])
#print(df['Publication date'].head())

# plot 1 = patents per year

df2 = df['Publication date'].dt.year
plot1_data = df2.value_counts().sort_index()
plot1_data.plot(kind='line')
plt.title('Patents Published per Year')
plt.xlabel('Year')
plt.ylabel('Number of Patents Published')
plt.show()
#plt.savefig('c:\\users\\joshm\\documents\\mypythonscripts\\espacenet search\\Patents_per_year.png')
#plt.close()

"""
# plot 2 = patents by applicants(companies)
# Need some data prep before plot, like only plot top 20%

df3 = df['Applicants']
# Try to remove country codes to match duplicate entries,
# Use regex to compile match for [CC] and use method within series to replace regex with nothing
regex_cc = re.compile(r' \[\w{2}\]')


plot2_data = df3.str.replace(regex_cc, '').value_counts().sort_values()
plot2_data.nlargest(10).plot(kind='barh').invert_yaxis()
plt.title('Applicants by Patents Published')
plt.xlabel('Number of Patents Published')
plt.ylabel('Applicant')
plt.savefig('c:\\users\\joshm\\documents\\mypythonscripts\\espacenet search\\Patents_by_applicants.png', bbox_inches = 'tight')
plt.close()

# plot 3 = patents by inventors
# Need some data prep before plot, like only plot top 20%

df4 = df['Inventors']
plt.rcParams.update({'font.size': 5}) # change font size so names can be read on png file
plot3_data = df4.str.replace(regex_cc, '').value_counts().sort_values() 
plot3_data.nlargest(10).plot(kind='barh').invert_yaxis()
plt.title('Inventors by Patents Published')
plt.xlabel('Number of Patents Published')
plt.ylabel('Inventor')
plt.savefig('c:\\users\\joshm\\documents\\mypythonscripts\\espacenet search\\Patents_by_inventors.jpeg',orientation='landscape', dpi=300, bbox_inches='tight')
plt.close()
"""




"""
Heat Map/ Bubble chart for CPC/IPC codes / keywords in titles/abstract

"""

# Ideas for other plots
# CPC/IPC codes?
# Keyword of titles
 
