import random
import string
import hashlib

def generate_random_string():
    word_length=6
    return "".join(random.choices(string.ascii_letters + string.digits,k=word_length))

def generate_md5_dictionary(num=10):
    md5_dict={}
    for _ in range(num):
        random_string=generate_random_string()
        md5_hash=hashlib.md5(random_string.encode()).hexdigest()
        md5_dict[random_string]=md5_hash
    return md5_dict

if __name__=="__main__":
    user_input=input("Type random for random generation,or type in any word :")
    if user_input=="random":
        dictionary=generate_md5_dictionary(10)
        print("Random 6-word Strings and their md5 hashes")
        for key,value in dictionary.items():
            print(f"{key}:{value}")
    else:
        s=hashlib.md5(user_input.encode()).hexdigest()
        print(f"The hash is {s} ")