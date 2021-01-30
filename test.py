from prance import ResolvingParser, BaseParser
parser = ResolvingParser('api/majora.yaml')
spec = parser.specification  # contains fully resolved specs as a dict

def flatten_object(spec, prefix=""):
    flat_spec = {}

    all_of = True
    if "allOf" in spec:
        spec = spec["allOf"]
    else:
        spec = [spec]

    for sspec in spec:
        for field, field_spec in sspec.get("properties", {}).items():
            if field_spec.get("type") == "array":
                subspec = flatten_object(field_spec.get("items", {}), prefix+field+'.')
                flat_spec.update(subspec)
            else:
                flat_spec[field] = {
                    "path": prefix+field,
                    "name": field,
                    "type": field_spec.get("type"),
                    "required": field in sspec.get("required", []),
                    "description": field_spec.get("description", ""),
                    "enum": [x if x else "(blank)" for x in field_spec.get("enum", [])],
                    "example": field_spec.get("example"),
                    "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                }
    return flat_spec

for path, spec in spec["paths"].items():
    #print(spec['post'].keys())
    #print(spec['post']['tags'])

    print("## %s" % spec['post']['summary'])
    print("<code>%s</code>" % path)

    print("### Attributes")
    cmd_head = "ocarina " + spec['post'].get('x-ocarina-cmd', "")
    cmd = []
    cmd_req = []
    cmd_no = []
    for k, v in spec['post']['requestBody']['content']['application/json']['schema'].items():
        for item in v:
            flat = flatten_object(item)
            sort_flat = sorted(flat.items(), key=lambda x: (not x[1].get("required", False), x[1].get("name")))
            for kp, vp in sort_flat:
                if vp.get("x-ocarina-param") == "NA":
                    pass
                elif vp.get("x-ocarina-param") is None:
                    cmd_no.append(vp.get("name"))
                else:
                    example = vp.get("example")
                    if ' ' in vp.get("example"):
                        example = "'%s'" % example
                    cmd.append("\t%s %s \\" % (vp.get("x-ocarina-param"), example))

                    if vp.get("required"):
                        cmd_req.append("\t%s %s \\" % (vp.get("x-ocarina-param"), example))


        if spec["post"].get("x-ocarina-cmd", ""):
            if spec["post"]["x-ocarina-cmd"]:
                if len(cmd) > 0:
                    cmd[-1] = cmd[-1][:-1]
                    cmd_req[-1] = cmd_req[-1][:-1]
                print("""<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>""")
                print("```shell--ocarina")
                print(cmd_head + ' \\' )
                print('\n'.join(cmd_req))
                print("```")

                print("""<blockquote class="lang-specific shell--ocarina"><p>Full Ocarina command example:</p></blockquote>""")
                print("```shell--ocarina")
                print(cmd_head + ' \\' )
                print('\n'.join(cmd))
                print("```")

                print("""<blockquote class="lang-specific shell--ocarina"><p>Attributes currently unsupported by Ocarina: %s</p></blockquote>""" % ', '.join(["<code style='word-break: normal'>%s</code>" % f for f in cmd_no]))
            else:
                print("""<blockquote class="lang-specific shell--ocarina"><p>Function not currently implemented in Ocarina command line interface</p></blockquote>""")
        else:
            print("""<blockquote class="lang-specific shell--ocarina"><p>Function not currently implemented in Ocarina command line interface</p></blockquote>""")

        if spec["post"].get("x-ocarina-api", ""):
            if spec["post"]["x-ocarina-api"]:
                pass
            else:
                print("""<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>""")
        else:
            print("""<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>""")


        if spec["post"].get("x-uploader-doc", ""):
            if spec["post"]["x-uploader-doc"]:
                print("""<blockquote class="lang-specific plaintext--uploader"><p>Documentation for this function can be found on the CGPS uploader website linked below:</br><a href="%s">%s</a></p></blockquote>""" % (spec["post"]["x-uploader-doc"], spec["post"]["x-uploader-doc"]))
            else:
                print("""<blockquote class="lang-specific plaintext--uploader"><p>Function not currently implemented in CGPS Metadata Uploader</p></blockquote>""")
        else:
            print("""<blockquote class="lang-specific plaintext--uploader"><p>Function not currently implemented in CGPS Metadata Uploader</p></blockquote>""")

        print("\nName | Description | Options")
        print("---- | ----------- | -------")
        for kp, vp in sort_flat:
            print(' | '.join([str(x) for x in [
                "<b><code %s>%s</code></b></br>%s%s%s" % ("style='color:#fff; background-color:#dc3545'" if vp["required"] else "", vp["name"], vp["type"], ", <i>required</i>" if vp["required"] else "", ", <i>enum</i>" if len(vp.get("enum")) > 0 else ""),
                #vp["path"],
                vp.get("description", "").replace('\n', "</br>"),
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))


