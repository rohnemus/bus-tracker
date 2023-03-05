#!/usr/bin/env python
# Display bus times on screen.
from samplebase import SampleBase
from rgbmatrix import graphics
import bustracker as bstk
import time


class DisplayBus(SampleBase):
    def __init__(self, *args, **kwargs):
        super(DisplayBus, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x13.bdf")
        textColor = graphics.Color(255, 0, 0)
        pos = offscreen_canvas.width

        while True:
            # offscreen_canvas.Clear()
            # len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            # pos -= 1
            # if (pos + len < 0):
            #     pos = offscreen_canvas.width

            # time.sleep(0.05)
            # offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            offscreen_canvas.Clear()
            print("\nRefreshing Data!")
            graphics.DrawText(offscreen_canvas, font, 2, 14, textColor, "Refreshing")
            graphics.DrawText(offscreen_canvas, font, 2, 28, textColor, "   Data   ")
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            try:
                visits = bstk.get_predictions([14159,14158],['IB'])

                for i in range(60):
                    print("")
                    print(i)
                    incomming_busses = bstk.update_predictions(visits,i)
                    parsed = bstk.parse_predictions(incomming_busses)
                    for predictions in parsed:
                        print(predictions)

                    if len(parsed) < 1:
                        offscreen_canvas.Clear()
                        print("\nNo Buses Predicted")
                        graphics.DrawText(offscreen_canvas, font, 8, 14, textColor, "No Buses")
                        graphics.DrawText(offscreen_canvas, font, 5, 28, textColor, "Predicted")                    

                    if len(parsed) < 2:
                        offscreen_canvas.Clear()
                        graphics.DrawText(offscreen_canvas, font, 2, 21, textColor, str(parsed[0]))

                    if len(parsed) >= 2:
                        offscreen_canvas.Clear()
                        graphics.DrawText(offscreen_canvas, font, 2, 14, textColor, str(parsed[0]))
                        graphics.DrawText(offscreen_canvas, font, 2, 28, textColor, str(parsed[1]))

                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                    time.sleep(1)

            except:
                offscreen_canvas.Clear()
                print("\nNetwork Error\n")
                graphics.DrawText(offscreen_canvas, font, 5, 14, textColor, " Network ")
                graphics.DrawText(offscreen_canvas, font, 5, 28, textColor, "  Error  ")
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(5)


# Main function
if __name__ == "__main__":
    run_text = DisplayBus()
    if (not run_text.process()):
        run_text.print_help()