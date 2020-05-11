if __name__ == '__main__':
    with open('text.rtf', 'r') as f:
        upper_case = 0
        total = 0
        line = f.readline()
        while line:
            for char in line:
                total += 1
                if char.isupper():
                    print(char)
                    upper_case += 1
            line = f.readline()
        print(f'number of upper case in the text is: {upper_case}')
        print(f'number of total characters in the text is: {total}')
        print(f'the ratio is: {round(float(upper_case)/float(total) * 100, 2)}%')
