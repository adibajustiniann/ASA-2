graph = {
    'A': {'J': 180, 'B': 69, 'S': 115},
    'B': {'A': 69, 'C': 195, 'G': 48},
    'C': {'B': 195, 'D': 120, 'U': 60},
    'D': {'C': 120, 'R': 67, 'E': 179},
    'E': {'D': 179, 'U': 70, 'H': 105, 'P': 142, 'V': 64, 'F': 96},
    'F': {'E': 96, 'R': 183, 'T': 108},
    'G': {'B': 48, 'H': 123},
    'H': {'G': 123, 'I': 90, 'E': 105},
    'I': {'S': 66, 'H': 90},
    'J': {'A': 180, 'K': 87, 'L': 135},
    'K': {'J': 87, 'L': 55},
    'L': {'K': 55, 'M': 43, 'J': 135},
    'M': {'L': 43, 'P': 67, 'N': 70, 'W': 44},
    'N': {'M': 70, 'O': 58, 'P': 90},
    'O': {'N': 58, 'T': 86, 'W': 85},
    'P': {'E': 142, 'Q': 73, 'N': 90, 'M': 67},
    'Q': {'P': 73, 'S': 105},
    'R': {'F': 183, 'D': 67},
    'S': {'A': 115, 'I': 66, 'Q': 105},
    'T': {'O': 86, 'V': 126, 'F': 108},
    'U': {'C': 60, 'E': 70},
    'V': {'E': 64, 'T': 126},
    'W': {'M': 44, 'O': 85}
}

heuristic = {
    'A' : 408,
    'B' : 368,
    'C' : 276,
    'D' : 180,
    'E' : 80,
    'F' : 53,
    'G' : 318,
    'H' : 216,
    'I' : 270,
    'J' : 254,
    'K' : 201,
    'L' : 163,
    'M' : 140,
    'N' : 104,
    'O' : 37,
    'P' : 179,
    'Q' : 238,
    'R' : 160,
    'S' : 334,
    'T' : 0,
    'U' : 231,
    'V' : 74,
    'W' : 134
}

hasil = []

def a_star(graph, curr, tujuan, heuristic, sumCost, path):
    if(curr == tujuan):
        hasil.append(sumCost)
        hasil.append(path)
        return

    neighbour = graph[curr]
    kunciMin = ''
    fTemp = 9999999999
    for kunci, cost in neighbour.items():
        if(kunci not in path):
            fn = cost + heuristic[kunci]
            if(fn < fTemp):
                fTemp = fn
                kunciMin = kunci
                gMin = cost

    a_star(graph, kunciMin, tujuan, heuristic, sumCost + gMin, path + " " + kunciMin)

start = str(input())

a_star(graph, start, 'T', heuristic, 0, start)

print("Final Cost :", hasil[0])
print("PATH:", hasil[1])