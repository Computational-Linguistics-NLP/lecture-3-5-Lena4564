text = input()
length = len(text)
if length < 2:
    print("чудовищно мало")
elif length < 5:
    print("очень мало")
elif length < 10:
    print("мало")
elif length < 30:
    print("ок")
elif length < 100:
    print("много")
else:
    print("чудовищно много")
