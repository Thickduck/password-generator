import random

def generate(hm_passwd, ln_passwd):
    stuff = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}\"',./<>?"
    for i in range(hm_passwd):
        passwd = ""
        for j in range(ln_passwd):
            choice = random.choice(stuff)
            passwd += choice
        return passwd

