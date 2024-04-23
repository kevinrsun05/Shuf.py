#!/usr/bin/env python3

import argparse
import random, sys

class shuf:
    def __init__(self, filename = None, echo = None, inputRange = None):
        if echo is None and inputRange is None and (filename is None or filename == "-"):
            self.lines = sys.stdin.read().strip().split('\n')
        elif echo is None and inputRange is None:
            f = open(filename, 'r')
            self.lines = [line.rstrip('\n') for line in f.readlines()]
            f.close()
        else:
            self.lines = []

            
    def shuffleFunc(self, head_count = None, repeat = False, echo = None, inputRange = None):
        if echo is not None and inputRange is not None:
            parser.error("cannot combine -e and -i options")
            sys.exit(1)
        if echo is not None:
            self.lines = echo
        if inputRange is not None:
            splitStr = inputRange.split("-")
            startNum = int(splitStr[0])
            endNum = int(splitStr[1])
            for i in range(startNum, endNum + 1):
                self.lines.append(i)
        random.shuffle(self.lines)
        if repeat:
            if head_count is None:
                counter = -1
            else:
                counter = head_count
            while counter != 0:
                print(random.choice(self.lines))
                counter = counter - 1
        else:
            for line in self.lines[:head_count]:
                print(line)
        
def main():
    parser = argparse.ArgumentParser(description = "The Python 3 version of GNU shuf")
    parser.add_argument("-e", "--echo", nargs = "+", help = "Treat each argument as a line")
    parser.add_argument("-i", "--input-range", type = str, help = "Lo to Hi input")
    parser.add_argument("-n", "--head-count", type = int, help = "Output at most count lines")
    parser.add_argument("-r", "--repeat", action = "store_true", help = "repeat output values")
    parser.add_argument("filename", nargs = "?", default = None, help= "Path to input file")
    args = parser.parse_args()
    
    if args.head_count:
        if args.head_count < 0:
            parser.error("Invalid head-count value")
            sys.exit(1)

    shuffler = shuf(args.filename, args.echo, args.input_range)
    shuffler.shuffleFunc(args.head_count, args.repeat, args.echo, args.input_range)

if __name__ == '__main__':
    main()
