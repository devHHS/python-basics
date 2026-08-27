# 0020 — 나머지 함수 테스트 추가 (add_note, update_note, find_all_by_title, find_all_notes)

## 무엇을 했나
레슨 16/18(pytest, fixture)에서 배운 패턴을 그대로 적용해, `notes.py`의 나머지 함수
(`add_note`, `update_note`, `find_all_by_title`, `find_all_notes`)에 대한 테스트를
거의 힌트 없이 스스로 작성했다. 최종적으로 `test_notes.py`에 테스트 12개, 전부 통과.

## 겪은 실수와 fix
- 없음 — 이번 세션은 큰 걸림 없이 매끄럽게 진행됨. fixture 재사용, `assert` 여러 개 쓰기,
  존재/미존재 두 경로 나눠 테스트하기 모두 스스로 적용함.
- 한 가지 정리할 거리: `test_update_note`와 `test_update_note_existing`을 중복으로 짰다가,
  기존 네이밍 규칙(`함수명_상황`: `test_find_note_by_id_existing`/`_not_found`)과 비교해보라는
  질문에 스스로 `test_update_note_existing`을 남기고 중복을 지움.

## 확인한 개념
- **`is`로 mutation 확인**: `add_note`가 새 리스트를 만드는 게 아니라 기존 리스트를 직접
  수정(`append`)한다는 걸, `assert updated_notes is sample_notes`(`==`이 아니라 `is`)로
  검증. `==`은 값 비교, `is`는 객체(메모리 주소) 비교라는 차이를 정확히 자기 말로 설명함.
- **테스트 네이밍 컨벤션**: 여러 테스트가 쌓이면서 자연스럽게 `함수명_상황` 패턴이 자리잡았고,
  본인이 이 패턴을 인식하고 새 테스트에도 일관되게 적용함.
- `find_all_notes`는 스스로 시나리오를 3개(기본/빈 리스트/여러 개)로 나눠 테스트 — 요구한
  것보다 더 꼼꼼하게 커버함.

## Implications
- `notes.py`의 모든 함수가 테스트로 커버됨 (`search_title`은 `input()` 기반이라 의도적으로
  제외 — mocking은 미션 범위 밖).
- 이번 세션은 새 개념 없이 기존 pytest/fixture 스킬의 반복 인출(retrieval practice)이었고,
  매끄럽게 통과한 걸 보면 storage strength가 잘 붙은 걸로 판단됨. 새 lesson HTML은 만들지 않음
  (0016/0018과 동일 개념의 연습이라 별도 레슨보다 이 기록으로 충분).
- 다음 세션 후보: (1) Git 자체를 다루는 레슨(로그/diff/브랜치 등 — 지금까지는 커밋 습관만
  형성됐고 개념 레슨은 없었음), (2) 0019에서 나온 Pydantic 맛보기(선택), (3) SE 관점에서
  "함수를 작게 쪼개는 이유"를 `notes.py` 코드로 직접 다루는 레슨(미션표에 있으나 아직
  전용 레슨 없음).
