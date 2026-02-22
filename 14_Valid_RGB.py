def is_valid_rgb(color):
    if len(color) != 3:
        return False
    
    for value in color:
        if not isinstance(value, int):
            return False
        if value < 0 or value > 255:
            return False
    
    return True

def main():
    try:
        r, g, b = map(int, input("Enter RGB values: ").split())
        color = (r, g, b)

        if is_valid_rgb(color):
            print("Valid RGB color: ", color)
        else: 
            print("Invalid RGB color.")
    
    except ValueError:
        print("Please enter valid integers")

if __name__ == "__main__":
    main()