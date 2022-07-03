fahrenheit = int(input("Please enter fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9

("Formating...")

formattedcelsius = res = "{:.1f}".format(celsius)

print(f"{fahrenheit} fahrenheit is {formattedcelsius} celsius.")