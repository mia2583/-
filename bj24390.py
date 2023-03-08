m, s = map(int, input().split(':'))

sec = 60 * m + s
count = 0


count += sec // 600
sec = sec % 600


count += sec // 60
sec = sec % 60


if sec >= 30:
    count += sec // 30
    sec = sec % 30
else:
    count += 1


count += sec // 10


print(count)



