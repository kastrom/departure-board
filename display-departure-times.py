#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time

class DisplayDepartureTimes(SampleBase,):
#class DisplayDepartureTimes(SampleBase, DepartureTimes):
    def __init__(self, *args, **kwargs):
        super(DisplayDepartureTimes, self).__init__(*args, **kwargs)
        self.parser.add_argument("-font", "--font-input", help="The font to pass in", default="tom-thumb.bdf")

        def run(self):
            #DepartureTimes.getDepartureTimes()
            canvas = self.matrix
            font = graphics.Font()
            font.LoadFont("fonts/" + self.args.font_input)
            lineHeight = 8
            maxLength = 11
            charWidth = 4
            baseTimePosition = 47
            trainColor = graphics.Color(241, 171, 0)
            boatColor = graphics.Color(0, 171, 255)

            departures = [["Waterloooooooo","3"],["Embankment","5"],["Waterloo", "9"],["Waterloooooooo","17"]]

            for n in range(4):

                if len(departures[n][1]) == 1: # test to see if there is a single digit time
                    timePosition = baseTimePosition # display the time component in the appropriate position
                if len(departures[n][0]) >= maxLength: # if the departure name length is above the maximum
                    departures[n][0] = departures[n][0][:maxLength-1] + "_" # truncate the name
            else:
                timePosition = baseTimePosition - charWidth # if there is more than one digit, move the time 4 digits to the left
                if len(departures[n][0]) >= maxLength - 1: # this time test for a shorter truncation length
                    departures[n][0] = departures[n][0][:maxLength-2] + "_"

                textColor = graphics.Color(200, 200, 200)
                y = (lineHeight*(n+1))-2
                graphics.DrawText(canvas, font, 1, y, textColor, departures[n][0])
                graphics.DrawText(canvas, font, timePosition, y, textColor, departures[n][1])
                graphics.DrawText(canvas, font, 52, y, textColor, "min")

                time.sleep(100) # show display for 100 seconds before exit


                # Main function
                if __name__ == "__main__":
                    #departure_times = DepartureTimes()
                    display_departure_times = DisplayDepartureTimes(departure_times)
                    if (not display_departure_times.process()):
                        display_departure_times.print_help()
