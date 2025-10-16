letter = '''
             Dear  <|Name|> ,
             You Are Selected
             <|Date|>'''

print(letter.replace("<|Name|>", "Arush").replace("<|Date|>" , " 25 July 2007 "))
