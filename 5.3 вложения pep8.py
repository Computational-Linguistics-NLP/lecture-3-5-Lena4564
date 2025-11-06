text = input()
length = len(text)

if length < 2:
    print("чудовищно мало")
else:
    if length < 5:
        print("очень мало")
    else:
        if length < 10:
            print("мало")
        else:
            if length < 30:
                print("ок")
            else:
                if length < 100:
                    print("много")
                else:
                    print("чудовищно много")
