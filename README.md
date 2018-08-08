## excel-data-visualization

This python code visualizes line chart of a multi-sheet excel file having format like 'data.xlsx' file


## Requirements:

* [Python 3]


## Dependencies:         
                  
* [pandas]    

* [numpy]      

* [matplotlib]   

* [xlrd]


## Usage:

1. Excel file should be in same directory as the python file.

2. Run the python code.
      * python Excel_plot.py

    Command-line arguements:

      See Excel_plot.py for default arguements

      * '--file_name'   : Excel file name whose data is to be visualized.         
      * '--x_label1'    : x-axis label for 1st line chart
      * '--y_label1'    : y-axis label for 1st line chart
      * '--x_label2'    : x-axis label for 2nd line chart
      * '--y_label2'    : y-axis label for 2nd line chart
      * '--line_label1' : Line label for 1st line chart
      * '--line_label2' : Line label for 2nd line chart
      * '--chart_title1': Chart title for 1st line chart
      * '--chart_title2': Chart title for 2nd line chart

      Example: python Excel_plot.py --file_name 'data.xlsx' --x_label1 'Year in AD' --chart_title1 'Data over Years of Station '



