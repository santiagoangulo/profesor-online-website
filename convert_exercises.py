#!/usr/bin/env python3
import re
import os
import markdown
from pathlib import Path

TEMPLATE_PATH = "/Users/santi/workspace/personal/profesor-online-website/material-didactico/en/exercises-ch01-02.html"
OUTPUT_DIR = "/Users/santi/workspace/personal/profesor-online-website/material-didactico/en"

CONVERSIONS = [
    {
        "md": "/Users/santi/workspace/personal/profesor-online-website/material_didactico/en/exercises-ch03-04.md",
        "html": "exercises-ch03-04.html",
        "title": "Exercises: Chapters 3-4 — Systems of Linear Equations and Vectors",
        "description": "Step-by-step solved exercises on Systems of Linear Equations and Vectors in Space. Includes basic, intermediate, EVAU level problems and multiple choice tests."
    },
    {
        "md": "/Users/santi/workspace/personal/profesor-online-website/material_didactico/en/exercises-ch05.md",
        "html": "exercises-ch05.html",
        "title": "Exercises: Chapter 5 — Analytic Geometry in Space",
        "description": "Step-by-step solved exercises on Analytic Geometry in Space. Includes basic, intermediate, EVAU level problems and multiple choice tests."
    },
    {
        "md": "/Users/santi/workspace/personal/profesor-online-website/material_didactico/en/exercises-ch06-07.md",
        "html": "exercises-ch06-07.html",
        "title": "Exercises: Chapters 6-7 — Limits, Derivatives and Applications",
        "description": "Step-by-step solved exercises on Limits, Derivatives and their Applications. Includes basic, intermediate, EVAU level problems and multiple choice tests."
    },
    {
        "md": "/Users/santi/workspace/personal/profesor-online-website/material_didactico/en/exercises-ch08-09.md",
        "html": "exercises-ch08-09.html",
        "title": "Exercises: Chapters 8-9 — Functions, Integration and Applications",
        "description": "Step-by-step solved exercises on Functions, Integration and their Applications. Includes basic, intermediate, EVAU level problems and multiple choice tests."
    },
    {
        "md": "/Users/santi/workspace/personal/profesor-online-website/material_didactico/en/exercises-ch10-11.md",
        "html": "exercises-ch10-11.html",
        "title": "Exercises: Chapters 10-11 — Probability and Statistics",
        "description": "Step-by-step solved exercises on Probability and Statistics. Includes basic, intermediate, EVAU level problems and multiple choice tests."
    },
]

def find_template_positions(template):
    """Find the exact byte positions for template splitting."""
    nav_matches = list(re.finditer(r'</nav>', template))
    sec_matches = list(re.finditer(r'</section>', template))
    
    nav0_pos = nav_matches[0].start()
    sec0_pos = sec_matches[0].start()
    toc_nav_pos = nav_matches[1].start()
    content_page_end_pos = sec_matches[1].start()
    
    return nav0_pos, sec0_pos, toc_nav_pos, content_page_end_pos

def split_template(template, nav0_pos, sec0_pos, toc_nav_pos, content_page_end_pos):
    """Split template into 5 parts."""
    BEFORE = template[:nav0_pos+6]
    HEADER_OPEN = template[nav0_pos+6:sec0_pos+11]
    CONTENT_PAGE_OPEN = template[sec0_pos+11:toc_nav_pos+6]
    CONTENT = template[toc_nav_pos+6:content_page_end_pos]
    FOOTER = template[content_page_end_pos:]
    return BEFORE, HEADER_OPEN, CONTENT_PAGE_OPEN, CONTENT, FOOTER

def extract_chapters(markdown_content):
    """Extract chapter names and IDs from markdown content."""
    pattern = r'#\s*CHAPTER\s+(\d+)[\.\s]*([^#\n]+)'
    matches = re.findall(pattern, markdown_content)
    chapters = []
    for i, (num, title) in enumerate(matches, 1):
        chapter_id = f"cap{i}"
        full_title = f"Chapter {num} — {title.strip()}"
        chapters.append((chapter_id, full_title))
    return chapters

