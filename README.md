# Composer - Pipe function for Python

## Usage

```python
from composer import Composer
def func0(x):
    return x*2

initial_value = 10

composer  = Composer(func0,initial_value)

def func1(x):
    return x+5

print(composer.then(func1).value) ##25
```

alternatively, you can use `|` or `>`

```python
print((composer > func1).value)
# Note that you would need to use parenthesis for piping through multiple functions
# like this
def func2(x):
    return x**2

composer = Composer(func0,10)
result = (composer > func1) > func2
print(result.value)
```

You can build a composer without assigning any function by using Composer.identity

```python
value = 10
composed = Composer.identity(value)
```

# Another example

```python
from composer import Composer
from requests import get
from bs4 import BeautifulSoup as Soup

def make_soup(response):
    return Soup(response.text,"html.parser")

composer = Composer(get,"https://example.com").then(make_soup)
soup = composer.value

```
