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

def find_all_by_title(notes, title):
    found_notes = []
    for n in notes:
        if n["title"] == title:
            found_notes.append(n)
    return found_notes

def update_note(notes, title, new_content):
    n = find_note(notes, title)
    if n is None:
        return None
    else:    
        n["content"] = new_content
        return n

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
    return input("Title to search: ").strip()