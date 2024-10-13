import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
else:
    print('display found')
    print(os.environ.get('DISPLAY',''))


# from utils_ import display

# def main():
#     display([[0, 0, 0], [0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 1, 2], [3, 4, 5]])


# if __name__ == "__main__":
#     main()