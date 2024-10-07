def words_count(name):
    try:
        with open(name,'r', encoding='UTF-8') as file:
            text=file.read()
            words=text.split()
            return len(words)
    except FileNotFoundError:
        return "Такой файл не существует"
name= "text.txt"
count=words_count(name)
print(f"Количество слов в файле {name}:{count}")
