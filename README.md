# WebScraper

## Objective
The aim of this project is to make a simple console program, which given a URL, will output the number of HTML elements in it and the 5 most used tags, along with how many times they were used. This porject is meant to stand by itself, so only built-in libraries were used

## Assumptions
It is assumed the web page will have valid HTML code, i.e. it is expected that every opening tag will have a closing tag, and that there are no syntax errors like

`<p Hello! </p>`.

Therefore, when results are informed, only opening tags are taken into account. Sometimes a warning may appear stating:
_Opening and closing tag numbers do not match_
This may be caused by some standalone elements like `<link>`, `<meta>` or `<br>` and is safe to ignore.

## How to use

Using the command line, the simple use is 
`python -m WebScraper <URL>`

Optionally, using the -f parameter, you may specify a file into which results will be written. If you do this, results won't be shown in the console.
Example:
`python -m WebScraper <URL> -f <filename>`

Aditionally, using the --excluded_blocks option, you can specify which html elements will have their content ignored. This is useful for elements like `<pre>` or `<code>` which may contain HTML code, but it is not meant to be rendered.
Example excluding the content of `<div>` and `<pre>`
`python -m WebScraper <URL> --excluded_blocks div pre`

For more information, you may also use
`python -m WebScraper -h`

## Requirements
This project was made using Python 3.7, but it should work under any Python 3.x.

## Built-in libraries used
- [argparse](https://docs.python.org/3.7/library/argparse.html)
- [logging](https://docs.python.org/3/library/logging.html)
- [os](https://docs.python.org/3.7/library/os.html)
- [sys](https://docs.python.org/3.7/library/sys.html)
- [collections](https://docs.python.org/3.7/library/collections.html)
- [html.parser](https://docs.python.org/3/library/html.parser.html)
- [unittest](https://docs.python.org/3/library/unittest.html)

## Run tests
All unit tests are in the Tests folder. In order to run all at once, place yourself at the Webscraper directory and run
`python -m unittest discover Tests` 
