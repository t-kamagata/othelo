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
    
b = Board()
b.print()

inputs = ()

while True:
    (success, inputs) = get2Input()
    if success:
        break
b.put(int(inputs[0]), int(inputs[1]))