lunch = {
    '20층' : '123-456',
    '양자강' : '456-789',
    '백수산' : '456-123'
}
print(lunch.items())

# 1. String formatting
with open('lunch.csv','w',encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0],item[1]}\n')

# 2. Join method 활용
with open('lunch2.csv','w',encoding='utf-8') as f:
    for item in lunch.items():
        f.write(','.join(item) + '\n')

# 3. csv.writer
import csv
with open('lunch3.csv', 'w', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item) # 한줄작성
