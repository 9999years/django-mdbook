from cached_property import cached_property
from django.shortcuts import render
from django.views import View
import toml


class MdBookView(View):
    # path to book.toml
    book_config = None

    @cached_property
    def config(self) -> dict:
        """
        Lazy-loading configuration, from `book_config`
        """
        with open(self.book_config) as cfg:
            return toml.load(cfg)

    def src(self):
        book: dict = self.config['book']
        # default source directory is 'src'
        return book.setdefault('src', 'src')
