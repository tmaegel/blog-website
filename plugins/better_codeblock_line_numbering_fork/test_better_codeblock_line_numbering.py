import pytest
from better_codeblock_line_numbering_fork import add_line_wrappers


@pytest.mark.parametrize(
    "input, output",
    [
        (
            ("<pre>\n" "<span></span>\n" "<code>\n" "echo\n" "</code>\n" "</pre>"),
            (
                "<pre>\n"
                "<code>\n"
                '<span class="code-line">echo</span>\n'
                "</code>\n"
                "</pre>"
            ),
        ),
        (
            ("<pre>\n" "<span></span><code>\n" "echo\n" "</code>\n" "</pre>"),
            (
                "<pre>\n"
                "<code>\n"
                '<span class="code-line">echo</span>\n'
                "</code>\n"
                "</pre>"
            ),
        ),
        (
            ("<pre><span></span><code>\n" "echo\n" "</code></pre>"),
            (
                "<pre>\n"
                "<code>\n"
                '<span class="code-line">echo</span>\n'
                "</code>\n"
                "</pre>"
            ),
        ),
        (
            ("<pre><span></span><code>echo</code></pre>"),
            (
                "<pre>\n"
                "<code>\n"
                '<span class="code-line">echo</span>\n'
                "</code>\n"
                "</pre>"
            ),
        ),
        (
            ("<pre><span></span><code>echo\n\necho</code></pre>"),
            (
                "<pre>\n"
                "<code>\n"
                '<span class="code-line">echo</span>\n'
                '<span class="code-line"></span>\n'
                '<span class="code-line">echo</span>\n'
                "</code>\n"
                "</pre>"
            ),
        ),
        (
            ("<pre><span></span><code>\n\necho\n\n</code></pre>"),
            (
                "<pre>\n"
                "<code>\n"
                '<span class="code-line"></span>\n'
                '<span class="code-line">echo</span>\n'
                '<span class="code-line"></span>\n'
                "</code>\n"
                "</pre>"
            ),
        ),
    ],
)
def test_add_line_wrappers(input, output):
    result = add_line_wrappers(input)
    assert result == output
