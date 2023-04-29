from board import Board

def get2Input():
    inputs = input("入力(行, 列)＞").strip().split()
    length = len(inputs)
    if length == 2:
        return (True, (inputs[0], inputs[1]))
    elif length > 2:
        print("要素が多すぎます")
        return (False, (0, 0))
        pass
    else:
        print("要素が少ないです")
        return (False, (0, 0))
    
def parseNumber(num1, num2):
    try:
        a = int(num1)
        b = int(num2)
        return (True, a, b)
    except:
        print("数字を入力してください")
        return (False, 0, 0)

b = Board()
b.print()

inputs = ()

while True:
    (success, inputs) = get2Input()
    if not success:
        continue

    success, x, y = parseNumber(inputs[0], inputs[1])
    if not success:
        continue
    
    if not b.puttable(x, y):
        print("置けません")
        continue


b.put(int(inputs[0]), int(inputs[1]))