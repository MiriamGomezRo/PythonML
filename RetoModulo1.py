# Open file
file_handler = open('/content/sample_data/Employees.csv', 'r')
next(file_handler)

# Counts for Gender
contadorFemale = 0
contadorMale = 0

# Counts for Avegare
totalAge = 0
totalCount = 0

# Process each line in the file
for line in file_handler:
    # Broke with ,   
    line = line.split(',')
    # Process gender counts
    if line[1] == 'F':
        contadorFemale = contadorFemale + 1
    if line[1] == 'M':
        contadorMale = contadorMale + 1  
    # Process Average year
    if len(line[2]) > 0:
              totalAge = totalAge + int(line[2])
              totalCount = totalCount + 1

# Define higher and lower counts  
if contadorFemale < contadorMale :
    print ('Existen más hombres que mujeres en la muestra')
else :   
    print ('Existen más mujeres que hombres en la muestra')

# Show 
print ('La edad promedio de los empleados es de :' , totalAge / totalCount)
