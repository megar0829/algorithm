import sys
input = sys.stdin.readline


def psy_dis(mbti1, mbti2):
    cnt = 0
    for x in range(4):
        if mbti1[x] == mbti2[x]:
            pass
        else:
            cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    mbti_set = list(set(mbti))
    n = len(mbti_set)
    mbti_dist = []
    mbti_2_lst = []
    mbti_3 = 0
    for i in mbti_set:
        if mbti.count(i) >= 3:
            mbti_3 += 1
        elif mbti.count(i) == 2:
            mbti_2_lst.append(i)
    if N > 256 or n == 1 or mbti_3 != 0:
        print(0)
    elif N > 16 or len(mbti_2_lst) > 0:
        for i in mbti_2_lst:
            for j in mbti_set:
                if i == j:
                    pass
                else:
                    mbti_dist.append(psy_dis(i, j) * 2)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    dist_1 = psy_dis(mbti_set[i], mbti_set[j])
                    dist_2 = psy_dis(mbti_set[j], mbti_set[k])
                    dist_3 = psy_dis(mbti_set[k], mbti_set[i])
                    mbti_dist.append(dist_1 + dist_2 + dist_3)
        print(min(mbti_dist))
    else:
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    dist_1 = psy_dis(mbti_set[i], mbti_set[j])
                    dist_2 = psy_dis(mbti_set[j], mbti_set[k])
                    dist_3 = psy_dis(mbti_set[k], mbti_set[i])
                    mbti_dist.append(dist_1 + dist_2 + dist_3)
        print(min(mbti_dist))