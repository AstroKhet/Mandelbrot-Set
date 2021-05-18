from PIL import Image, ImageDraw
import time

# Widht and height should be even
width = 10000
height = 6666

real_start = -2
real_end = 1
imag_start = -1
imag_end = 1
iterations = 80

img = Image.new('RGB', (width, height), (0, 0, 0))
canvas = ImageDraw.Draw(img)


def heat(n):
    # Smaller n is, closer to white/yellow  
    # Larger n is, closer to black, blue    
    # Honestly I have no idea what I'm doing
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
        c = complex(real_start + (x / width) * (real_end - real_start),
                    imag_start + (y / height) * (imag_end - imag_start))

        col = get_colour(c)
        canvas.point([x, y], col)
end = time.time()

print(f"Time taken: {round(end - start, 2)} seconds")
img.convert('RGB').save('Gallery/image.png', 'PNG')
