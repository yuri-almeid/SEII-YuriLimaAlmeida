import time 
from PIL import Image, ImageFilter

imagens_names = [             
'chuttersnap-dijDmGXAiFY-unsplash.jpg'
]
t1 = time.perf_counter()
size = (640,427)

for imagens in imagens_names:
  img = Image.open(imagens)
  img = img.filter(ImageFilter.GaussianBlur(15))

  img.thumbnail(size)
  img.save(f'processed/{imagens}')
  print(f'{imagens} was processed.')

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
