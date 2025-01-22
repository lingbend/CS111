import sys
import re
from RequestGuard import RequestGuard
import bs4
import requests
from matplotlib import pyplot
import shutil
from image_processing import sepia, grayscale, flipped, mirror


def validate_commands(*args):
    args = args[0]
    if len(args) == 4:
        if args[0] in ['-c','-p'] and len(args[2]) >= 4 and len(args[3]) >= 4 and '.csv' in args[3]:
            return True
        elif args[0] == '-i' and args[3] in ['-s','-g','-f','-m']:
            return True
    print('The commands contain invalid arguments.')
    return False

def count_links(*args):
    args = args[0]
    first_domain = extract_domain(args[1])
    guard_obj = RequestGuard(first_domain)
    link_list = [args[1]]
    appearance_count = {}
    while len(link_list) != 0:
        current_link = link_list.pop()
        if current_link in appearance_count:
            appearance_count[current_link] += 1
        else:
            appearance_count[current_link] = 1
            if guard_obj.can_follow_link(current_link):
                link_list.extend(get_links(current_link, first_domain, guard_obj))
    frequencies = appearance_count.values()
    values, bins, garbage = pyplot.hist(frequencies, bins=list(range(min(frequencies), max(frequencies) + 2)))
    pyplot.savefig(args[2])
    pyplot.clf()
    with open(args[3], 'w') as file:
        for bin, value in zip(bins, values):
            file.write(f'{bin},{value}\n')

def get_links(url, main_domain, guard_obj):
    page_links = []
    page = requests.get(url)
    if guard_obj.can_follow_link(page.url) and page.status_code == 200:
        html = bs4.BeautifulSoup(page.text, features="html.parser")
        a_tags = html.find_all('a')
        for tag in a_tags:
            link = tag.get('href')
            out_url = clean_sub_links(link, url, main_domain)
            page_links.extend(out_url)
        return page_links
    else:
        return []

def clean_sub_links(url, sub_domain, main_domain):
    if re.match(r'\bhttps?.*', url):
        if re.match(r'\b.*#.*', url):
            return [clean_hashtags_slashs(re.match(r'\b(.*)#.*', url).group(1))]
        else:
            return [url]
    elif re.match(r'/.*', url):
        return [clean_hashtags_slashs(re.match(r'(.*?)/?$', main_domain).group(1) + url)]
    elif re.match(r'#.*', url):
        return [sub_domain]
    elif re.match(r'javascript:.*', url) or re.match(r'mailto:.*', url):
        return []
    else:
        return [clean_hashtags_slashs(re.match(r'(\b.*/).*', sub_domain).group(1) + url)]


def clean_hashtags_slashs(url):
    if re.search(r'.*#.*', url):
        url = re.search(r'(.*)#.*', url).group(1)
    if not re.match(r'.*/$', url) and not re.search(r'.*/.*\..*$', url):
        return url + '/'
    else:
        return url


def extract_domain(url):
    return re.match(r'\b((https?:)?(//)?[^/]*)/?', url).group(1)


def extract_web_table(*args):
    args = args[0]
    url = args[1]
    first_domain = extract_domain(args[1])
    guard_obj = RequestGuard(first_domain)
    if guard_obj.can_follow_link(url):
        page = requests.get(url)
        if page.status_code == 200:
            html = bs4.BeautifulSoup(page.text, features="html.parser")
            table_data = get_table(html)
            x_set = table_data[0]
            for y_set, color in zip(table_data[1:],['b', 'g', 'r', 'k']):
                pyplot.plot(x_set, y_set, color)
            pyplot.savefig(args[2])
            pyplot.clf()
            with open(args[3], 'w') as file:
                for i in range(len(table_data[0])):
                    file_string = ''
                    for j in range(len(table_data)):
                        file_string += str(table_data[j][i]) + ','
                    file.write(f'{file_string[:-1]}\n')
        else:
            raise Exception("Error loading webpage.")


def get_table(html):
    project_table = None
    table_data = []
    tables = html.find_all('table')
    for table in tables:
        if table.get('id') == 'CS111-Project4b':
            project_table = table
    if project_table:
        for row in project_table.find_all('tr'):
            row_data = []
            for cell in row.find_all('td'):
                row_data.append(float(cell.string))
            table_data.append(row_data)
        refactored_table = []

        for i in range(len(table_data[0])):
            refactored_table.append([])
            for j in range(len(table_data)):
                refactored_table[i].append(table_data[j][i])
    else:
        raise Exception("Table not found.")
    return refactored_table

def modify_images(*args):
    args = args[0]
    main_domain = extract_domain(args[1])
    guard_obj = RequestGuard(main_domain)
    if guard_obj.can_follow_link(args[1]):
        pic_links = get_srcs(args[1], main_domain, guard_obj)
        for url in pic_links:
            print(url)
            output_filename = re.match(r'.*/(.*)$', url).group(1)
            response = requests.get(url, stream=True)
            with open(output_filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            new_filename = args[2] + output_filename
            if args[3] == '-s':
                sepia(output_filename, new_filename)
            elif args[3] == '-g':
                grayscale(output_filename, new_filename)
            elif args[3] == '-f':
                flipped(output_filename, new_filename)
            elif args[3] == '-m':
                mirror(output_filename, new_filename)


def get_srcs(url, main_domain, guard_obj):
    page_links = []
    page = requests.get(url)
    if guard_obj.can_follow_link(page.url) and page.status_code == 200:
        html = bs4.BeautifulSoup(page.text, features="html.parser")
        img_tags = html.find_all('img')
        for tag in img_tags:
            link = tag.get('src')
            out_url = clean_sub_links(link, url, main_domain)
            page_links.extend(out_url)
        return page_links
    else:
        return []


if __name__ == '__main__':
    commands = sys.argv[1:]
    if validate_commands(commands):
        try:
            if commands[0] == '-c':
                count_links(commands)
            elif commands[0] == '-p':
                extract_web_table(commands)
            elif commands[0] == '-i':
                modify_images(commands)
        except Exception as e:
            print(e)
