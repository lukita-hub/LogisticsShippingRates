#Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package wight in kilograms: "))
rate = float(inout("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## DIsplay the result
print(f"Shipping Cost: {shipping_cost} USD")
