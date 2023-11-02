AUTHOR = "Toni Mägel"
SITENAME = "tonimaegel.de"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "de"

# Uncomment following line if you want document-relative URLs when developing
# Can be useful in development, but set to False when you're ready to publish
# RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("github", "https://github.com/tmaegel/"),
    ("linkedin", "https://de.linkedin.com/in/toni-maegel"),
    ("envelope-fill", "mailto:tmaegel@posteo.de"),
)

GITHUB_URL = "https://github.com/tmaegel/"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
    ("Posts", "/index.html"),
    ("Themen", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 10

PLUGIN_PATH = ["plugins"]
PLUGINS = ["better_codeblock_line_numbering_fork"]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "linenums": False,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

THEME = "themes/custom"
