# Задан словарь, его значения необходимо внести по соответствующим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wis    is enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""

new_lines = []
for line in template.splitlines(keepends=True):
    if '?' in line:
        for key, value in page.items():
            if key in line:
                line = line.replace('?', value)
                break
    new_lines.append(line)


fd = open('index.html', 'w+', encoding='utf-8')
fd.writelines(new_lines)
fd.close()
