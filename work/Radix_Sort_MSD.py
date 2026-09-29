BUCKET_COUNT = 27


def character_bucket(word, depth):
    # 단어 끝은 0, a~z는 1~26번 버킷입니다.
    if depth >= len(word):
        return 0
    return ord(word[depth]) - ord("a") + 1
