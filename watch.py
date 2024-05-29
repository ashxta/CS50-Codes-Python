import re
import sys

def main():
    html = input("HTML: ")
    result = parse(html)
    if result:
        print(result)
    else:
        print("No YouTube URL found.")

def parse(s):
    iframe_pattern = r'<iframe.*?src="(http|https)://(www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)"'

    match = re.search(iframe_pattern, s)

    if match:

        video_code = match.group(3)
        youtu_be_url = f'https://youtu.be/{video_code}'
        return youtu_be_url
    else:
        return None

if __name__ == "__main__":
    main()
