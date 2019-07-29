# http://strftime.org/ 
#for dates

# Provide the correct format for the date
#Saturday January 27, 2017
date_data_one = pd.to_datetime(date_data_one, format='%A %B %d, %Y')
print(date_data_one)

#2017-08-01
# Provide the correct format for the date
date_data_two = pd.to_datetime(date_data_two, format='%Y-%m-%d')
print(date_data_two)

#08/17/1978
# Provide the correct format for the date
date_data_three = pd.to_datetime(date_data_three, format='%m/%d/%Y')
print(date_data_three)

#2016 March 01 01:56
# Provide the correct format for the date
date_data_four = pd.to_datetime(date_data_four, format='%Y %B %d %H:%M')
print(date_data_four)
