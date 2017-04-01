#program to find the area of circle

def main():
	radius = input('Enter radius of circle(meters): ')

	

	try:
		radius = float(radius)
		area = area_of_circle(radius)
		print("\nArea of circle =%.2f sq. meters" %area)

	except ValueError:
		print('Invalid Inpput.Please enter a numeric value.\n')

def area_of_circle(radius):
	PI = 3.145
	return PI * radius ** 2

main()
