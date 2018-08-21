lines = ["we'll find a way we always have - Interstellar\n",
         "I'll find you and I'll kill you - Taken\n",
         "I'll be back - Terminator 2\n",
         "신과함께"]

with open('movie.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)
