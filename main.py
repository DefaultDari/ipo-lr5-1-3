filename = open("text.txt",'r', encoding="utf-8") #Открытие файла в режиме чтения
text= filename.read() #Чтение содержимого файла
print(text) #Вывод самого текста
word_count = len(text.split()) #Подсчет количества слов
print(f"Количество слов в файле : {word_count}") #Вывод кол-ва слов
filename.close() #Закрытие файла
