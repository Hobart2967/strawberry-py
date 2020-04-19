def to_snake_case(name) -> str:
  result = ''
  begin = True
  lastUppercase = False
  for i in range(0, len(name)):
    ch = name[i]
    if ch.isupper():
      if begin:
        result = result + ch
      else:
        if lastUppercase:
          if (i + 1) < len(name):
            next = name[i + 1]
            if next.isupper():
              result = result + ch
            else:
              result = result + '_' + ch
          else:
            result = result + ch
        else:
          result = result + '_' + ch
      lastUppercase = True
    else:
      result = result + ch.upper()
      lastUppercase = False
    begin = False
  return result.lower()