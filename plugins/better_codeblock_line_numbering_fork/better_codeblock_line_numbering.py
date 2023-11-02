import re

from pelican import signals  # For making this plugin work with Pelican.


def add_line_wrappers(content: str) -> str:
    """
    A function to read through each page and post as it comes through
    from Pelican to find all instances of triple-backtick (```...```) code
    blocks and add an html line wrapper to each line of each of those code
    blocks.

    <div class="highlight">
        <pre>
            <span></span>
            <code>
                codeline1
                codeline2
                codeline3
            </code>
        </pre>
    </div>
    """

    pre_list = re.findall("<pre>.*?</pre>", content, re.DOTALL)

    if not pre_list:
        return content

    for pre in pre_list:
        pre_section = ["<pre>", "<code>"]
        code = re.findall(
            "<pre>\n?<span></span>\n?<code>(?P<code>.*?)</code>\n?</pre>",
            pre,
            re.DOTALL,
        )
        if len(code) != 1:
            continue

        lines = code[0].split("\n")
        if not lines:
            continue

        # Remove first empty code line.
        if len(lines) >= 1 and not lines[0]:
            del lines[0]
        # Remove last empty code line.
        if len(lines) >= 1 and not lines[-1]:
            del lines[-1]

        for line in lines:
            pre_section.append(f'<span class="code-line">{line}</span>')

        pre_section.extend(["</code>", "</pre>"])
        content = content.replace(pre, "\n".join(pre_section))

    return content


def main(input) -> None:
    if input._content:
        input._content = add_line_wrappers(input._content)
    else:
        # Exit the function, essentially passing over the (non-text) file.
        return


def register():
    signals.content_object_init.connect(main)
