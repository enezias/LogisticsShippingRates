# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

## Weekly rate calculation
shipments_per_week = int(input("Enter the number of shipments per week: "))
weekly_cost = shipping_cost * shipments_per_week

## Display the weekly result
print(f"Weekly Shipping Cost ({shipments_per_week} shipments): {weekly_cost} USD")
