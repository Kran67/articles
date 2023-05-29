import json

print('Compiling Shortcuts to Markdown Article ...')

shortcutData = json.load(open('shortcuts.json', 'r'))

result = """---
name: 'Keyboard Shortcuts'
slug: 'keyboard-shortcuts'
description: 'A list of Shortcuts I use in my daily life, feel free to skim through it and maybe learn about new things in your favourite applications.'
tag: 'shortcuts'
category: 'general'
status: 'publish'
---

This is a list of many Shortcuts I encountered / Use now in my daily life. I will try to keep this list up to date. If you have any suggestions, please let me know by opening an [issue](https://github.com/Maximinodotpy/articles/issues) on Github.


**Applications / Places**\n
"""


for slug in shortcutData:
    name = shortcutData[slug]['name']
    result += f'- [{name}](#content-{slug})\n'

result += "\n\n"

for slug in shortcutData:
    application = shortcutData[slug]

    result += f"## {application['name']}\n\n"
    result += f"{application['description']}\n\n"

    result += f"| Shortcut | Description |\n"
    result += f"| --- | --- |\n"
    for shortcut in application['shortcuts']:
        result += f"| `{shortcut['keys']}` | {shortcut['description']} |\n"

    result += f'\n[Edit this Article in the Repository](https://github.com/Maximinodotpy/articles/tree/main/039%20-%20Keyboard%20Shortcuts)\n'

    result += "\n\n"

with open('_blog/article.md', 'w') as f:
    f.write(result)