# Review Note

## Provide env info in `.env.example`

## Flask app factory pattern

- [Application Factories](https://flask.palletsprojects.com/en/stable/patterns/appfactories/)

- [Configuration Best Practices](https://flask.palletsprojects.com/en/stable/config/#configuration-best-practices)

- health-check endpoint

- further step: [Blueprint](https://flask.palletsprojects.com/en/stable/blueprints/)

In development, running the app with command:

```bash
.venv/bin/flask --app weather_bot run \
    --host=0.0.0.0 \
    --port=5000 \
    --debug
```

## `handle_message`, `handle_postback`

- Allocate responsibilities with extracted functions
- [walrus operator](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions)
- [Use `is` operator to confirm `None` value](https://youtu.be/pDhUWOj_a0M?si=bh9tG0TE28DTH6Ju)
- Check type with `isinstance`
- Early return to reduce cognitive load of condition branching.

## Python code refactor

Review order:

1. `get.py`
2. `OOP_and_Function.py`
3. `main_function.py`
4. `weather_bot/line_bot.py`

Refactor point:

- Typo ([Spell Checker extension](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker))

- Replace comments with function docstring

- Use tuple for const (for clarity and space efficiency)

- Typing: `Literal`

- Avoid returning vague complex data structure (list, tuple, dict etc.)

- Function should be responsible for solely 1 duty at a time.
  (eg. `get_weather_data` do both "city name validation" and "compose weather info" within function)
  -> extract "city name validation" job from it.

- Use `map` to transform elements in iterable ([ref](https://medium.com/ccclub/py-instant-tips-filter-map-reduce-a37f942a486f))

- Use `namedtuple` / `Typeddict` / `Dataclass` to organize sequence of data ([ref](https://medium.com/@40243105s/how-python-structures-data-set-12dbc86f83ea))

- `serch_city` seems to be a non-sense function?

## Replace hard_coded with Enum / Const

- http.HTTPMethod
- http.HTTPStatus
