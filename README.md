# URL Token Extractor

This Python script extracts tokens from a file of URLs. Tokens can be essential for content discovery when you decide to generate your own wordlist (which is, most of the time, more effective, btw).

## Usage

1. **Obtain a File with URLs**

- Open Burp Suite.
- Navigate to the "Target" tab and select the host you want to investigate.
- Access the "Site map" tab.
- Right-click on the chosen host and select "Copy URLs in this host."

2. **Run the Script**

   ```bash
   python extract_tokens.py file_with_urls.txt
   ```

   - Replace `file_with_urls.txt` with your URL file.
   - The default pattern extracts tokens from paths.

3. **Save Extracted Tokens to a File (Optional)**

   To save tokens to a file, use the `-o` or `--output` option:

   ```bash
   python extract_tokens.py file_with_urls.txt --output output.txt
   ```

## Example

Extract tokens from `example_urls.txt` and save them to `tokens.txt`:

```bash
python extract_tokens.py example_urls.txt --output tokens.txt
```

For basic extraction without saving:

```bash
python extract_tokens.py example_urls.txt
```

## License

This script is provided under the BSD-3 License. Feel free to use, modify, and distribute it.

