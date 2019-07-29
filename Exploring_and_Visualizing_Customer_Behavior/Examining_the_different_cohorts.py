# Plot the average first week purchases for each country by registration date
country_pivot.plot(x='reg_date', y=['USA', 'CAN', 'FRA', 'BRA', 'TUR', 'DEU'])
plt.show()

device_pivot.plot(x='reg_date', y=['and', 'iOS'])
plt.show()
