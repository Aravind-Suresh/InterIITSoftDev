# Inter IIT 2016 Soft-dev

The repository consists of a python tool to load and display student data from the cloud. It also performs a local search and displays results.

## Dependencies
* PIL
* Tkinter
* BeautifulSoup

## Trial

First clone the repository.

To display student data,
```
$ python main.py -r <rollNumber>
```

To display student data and save it, add a param --save.
```
$ python main.py -r <rollNumber> --save
```

To search and display student data which is saved locally, add a param --load.

```
$ python main.py -r <rollNumber> --load
```
