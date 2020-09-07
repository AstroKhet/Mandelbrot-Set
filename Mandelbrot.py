from PIL import Image, ImageDraw
import time

# Widht and height should be even
width = 10000
height = 6666

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1
iterations = 80

img = Image.new('RGB', (width, height), (0, 0, 0))
canvas = ImageDraw.Draw(img)


def heat(n):
    # Smaller n is, closer to white/yellow  (R^, G^-, B^--)
    # Larger n is, closer to black, blue    (Rv, Gv-, Bv--)
    # Honestly I have no idea what to do
    r = min(round((255 * n)/(0.6*iterations)), 255)
    g = min(round((255 * n)/(0.3*iterations)), 255)
    b = min(round((255 * n)/(0.15*iterations)), 255)
    return r, g, b


def get_colour(C: complex):
    tend = complex(C.real, C.imag)
    n = 0
    while n < iterations:
        tend = tend**2 + C
        if abs(tend.real + tend.imag) > 16:
            break
        n += 1

    return (0, 0, 0) if n == iterations else heat(n)


start = time.time()
for y in range(height):
    for x in range(width):
        c = complex(RE_START + (x / width) * (RE_END - RE_START),
                    IM_START + (y / height) * (IM_END - IM_START))

        col = get_colour(c)
        canvas.point([x, y], col)
end = time.time()

print(end - start)
img.convert('RGB').save('Gallery/image.png', 'PNG')
