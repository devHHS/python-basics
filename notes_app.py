import json


# 함수(def): 반복되거나 의미 단위로 묶을 수 있는 코드를 이름 붙여 재사용하는 방법.
# 함수는 "정의"만 해두면 실행되지 않고, 호출해야 실제로 동작한다.
# (그래서 호출되는 시점보다 앞에 정의되어 있어야 한다.)

# 딕셔너리: {key: value}로 title/content를 하나의 note로 묶고, 리스트(notes)에 추가한다.
def add_note(notes, title, content):
    note = {"title": title, "content": content}
    notes.append(note)
    return notes

# 리스트 순회 + 조건 검사: 제목이 같은 노트를 찾아서 돌려준다. 끝까지 못 찾으면 None.
def find_note(notes, title):
    for n in notes:
        if n["title"] == title:
            return n
    return None

# enumerate(): 리스트를 순회하며 인덱스(i)와 원소(n)를 같이 얻는다.
# del notes[i]로 그 인덱스의 원소를 지운다.
def delete_note(notes, title):
    for i, n in enumerate(notes):
        if n["title"] == title:
            del notes[i]
            return notes
    return None

# 함수는 매개변수 없이도 만들 수 있다. 이 함수는 밖에서 값을 받을 필요 없이,
# 스스로 input()을 받아서 그 결과를 return으로 밖에 돌려주기만 한다.
def search_title():
    return input("찾을 제목: ").strip()


# json.dump(note, f) / json.load(f): 딕셔너리 하나를 파일에 저장하고 다시 불러오는 방법.
# (노트를 여러 개 다루도록 리스트로 바꿨기 때문에, 지금은 참고용으로만 남겨둔다.)
# with open("note.json", "w") as f:
#     json.dump(note, f)
# with open("note.json", "r") as f:
#     loaded_note = json.load(f)
# print(f"제목: {loaded_note['title']} \n내용: {loaded_note['content']}")

# try/except: notes.json이 없을 수도 있으니(처음 실행 등), 없으면 에러로 멈추는 대신
# 빈 리스트로 시작한다.
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = []

# if로 한 번만 검사하던 빈 값 검증 (레슨 3). 아래 while 검증으로 대체되어 지금은 안 쓴다.
#title = input("제목이 뭔가요: ").strip()
#content = input("내용을 작성해주세요: ").strip()
# if title == "" or content == "":
#     print("제목과 내용을 모두 입력해야합니다")
# else:
#     notes = add_note(notes, title, content)

# while로 재입력받는 검증 (레슨 4). 메뉴 안(1. 추가)으로 옮겨져서 지금은 안 쓴다.
# title = input("제목이 뭔가요: ").strip()
# while title == "":
#     print("제목을 입력하세요")
#     title = input("제목이 뭔가요: ").strip()

# content = input("내용을 작성해주세요: ").strip()
# while content == "":
#     print("내용을 입력하세요")
#     content = input("내용을 작성해주세요: ").strip()

# while True + break + if/elif: "4. 종료"를 고를 때까지 계속 메뉴를 보여준다.
while True:
    choice = input("1.추가 2.찾기 3.삭제 4.종료: ").strip()
    if choice == "1":
        # while문: 값이 입력될 때까지 계속 다시 물어본다 (빈 문자열은 거짓으로 취급됨).
        title = input("제목이 뭔가요: ").strip()
        while title == "":
            print("제목을 입력하세요")
            title = input("제목이 뭔가요: ").strip()
        content = input("내용을 작성해주세요: ").strip()
        while content == "":
            print("내용을 입력하세요")
            content = input("내용을 작성해주세요: ").strip()
        add_note(notes, title, content)

    elif choice == "2":
        title = search_title()
        found = find_note(notes, title)
        if found is None:
            print(f"{title} is not found")
        else:
            print(f"{title} is found")

    elif choice == "3":
        title = search_title()
        found = delete_note(notes, title)
        if found is None:
            print(f"{title} is not found")
        else:
            print(f"{title} is deleted")

    elif choice == "4":
        break

# 예전에 함수 동작을 하나씩 확인해보던 테스트 코드 (레슨 5). 지금은 메뉴로 대체됐다.
# print(notes)
# print(find_note(notes, "6"))
# print(delete_note(notes, "6"))

# json.dump: 메뉴에서 어떤 작업을 했든, 종료할 때 최종 notes 상태를 한 번에 저장한다.
with open("notes.json", "w") as f:
    json.dump(notes, f)
