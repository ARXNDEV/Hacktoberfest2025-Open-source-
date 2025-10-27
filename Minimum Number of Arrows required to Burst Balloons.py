def findMinArrowShots(points):



    points.sort(key=lambda x: x[1])
    arrows = 0
    last_arrow = float('-inf')
    for xstart, xend in points:
        if xstart > last_arrow:
            arrows += 1
            last_arrow = xend
    return arrows
