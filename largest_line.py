def shortest_line():
    f=open("b.txt")
    for line in f:
        short_line = line
        short_line_len = len(line)
    
    
            if len(line) < short_line_len:
                small_line_len = len(line)
                small_line = line

    print small_line






def longest_line():
    
    large_line = ''
    large_line_len = 0
    filename = "b.txt"

    with open(filename, 'r') as f:
        for line in f:
            if len(line) > large_line_len:
                large_line_len = len(line)
                large_line = line

    print( "Longest line in the file is ",large_line)
    shortest_line()




if(__name__=='__main__'):
    longest_line()
    
