AUTHOR = "Toni Mägel"
SITENAME = "tonimaegel.de"
SITEURL = "https://tmaegel.github.io/blog-website/"

PATH = "content"

ARTICLE_ORDER_BY = "date"
PAGE_ORDER_BY = "reversed-basename"

TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"

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
SOCIAL = (("github", "https://github.com/tmaegel/"),)

GITHUB_URL = "https://github.com/tmaegel/"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
    ("Posts", "/index.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 2

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
