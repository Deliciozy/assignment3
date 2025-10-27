## Toy Tokenizer Instruction

I stored the vocabulary as a Python list because the order of items is preserved, which is helpful for greedy longest-match searches. Lists are easy to iterate over and check membership when trying to match subwords in a word. This makes implementing the WordPiece-style tokenizer straightforward.
