from re import sub, MULTILINE
from os import path

try:
    from markdown2 import markdown
    MARKDOWN_LIBRARY = 'markdown2'
except ImportError:
    try:
        from markdown import markdown
        MARKDOWN_LIBRARY = 'markdown'
    except ImportError:
        raise ImportError(
            "No Markdown library available. \
            Please install either markdown or markdown2."
            )

##————————————————————————————————————————————————————————————————————————————##

def md_to_html(md_data:str) : # -> markdown2.UnicodeWithAttrs : 
    if MARKDOWN_LIBRARY == 'markdown2':
        html_data = markdown(md_data, extras=[
            'tables', 'footnotes', 'fenced-code-blocks', 'break-on-newline', 
            'mdx_math', 'code-friendly'
            ])
    else:
        html_data = markdown(md_data, extensions=[
            'tables', 'footnotes', 'fenced_code', 'breaks', 'mdx_math', 
            'code-friendly'
            ])

    return html_data

##————————————————————————————————————————————————————————————————————————————##

def convert_https_links(text:str) -> str:
    pattern = r'(?<!\]\()' + r'http(s)?://[^\s]+'

    # text_with_links = sub(pattern, r'[\1](\1)', text, flags=MULTILINE)

    def escape_underscores(match):
        url = match.group(0)
        escaped_url = url.replace('_', r'\_')
        return f'[{escaped_url}]({escaped_url})'

    text_with_links = sub(pattern, escape_underscores, text, flags=MULTILINE)

    return text_with_links



def convert_strikethrough_text(text:str) -> str:
    pattern = r'~~(.*?)~~'
    result = sub(pattern, r'<s>\1</s>', text)
    return result



def convert_highlighted_text(text:str) -> str:
    pattern = r'==(.*?)=='
    result = sub(pattern, r'<mark>\1</mark>', text)
    return result


