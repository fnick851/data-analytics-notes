import requests
import os.path


def download(src, id, dirname):
    dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)) + '/' + dirname,
        str(id) + '.jpg'
    )
    print(dir)
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('unable to download image')
