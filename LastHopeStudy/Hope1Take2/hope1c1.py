def turn(h,m):
    ah = h * 60 + m      # hour hand * 2 degrees
    am = m * 12          # minute hand * 2 degrees
    cw = (am - ah) % 720
    ccw = (ah - am) % 720
    if cw < ccw:
        return "CW"
    if ccw < cw:
        return "CCW"
    return "EITHER"


assert turn(1, 30) == "CW", turn(1, 30)
assert turn(1, 45) == "CCW", turn(1, 45)
assert turn(6, 0) == "EITHER", turn(6, 0)
