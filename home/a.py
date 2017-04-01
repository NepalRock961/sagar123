def main():
    while True:
        radius = input('Enter radius of circle(meters): ')

        try:
            radius = float(radius)
            area = area_of_circle
            print("\nArea of circle =%.2f sq. meters" % area)

        except ValueError:
            print('Invalid Input. Please enter a numeric value.\n')

        try_again = input('\nTry Again (Y/N)? ')

        # if the user doesnt want to try again exit the loop
        if try_again.upper() != "Y":
            break
            print()
        def area_of_circle(radius):
            PI = 3.1415
            return PI * radius ** 2

    print('Good Bye!')

main()