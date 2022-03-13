# sharksearch

    \.          |\
       \`.___---~~  ~~~--_
       //~~----___  (_o_-~
      '           |/'

## A simple search API for SharkBook

sharksearch has two parts: a crawl, and a search API with a single endpoint `/search`, which takes a parameter *query* and an optional parameter *category*. No assumptions are made about the typical form of the query. Search does substring match on names and is case-sensitive. Duplicate names are supported.

#### You can test sharksearch out for yourself! 

###### Installations:

`pip install -r requirements.txt`

###### Running:

`python3 crawl.py`
`flask run`

To search through some sharks, clone the repository and run crawl.py. (For testing purposes, the call to shark_crawl() in crawl.py may be given a max_sharks. By default, this is positive infinity.) After the crawl finishes (indicated by a log message, which also displays the number of sharks crawled), you may freely call run flask and use the web browser or otherwise to make HTTP requests to search. 

###### Unit tests:

`python3 -m unittest`

Unit tests are implemented for crawl and search by faking, using the Python unittest framework. The unit test for search relies on crawl on the FakeSharkbook.

