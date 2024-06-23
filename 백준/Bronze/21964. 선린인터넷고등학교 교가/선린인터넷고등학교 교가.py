def sunrin_internet_highschool_music(text):
    return text[-5:]

if __name__ == "__main__":
    N = int(input())
    text = input()
    
    print(sunrin_internet_highschool_music(text=text))