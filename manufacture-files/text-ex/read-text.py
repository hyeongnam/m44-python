with open('mulcam.txt', 'r') as f:
    # f.readlines()
    # 파일의 모든 라인을 읽어서 각각의 줄을
    # member item 으로 갖는 list 를 반환
    lines = f.readlines()
    for line in lines:
        print(line)
    f.read()
    # 파일 내용 전체를 문자열로 반환
    all_text = f.read()
    print(all_text)
