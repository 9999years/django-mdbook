Provides a simple view for [mdBooks][mdbook], allowing them to exist within a
Django site. Note that because all requests are proxied through the
`MdBookView`, it will be a bit slower than using Apache or Nginx directly;
however, using a Django view allows fine-grained access control.

Example use:

```python
import os.path

from django.contrib.auth.decorators import permission_required
from django.urls import path
from django.views.generic import RedirectView

from django_mdbook.views import MdBookView

directory = os.path.dirname(__file__)


def rel_to_abs(path: str) -> str:
    """
    Given a path relative to this file, give its absolute name
    :param path: a relative path to resolve
    :return: an absolute path
    """
    return os.path.join(directory, path)

urlpatterns = [
    path('doc/foo/',
        RedirectView.as_view(url='index.html', permanent=True),
        name='foo_doc_index'),
    path('doc/foo/<path:path>',
        permission_required('doc.foo_documentation')(
            # Note: book_root is the directory with book.toml, not the built directory
            MdBookView.as_view(book_root=rel_to_abs('foo'))),
        name='foo_docs')
]
```

[mdbook]: https://github.com/rust-lang-nursery/mdBook
