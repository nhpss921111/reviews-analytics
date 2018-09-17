import time
import progressbar

# 讀取檔案+計數+動態顯示進度
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        bar.update(count)
print('檔案讀取完了，總共有', len(data), '筆資料')

# 算平均留言長度
sun_len = 0
for d in data:
    sun_len += len(d)

print('每筆留言的平均長度為', sun_len/len(data))

# 篩選留言小於100
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

# 篩選有good的留言
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

# 篩選有good的留言(快寫法)
good = [d for d in data if 'good' in d]
print(good)

# 利用布林值，看有沒有bad的留言
bad = ['bad' in d for d in data]
print(bad)

# 篩選有good的留言的個數
good = [1 for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')

# 計算字出現的次數
wc = {} # word_count
for d in data:
     words = d.split()
     for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print('字典裡總共有', len(wc), '個字')

print('開放查詢功能')

while True:
    word = input('請輸入查詢的字: ')
    if word == 'q':
        break
    elif word in wc:
        print(word, '有出現過', wc[word], '次')
    else:
        print('這個字沒有出現過喔，請重新輸入')

print('感謝使用本查詢功能')
