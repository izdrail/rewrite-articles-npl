from text_rewrite import TextRewrite


text = "The Scottish government is in line for a windfall of almost £700m after the largest ever auction of the countrys seabed plots attracted bids from big oil and renewable energy companies"

new_sentence = TextRewrite(text).work() 

print(new_sentence)
