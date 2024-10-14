def count_words_in_file(filename): # Определение функции , которая принимает один аргумент
    try: 
        with open(filename, 'r') as file: #Попытка выполнить следующие инструкции, если файл существует
            text = file.read() # Считывание содержимого файла
            words = text.split()  # Разделение текста на отдельные слова, используя пробелы и знаки табуляции
            return len(words) #Подсчет количества элементов (слов)
    except FileNotFoundError: # Если файл не найден, то будет вызвано это исключение
        print("Файл не найден.") # Вывод сообщения о том, что файл не найден
        return None  # Возврат значения None, чтобы показать, что файл не был найден
filename = 'C:\\Users\\agjjj\Desktop\\text.txt' # Указание пути к файлу, который нужно прочитать
word_count = count_words_in_file(filename) # Вызов функции и сохранение результата в word_count
if word_count is not None: # Проверка, найден ли файл
    print(f"Количество слов в файле '{filename}': {word_count}") # Вывод количества слов в файле
