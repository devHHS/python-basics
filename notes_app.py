import json
from notes import add_note, find_note, find_all_by_title, update_note, delete_note, search_title

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
    choice = input("1. Add 2. Find 3. Delete 4. Update 5. Quit: ").strip()
    if choice == "1":
        # while문: 값이 입력될 때까지 계속 다시 물어본다 (빈 문자열은 거짓으로 취급됨).
        title = input("Title: ").strip()
        while title == "":
            print("Please enter a title.")
            title = input("Title: ").strip()
        content = input("Content: ").strip()
        while content == "":
            print("Please enter some content.")
            content = input("Content: ").strip()
        add_note(notes, title, content)

    elif choice == "2":
        title = search_title()
        found_notes = find_all_by_title(notes, title)
        if not found_notes:
            print(f"{title} was not found.")
        else:
            for i, n in enumerate(found_notes):
                print(f"{i}: title={title}, content={n['content']}")

    elif choice == "3":
        choice_2 = input("1. Delete one 2. Delete all with this title 3. Delete everything: ").strip()
        if choice_2 == "1":
            title = search_title()
            found_notes = find_all_by_title(notes, title)
            if not found_notes:
                print(f"{title} was not found.")
            else:
                for i, n in enumerate(found_notes):
                    print(f"{i}: title={title}, content={n['content']}")
                index_number = int(input("Which number? ").strip())
                chosen = found_notes[index_number]
                notes.remove(chosen)
                print(f"title={title}, content={chosen['content']} was deleted.")

        elif choice_2 == "2":
            title = search_title()
            found_notes = find_all_by_title(notes, title)
            if not found_notes:
                print(f"{title} was not found.")
            else:
                for n in found_notes:
                    notes.remove(n)
                print(f"All notes titled {title} were deleted.")

        elif choice_2 == "3":
            notes.clear()
            print("All notes were deleted.")

    elif choice == "4":
        title = search_title()
        found_notes = find_note(notes, title)
        if found_notes is None:
            print(f"{title} was not found.")
        else:
            new_content = input("Content: ").strip()
            update = update_note(notes, title, new_content)
            print(f"{title} was updated.")

    elif choice == "5":
        break

# 예전에 함수 동작을 하나씩 확인해보던 테스트 코드 (레슨 5). 지금은 메뉴로 대체됐다.
# print(notes)
# print(find_note(notes, "6"))
# print(delete_note(notes, "6"))

# json.dump: 메뉴에서 어떤 작업을 했든, 종료할 때 최종 notes 상태를 한 번에 저장한다.
with open("notes.json", "w") as f:
    json.dump(notes, f)
