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


def distribute(array, left, right, depth, result):
    counts = count_buckets(array, left, right, depth)
    # starts[b]는 현재 구간 안에서 b 버킷이 시작하는 상대 위치입니다.
    starts = [0] * (BUCKET_COUNT + 1)
    for bucket in range(BUCKET_COUNT):
        starts[bucket + 1] = starts[bucket] + counts[bucket]

    next_position = starts[:-1].copy()
    for i in range(left, right):
        bucket = character_bucket(array[i], depth)
        result[left + next_position[bucket]] = array[i]
        next_position[bucket] += 1

    array[left:right] = result[left:right]
    return starts
