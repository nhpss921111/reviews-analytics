data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 ==0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

# 算平均留言長度
sun_len = 0
for d in data:
    sun_len += len(d)

print('每筆留言的平均長度為', sun_len/len(data))

