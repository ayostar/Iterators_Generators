# """comprehensions"""
# list_comprehensions = [i for i in range(10000) if i%2==0]
# gen_comprehensions = (i for i in range(10000) if i%2==0)
#
#
#
'generator foo'
def my_range(start, end):
    while start < end:
        yield start
        start += 1


if __name__ == '__main__':
    for i in my_range(1, 10):
        print(i)
#
#
# 'habr gen'
import re
import requests
#
#
# HABR_MAIN = 'http://habr.com'
#
#
# def habr_pages():
#     session = requests.Session()
#     habr_main = session.get(HABR_MAIN).text
#     links = set(re.findall(r'<a href="(.*?)" class="post__title_link">', habr_main))
#     for link in links:
#         yield requests.get(link).text
#     session.close()
#
#
# for page in habr_pages():
#     print(page)
#
# 'iter_class'


# class MyRange:
#
#     def __init__(self, start, end):
#         self.start = start - 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start == self.end:
#             raise StopIteration
#         return self.start
#
#
# if __name__ == '__main__':
#     for i in MyRange(1, 10):
#         print(i)
#     ints = list((MyRange(1, 10)))
#     print(ints)


# class WebLinks:
#     def __init__(self, target_site):
#         self.target_site = target_site
#
#     def __iter__(self):
#         text_data = requests.get(self.target_site).text
#         self.all_links = re.findall(r'<a.*?href=[\'\"](.*?)[\'\"]', text_data)
#         self.cursor = -1
#         return self
#
#     def __next__(self):
#         self.cursor += 1
#         if len(self.all_links) == self.cursor:
#             raise StopIteration
#         return self.all_links[self.cursor]
#
# site = 'https://yandex.ru'
# YA_weblinks = WebLinks(site)
# for item in YA_weblinks:
#     print(item)

# 'iter_sw'
# import requests
#
#
# class StarWarsCharacters:
#     URL = 'https://swapi.dev/api/people/'
#
#     def get_character(self, character_id):
#         response = requests.get(f'{self.URL}/{character_id}')
#         if response.ok:
#             return response.json()
#
#     def __iter__(self):
#         self.cursor = 0
#         return self
#
#     def __next__(self):
#         self.cursor += 1
#         character = self.get_character(self.cursor)
#         if character is None:
#             raise StopIteration
#         return character
#
#
# for character in StarWarsCharacters():
#     print(character)
