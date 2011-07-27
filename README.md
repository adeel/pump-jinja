# pump-jinja

`pump-jinja` is a [Pump](http://adeel.github.com/pump) middleware that uses the [Jinja templating system](http://jinja.pocoo.org/) to render responses.

## Installation

To install, type

	$ pip install pump-jinja

or to grab it from GitHub:

	$ git clone git://github.com/adeel/pump-jinja.git
	$ cd pump-jinja
	$ python setup.py install

## Usage

Just wrap your app with `pump_jinja.wrap_jinja`.

If your app's response is a tuple, Jinja will be used render the response.  The first element of the tuple is parsed as the template name, and the second should be a dictionary of data to be passed to the template.  Example:

    def view_product(req, id):
      # product = ...
      return "products/view", {"product": product}

If [sessions](https://github.com/adeel/pump/blob/master/pump/middleware/session.py) are enabled, a `session` key will be added to the data and sent
to the template.

It takes a `template_dir` option, which should be the path to your template directory, and a `config` option, which can be a dict that will be passed to all your views.