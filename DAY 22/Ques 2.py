def word_analysis(s):
        words      = s.split()
            word_count = len(words)
                char_count = sum(1 for _ in s)
                    char_no_sp = sum(1 for c in s if c != ' ')
                        sentences  = s.count('.') + s.count('!') + s.count('?')
                            unique     = len(set(w.lower() for w in words))
                                longest    = max(words, key=len) if words else ""
                                    shortest   = min(words, key=len) if words else ""
                                        avg_len    = (round(sum(len(w) for w in words)
                                                          / word_count, 2) if word_count else 0)

                                                              return {
                                                                      "words"      : words,
                                                                              "word_count" : word_count,
                                                                                      "char_count" : char_count,
                                                                                              "char_no_sp" : char_no_sp,
                                                                                                      "sentences"  : sentences,
                                                                                                              "unique"     : unique,
                                                                                                                      "longest"    : longest,
                                                                                                                              "shortest"   : shortest,
                                                                                                                                      "avg_len"    : avg_len
                                                                                                                                          }

                                                                                                                                          s = input("Enter a sentence: ")
                                                                                                                                          r = word_analysis(s)

                                                                                                                                          print(f"\n{'─'*45}")
                                                                                                                                          print(f"  Sentence      : '{s}'")
                                                                                                                                          print(f"  Words         : {r['words']}")
                                                                                                                                          print(f"  Word Count    : {r['word_count']}")
                                                                                                                                          print(f"  Unique Words  : {r['unique']}")
                                                                                                                                          print(f"  Char Count    : {r['char_count']}")
                                                                                                                                          print(f"  Chars (no sp) : {r['char_no_sp']}")
                                                                                                                                          print(f"  Longest Word  : '{r['longest']}'")
                                                                                                                                          print(f"  Shortest Word : '{r['shortest']}'")
                                                                                                                                          print(f"  Avg Word Len  : {r['avg_len']}")
                                                                                                                                          print(f"  Sentences     : {r['sentences']}")
                                                                                                                                          print(f"{'─'*45}")