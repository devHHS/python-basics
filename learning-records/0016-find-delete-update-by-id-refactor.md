# 0016 — find/delete/update를 title에서 id 기준으로 리팩터링

## 무엇을 했나
`notes.py`/`notes_app.py`의 검색·수정·삭제를 title 대신 id 기준으로 바꿨다. 레슨 14에서
"찾아보기(browse)"와 "정확히 하나를 지정해야 하는 작업"을 스스로 구분해냄 — title은 훑어보는 용도(2번
메뉴)로 남기고, update(3번)·delete(4번)는 id로 바꿔야 한다고 먼저 판단한 뒤 구현에 들어갔다. 2번(Find)도
`enumerate`로 임의 번호를 매기던 것 대신 노트의 실제 `id`를 보여주자는 아이디어를 스스로 냈다.

## 겪은 실수와 fix
1. `find_note`를 본떠 `find_note_by_id`를 만들 때는 정확했지만, 화면 출력 코드에서
   `f"n{id}"`처럼 파이썬 내장 함수 `id()`를 그대로 참조하는 실수가 있었다 — `n['id']`로 고쳐야 한다는
   걸 "이게 왜 저렇게 나오지?" 질문으로 스스로 알아챔.
2. 4번(Update)에서 `id = find_note_by_id(...)`로 **dict**를 받아놓고 그 변수를 그대로
   `update_note(notes, id, ...)`에 다시 넘기는 버그가 있었다 — `update_note` 내부에서 다시
   `find_note_by_id(notes, id)`를 호출하니 `n["id"] == {dict}` 비교가 항상 거짓이 되어 조용히
   실패했다(에러 없이 "updated" 메시지만 거짓으로 뜸). "정수를 담을 변수와 dict를 담을 변수를
   분리한다"(`id`/`found_note`)는 방법으로 스스로 고쳤다.
3. 2번(Find by title) 리팩터링 중 `find_all_by_title`이 **list**를 반환한다는 걸 깜빡하고
   `found_note['id']`로 바로 인덱싱해서 `TypeError: list indices must be integers or slices, not str`을
   만남 — 에러 메시지에서 "list인데 str로 인덱싱하려 했다"는 걸 스스로 읽어내고, 이미 다른 분기에 있던
   `for n in found_notes:` 패턴을 가져와 고쳤다.

## 확인한 개념
- **id vs title의 용도 분리**: 여러 개가 겹칠 수 있는 title은 훑어보기용, 겹치지 않는 id는 "정확히
  하나를 골라야 하는" 연산(update/delete)용이라는 걸 힌트 없이 스스로 설계 판단으로 내림.
- 함수가 뭘 반환하는지(단일 dict vs list vs None)를 변수명·다음 줄 코드보다 **함수 정의를 직접 다시
  확인**해서 판단하는 습관이 자리잡음 — 세 버그 모두 "이 함수가 뭘 리턴하더라?"로 스스로 되짚어 해결.

## Implications
- title 중복 문제(레슨 9~10)와 그 임시방편(`find_all_by_title` + 번호 선택)이 이제 완전히 걷어짐 —
  id 도입(레슨 13)의 목적이 실제로 코드에 반영됨.
- "변수 하나에 dict를 넣어놓고 다른 함수에 int 자리로 잘못 넘기는" 유형의 버그를 최소 2번(2번째 실수)
  겪었으니, 이후 함수 시그니처를 다룰 때 "이 매개변수가 정확히 뭘 기대하는지" 되짚는 질문을 계속
  던지면 좋겠다.
- 다음 세션 후보: pytest로 `notes.py`의 함수들(`find_note_by_id`, `update_note`, `next_id` 등)에
  대한 테스트 짜보기 — 리팩터링하며 겪은 회귀(regression) 버그들을 테스트로 미리 잡는 경험과 연결하기
  좋은 타이밍.
