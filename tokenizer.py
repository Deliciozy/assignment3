# Tokenizer Game

vocab = {
    "root": [
        "cmd", "the", "a", "an", "i", "you", "we", "they", "it", "is", "are", "was", "were",
        "be", "have", "has", "do", "did", "not", "no", "go", "play", "read", "write", "un",
        "re", "in", "dis", "like", "love", "book", "game", "learn", "machine", "token",
        "data", "model"
    ],
    "cont": [
        "##s", "##es", "##ed", "##ing", "##er", "##ers", "##able", "##ment", "##tion", "##al",
        "##ly", "##ize", "##ized", "##ization", "##less", "##ful", "##read"
    ]
}

def tokenize(text):
    text = text.lower()
    import re
    words = re.findall(r"[a-z]+|[.,!?();:→]", text)
    tokens = []

    for word in words:
        if not word.isalpha():
            tokens.append(word)
            continue

        i = 0
        pieces = []
        while i < len(word):
            matched = False
            for j in range(len(word), i, -1):
                sub = word[i:j]
                vocab_list = vocab["root"] if i == 0 else vocab["cont"]
                if sub in vocab_list or ("##" + sub in vocab_list):
                    piece = sub if i == 0 else "##" + sub
                    pieces.append(piece)
                    i = j
                    matched = True
                    break
            if not matched:
                pieces = ["[UNK]"]
                break
        tokens.extend(pieces)
    return " ".join(tokens)

print(tokenize("Rewriting tokens → tokenization is fun."))
