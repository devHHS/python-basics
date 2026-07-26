# enumerate/find/delete + 타입 불일치(str vs int) 체감

`find_note`, `delete_note` 함수를 직접 정의해 테스트했다. 처음 `find_note(notes, 6)`(정수)로 호출했다가 `None`이 나온 걸 보고,
`input()`은 항상 문자열을 돌려준다는 걸 스스로 연결해 `find_note(notes, "6")`으로 고쳐서 정상 동작을 확인했다.
`delete_note`가 동일 제목이 여러 개일 때 첫 번째 것만 지운다는 점(early return 때문)도 실제 테스트로 관찰했다.
이후 `json.dump`가 `delete_note` 호출 *전에* 실행되고 있어서 삭제가 파일에 반영 안 된다는 걸 스스로 짚어내고,
`json.dump`를 모든 연산(add/find/delete) 이후로 옮겨서 해결했다.

**Implications**: 타입 불일치 버그(str vs int)를 실전에서 스스로 진단할 수 있음. "연산 순서 → 저장 시점"의 감각도
레슨 2에 이어 두 번째로 스스로 짚어낸 것이라 이제 안정적인 습관으로 봐도 될 듯. 다음 레슨은 지금까지 만든
add/find/delete/load/save를 하나의 반복 메뉴(while True + 사용자 선택)로 묶는 것이 자연스러운 다음 단계.
