
def summarize_text_file(filename):
    with open (filename, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        words = content.split()
        characters = list(content.replace('\n', ''))
        return len(lines), len(words), len(characters)
    
filename = r"C:\Users\username\OneDrive\Desktop\DEProjects\requirements.txt"    

num_lines, num_words, num_characters = summarize_text_file(filename)

print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters (excluding newlines): {num_characters}")