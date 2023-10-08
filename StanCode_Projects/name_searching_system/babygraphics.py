"""
File: babygraphics.py
Name: jay wu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 300


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # Calculate the gap between each year's line
    total_years = len(YEARS)
    gap = width / total_years
    # decide every x location
    x_coordinate = year_index * gap

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    margin = GRAPH_MARGIN_SIZE
    height = CANVAS_HEIGHT
    width = CANVAS_WIDTH

    # create every x line
    for i in range(len(YEARS)):
        x = get_x_coordinate(width - 2 * margin, i) + margin
        canvas.create_line(x, 0, x, height, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, height - margin, anchor=tkinter.NW, text=str(YEARS[i]))

    # create the left-most line
    canvas.create_line(margin, 0, margin, height, width=LINE_WIDTH)
    # create the upper line
    canvas.create_line(margin, margin, width-margin, margin, width=LINE_WIDTH)
    # create the bottom line
    canvas.create_line(margin, height-margin, width-margin, height-margin)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    margin = GRAPH_MARGIN_SIZE
    height = CANVAS_HEIGHT
    width = CANVAS_WIDTH

    max_rank = MAX_RANK
    min_rank = 1
    y_scale = (height - 2 * margin) / (max_rank - min_rank)

    color_index = 0

    # type a name and search it
    for name in lookup_names:

        prior_list = []
        color = COLORS[color_index]
        i = 0

        # if the rank is out of max_rank, replace the rank with '*'
        for year in YEARS:
            name_points = name_data[name]
            if name_points.get(str(year)) is None:
                name_data[name][str(year)] = '*'
            elif name_points[str(year)] == '*':
                pass
            elif int(name_points[str(year)]) > MAX_RANK:
                name_data[name][str(year)] = '*'

        # find the year, rank in the name
        name_points = name_data[name]

        # write the name and rank on every x line
        for year, rank in name_points.items():
            x = get_x_coordinate(width - 2 * margin, YEARS.index(int(year))) + margin
            if rank == "*":
                y = height - margin
            else:
                y = (int(rank) - min_rank) * y_scale + margin
            canvas.create_text(x + TEXT_DX, y, anchor=tkinter.SW, text=f"{name} {rank}", fill=color)

        # draw a line between every x
        for year in YEARS:

            # get the rank under every year
            rank = name_data[name][str(year)]

            # get the gap between every x
            total_years = len(YEARS)
            gap = (width-2 * margin) / total_years

            # start from the first x
            if len(prior_list) == 0:
                rank = name_data[name][str(year)]
                # if first x is '*', replace it with the most bottom y
                if rank == '*':
                    first_rank = height - margin
                else:
                    first_rank = name_data[name][str(year)]

                # store the first rank, it will use on drawing line
                prior_list.append(first_rank)

            else:
                # call the prior rank we store
                prior_rank = prior_list[-1]

                # if first x is '*', replace it with the most bottom y
                if rank == '*':
                    target_rank = height - margin
                else:
                    target_rank = name_data[name][str(year)]

                # draw a line if prior rank is most bottom y
                if prior_rank == height - margin and target_rank != height - margin:
                    canvas.create_line(margin + gap * i,
                                       height-margin, margin + gap * (i + 1),
                                       (int(target_rank) - min_rank) * y_scale + margin,
                                       fill=color, width=LINE_WIDTH)

                # draw a line if target rank is most bottom y
                elif target_rank == height - margin and prior_rank != height - margin:
                    canvas.create_line(margin + gap * i,
                                       (int(prior_rank) - min_rank) * y_scale + margin, margin + gap * (i + 1),
                                       height - margin,
                                       fill=color, width=LINE_WIDTH)

                # draw a line if prior rank and target rank is most bottom y
                elif target_rank == height - margin and prior_rank == height - margin:
                    canvas.create_line(margin + gap * i,
                                       height - margin, margin + gap * (i + 1),
                                       height - margin,
                                       fill=color, width=LINE_WIDTH)

                # draw a line
                else:
                    canvas.create_line(margin + gap * i,
                                       (int(prior_rank) - min_rank) * y_scale + margin, margin + gap * (i+1),
                                       (int(target_rank) - min_rank) * y_scale + margin,
                                       fill=color, width=LINE_WIDTH)

                # store the rank, it will use on drawing line
                prior_list.append(target_rank)
                # use on calculate the gap
                i += 1
                # use on choosing color in color index
                color_index += 1
                if color_index == 4:
                    color_index = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
