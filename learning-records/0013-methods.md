# 0013 — 클래스 메서드 (preview, rename)

## 무엇을 했나
`class_practice.py`의 `Note` 클래스에 메서드 두 개를 추가했다.

```python
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def preview(self):
        return self.title[:10] + ":" + self.content[:10]

    def rename(self, new_title):
        self.title = new_title

n1 = Note("장보기", "우유, 계란")
n1.rename("New Title_123456678")
print(n1.title)      # "New Title_123456678"
print(n1.preview())  # "New Title_:우유, 계란"
```

## 겪은 실수와 fix
- `rename()` 호출 후에도 아래 `print(n1.title)` 옆에 남아있던 `# "장보기"` 주석이 실제 값과 안 맞는 걸 스스로 짚어내지 못하고
  넘어갈 뻔했다 — 리팩터링/코드 변경 시 옆에 있는 설명 주석이 낡을 수 있다는 걸 짚어줌 (코드가 하는 일을 설명하는 주석은
  코드가 바뀌면 같이 낡는다는 레슨 12 이후 첫 실전 사례).
- `preview()`를 정의만 하고 처음엔 호출하지 않았다 — "정의했다"와 "작동을 확인했다"는 다르다는 걸 재확인.

## 확인한 개념
- 메서드는 클래스 안에 정의된 함수이고, 첫 매개변수는 항상 `self`
- `n.preview()`라고 부르면 파이썬이 자동으로 `Note.preview(n)`으로 바꿔 실행 — `self`를 직접 넘기지 않아도 되는 이유를
  **자기 말로 정확히 설명함** ("n.preview()라고 쓰면 파이썬이 자동으로 Note.preview(n1)로 바꿔 불러줘서")
- `self` 뒤에 매개변수를 더 받을 수 있다 (`rename(self, new_title)`)

## Implications
- 클래스 기본기(속성 + 메서드) 완료 — `__init__`, `self`, 점 표기법, 메서드 정의/호출까지 자기 말로 설명 가능한 수준
- 다음 후보: `notes_app.py`를 딕셔너리 대신 `Note` 클래스로 리팩터링 (메서드까지 배웠으니 이제 현실적인 크기의 작업) /
  고유 ID 부여 / 가상환경 & pip (원본 미션의 다음 큰 영역)
