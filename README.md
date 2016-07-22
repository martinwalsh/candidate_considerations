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

* A completed sample [survey](survey.csv)
* An ipython/jupyter [notebook](Candidate Considerations Survey Visualization.ipynb) (where the action is)
* A [Makefile](#other-make-targets)

## Requirements

* python2.7
* virtualenv
* make (and awk, for help text)

## Launching the Jupyter notebook

```
make run
```

The above will check that python (and virtualenv) are installed, `pip install`
the python dependencies, and launch the jupyter notebook.

## Other make targets

```
$ make help
Targets:
  virtualenv          installs python dependencies
  clean               remove build artifacts
  run                 Launch the jupyter playbook
  help                displays this message
```

