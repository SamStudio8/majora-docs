import sys
import json

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
                    "enum": sorted([x if x else "(blank)" for x in field_spec.get("enum", [])]),
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
                subspec = flatten_object2(field_spec.get("items", {}), prefix+field+'.')
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
                subspec = flatten_object2(field_spec, prefix+field+'.')
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





def insert_path(node, path, v_type, v):
    if len(path) == 0:
        return

    if len(path) == 1:
        prefix = []
    else:
        prefix = path[:-1]
    field = path[-1]

    if isinstance(node, list):
        node = node[0]

    if len(prefix) > 0:
        if prefix[0] not in node:
            node[ prefix[0] ] = {}
        insert_path(node[prefix[0]], path[1:], v_type, v)
    else:

        if path[0] not in node:
            if v_type == "array":
                d = {}
                node[ path[0] ] = [d]
                insert_path(d, path[1:], v_type, v)
            elif v_type == "object":
                node[ path[0] ] = {}
                insert_path(node[ path[0] ], path[1:], v_type, v)
            else:
                node[path[0]] = v
                insert_path(node, path[1:], type, v)
        else:
            if type(node) is list:
                if len(node) == 0:
                    node.append({})
                node = node[0]

            if field not in node:
                node[ path[0] ] = v


for path, spec in spec["paths"].items():
    spec = spec["post"] # handle POST first for now

    lines = []

    #print(spec['post'].keys())
    #print(spec['post']['tags'])

    metadata = metrics = 0

    lines.append("## %s" % spec['summary'])

    lines.append("\n<code>%s</code>" % path)

    lines.append("\n\n### Attributes")
    cmd_head = "ocarina " + spec.get('x-ocarina-cmd', "")
    cmd = []
    cmd_req = []
    cmd_no = []
    uploader_map = {}

    json_example = {}
    for k, v in spec['requestBody']['content']['application/json']['schema'].items():
        for item in v:
            flat = flatten_object2(item)
            sort_flat = sorted(flat.items(), key=lambda x: (x[1].get("x-priority", 100), x[1].get("name")))
            for kp, vp in sorted(flat.items(), key=lambda x: x[1]["path"]):
                print("inserting", vp["path"].split('.'), vp.get("type", "str"))
                insert_path(json_example, vp["path"].split('.'), vp.get("type", "str"), vp.get("json_example"))
    #print(json_example)


    for k, v in spec['requestBody']['content']['application/json']['schema'].items():
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
            #sys.stderr.write(str(json_example) + '\n\n')

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


        if json_example:
            lines.append("```json--raw")
            lines.append(json.dumps(json_example, indent=4, sort_keys=True))
            lines.append("```")


        if spec.get("x-ocarina-cmd", ""):
            if spec["x-ocarina-cmd"]:
                if len(cmd) > 0:
                    cmd[-1] = cmd[-1][:-1]
                    cmd_req[-1] = cmd_req[-1][:-1]
                lines.append("""<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>""")
                lines.append("```shell--ocarina")
                lines.append(cmd_head + ' \\' )
                lines.append('\n'.join(cmd_req))
                lines.append("```")

                lines.append("""<blockquote class="lang-specific shell--ocarina"><p>Full Ocarina command example:</p></blockquote>""")
                lines.append("```shell--ocarina")
                lines.append(cmd_head + ' \\' )
                lines.append('\n'.join(cmd))
                lines.append("```")

                if len(nargs) > 0:
                    note_str = []
                    for d in narg_notes:
                        for narg_note_name, narg_note_list in d.items():
                            curr_note_pos_names = ["<code>%s</code>" % s for s in narg_note_list]
                            note_str.append("<li><code>%s</code> ▶ %s</li>" % (narg_note_name, ' '.join(curr_note_pos_names)))

                    lines.append("""<blockquote class="lang-specific shell--ocarina"><p>Attributes merged into positional arguments by Ocarina:<ul>""")
                    for s in note_str:
                        lines.append(s)
                    lines.append("""</ul></blockquote>""")

                if len(cmd_no) > 0:
                    lines.append("""<blockquote class="lang-specific shell--ocarina"><p>Attributes currently unsupported by Ocarina: %s</p></blockquote>""" % ', '.join(["<code style='word-break: normal'>%s</code>" % f for f in cmd_no]))

            else:
                lines.append("""<blockquote class="lang-specific shell--ocarina"><p>Function not currently implemented in Ocarina command line interface</p></blockquote>""")
        else:
            lines.append("""<blockquote class="lang-specific shell--ocarina"><p>Function not currently implemented in Ocarina command line interface</p></blockquote>""")

        if spec.get("x-ocarina-api", ""):
            if spec["x-ocarina-api"]:
                pass
            else:
                lines.append("""<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>""")
        else:
            lines.append("""<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>""")


        if spec.get("x-uploader-doc", ""):
            if spec["x-uploader-doc"]:
                lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>Documentation for this function can be found on the CGPS uploader website linked below:</br><a href="%s">%s</a></p></blockquote>""" % (spec["x-uploader-doc"], spec["x-uploader-doc"]))
                lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>There may be some differences between this specification and the uploader, particularly for providing Metrics and Metadata. See the Metadata and Metrics sections below for column names that are compatible with the API spec.</p></blockquote>""")

                if len(uploader_map) > 0:
                    lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>Some attributes are named differently on the CGPS uploader:</p>""")
                    lines.append("<ul>%s</ul>" % '\n'.join(["<li><code>%s</code> ▶ <code>%s</code></li>" % (k, v) for k, v in uploader_map.items()]))
                    lines.append("</blockquote>")
            else:
                lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>Function not currently implemented in CGPS Metadata Uploader</p></blockquote>""")
        else:
            lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>Function not currently implemented in CGPS Metadata Uploader</p></blockquote>""")

        lines.append("\nName | Description | Options")
        lines.append("---- | ----------- | -------")
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

            lines.append(' | '.join([str(x) for x in [
                name + '</br>' + field_description,
                #vp["path"],
                vp.get("description", "").replace('\n', "</br>") + aside,
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))


    if metrics > 0:
        lines.append("\n\n### Metrics")
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

        if spec.get("x-ocarina-cmd", ""):
            if spec["x-ocarina-cmd"]:
                if len(cmd_metric) > 0:
                    cmd_metric[-1] = cmd_metric[-1][:-1]
                lines.append("""<blockquote class="lang-specific shell--ocarina"><p>To provide metrics with Ocarina:</p></blockquote>""")
                lines.append("```shell--ocarina")
                lines.append(cmd_head + ' \\' )
                lines.append("\t...")
                lines.append('\n'.join(cmd_metric))
                lines.append("```")
                lines.append("""<blockquote class="lang-specific shell--ocarina"><p>If a particular metric supports storing multiple records, you can provide them by incrementing a numerical suffix after the metric's namespace: <i>e.g.</i> <code>--metric name.1 key value</code> ... <code>--metric name.N key value.</code></blockquote>""")

        if len(uploader_map) > 0:
            lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>Some metrics can be provided via the uploader using these column names:</p>""")
            lines.append("<ul>%s</ul>" % '\n'.join(["<li><code>%s</code> ▶ <code>%s</code></li>" % (k, v) for k, v in uploader_map.items()]))
            lines.append("</blockquote>")

        lines.append("Some artifacts in Majora can be annotated with additional Metric objects.")
        lines.append("Metric objects group together specific information that allows for additional description of an artifact, but does not belong in the artifact itself.")
        lines.append("Each metric has its own namespace, containing a fixed set of keys. Some or all of the keys may need a value to validate the Metric.")
        lines.append("This endpoint allows you to submit the following Metrics:")

        lines.append("\nNamespace | Name | Description | Options")
        lines.append("--- | ---- | ----------- | -------")
        for kp, vp in sort_flat:
            if "metric" not in vp["path"]:
                continue
            lines.append(' | '.join([str(x) for x in [
                "<b><code>%s</code></b>" % vp["x-ocarina-namespace"],
                "<b><code>%s</code></b>" % vp["name"],
                vp.get("description", "").replace('\n', "</br>"),
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))

    if metadata > 0:
        lines.append("\n\n### Metadata\n")
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

        if spec.get("x-ocarina-cmd", ""):
            if spec["x-ocarina-cmd"]:
                if len(cmd_meta) > 0:
                    cmd_meta[-1] = cmd_meta[-1][:-1]
                lines.append("""<blockquote class="lang-specific shell--ocarina"><p>To provide metadata with Ocarina:</p></blockquote>""")
                lines.append("```shell--ocarina")
                lines.append(cmd_head + ' \\' )
                lines.append("\t...")
                lines.append('\n'.join(cmd_meta))
                lines.append("```")

        if len(uploader_map) > 0:
            lines.append("""<blockquote class="lang-specific plaintext--uploader"><p>Some metadata can be provided via the uploader using these column names:</p>""")
            lines.append("<ul>%s</ul>" % '\n'.join(["<li><code>%s</code> ▶ <code>%s</code></li>" % (k, v) for k, v in uploader_map.items()]))
            lines.append("</blockquote>")

        lines.append("Any artifact in Majora can be 'tagged' with arbitrary key-value metadata.")
        lines.append("Unlike Metrics, there is no fixed terminology or validation on the keys or their values. Like Metrics, to aid organisation, metadata keys are grouped into namespaces.")
        lines.append("This endpoint has 'reserved' metadata keys that should only be used to provide meaningful information:")

        lines.append("\nNamespace | Name | Description | Options")
        lines.append("--- | ---- | ----------- | -------")
        for kp, vp in sort_flat:
            if "metadata" not in vp["path"]:
                continue
            lines.append(' | '.join([str(x) for x in [
                "<b><code>%s</code></b>" % vp["x-ocarina-namespace"],
                "<b><code>%s</code></b>" % vp["name"],
                vp.get("description", "").replace('\n', "</br>"),
                "<ul>" + ''.join(["<li><code>%s</code></li>" % f for f in vp.get("enum", "")]) + "</ul>",
            ]]))


    # Scopes
    lines.append("\n\n### Scopes\n")
    lines.append("<ul>\n")
    if spec.get("x-majora-scopes"):
        scopes = spec.get("x-majora-scopes", "").split(" ")
        if len(scopes) > 0:
            for scope in sorted(scopes):
                if scope[0] == '!':
                    pri_colour = PRIORITY_COLOUR.get(0)
                    scope_style = "<b><code%s>%s</code> (This scope must be requested)</b>" % (" style='%s'" % pri_colour, scope[1:])
                else:
                    pri_colour = PRIORITY_COLOUR.get(None)
                    scope_style = "<b><code%s>%s</code></b>" % (" style='%s'" % pri_colour, scope)
                lines.append("<li>%s</li>" % scope_style)
        else:
            lines.append("<li>This endpoint is scopeless and will work with any valid OAuth token</li>")
    else:
        lines.append("<li>This endpoint is scopeless and will work with any valid OAuth token</li>")
    lines.append("</ul>\n")

    lines.append("\n\n")

    with open("includes/%s.md.erb" % spec["operationId"].replace('.', '_'), 'w') as include_fh:
        include_fh.write('\n'.join(lines))
