import numpy as np
import pandas as pd
import math
import argparse
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import style

style.use('dark_background')



# Functions

def create_pdf():

     # Create multi-page PDF files to store plots

    annual_pdf = PdfPages('Annual.pdf')
    c_annual_pdf = PdfPages('Cummulative annual.pdf')
    return annual_pdf, c_annual_pdf



def get_sheet_names(file_name):

    # Extract sheet names of excel file

    xl = pd.ExcelFile(file_name)
    xl_sheets = xl.sheet_names
    return xl_sheets



def load_data(file_name, sheet):

    # Loads data of all sheets and stores into a dataframe

    df = pd.read_excel(io = file_name, sheet_name = sheet, squeeze = True, header = None)
    df = df.T    
    return df



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



def plot_annual(year, annual, sheet, annual_pdf, x_label1, y_label1, line_label1, chart_title1):

    # Plot year (x-axis) & annual (y-axis)

    plt.plot(year,annual,"bo-",linewidth=2, markersize=3, label = line_label1)	    
    plt.xlabel(x_label1)	
    plt.ylabel(y_label1)
    plt.title('{} {}'.format(chart_title1, sheet))
    plt.axis('auto')
    plt.legend(loc="upper right")
    #plt.show()    
    plt.savefig(annual_pdf, format='pdf')
    plt.clf()      

        

def plot_c_annual(c_annual, sheet, c_annual_pdf, x_label2, y_label2, line_label2, chart_title2):

    # Plot cummulative annual (y-axis only in default)

    plt.plot(c_annual,"bo-",linewidth=2, markersize=3, label = line_label2)	
    plt.xlabel(x_label2)	
    plt.ylabel(y_label2)
    plt.title('{} {}'.format(chart_title2, sheet))
    plt.axis('auto')
    plt.legend(loc="upper right")
    #plt.show()    
    plt.savefig(c_annual_pdf, format='pdf')
    plt.clf()



def close_pdf(annual_pdf, c_annual_pdf):

    # Close the files

    annual_pdf.close()
    c_annual_pdf.close()        





def main():

    parser = argparse.ArgumentParser(description='Visualize data')
    parser.add_argument('--file_name', type=str, default = 'data.xlsx',
                    help='Excel file name whose data is to be visualized.')
    parser.add_argument('--x_label1', type=str, default = 'Year',
                    help='x-axis label for 1st line chart')
    parser.add_argument('--y_label1', type=str, default = '',
                    help='y-axis label for 1st line chart')
    parser.add_argument('--x_label2', type=str, default = 'Year',
                    help='x-axis label for 2nd line chart')
    parser.add_argument('--y_label2', type=str, default = '',
                    help='y-axis label for 2nd line chart')
    parser.add_argument('--line_label1', type=str, default = 'Annual',
                    help='Line label for 1st line chart')
    parser.add_argument('--line_label2', type=str, default = 'Cummulative Annual',
                    help='Line label for 2nd line chart')
    parser.add_argument('--chart_title1', type=str, default = 'Station no.',
                    help='Chart title for 1st line chart')
    parser.add_argument('--chart_title2', type=str, default = 'Station no.',
                    help='Chart title for 2nd line chart')
    args = parser.parse_args()


    file_name, x_label1, y_label1, x_label2, y_label2, line_label1, line_label2, chart_title1, chart_title2 = args.file_name, args.x_label1, args.y_label1, args.x_label2, args.y_label2, args.line_label1, args.line_label2, args.chart_title1, args.chart_title2
    print('Visualizing File: {}'.format(file_name))   


    annual_pdf, c_annual_pdf = create_pdf()
    xl_sheets = get_sheet_names(file_name) 


    for sheet in xl_sheets:
        df = load_data(file_name, sheet)
        year, annual, c_annual = sheet_var(df)   
        plot_annual(year, annual, sheet, annual_pdf, x_label1, y_label1, line_label1, chart_title1)        
        plot_c_annual(c_annual, sheet, c_annual_pdf, x_label2, y_label2, line_label2, chart_title2)
        print("\nStatus:  Plotted Sheet No. {}".format(sheet))    # Status output
        

    close_pdf(annual_pdf, c_annual_pdf)



if __name__ == "__main__":
    main()





