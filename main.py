###############################################################
# All code written by Rusty Dotson
#
# Test file for creating a visual representation
# of a Euclidean Rhythm from a list
#
# More information about Euclidean Rhythms
# at http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf
###############################################################


def get_beat_size():
    numNotes = -1
    barSize = -1
    while numNotes < 0:
        numNotes = int(input("input the amount of beats you want in the bar:"))
    while barSize < 0:
        barSize = int(input("input the size of notes to use (ex. 16 = 16th notes):"))
    return numNotes, barSize


def convert(beats, size):
    bar = []

    counter = 0
    for i in range(size):
        counter += beats
        if counter >= size:
            counter -= size
            bar.append(1)
        else:
            bar.append(0)
    return bar


def printBar(bar):
    print([i for i in bar])


def main():
    numNotes, beatSize = get_beat_size()
    bar = convert(numNotes, beatSize)
    printBar(bar)


main()
