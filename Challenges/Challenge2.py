ipAddress = input('Please enter the IP Address: ')
if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segmentLength = 0

for char in ipAddress:
    if char == '.':
        print("Segment {} length is {}".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1