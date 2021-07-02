import hashlib
import base64


href = "https://www.youtube.com/watch?v=GlE_526r3sc"
href2 = "https://www.youtube.com/watch?v=skLvb0JCNJk"


def get_hash(hr):
    hash_object = hashlib.md5(hr.encode())
    shorter_id = base64.urlsafe_b64encode(hashlib.md5(hr.encode()).digest())[:6]
    return str(shorter_id)[2:8]


if __name__ == "__main__":
    print(get_hash(href))
    print(get_hash(href2))
