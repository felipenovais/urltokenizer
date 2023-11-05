import re
import argparse

def extract_tokens(urls_file, pattern):
    tokens = set()

    with open(urls_file, 'r') as file:
        urls = file.readlines()

    for url in urls:
        matches = re.findall(pattern, url)
        tokens.update(matches)

    return list(tokens)

def main():
    parser = argparse.ArgumentParser(description='Extract tokens from a file of URLs.')
    parser.add_argument('urls_file', help='Path to the file containing URLs')
    parser.add_argument('--pattern', default=r'\/(\w+)\/', help='Regular expression pattern to extract tokens')
    parser.add_argument('--output', '-o', default=None, help='Path to the output file to save tokens')

    args = parser.parse_args()
    urls_file = args.urls_file
    pattern = args.pattern

    extracted_tokens = extract_tokens(urls_file, pattern)

    if args.output:
        with open(args.output, 'w') as output_file:
            for token in extracted_tokens:
                output_file.write(token + '\n')
        print(f'Tokens have been saved to {args.output}')
    print("Extracted tokens:")  # Print the extracted tokens to the console
    for token in extracted_tokens:
        print(token)  # Print each token in the list line by line

if __name__ == '__main__':
    main()

