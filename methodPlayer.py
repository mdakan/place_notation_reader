import sys
import time
from audiotest import playWav


def intChange(strChange):
    change = []
    for bell in strChange.split():
        if bell == "0":
            bell = 10
        elif bell == "E":
            bell = 11
        elif bell == "T":
            bell = 12
        else:
            bell = int(bell)
        change.append(bell)
    return(change)


def methodPlayer(printout):
    f = open(printout)
    stage = int(f.readline())
    rows = f.readlines()

    # play rounds an extra time before starting
    for bell in intChange(rows[0]):
        playWav(str(stage + 1 - bell))
    handstroke = True
    for row in rows:  # then play all the rows, with handstroke pauses
        for bell in intChange(row):
            playWav(str(stage + 1 - bell))
        if handstroke:
            time.sleep(0.2)
        handstroke = not handstroke


if __name__ == "__main__":
    methodPlayer(str(sys.argv[1]))
