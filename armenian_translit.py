import sys

# Define transliteration map
translit_map = {
    'Ա': 'A', 'Բ': 'B', 'Գ': 'G', 'Դ': 'D', 'Ե': 'E', 'Զ': 'Z', 'Է': 'E', 'Ը': 'Y', 'Թ': 'T',
    'Ժ': 'Zh', 'Ի': 'I', 'Լ': 'L', 'Խ': 'X', 'Ծ': 'Ts', 'Կ': 'K', 'Հ': 'H', 'Ձ': 'Dz', 'Ղ': 'Gh',
    'Ճ': 'Ch', 'Մ': 'M', 'Յ': 'Y', 'Ն': 'N', 'Շ': 'Sh', 'Ո': 'Vo', 'Չ': 'Ch', 'Պ': 'P', 'Ջ': 'J',
    'Ռ': 'R', 'Ս': 'S', 'Վ': 'V', 'Տ': 'T', 'Ր': 'R', 'Ց': 'Ts', 'ՈՒ': 'U', 'Փ': 'P', 'Ք': 'K',
    'ԵՒ': 'Ev', 'Օ': 'O', 'Ֆ': 'F', 'ա': 'a', 'բ': 'b', 'գ': 'g', 'դ': 'd', 'ե': 'e', 'զ': 'z',
    'է': 'e', 'ը': 'y', 'թ': 't', 'ժ': 'zh', 'ի': 'i', 'լ': 'l', 'խ': 'x', 'ծ': 'ts', 'կ': 'k',
    'հ': 'h', 'ձ': 'dz', 'ղ': 'gh', 'ճ': 'ch', 'մ': 'm', 'յ': 'y', 'ն': 'n', 'շ': 'sh', 'ո': 'vo',
    'չ': 'ch', 'պ': 'p', 'ջ': 'j', 'ռ': 'r', 'ս': 's', 'վ': 'v', 'տ': 't', 'ր': 'r', 'ց': 'ts',
    'ու': 'u', 'փ': 'p', 'ք': 'k', 'եւ': 'ev', 'օ': 'o', 'ֆ': 'f'
}

def transliterate_word(word):
    result = []
    for i, char in enumerate(word):
        if char in ('Ո', 'ո'):
            if i == 0:
                result.append('Vo' if char == 'Ո' else 'vo')
            else:
                result.append('O' if char == 'Ո' else 'o')
        else:
            result.append(translit_map.get(char, char))
    return ''.join(result)

def transliterate(text):
    lines = text.split('\n')
    transliterated_lines = [' '.join([transliterate_word(word) for word in line.split()]) for line in lines]
    return '\n'.join(transliterated_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt [output.txt]")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    if len(sys.argv) == 3:
        output_filename = sys.argv[2]
    else:
        output_filename = "translit_" + input_filename
    
    with open(input_filename, 'r', encoding='utf-8') as infile:
        text = infile.read()
    
    transliterated_text = transliterate(text)
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(transliterated_text)
    
    print(f"Transliteration complete. Output saved to {output_filename}")
