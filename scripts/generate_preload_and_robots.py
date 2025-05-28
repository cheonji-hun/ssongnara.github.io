import os

WEBP_DIR = '.'
PRELOAD_FILE = 'preload.html'
ROBOTS_FILE = 'robots.txt'
SITEMAP_LINE = 'Sitemap: https://ssongnara.com/sitemap.xml\n'

# 1. preload.html 생성
def generate_preload():
    links = []
    for fname in os.listdir(WEBP_DIR):
        if fname.endswith('.webp'):
            link = f'<link rel="preload" as="image" href="{fname}" type="image/webp">'
            links.append(link)
    with open(PRELOAD_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(links))

# 2. robots.txt 보완 (sitemap 누락시 자동 삽입)
def patch_robots():
    if not os.path.exists(ROBOTS_FILE):
        with open(ROBOTS_FILE, 'w') as f:
            f.write('User-agent: *\nDisallow:\n')
    with open(ROBOTS_FILE, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        if not any('sitemap.xml' in line.lower() for line in lines):
            lines.append('\n' + SITEMAP_LINE)
            f.seek(0)
            f.writelines(lines)

if __name__ == '__main__':
    generate_preload()
    patch_robots()
