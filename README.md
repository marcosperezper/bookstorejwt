#### **Bookstore API**

A simple project using Django, Django-rest framework, jwt for the authentication and postgres as a database manager.

In the API are 2 endpoints:

**/books**: Here you can list all the books and create another one or
filter one by one using the title of the book as field to search(e.g _books/El hobbit_)

**/authors**: where you can list all the authors and create another one or
filter one by one using the name of the author as field to search(e.g _authors/J.R Tolkien_)

There is a superuser created with the following credentials:

**user: librero**

**password: librero**

The API has enabled all the basic endpoints to login and register that are included in the _rest_auth_ package