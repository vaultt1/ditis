# 5. Write a program that prompts the user to input number of calls and calculate the monthly telephonebills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

calls = int(input("Enter the number of calls: "))

bill = 200

if calls > 100 and calls <= 150:
    bill += (calls - 100) * 0.60
elif calls > 150 and calls <= 200:
    bill += (50 * 0.60) + (calls - 150) * 0.50
elif calls > 200:
    bill += (50 * 0.60) + (50 * 0.50) + (calls - 200) * 0.40

# Display the calculated bill
print(f"The total bill for {calls} calls is Rs. {bill:.2f}")
