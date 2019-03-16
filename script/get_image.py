import requests
IMAGE_URL = "http://img.moeimg.net/wp-content/uploads/archives10/10658/46_e4ejovby8g.jpg"

responce = requests.get(IMAGE_URL)
with open("image/megane.jpg","wb") as f:
    f.write(responce.content)
