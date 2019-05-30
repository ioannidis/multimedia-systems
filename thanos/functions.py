from math import ceil
import numpy as np

window = 16
k = 16


def frame_to_macroblocks(frame):
    old_width = frame.shape[0]
    width = fit_size(old_width)
    old_height = frame.shape[1]
    height = fit_size(old_height)

    width_pad = (0, width - old_width)
    height_pad = (0, height - old_height)
    depth_pad = (0, 0)
    padding = (width_pad, height_pad, depth_pad)

    padded_frame = np.pad(frame, padding, mode='constant')

    macroblocks = []

    for w in range(0, width - window, window):
        row = []
        for h in range(0, height - window, window):
            macroblock = padded_frame[w:w + window, h:h + window]
            row.append(macroblock)
        macroblocks.append(row)

    return macroblocks


def macroblocks_to_frame(macroblocks):
    rows = []
    for row in macroblocks:
        rows.append(np.concatenate([macroblock for macroblock in row], axis=1))

    frame = np.concatenate([row for row in rows], axis=0)
    return frame


def fit_size(x):
    return window * ceil(x / window)


def get_sad(m_prev, m_next):
    value = 0

    for i in range(window):
        for j in range(window):
            pixel_prev = m_prev[i, j]
            pixel_next = m_next[i, j]

            for k in range(3):
                color_prev = int(pixel_prev[k])
                color_next = int(pixel_next[k])
                value += abs(color_next - color_prev)

    return value


def get_best_match(ms_prev, next_row, next_col, m_next):
    # Logarithmic search for motion estimation

    step = k / 2
    result = None

    while step != 1:
        neighbours = []

        try:
            neighbours.append([next_row + 1, next_col + 1, ms_prev[next_row + 1][next_col + 1]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row + 1, next_col - 1, ms_prev[next_row + 1][next_col - 1]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row - 1, next_col + 1, ms_prev[next_row - 1][next_col + 1]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row - 1, next_col - 1, ms_prev[next_row - 1][next_col - 1]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row + 1, next_col, ms_prev[next_row + 1][next_col]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row, next_col - 1, ms_prev[next_row][next_col - 1]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row, next_col + 1, ms_prev[next_row][next_col + 1]])
        except IndexError:
            pass

        try:
            neighbours.append([next_row - 1, next_col, ms_prev[next_row - 1][next_col]])
        except IndexError:
            pass

        sad_values = [get_sad(neighbour[2], m_next) for neighbour in neighbours]
        sad_min = min(sad_values)

        min_index = sad_values.index(sad_min)
        next_row, next_col, m_next = neighbours[min_index]

        step /= 2
        result = m_next

    return result