def convert_markdown(md_content):
    """Convert markdown to HTML."""
    header_pattern = r'^#\s+Mathematics[^\n]*\n+##\s+[^\n]+\n+([^\n]*\n)*?^---\s*\n'
    md_content = re.sub(header_pattern, '', md_content, flags=re.MULTILINE)
    
    chapter_pattern = r'^#\s+CHAPTER\s+\d+[\.\s]*[^\n]*\s*\n*\n*---\s*\n'
    md_content = re.sub(chapter_pattern, '', md_content, flags=re.MULTILINE)
    
    chapter_pattern2 = r'^#\s+Mathematics[^\n]*\n+'
    md_content = re.sub(chapter_pattern2, '', md_content, flags=re.MULTILINE)
    
    chapter_pattern3 = r'^##\s+[^\n]+\n+'
    md_content = re.sub(chapter_pattern3, '', md_content, flags=re.MULTILINE)
    
    md_content = re.sub(r'^##\s+(.+)$', lambda m: f'<h4>{m.group(1)}</h4>', md_content, flags=re.MULTILINE)
    
    md_content = re.sub(r'^####\s+(.+)$', lambda m: f'<h5>{m.group(1)}</h5>', md_content, flags=re.MULTILINE)
    
    html = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    
    return html

def build_toc_nav(chapters):
    """Build TOC nav HTML from chapter list."""
    toc_html = '      <nav class="toc-nav">\n'
    for chapter_id, title in chapters:
        toc_html += f'        <a href="#{chapter_id}">{title}</a>\n'
    toc_html += '      </nav>\n\n'
    return toc_html

def generate_html(title, description, before, header_open, content_page_open, md_html, footer, chapters, html_filename):
    """Build final HTML with correct structure."""
    
    title_pattern = r'<title>[^<]+</title>'
    title_replacement = f'<title>Mathematics II — {title} | Profesor Online</title>'
    before = re.sub(title_pattern, title_replacement, before)
    
    desc_pattern = r'<meta name="description" content="[^"]*"'
    desc_replacement = f'<meta name="description" content="{description}"'
    before = re.sub(desc_pattern, desc_replacement, before)
    
    canonical_pattern = r'<link rel="canonical" href="[^"]+"'
    canonical_replacement = f'<link rel="canonical" href="https://profesor-online-matematicas-ciencias.netlify.app/material-didactico/en/{html_filename}"'
    before = re.sub(canonical_pattern, canonical_replacement, before)
    
    h1_pattern = r'<h1>[^<]+</h1>'
    h1_replacement = f'<h1>{title}</h1>'
    header_open = re.sub(h1_pattern, h1_replacement, header_open)
    
    desc_pattern = r'<p>[^<]+</p>'
    header_open = re.sub(desc_pattern, f'<p>{description}</p>', header_open, count=1)
    
    toc_nav = build_toc_nav(chapters)
    content_page_open = content_page_open.replace(
        '      <nav class="toc-nav">\n        <a href="#cap1">Chapter 1: Matrices</a>\n        <a href="#cap2">Chapter 2: Determinants</a>\n      </nav>',
        toc_nav,
        1
    )
    
    final_html = before + header_open + content_page_open + md_html + footer
    return final_html

def verify_html(html_path, expected_h1):
    """Verify the generated HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    size = os.path.getsize(html_path)
    
    checks = {
        "starts with DOCTYPE": content.startswith('<!DOCTYPE html>'),
        "ends properly": content.rstrip().endswith('</body>\n</html>'),
        "contains exactly one h1": content.count('<h1>') == 1 and content.count('</h1>') == 1,
        "h1 contains correct title": expected_h1 in content,
        "contains content-page section": '<section class="content-page">' in content,
        "content-page closes properly": content.count('</section>') >= 2,
    }
    
    return size, checks

def main():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    nav0_pos, sec0_pos, toc_nav_pos, content_page_end_pos = find_template_positions(template)
    BEFORE, HEADER_OPEN, CONTENT_PAGE_OPEN, CONTENT, FOOTER = split_template(
        template, nav0_pos, sec0_pos, toc_nav_pos, content_page_end_pos
    )
    
    results = []
    
    for conv in CONVERSIONS:
        print(f"Processing: {conv['html']}")
        
        with open(conv['md'], 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        md_html = convert_markdown(md_content)
        
        chapters = extract_chapters(md_content)
        
        final_html = generate_html(
            conv['title'],
            conv['description'],
            BEFORE,
            HEADER_OPEN,
            CONTENT_PAGE_OPEN,
            md_html,
            FOOTER,
            chapters,
            conv['html']
        )
        
        output_path = os.path.join(OUTPUT_DIR, conv['html'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        size, checks = verify_html(output_path, conv['title'])
        
        print(f"  File size: {size:,} bytes")
        for check_name, passed in checks.items():
            print(f"  {check_name}: {'PASS' if passed else 'FAIL'}")
        
        results.append({
            'file': conv['html'],
            'size': size,
            'passed': all(checks.values())
        })
    
    print("\n=== Summary ===")
    for r in results:
        status = "PASS" if r['passed'] else "FAIL"
        print(f"{r['file']}: {r['size']:,} bytes - {status}")

if __name__ == "__main__":
    main()
