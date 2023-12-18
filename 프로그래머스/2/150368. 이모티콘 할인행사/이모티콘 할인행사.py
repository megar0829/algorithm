cnt, total_price = 0, 0

def solution(users, emoticons):
    global cnt, total_price
    
    discounts = [10, 20, 30, 40]

    n = len(emoticons)

    price = [[0] * 4 for _ in range(n)]
    for i in range(n):
        for j in range(4):
            price[i][j] = emoticons[i] // 10 * (10 - discounts[j] // 10)

    used = [[0] * 4 for _ in range(n)]

    emo_prices = [0] * n

    def dfs(idx):
        global cnt, total_price
        
        if idx == n:
            count_user, save_price = 0, 0
            for discount, limit_price in users:
                sum_price = 0
                for emo_dis, emo_price in emo_prices:
                    if emo_dis >= discount:
                        sum_price += emo_price

                if sum_price >= limit_price:
                    count_user += 1
                else:
                    save_price += sum_price

            if count_user > cnt:
                cnt = count_user
                total_price = save_price

            elif count_user == cnt and save_price > total_price:
                total_price = max(total_price, save_price)

            return

        for j in range(4):
            if not used[idx][j]:
                used[idx][j] = 1
                emo_prices[idx] = (discounts[j], price[idx][j])
                dfs(idx + 1)
                used[idx][j] = 0
                emo_prices[idx] = 0

    dfs(0) 

    answer = [cnt, total_price]
    
    return answer