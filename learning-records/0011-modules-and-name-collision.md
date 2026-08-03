# 0011 — 모듈 분리(import)와 이름 충돌

## 무엇을 했나
`notes_app.py`에 있던 노트 관련 함수들(`add_note`, `find_note`, `find_all_by_title`,
`update_note`, `delete_note`, `search_title`)을 `notes.py`로 분리하고, `notes_app.py`에서
import해서 쓰도록 바꿨다.

## 겪은 에러와 원인
`import notes` 방식(모듈 전체를 가져와 `notes.함수이름()`으로 호출)을 먼저 시도했는데,
`AttributeError: 'list' object has no attribute 'add_note'`가 발생했다.

원인: 노트를 담는 리스트 변수 이름도 `notes`였다. `notes = []` (또는 `notes = json.load(f)`)가
실행되는 순간, import로 가져온 모듈 참조가 리스트 값으로 덮어써졌다. 그 뒤로 `notes.add_note(...)`는
"리스트 객체에 add_note 메서드를 찾는" 시도가 되어 실패했다.

## 해결
`from notes import add_note, find_note, find_all_by_title, update_note, delete_note, search_title`로
바꿔서, 모듈 이름(`notes`) 자체를 코드에 등장시키지 않고 함수 이름만 가져왔다. 이후 함수 호출도
`notes.add_note(...)` → `add_note(...)` 형태로 되돌렸다. `notes.remove(...)`, `notes.clear()`는
리스트 메서드이므로 그대로 두었다 — 이름은 같아 보여도 하나는 모듈 접근, 하나는 리스트 메서드 호출이라는
점을 구분해야 했다.

## 왜 중요한가
모듈 이름과 변수 이름이 겹치면 이름이 덮어써질 수 있다는 걸 실제 에러로 겪었다. 실무에서도 흔한
함정이라, "이 함수/변수 이름이 다른 모듈 이름과 겹치지 않는가"를 신경 쓰는 습관이 여기서부터 시작된다.

## Implications
- 모듈-변수 이름 충돌 개념을 스스로 설명할 수 있음 (다음 세션에 재확인 불필요, 다만 새 모듈 만들 때 상기시켜줄 것)
- 다음 후보: 고유 ID 부여, 부분 문자열 검색, 클래스 도입 — 사용자가 준비됐다고 할 때 진행 (지난 세션 페이싱 체크 참고)
