from setuptools import setup

setup(
  name="pump-jinja",
  version="0.0.2",
  description="A Pump middleware that uses the Jinja templating system to render responses.",
  author="Adeel Ahmad Khan",
  author_email="adeel@adeel.ru",
  py_modules=["pump_jinja"],
  requires=["Jinja2"],
  license="MIT")