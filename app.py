
print('Welcome to the English-Metric Converter')
ynKelvin = input('For Temperature Conversions, would you like to also see Kelvin (K) in the results? [Y/N]: ')
ctype = -1
while (ctype != '0'):

    ctype = input('\n[1 = Mi to Km, 2 = Oz to Gr, 3 = F to C, 4 = C to F, 5 = M to Ft, 6 = Li to Gal, 0 = Exit Program]\nPlease Select a Type of Conversion: ')

    # Mile to Kilometer
    if ctype == "1":

        Mile = input('Please enter your Mile(s): ')
        try:
            if (float(Mile) >= 0):
                MitoKm = (float(Mile) * 1.60934)
                Kilometer = round(MitoKm, 3)
                print('Distance of ' + str(Mile) + ' Mile(s)' + ' = ' + str(Kilometer) + ' Kilometer(s)')
            else:
                print('Data Error: Mile(s) must be positive')
        except:
            print('General Error: Mile(s) must be numeric')

    # Ounce to Gram
    elif ctype == "2":
        Ounce = input('Please enter your Ounces: ')
        try:
            if (float(Ounce) >= 0):
                OztoGr = (float(Ounce) * 28.3495)
                Gram = round(OztoGr, 3)
                print('Weight of ' + str(Ounce) + ' Ounce(s)' + ' = ' + str(Gram) + ' Grams')
            else:
                print('Data Error: Ounce(s) must be positive')
        except:
            print('General Error: Ounce(s) must be numeric')

    # Fahrenheit to Celsius
    elif ctype == "3":
        if (ynKelvin == 'Y'):
            Fahrenheit = input('Please enter your Fahrenheit: ')
            try:
                if (float(Fahrenheit) >= 0):
                    FtoC = ((5/9) * (float(Fahrenheit) - 32))
                    CtoK = (FtoC + 273.15)
                    Celsius = round(FtoC, 3)
                    Kelvin = round(CtoK, 3)
                    print('Temperature of ' + str(Fahrenheit) + ' Fahrenheit' + ' = ' + str(Celsius) + ' Celsius')
                    print('Temperature of ' + str(Fahrenheit) + ' Fahrenheit' + ' = ' + str(Kelvin) + ' Kelvin')
            except:
                print('General Error: Fahrenheit must be numeric')
        elif (ynKelvin == 'N'):
            Fahrenheit = input('Please enter your Fahrenheit: ')
            try:
                if (float(Fahrenheit) >= 0):
                    FtoC = ((5/9) * (float(Fahrenheit) - 32))
                    Celsius = round(FtoC, 3)
                    print('Temperature of ' + str(Fahrenheit) + ' Fahrenheit' + ' = ' + str(Celsius) + ' Celsius')
            except:
                print('General Error: Fahrenheit must be numeric')

    # Celsius to Fahrenheit
    elif ctype == "4":
        if (ynKelvin == 'Y'):
            Celsius = input('Please enter your Celsius: ')
            try:
                if (float(Celsius) >= 0):
                    CtoF = ((5/9) * (float(Celsius) + 32))
                    FtoK = (CtoF + 273.15)
                    Fahrenheit = round(CtoF, 3)
                    Kelvin = round(FtoK, 3)
                    print('Temperature of ' + str(Celsius) + ' Celsius' + ' = ' + str(Fahrenheit) + ' Fahrenheit')
                    print('Temperature of ' + str(Celsius) + ' Celsius' + ' = ' + str(Kelvin) + ' Kelvin')
            except:
                print('General Error: Celsius must be numeric')
        elif (ynKelvin == 'N'):
            Fahrenheit = input('Please enter your Celsius: ')
            try:
                if (float(Celsius) >= 0):
                    CtoF = ((5/9) * (float(Celsius) - 32))
                    Celsius = round(CtoF, 3)
                    print('Temperature of ' + str(Celsius) + ' Celsius' + ' = ' + str(Fahrenheit) + ' Fahrenheit')
            except:
                print('General Error: Celsius must be numeric')

    # Meter to Feet
    elif ctype == "5":
        Meter = input("Please enter your Meter(s): ")
        try:
            if (float(Meter >= 0)):
                MtoF = (float(Meter) * 3.2808)
                Feet = round(MtoF, 3)
                print('Distance of ' + str(Meter) + ' Meter(s) ' + ' = ' + str(Feet) + ' Feet')
            else:
                print('Data Error: Meter(s) must be positive')
        except:
            print('General Error: Meter(s) must be numeric')

    # Liter to Gallon
    elif ctype == "6":
        Liter = input('Please enter your Liter(s): ')
        try:
            if (float(Liter >= 0)):
                LtoG = (float(Liter) * 0.26417)
                Gallon = round(LtoG, 3)
                print('Volume of ' + str(Liter) + ' Liter(s) ' + ' = ' + str(Gallon) + ' Gallon(s)')
            else:
                print('Data Error: Liter(s) must be positive')
        except:
            print('General Error: Liter(s) must be numeric')

    elif ctype == "0":
        print('Thank you for using my Converter :)')
        break

