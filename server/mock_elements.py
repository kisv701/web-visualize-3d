import colorsys

def generate_box(scale = 1.0) -> dict:
    """ Generates the vertices of a "unit cube" as 8 points.

    Args:
        scale (float, optional): Scales the distance between the points. Defaults to 1.0.

    Returns:
        dict: _description_
    """
    res = {
        'x': [],
        'y': [],
        'z': [],
        'r': [],
        'g': [],
        'b': []
    }
    index = 0
    for z in [-0.5, 0.5]:
        for y in [-0.5, 0.5]:
            for x in [-0.5, 0.5]:
                r, g, b = colorsys.hsv_to_rgb(float(index)/8.0, 1.0, 1.0)
                index += 1
                res['x'].append(x * scale)
                res['y'].append(y * scale)
                res['z'].append(z * scale)
                res['r'].append(r)
                res['g'].append(g)
                res['b'].append(b)
    return res
