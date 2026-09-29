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


def sort_range(array, left, right, depth, result):
    if right - left < 2:
        return
    starts = distribute(array, left, right, depth, result)
    # 0번 버킷은 단어가 끝났으므로 재귀하지 않습니다.
    for bucket in range(1, BUCKET_COUNT):
        child_left = left + starts[bucket]
        child_right = left + starts[bucket + 1]
        if child_right - child_left > 1:
            sort_range(array, child_left, child_right, depth + 1, result)


def Radix_Sort_MSD(array):
    if any(
        not isinstance(word, str)
        or any(not "a" <= char <= "z" for char in word)
        for word in array
    ):
        raise ValueError("MSD 기수 정렬은 소문자 a~z로 된 문자열만 지원합니다.")
    # 재귀 구간이 함께 사용하는 작업 배열은 한 번만 만듭니다.
    result = [None] * len(array)
    sort_range(array, 0, len(array), 0, result)
