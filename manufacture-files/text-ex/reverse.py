
with open('numbers.txt','r') as f:
    lines = f.readlines()
# 2.list 뒤집기
lines.reverse()

with open('numbers.txt','w') as f:
    for line in lines:
        # String.strip() 문자열의 처음과 끝의 공백을 지워주는 메서드
        f.write(line.rstrip() + '\n') # 오른쪽 공백만 지워라 => rstrip()



