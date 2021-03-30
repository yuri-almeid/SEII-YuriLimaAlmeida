import requests 
import time 
import concurrent.futures


# pega url das imagens
imagens_url = [             
'https://unsplash.com/photos/dF3UUgTdGGw',
'https://unsplash.com/photos/v-ti3sccORY'
]

t1 = time.perf_counter()


def download(img_url):
  img_bytes = requests.get(img_url).content
  img_name = img_url.split('/')[3]
  img_name = f'{img_name}.jpg'

  with open (img_name,'wb') as img_file:
    img_file.write(img_bytes)
    print(f'{img_name} was downloaded..')

with concurrent.futures.ThreadPoolExecutor() as executor:
  executor.map(download,imagens_url)

t2 = time.perf_counter()
print(f'Finished in {round(t2-t1,3)} second(s)')
