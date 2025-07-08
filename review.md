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
