with open('vocabulary.txt', 'a', encoding="utf-8") as f:
    while True:
        en_word = input("영어 단어를 입력하세요: ")
        if en_word == 'q':
            break
        else:
            f.write(f'{en_word}: ')
        kr_word = input("한국어 뜻을 입력하세요: ")
        if kr_word == 'q':
            break
        else:
            f.write(f'{kr_word}\n')
