#name: John Dale Shoemaker
#pitt username: jds140
#email: jdaleshoemaker@gmail.com
#date: 9/30/16
#class: CS0008 F2016
#assignment one
#instructor: max novelli (man8@pitt.edu)
miles_per_kilometer = 0.621371
gallons_per_liter =  0.264172
kilometer_per_mile = 1.60934
liter_per_gallon = 3.78541
unit_preferred = input('Enter your preferred unit:') #This will tell the user to choose a unit of measurement for the calculations
distance_driven = float(input('How far did you drive')) #This will ask the user how far he or she drove
gas_used = float(input('How much gas did you use')) #This will ask the user how much gas he or she used
#USC pathway begin
print ('{:25s} {:^25s} {:25s}'.format('','USC','Metric'))
if unit_preferred == 'Metric': # Distance in kilometers, Volume in liters

    #Distance string
    mile_string = '{:.3f} miles'.format(distance_driven * miles_per_kilometer)
    kilometer_string = '{:.3f} kilometers'.format(distance_driven)
    generic_distance_string = 'Distance {:f}'.format(distance_driven)
    end_distance_string = '{:25s}: {:^25s} {:25s}'.format(generic_distance_string, mile_string, kilometer_string)
    print (end_distance_string)

    #Gas string
    gallon_string = '{:.3f} gallons'.format(gas_used * gallons_per_liter)
    liter_string = '{:.3f} liters'.format(gas_used)
    generic_gas_string = 'Gas {:f}'.format(gas_used)
    end_gas_string = '{:25s}: {:^25s} {:25s}'.format(generic_gas_string, gallon_string, liter_string)
    print(end_gas_string)
    #string_distance = 'Distance '+distance_driven+':'

    #Consumption string
    USC_string = '{:.3f} mpg'.format(distance_driven * miles_per_kilometer / (gas_used * gallons_per_liter))
    Metric_string = '{:.3f} 1/100km'.format((gas_used / distance_driven)*100)
    generic_consumption_string = 'Consumption'
    end_consumption_string = '{:25s}: {:^25s} {:25s}'.format(generic_consumption_string, USC_string, Metric_string)
    print(end_consumption_string)
    print('')
    #Rating string
    USC_rating = (distance_driven * miles_per_kilometer / (gas_used * gallons_per_liter))
    Metric_rating = ((gas_used / distance_driven) * 100)
    if Metric_rating > 20:
        print('Gas Consumption Rating: Extremely Poor')
    elif Metric_rating > 15:
        print('Gas Consumption Rating: Poor')
    elif Metric_rating > 10:
        print('Gas Consumption Rating: Average')
    elif Metric_rating > 8:
        print('Gas Consumption Rating: Good')
    elif Metric_rating >=8:
        print('Gas Consumption Rating: Excellent')

    #Now it's time for the goddamn else statement

elif unit_preferred == 'USC': #the USC statements begin here
    #enter your prefered unit: USC
    #How far did you drive 25 miles
    #How much gas did you use 1 gallon
    #Distance string
    mile_string = '{:.3f} miles'.format(distance_driven)
    kilometer_string = '{:.3f} kilometers'.format(distance_driven * kilometer_per_mile)
    generic_distance_string = 'Distance {:f}'.format(distance_driven)
    end_distance_string = '{:25s}: {:^25s} {:25s}'.format(generic_distance_string, mile_string, kilometer_string)
    print (end_distance_string)

    #Gas string
    gallon_string = '{:.3f} gallons'.format(gas_used)
    liter_string = '{:.3f} liters'.format(gas_used * liter_per_gallon)
    generic_gas_string = 'Gas {:f}'.format(gas_used)
    end_gas_string = '{:25s}: {:^25s} {:25s}'.format(generic_gas_string, gallon_string, liter_string)
    print(end_gas_string)

    #Consumption string
    USC_string = '{:.3f} mpg'.format(distance_driven * kilometer_per_mile / (gas_used * liter_per_gallon))
    Metric_string = '{:.3f} 1/100km'.format((gas_used / gallons_per_liter)/ (distance_driven / miles_per_kilometer) *100)
    generic_consumption_string = 'Consumption'
    end_consumption_string = '{:25s}: {:^25s} {:25s}'.format(generic_consumption_string, USC_string, Metric_string)
    print(end_consumption_string)
    print('')
    # Rating string
    USC_rating = (distance_driven * kilometer_per_mile / (gas_used * liter_per_gallon))
    Metric_rating = ((gas_used / gallons_per_liter)/ (distance_driven / miles_per_kilometer) *100)
    if  USC_rating > 20:
        print('Gas Consumption Rating: Extremely Poor')
    elif  USC_rating > 15:
        print('Gas Consumption Rating: Poor')
    elif  USC_rating > 10:
        print('Gas Consumption Rating: Average')
    elif  USC_rating > 8:
        print('Gas Consumption Rating: Good')
    elif  USC_rating >= 8:
        print('Gas Consumption Rating: Excellent')














