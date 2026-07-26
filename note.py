import json

# input(): 프로그램을 멈추고 사용자가 키보드로 입력한 뒤 엔터를 칠 때까지 기다렸다가,
# 입력한 내용을 문자열로 돌려준다.
title = input("제목이 뭔가요: ")
content = input("내용을 작성해주세요: ")

# 딕셔너리: {key: value} 쌍으로 여러 값을 하나로 묶는 자료구조.
# title, content를 따로 관리하지 않고 note 하나로 묶으면
# - "이 둘은 노트 하나를 나타낸다"는 의미가 코드에 드러나고
# - 나중에 노트가 여러 개로 늘어나도 대응하기 쉽고
# - json 같은 라이브러리로 파일에 저장/불러오기가 쉬워진다.
#note = {"title": title, "content": content}

# json.dump(note, f) / json.load(f): 딕셔너리 하나를 파일에 저장하고 다시 불러오는 방법.
# (노트를 여러 개 다루도록 아래에서 리스트로 바꿨기 때문에, 지금은 참고용으로만 남겨둔다.)
# with open("note.json", "w") as f:
#     json.dump(note, f)
# with open("note.json", "r") as f:
#     loaded_note = json.load(f)
# print(f"제목: {loaded_note['title']} \n내용: {loaded_note['content']}")

# 함수(def): 반복되거나 의미 단위로 묶을 수 있는 코드를 이름 붙여 재사용하는 방법.
# note 하나를 만들어서 notes 리스트에 추가하는 일을 통째로 여기로 옮겼다.
# 함수는 "정의"만 해두면 실행되지 않고, 아래에서 add_note(...)로 "호출"해야 실제로 동작한다.
# (그래서 호출되는 시점보다 앞에 정의되어 있어야 한다.)
def add_note(notes, title, content):
    note = {"title": title, "content": content}
    notes.append(note)
    return notes

# 리스트(list): [] 안에 값 여러 개를 순서대로 담는 자료구조.
# note 하나만 저장하지 않고, note들을 리스트로 모아서 여러 개를 남긴다.
with open("notes.json", "r") as f:
    notes = json.load(f)

notes = add_note(notes, title, content)

with open("notes.json", "w") as f:
    json.dump(notes, f)

# for문: 리스트 안의 원소를 하나씩 꺼내서, 원소 개수만큼 아래 코드를 반복 실행한다.
for n in notes:
    print(f"제목: {n['title']} \n내용: {n['content']}")
