from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import warnings


class WikiObject:
    def __init__(self, string):
        self.article_name = string
        self.page_details = None

    def check_validity(self):
        try:
            self.page_details = wikipedia.page(self.article_name)
            if self.page_details.title != self.article_name:
                warnings.warn("Given Article Name {0} could not be find. Using {1} instead".
                              format(self.article_name, self.page_details.title))
                return True
        except wikipedia.exceptions.PageError as e:
            print e
            return False

    def get_links(self):
        if self.check_validity():
            link_details = self.page_details.links
            return link_details


if __name__ == '__main__':
    test_object = WikiObject('akbarh')
    test_object.get_links()
