import jsonschema

jsonschema.validate(
    {
        'key': 'value'
    },
    {
        'type': 'object', 'additionalProperties': {'type': 'string'}
    }
)



