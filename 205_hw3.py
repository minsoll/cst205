#minsol Cho
# CST 205

from image_info import image_info
from PIL import Image

def my_search(search_term):
    search_term = search_term.lower()
    best_match = None
    max_matches = 0
    
    for image in image_info:
        title_matches = image['title'].lower().count(search_term)
        tag_matches = sum(tag.lower().count(search_term) for tag in image['tags'])
        
        total_matches = title_matches + tag_matches
        if total_matches > max_matches:
            best_match = image['id']
            max_matches = total_matches
    
    return best_match if best_match else "no_results"

def apply_sepia(image):
    width, height = image.size
    pixels = image.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            pixels[x, y] = min(tr, 255), min(tg, 255), min(tb, 255)
    
    return image

def apply_negative(image):
    return Image.eval(image, lambda x: 255 - x)

def apply_grayscale(image):
    return image.convert('L')

def apply_thumbnail(image):
    width, height = image.size
    image = image.resize((width // 2, height // 2))
    return image
