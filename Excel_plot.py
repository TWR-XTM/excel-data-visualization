import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import style

style.use('dark_background')



# Functions

def plot_annual(year, annual, sheet):

    # Plot year (x-axis) & annual (y-axis)

    plt.plot(year,annual,"bo-",linewidth=2, markersize=3, label = "Annual")	    
    plt.xlabel("Year")	
    #plt.ylabel("optional")
    plt.title('Station No. {}'.format(sheet))
    plt.axis('auto')
    plt.legend(loc="upper right")
    #plt.show()    
    plt.savefig(annual_pdf, format='pdf')
    plt.clf()      
        

def plot_c_annual(c_annual, sheet):

    # Plot cummulative annual (y-axis)

    plt.plot(c_annual,"bo-",linewidth=2, markersize=3, label = "Cumulative Annual")	
    plt.xlabel("Year")	
    #plt.ylabel("optional")
    plt.title('Station No. {}'.format(sheet))
    plt.axis('auto')
    plt.legend(loc="upper right")
    #plt.show()    
    plt.savefig(c_annual_pdf, format='pdf')
    plt.clf()

        
def sheet_var(df):

    # Split data of a sheet into component numpy arrays

    if (isinstance(df[1][0],str) or math.isnan(df[1][0])):  # Check if 1st entry is string to avoid headers
        year = df[1][1:]
        annual = df[2][1:]
        c_annual = df[3][1:]
    else:
        year = df[1][:]
        annual = df[2][:]
        c_annual = df[3][:]

    year = np.array(year)
    annual = np.array(annual)
    c_annual = np.array(c_annual)

    return year, annual, c_annual



# Create multi-page PDF files to store plots

annual_pdf = PdfPages('Annual.pdf')
c_annual_pdf = PdfPages('Cummulative annual.pdf')


# Extract sheet names of excel file

xl = pd.ExcelFile('data.xlsx')
xl_sheets = xl.sheet_names



for sheet in xl_sheets:

    # Loads data per sheet and plots the data

    df = pd.read_excel(io = 'data.xlsx', sheet_name = sheet, squeeze = True, header = None)
    df = df.T    
    year, annual, c_annual = sheet_var(df)   
    plot_annual(year, annual, sheet)        
    plot_c_annual(c_annual, sheet)
    print("\nStatus:  Plotted Sheet No. {}".format(sheet))    # Status output
    
  
# Close the files

annual_pdf.close()
c_annual_pdf.close()




