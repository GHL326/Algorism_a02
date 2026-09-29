BUCKET_COUNT = 27


def character_bucket(word, depth):
    # 단어 끝은 0, a~z는 1~26번 버킷입니다.
    if depth >= len(word):
        return 0
    return ord(word[depth]) - ord("a") + 1


def count_buckets(array, left, right, depth):
    """[left, right) 구간에서 depth 위치 문자의 빈도를 셉니다."""
    counts = [0] * BUCKET_COUNT
    for i in range(left, right):
        counts[character_bucket(array[i], depth)] += 1
    return counts
