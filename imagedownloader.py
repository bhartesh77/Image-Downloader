import requests
from bs4 import BeautifulSoup
import os

#counter=0

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    #print(soup.text)

    images = soup.find_all('img')

    #print(images)
    i=0
    for image in images:
        try:
            #print(image)
            #counter=counter+1

            name=str(i)+image['alt']
            link=image['src']
            with open(name.replace(' ', '-') + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('downloading: ', name)
            i = i + 1

        except:
            pass

print ('url ')
url = input()
print('folder name ')
folder_name = input()

imagedown(url, folder_name)

""""
def imagedown1(url):
    #try:
        #os.mkdir(os.path.join(os.getcwd(), folder))
    #except:
        #pass
    #os.chdir(os.path.join(os.getcwd(), folder))

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    #print(soup.text)

    images = soup.find_all('img')

    #print(images)
    for image in images:
        try:
            #print(image)
            name=image['alt']
            link=image['src']
            #counter=counter+1
            #print(name)
            with open(name + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('downloading: ', name)

        except:
            pass

i=2

while i < 3:
    imagedown1(url+str(i))
    i=i+1
    
"""