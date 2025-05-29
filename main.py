from lab9 import max_wire_length

def read_input(path):
    f = open(path, "r")
    w = int(f.readline())
    heights = f.readline().strip().split()
    i = 0
    while i < len(heights):
        heights[i] = int(heights[i])
        i += 1
    f.close()
    return w, heights

def write_output(path, result):
    f = open(path, "w")
    r = int(result * 100 + 0.5) / 100.0
    f.write("{:.2f}".format(r))
    f.close()
 
w, heights = read_input("input.txt")
result = max_wire_length(w, heights)
write_output("output.txt", result)