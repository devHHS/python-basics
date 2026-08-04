class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

n1 = Note("장보기", "우유, 계란")
print(n1.title)    # "장보기"
print(n1.content)  # "우유, 계란"

n2 = Note("자전거", "로드, MTB")
print(n2.title)    # "자전거"
print(n2.content)  # "로드, MTB"
n1.content = "Quark, Tomaten"

print(n1.content)