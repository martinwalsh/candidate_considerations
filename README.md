# Candidate Considerations Survey - Visualizations

## Rationale

This project is based on a
[worksheet](https://docs.google.com/spreadsheets/d/1opp6CWoIiu47ijEAaFF8MqvVLYnClSHSnq8VkYu1a_s)
developed by Matt Hoffman, and the folks at [re-factor](http://re-factor.co/),
and shared in the `#hiring-practices` channel of the [chicago-tech slack
community](http://www.chicagotechslack.com/).

As is its intended purpose, I used the survey to make a very difficult choice
between two great companies. I wondered how the data might "look" and began to
search for an effective method of representing it visually. This project is that
experiment.

What you'll find inside ...

* A completed sample [survey](src/survey.csv)
* An ipython/jupyter [notebook](src/CandidateConsiderations.ipynb) (where the action is)
* A [Makefile](#other-make-targets)

## Requirements

* docker
* docker-compose
* make (and awk, for help text)

NOTE: The makefile has been tested on Mac OS X (El Capitan) only, but should
work fine on any other unix-like platform. YMMV.

## Launching the Jupyter notebook

```
make up
```

## Other make targets

```
$ make help
Targets:
  build       build docker images in config (force rebuild with -B)
  down        run docker-compose down
  clean       remove docker-compose artifacts
  up          run docker-compose up
  help        displays this message
```
