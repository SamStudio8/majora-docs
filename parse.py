import sys

from prance import ResolvingParser, BaseParser
parser = ResolvingParser('api/majora.yaml')
spec = parser.specification  # contains fully resolved specs as a dict

def flatten_object(spec, prefix="", array=False):
    flat_spec = {}

    #TODO Handle all types of oneOf/allOf etc.
    all_of = True
    if "allOf" in spec:
        spec = spec["allOf"]
    else:
        spec = [spec]

    sprefix = prefix
    for sspec in spec:
        if array:
            prefix = "%s:%s." % (sprefix.rstrip('.'), sspec.get("title", "?"))

        for field, field_spec in sspec.get("properties", {}).items():

            if field_spec.get("type") == "array":
                subspec = flatten_object(field_spec.get("items", {}), prefix+field+'.', field_spec.get("type") == "array")
                flat_spec.update(subspec)

                field_spec.update({
                    "name": field,
                    "path": prefix+field,
                    "required": field in sspec.get("required", []),
                })
                #del field_spec["items"] # No need to unfurl these
                flat_spec.update({field: field_spec})

            elif field_spec.get("type") == "object":
                subspec = flatten_object(field_spec, prefix+field+'.')
                flat_spec.update(subspec)

                field_spec.update({
                    "name": field,
                    "path": prefix+field,
                    "required": field in sspec.get("required", []),
                })
                flat_spec.update({field: field_spec})
            else:
                flat_spec[field] = field_spec
                flat_spec[field] = {
                    "path": prefix+field,
                    "name": field,
                    "required": field in sspec.get("required", []),
                    "enum": [x if x else "(blank)" for x in field_spec.get("enum", [])],
                    "example": str(field_spec.get("example", "unknown")),
                    "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                }
    return flat_spec


for path, spec in spec["paths"].items():
    for k, v in spec['post']['requestBody']['content']['application/json']['schema'].items():
        for item in v:
            flat = flatten_object(item)

            for k, v in flat.items():
                print(k,v)
        print()
        print()





