import unittest
from markdown_htmlnode import markdown_to_html_node

class TestMarkdownHTMLNode(unittest.TestCase):
    
    def test_markdown_html_node_code(self):
        md = """```
A code snippet
```
"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html_code,
"""<div><pre><code>
A code snippet
</code></pre></div>"""
        )

    def test_markdown_html_node_code_inline_elements(self):
        md = """```
A code snippet with <b>inline</b>
```
"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html_code,
"""<div><pre><code>
A code snippet with <b>inline</b>
</code></pre></div>""")
            
    def test_markdown_html_node_heading(self):
        md = """# Level 1 heading"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><h1>Level 1 heading</h1></div>""")

        md = """## Level 2 heading"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><h2>Level 2 heading</h2></div>""")

        md = """### Level 3 heading"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><h3>Level 3 heading</h3></div>""")

        md = """#### Level 4 heading"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><h4>Level 4 heading</h4></div>""")

        md = """##### Level 5 heading"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><h5>Level 5 heading</h5></div>""")

        md = """###### Level 6 heading"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><h6>Level 6 heading</h6></div>""")

    def test_markdown_html_node_quote(self):
        md = """> A simple quote"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,"""<div><blockquote>A simple quote</blockquote></div>""")
    
    def test_markdown_html_node_ul(self):
        md = """- First element
- Second element
- Third element"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,
"""<div><ul><li>First element</li><li>Second element</li><li>Third element</li></ul></div>""")
    
    def test_markdown_html_node_ol(self):
        md = """1. First element
2. Second element
3. Third element"""
        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(html_code,
"""<div><ol><li>First element</li><li>Second element</li><li>Third element</li></ol></div>""")
        
    def test_markdown_html_node_lists_combined(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        html_code = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html_code,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_markdown_html_node_paragraph(self):
            md = """A simple paragraph"""
            html_code = markdown_to_html_node(md).to_html()
            self.assertEqual(html_code,"""<div><p>A simple paragraph</p></div>""")

    def test_markdown_html_node_paragraphs(self):
            md = """# The begining

In the beginning there were the begning

It is _the_ **beginning** ok?

## THE END"""
            html_code = markdown_to_html_node(md).to_html()
            self.assertEqual(html_code,
"""<div><h1>The begining</h1><p>In the beginning there were the begning</p><p>It is <i>the</i> <b>beginning</b> ok?</p><h2>THE END</h2></div>""")

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )