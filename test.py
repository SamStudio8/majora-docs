import sys

from prance import ResolvingParser, BaseParser
parser = ResolvingParser('api/majora.yaml')
spec = parser.specification  # contains fully resolved specs as a dict


PRIORITY_COLOUR = {
    0: "color:#fff; background-color:#dc3545",
    1: "color:#000; background-color:#ffc107",
    2: "color:#fff; background-color:#17a2b8",
    None: "color:#fff; background-color:#6c757d",
}
PRIORITY_NAME = {
    0: "required",
    1: "possibly required",
    2: "recommended",
    None: "",
}

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

                if field_spec.get("x-ocarina-nargs-root"):
                    flat_spec.update({field: {
                        "name": field,
                        "type": field_spec.get("type"),
                        "path": prefix+field,
                        "required": field in sspec.get("required", []),
                        "x-priority": field_spec.get("x-priority", 100),
                        "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                        "x-ocarina-nargs-root": field_spec.get("x-ocarina-nargs-root"),
                    }})
            elif field_spec.get("type") == "object":
                subspec = flatten_object(field_spec, prefix+field+'.')
                flat_spec.update(subspec)
            else:
                flat_spec[field] = {
                    "path": prefix+field,
                    "name": field,
                    "type": field_spec.get("type"),
                    "required": field in sspec.get("required", []),
                    "x-priority": field_spec.get("x-priority", 100),
                    "description": field_spec.get("description", ""),
                    "enum": [x if x else "(blank)" for x in field_spec.get("enum", [])],
                    "example": str(field_spec.get("example", "unknown")),
                    "json_example": field_spec.get("example"),
                    "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                    "x-ocarina-warning": field_spec.get("x-ocarina-warning", ""),
                    "x-ocarina-namespace": field_spec.get("x-ocarina-namespace", ""),
                    "x-ocarina-in-record": field_spec.get("x-ocarina-in-record", False),
                    "x-uploader-column": field_spec.get("x-uploader-column"),
                    "x-uploader-limit": field_spec.get("x-uploader-limit"),
                    "x-ocarina-nargs-name": field_spec.get("x-ocarina-nargs-name"),
                    "x-ocarina-nargs-pos": field_spec.get("x-ocarina-nargs-pos"),
                }
    return flat_spec




def flatten_object2(spec, prefix=""):
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

                flat_spec.update({field: {
                    "name": field,
                    "type": field_spec.get("type"),
                    "path": prefix+field,
                    "required": field in sspec.get("required", []),
                    "x-priority": field_spec.get("x-priority", 100),
                    "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                    "x-ocarina-nargs-root": field_spec.get("x-ocarina-nargs-root"),
                }})
            elif field_spec.get("type") == "object":
                subspec = flatten_object(field_spec, prefix+field+'.')
                flat_spec.update(subspec)
                flat_spec.update({field: {
                    "name": field,
                    "type": field_spec.get("type"),
                    "path": prefix+field,
                    "required": field in sspec.get("required", []),
                    "x-priority": field_spec.get("x-priority", 100),
                    "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                    "x-ocarina-nargs-root": field_spec.get("x-ocarina-nargs-root"),
                }})
            else:
                flat_spec[field] = {
                    "path": prefix+field,
                    "name": field,
                    "type": field_spec.get("type"),
                    "required": field in sspec.get("required", []),
                    "x-priority": field_spec.get("x-priority", 100),
                    "description": field_spec.get("description", ""),
                    "enum": [x if x else "(blank)" for x in field_spec.get("enum", [])],
                    "example": str(field_spec.get("example", "unknown")),
                    "json_example": field_spec.get("example"),
                    "x-ocarina-param": field_spec.get("x-ocarina-param", "NA"),
                    "x-ocarina-warning": field_spec.get("x-ocarina-warning", ""),
                    "x-ocarina-namespace": field_spec.get("x-ocarina-namespace", ""),
                    "x-ocarina-in-record": field_spec.get("x-ocarina-in-record", False),
                    "x-uploader-column": field_spec.get("x-uploader-column"),
                    "x-uploader-limit": field_spec.get("x-uploader-limit"),
                    "x-ocarina-nargs-name": field_spec.get("x-ocarina-nargs-name"),
                    "x-ocarina-nargs-pos": field_spec.get("x-ocarina-nargs-pos"),
                }
    return flat_spec





def insert_path(node, path, type, v):

    if len(path) == 0:
        return

    #print('*', node, path)
    if path[0] not in node:
        if type == "array":
            node[ path[0] ] = []
        elif type == "object":
            node[ path[0] ] = {}
        else:
            node[ path[0] ] = v
        insert_path(node[ path[0] ], path[1:], type, v)
    else:
        insert_path(node, path[1:], type, v)





    #print(d, parts, type, v)
    #if not v:
    #    if type == "array":
    #        node[parts[-1]] = [{}]
    #    elif type == "object":
    #        node[parts[-1]] = {}
    #else:
    #    if type(node[parts[-1]]) is list:
    #        node[parts[-2]][0][parts
    #    node[parts[-1]] = v

for path, spec in spec["paths"].items():
    #print(spec['post'].keys())
    #print(spec['post']['tags'])

    metadata = metrics = 0

    print("## %s" % spec['post']['summary'])

    print("\n<code>%s</code>" % path)

    print("\n\n### Attributes")
    cmd_head = "ocarina " + spec['post'].get('x-ocarina-cmd', "")
    cmd = []
    cmd_req = []
    cmd_no = []
    uploader_map = {}

    json_example = {}
    for k, v in spec['post']['requestBody']['content']['application/json']['schema'].items():
        for item in v:
            flat = flatten_object2(item)
            sort_flat = sorted(flat.items(), key=lambda x: (x[1].get("x-priority", 100), x[1].get("name")))
            for kp, vp in sort_flat:
                insert_path(json_example, vp["path"].split('.'), vp.get("type", "str"), vp.get("json_example"))
    print(json_example)


    for k, v in spec['post']['requestBody']['content']['application/json']['schema'].items():
        for item in v:
            flat = flatten_object(item)
            sort_flat = sorted(flat.items(), key=lambda x: (x[1].get("x-priority", 100), x[1].get("name")))

            nargs = {}
            narg_notes = []
            for kp, vp in sort_flat:


                if "metric" in vp["path"]:
                    metrics += 1
                    continue
                elif "metadata" in vp["path"]:
                    metadata += 1
                    continue
                if vp.get("x-ocarina-nargs-name"):
                    narg_name = vp.get("x-ocarina-nargs-name")
                    if narg_name not in nargs:
                        nargs[narg_name] = {}
                    nargs[narg_name][vp.get("x-ocarina-nargs-pos")] = {"name": vp.get("name"), "example": vp.get("example")}
            sys.stderr.write(str(json_example) + '\n\n')

            for kp, vp in sort_flat:
                if "metric" in vp["path"]:
                    metrics += 1
                    continue
                elif "metadata" in vp["path"]:
                    metadata += 1
                    continue

                if vp.get("x-ocarina-param") == "NA":
                    pass
                elif vp.get("x-ocarina-param") is None:
                    cmd_no.append(vp.get("name"))
                elif vp.get("x-ocarina-nargs-root") in nargs:
                    narg_name = vp.get("x-ocarina-nargs-root")
                    narg_example = []
                    narg_note = []

                    top_pos = max(nargs[narg_name].keys())
                    for i in range(top_pos+1):
                        if i == 0:
                            narg_example.append(vp.get("x-ocarina-param"))
                        else:
                            example = nargs[vp["x-ocarina-nargs-root"]].get(i, {}).get("example", "''")
                            if ' ' in example:
                                example = "'%s'" % example
                            narg_example.append(example)
                            narg_note.append(nargs[vp["x-ocarina-nargs-root"]].get(i, {}).get("name"))
                    cmd.append("\t%s \\" % ' '.join(narg_example))
                    narg_notes.append({narg_name: narg_note})
                    if vp.get("required"):
                        cmd_req.append("\t%s \\" % ' '.join(narg_example))

                else:
                    example = vp.get("example")
                    if ' ' in vp.get("example"):
                        example = "'%s'" % example
                    cmd.append("\t%s %s \\" % (vp.get("x-ocarina-param"), example))

                    if vp.get("required"):
                        cmd_req.append("\t%s %s \\" % (vp.get("x-ocarina-param"), example))

                if vp.get("x-uploader-column"):
                    uploader_map[vp.get("name")] = "%s%s" % (vp.get("x-uploader-column"), " (limit %d)" % vp.get("x-uploader-limit") if vp.get("x-uploader-limit") else "")


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

                if len(nargs) > 0:
                    note_str = []
                    for d in narg_notes:
                        for narg_note_name, narg_note_list in d.items():
                            curr_note_pos_names = ["<code>%s</code>" % s for s in narg_note_list]
                            note_str.append("<li><code>%s</code> ▶ %s</li>" % (narg_note_name, ' '.join(curr_note_pos_names)))

                    print("""<blockquote class="lang-specific shell--ocarina"><p>Attributes merged into positional arguments by Ocarina:<ul>""")
                    for s in note_str:
                        print(s)
                    print("""</ul></blockquote>""")

                if len(cmd_no) > 0:
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
                print("""<blockquote class="lang-specific plaintext--uploader"><p>There may be some differences between this specification and the uploader, particularly for providing Metrics and Metadata. See the Metadata and Metrics sections below for column names that are compatible with the API spec.</p></blockquote>""")

                if len(uploader_map) > 0:
                    print("""<blockquote class="lang-specific plaintext--uploader"><p>Some attributes are named differently on the CGPS uploader:</p>""")
                    print("<ul>%s</ul>" % '\n'.join(["<li><code>%s</code> ▶ <code>%s</code></li>" % (k, v) for k, v in uploader_map.items()]))
                    print("</blockquote>")
            else:
                print("""<blockquote class="lang-specific plaintext--uploader"><p>Function not currently implemented in CGPS Metadata Uploader</p></blockquote>""")
        else:
            print("""<blockquote class="lang-specific plaintext--uploader"><p>Function not currently implemented in CGPS Metadata Uploader</p></blockquote>""")

        print("\nName | Description | Options")
        print("---- | ----------- | -------")
        for kp, vp in sort_flat:
            if "metric" in vp["path"] or "metadata" in vp["path"] or vp.get("x-ocarina-nargs-root"):
                continue

            pri_colour = PRIORITY_COLOUR.get(vp["x-priority"])
            if not pri_colour:
                pri_colour = PRIORITY_COLOUR.get(None)
            name = "<b><code%s>%s</code></b>" % (" style='%s'" % pri_colour, vp["name"])
            field_description = "%s%s%s" % (vp["type"], ", <i>%s</i>" % PRIORITY_NAME.get(vp["x-priority"]) if PRIORITY_NAME.get(vp["x-priority"]) else "", ", <i>enum</i>" if len(vp.get("enum")) > 0 else "")

            aside = ""
            if vp.get("x-ocarina-warning"):
                aside = "<aside class='warning' style='padding: 1em'>%s</aside>" % vp["x-ocarina-warning"]

            print(' | '.join([str(x) for x in [
                name + '</br>' + field_description,
                #vp["path"],
                vp.get("description", "").replace('\n', "</br>") + aside,
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))


    if metrics > 0:
        print("\n\n### Metrics")
        cmd_metric = []
        uploader_map = {}
        for kp, vp in sort_flat:
            if "metric" not in vp["path"]:
                continue
            if vp.get("x-ocarina-param") == "NA":
                pass
            else:
                example = vp.get("example")
                if ' ' in vp.get("example"):
                    example = "'%s'" % example
                cmd_metric.append("\t--metric %s%s %s %s \\" % (vp.get("x-ocarina-namespace"), ".#" if vp.get("x-ocarina-in-record") else "", vp.get("x-ocarina-param"), example))

            if vp.get("x-uploader-column"):
                uploader_map["%s %s" % (vp.get("x-ocarina-namespace"), vp.get("x-ocarina-param"))] = "%s%s" % (vp.get("x-uploader-column"), " (limit %d)" % vp.get("x-uploader-limit") if vp.get("x-uploader-limit") else "")

        if spec["post"].get("x-ocarina-cmd", ""):
            if spec["post"]["x-ocarina-cmd"]:
                if len(cmd_metric) > 0:
                    cmd_metric[-1] = cmd_metric[-1][:-1]
                print("""<blockquote class="lang-specific shell--ocarina"><p>To provide metrics with Ocarina:</p></blockquote>""")
                print("```shell--ocarina")
                print(cmd_head + ' \\' )
                print("\t...")
                print('\n'.join(cmd_metric))
                print("```")
                print("""<blockquote class="lang-specific shell--ocarina"><p>If a particular metric supports storing multiple records, you can provide them by incrementing a numerical suffix after the metric's namespace: <i>e.g.</i> <code>--metric name.1 key value</code> ... <code>--metric name.N key value.</code></blockquote>""")

        if len(uploader_map) > 0:
            print("""<blockquote class="lang-specific plaintext--uploader"><p>Some metrics can be provided via the uploader using these column names:</p>""")
            print("<ul>%s</ul>" % '\n'.join(["<li><code>%s</code> ▶ <code>%s</code></li>" % (k, v) for k, v in uploader_map.items()]))
            print("</blockquote>")

        print("Some artifacts in Majora can be annotated with additional Metric objects.")
        print("Metric objects group together specific information that allows for additional description of an artifact, but does not belong in the artifact itself.")
        print("Each metric has its own namespace, containing a fixed set of keys. Some or all of the keys may need a value to validate the Metric.")
        print("This endpoint allows you to submit the following Metrics:")

        print("\nNamespace | Name | Description | Options")
        print("--- | ---- | ----------- | -------")
        for kp, vp in sort_flat:
            if "metric" not in vp["path"]:
                continue
            print(' | '.join([str(x) for x in [
                "<b><code>%s</code></b>" % vp["x-ocarina-namespace"],
                "<b><code>%s</code></b>" % vp["name"],
                vp.get("description", "").replace('\n', "</br>"),
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))

    if metadata > 0:
        print("\n\n### Metadata\n")
        cmd_meta = []
        uploader_map = {}
        for kp, vp in sort_flat:
            if "metadata" not in vp["path"]:
                continue
            if vp.get("x-ocarina-param") == "NA":
                pass
            else:
                example = vp.get("example")
                if ' ' in vp.get("example"):
                    example = "'%s'" % example
                cmd_meta.append("\t-m %s %s %s \\" % (vp.get("x-ocarina-namespace"), vp.get("x-ocarina-param"), example))

            if vp.get("x-uploader-column"):
                uploader_map["%s %s" % (vp.get("x-ocarina-namespace"), vp.get("x-ocarina-param"))] = "%s%s" % (vp.get("x-uploader-column"), " (limit %d)" % vp.get("x-uploader-limit") if vp.get("x-uploader-limit") else "")

        if spec["post"].get("x-ocarina-cmd", ""):
            if spec["post"]["x-ocarina-cmd"]:
                if len(cmd_meta) > 0:
                    cmd_meta[-1] = cmd_meta[-1][:-1]
                print("""<blockquote class="lang-specific shell--ocarina"><p>To provide metadata with Ocarina:</p></blockquote>""")
                print("```shell--ocarina")
                print(cmd_head + ' \\' )
                print("\t...")
                print('\n'.join(cmd_meta))
                print("```")

        if len(uploader_map) > 0:
            print("""<blockquote class="lang-specific plaintext--uploader"><p>Some metadata can be provided via the uploader using these column names:</p>""")
            print("<ul>%s</ul>" % '\n'.join(["<li><code>%s</code> ▶ <code>%s</code></li>" % (k, v) for k, v in uploader_map.items()]))
            print("</blockquote>")

        print("Any artifact in Majora can be 'tagged' with arbitrary key-value metadata.")
        print("Unlike Metrics, there is no fixed terminology or validation on the keys or their values. Like Metrics, to aid organisation, metadata keys are grouped into namespaces.")
        print("This endpoint has 'reserved' metadata keys that should only be used to provide meaningful information:")

        print("\nNamespace | Name | Description | Options")
        print("--- | ---- | ----------- | -------")
        for kp, vp in sort_flat:
            if "metadata" not in vp["path"]:
                continue
            print(' | '.join([str(x) for x in [
                "<b><code>%s</code></b>" % vp["x-ocarina-namespace"],
                "<b><code>%s</code></b>" % vp["name"],
                vp.get("description", "").replace('\n', "</br>"),
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))



    print("\n\n")
