"""
Plots and saves frames for animations when 2012 is changed by 2013.
Last digit is rolling from top.
"""

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from numpy import arange

N_FRAMES = 20

alignment = {'horizontalalignment': 'center', 'verticalalignment': 'center'}

fig = plt.figure(figsize=(5, 3))
renderer = fig.canvas.get_renderer()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')

font1 = FontProperties(size=128, fname='Roboto-Light.ttf')
font2 = FontProperties(size=128, fname='Roboto-Regular.ttf')

# determine height of the letter in data coordinates
# http://stackoverflow.com/questions/5466539/get-bbox-in-data-coordinates-in-matplotlib

txt_tmp = plt.text(0.5, 0.5, '2', fontproperties=font2, **alignment)
bb = txt_tmp.get_window_extent(renderer=renderer)
bb2 = bb.transformed(ax.transData.inverted())
height_txt = bb2.ymax - bb2.ymin


# three auxiliary functions to convert bbox coordinates
def center_to_top(y):
    return y + height_txt / 2


def center_to_bottom(y):
    return y - height_txt / 2


def top_to_center(y):
    return y - height_txt / 2


def plot_frame(t):
    """
    Plots one frame.

    :param t: a parameter that changes from 0 to 1.
    """

    plt.clf()
    plt.axes([0, 0, 1, 1])
    plt.axis('off')

    x0 = 0.23
    dx = 0.19
    dy_spacing = 0.1

    year = '2012'

    for i in range(3):
        if i < 2:
            font = font1
        else:
            font = font2
        plt.text(x0 + i * dx, 0.5, year[i], fontproperties=font, **alignment)

    i += 1

    y_initial = 1.3
    y_final = 0.1

    y_3_center = y_initial + (y_final - y_initial) * t
    y_3_bottom = center_to_bottom(y_3_center)
    y_2_top = y_3_bottom - dy_spacing
    y_2_center = top_to_center(y_2_top)

    if y_3_center < 0.5:
        y_3_center = 0.5

    if y_2_center > 0.5:
        y_2_center = 0.5

    plt.text(
        x0 + i * dx,
        y_3_center,
        '3',
        fontproperties=font, **alignment)

    plt.text(
        x0 + i * dx,
        y_2_center,
        '2',
        fontproperties=font, **alignment)


for i, t in enumerate(arange(0, 1, 1. / N_FRAMES)):
    print t
    plot_frame(t)
    plt.savefig('images/%02d.png' % i, dpi=72)
