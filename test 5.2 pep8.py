text = input()
length = len(text)
if length < 2:
    print("чудовищно мало")
if length >= 2 and length < 5:
    print("очень мало")
if length >= 5 and length < 10:
    print("мало")
if length >= 10 and length < 30:
    print("ок")
if length >= 30 and length < 100:
    print("много")
if length >= 100:
    print("чудовищно много")
