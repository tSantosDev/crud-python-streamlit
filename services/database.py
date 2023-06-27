import pyodbc;

server = 'DESKTOP-NE3D3OR\SQLEXPRESS' 
database = 'posto'
cnxn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()
 