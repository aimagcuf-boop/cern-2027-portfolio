
# Scientific Data Analysis Tool
# Project 01 - CERN 2027 Portfolio

# Sample temperature readings in Celsius
temperatures = [28, 30, 27, 32, 29]

# Calculate average temperature
average = sum(temperatures) / len(temperatures)

# Display results
print("SCIENTIFIC DATA ANALYSIS")
print("------------------------")

print("Temperature readings:", temperatures)

print("Average temperature:", round(average, 2), "°C")

print("Highest temperature:", max(temperatures), "°C")

print("Lowest temperature:", min(temperatures), "°C")
