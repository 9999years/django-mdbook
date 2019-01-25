import mimetypes
import os
import subprocess
from typing import Tuple

import toml
from cached_property import cached_property
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.views import View


class MdBookView(View):
    # path to directory containing book.toml
    book_root = None

    @cached_property
    def config(self) -> dict:
        """
        Lazy-loading configuration, from `book_config`
        """
        with open(os.path.join(self.book_root, 'book.toml'), encoding='utf-8') as cfg:
            return toml.load(cfg)

    @cached_property
    def src_dir(self) -> str:
        """
        The source directory for this book
        """
        book: dict = self.config['book']
        # default source directory is 'src'
        return book.get('src', 'src')

    @cached_property
    def book_dir(self) -> str:
        """
        The directory of rendered HTML / CSS / JS files for this book
        """
        return os.path.join(
            self.book_root,
            self.config.get('build', {}).get('build-dir', 'book/'))

    def build_book(self, mdbook: str = 'mdbook', args=[]) -> subprocess.CompletedProcess:
        """
        Build the book by running `mdbook build`
        :param mdbook: Path to the mdbook executable
        :param args: Other arguments to pass to `mdbook build` before the
        destination directory
        :return: The completed process
        """
        return subprocess.run([mdbook, 'build', *args, self.book_root],
                             capture_output=True, text=True)

    def get(self, request: HttpRequest, path: str = None) -> HttpResponse:
        if not path:
            path = request.path
        # get filesystem path
        filepath = os.path.join(self.book_dir, path)

        # 404
        if not os.path.exists(filepath):
            return HttpResponseNotFound()

        with open(filepath, 'rb') as f:
            # guess mime type
            mime, _ = mimetypes.guess_type(filepath)
            return HttpResponse(f, content_type=mime)
