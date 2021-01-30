---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell--ocarina: ocarina
  - plaintext--uploader: uploader
  - python: python

toc_footers:
  - <a href='#'>Sign Up for a Developer Key</a>
  - <a href='https://github.com/slatedocs/slate'>Documentation Powered by Slate</a>

includes:
  - errors

search: true

code_clipboard: true
---

# Introduction

Hello, Majora!

This example API documentation page was created with [Slate](https://github.com/slatedocs/slate). Feel free to edit it and use it as a base for your own API's documentation.

# Authentication

> To authorize, use this code:

```plaintext--uploader

See https://metadata.docs.cog-uk.io/

## Hello

import kittn

api = kittn.authorize('meowmeowmeow')
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
```

```shell
# With shell, you can just pass the correct header with each request
curl "api_endpoint_here" \
  -H "Authorization: meowmeowmeow"
```

> Make sure to replace `meowmeowmeow` with your API key.

Kittn uses API keys to allow access to the API. You can register a new Kittn API key at our [developer portal](http://example.com/developers).

Kittn expects for the API key to be included in all API requests to the server in a header that looks like the following:

`Authorization: meowmeowmeow`

<aside class="notice">
You must replace <code>meowmeowmeow</code> with your personal API key.
</aside>

# Biosamples

## Add one or more biosamples
<code>/artifact/biosample/add/</code>
### Attributes
<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>
```shell--ocarina
ocarina put biosample \
	--adm1 UK-ENG \
	--central-sample-id BIRM-12345 \
	--collection-date 2020-06-03 \
	--is-surveillance Y 
```
<blockquote class="lang-specific shell--ocarina"><p>Full Ocarina command example:</p></blockquote>
```shell--ocarina
ocarina put biosample \
	--adm1 UK-ENG \
	--central-sample-id BIRM-12345 \
	--collection-date 2020-06-03 \
	--is-surveillance Y \
	--adm2 Birmingham \
	--adm2-private B20 \
	--biosample-source-id ABC12345 \
	--collecting-org 'Hypothetical University of Hooting' \
	--received-date 2020-06-04 \
	--root-sample-id PHA12345 \
	--sample-type-collected swab \
	--sample-type-received primary \
	--sender-sample-id LAB12345 \
	--source-age 29 \
	--source-sex F \
	--swab-site nose-throat 
```
<blockquote class="lang-specific shell--ocarina"><p>Attributes currently unsupported by Ocarina: <code style='word-break: normal'>admitted_date</code>, <code style='word-break: normal'>admitted_hospital_name</code>, <code style='word-break: normal'>admitted_hospital_trust_or_board</code>, <code style='word-break: normal'>admitted_with_covid_diagnosis</code>, <code style='word-break: normal'>anonymised_care_home_code</code>, <code style='word-break: normal'>employing_hospital_name</code>, <code style='word-break: normal'>employing_hospital_trust_or_board</code>, <code style='word-break: normal'>is_care_home_resident</code>, <code style='word-break: normal'>is_care_home_worker</code>, <code style='word-break: normal'>is_hcw</code>, <code style='word-break: normal'>is_hospital_patient</code>, <code style='word-break: normal'>is_icu_patient</code></p></blockquote>
<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>Documentation for this function can be found on the CGPS uploader website linked below:</br><a href="https://metadata.docs.cog-uk.io/bulk-upload-1/bulk-upload">https://metadata.docs.cog-uk.io/bulk-upload-1/bulk-upload</a></p></blockquote>

Name | Description | Options
---- | ----------- | -------
<b><code style='color:#fff; background-color:#dc3545'>adm1</code></b></br>string, <i>required</i>, <i>enum</i> | Code of UK home nation of the patient from which the sample was collected | <ul><li><code>UK-ENG</code></li><li><code>UK-SCT</code></li><li><code>UK-WLS</code></li><li><code>UK-NIR</code></li></ul>
<b><code style='color:#fff; background-color:#dc3545'>central_sample_id</code></b></br>string, <i>required</i> | The centrally shared ID that you will use to refer to this sample inside the consortium. | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>collection_date</code></b></br>string, <i>required</i> | Provide where possible. When collection_date cannot be provided, you must provide received_date instead. | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>is_surveillance</code></b></br>string, <i>required</i>, <i>enum</i> | Whether this sample was collected under the COGUK surveillance protocol. | <ul><li><code>Y</code></li><li><code>N</code></li></ul>
<b><code >adm2</code></b></br>string | The city or county that the patient lives in (avoid abbreviations or short hand) | <ul></ul>
<b><code >adm2_private</code></b></br>string | The outer postcode for the patient's home address (first half of the postcode only) | <ul></ul>
<b><code >admitted_date</code></b></br>string | If is_hospital_patient, the date (YYYY-MM-DD) that the patient was admitted to hospital | <ul></ul>
<b><code >admitted_hospital_name</code></b></br>string | If is_hospital_patient, provide the name of the hospital. If you do not know the name, use HOSPITAL | <ul></ul>
<b><code >admitted_hospital_trust_or_board</code></b></br>string | If is_hospital_patient, provide the name of the trust or board that administers the hospital the patient was admitted to. | <ul></ul>
<b><code >admitted_with_covid_diagnosis</code></b></br>string, <i>enum</i> | If is_hospital_patient, whether the patient was admitted with a COVID diagnosis | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code >anonymised_care_home_code</code></b></br>string | A code to represent a particular care home, the mapping of this code to the care home should be kept securely by your organisation. You must take care to select a code that can not link the identity of the care home. | <ul></ul>
<b><code >biosample_source_id</code></b></br>string | A unique identifier of patient or environmental sample. If you have multiple samples from the same patient, enter the FIRST central_sample_id assigned to one of their samples here.</br></br>  DO NOT USE AN NHS NUMBER HERE.</br> | <ul></ul>
<b><code >collecting_org</code></b></br>string | The site (eg. hospital or surgery) that this sample was originally collected by. | <ul></ul>
<b><code >employing_hospital_name</code></b></br>string | If is_hcw, provide the name of the employing hospital. If you do not know the name, use HOSPITAL | <ul></ul>
<b><code >employing_hospital_trust_or_board</code></b></br>string | If is_hcw, provide the name of the employing trust or board. | <ul></ul>
<b><code >is_care_home_resident</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code >is_care_home_worker</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code >is_hcw</code></b></br>string, <i>enum</i> | Whether the sample was collected from a healthcare worker. This includes hospital-associated workers. | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code >is_hospital_patient</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code >is_icu_patient</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code >metadata</code></b></br>object |  | <ul></ul>
<b><code >metrics</code></b></br>object |  | <ul></ul>
<b><code >received_date</code></b></br>string | Date sample was first received by any lab. This date should be as close to possible to collection_date. This date must be provided if collection_date is missing. | <ul></ul>
<b><code >root_sample_id</code></b></br>string | Identifier assigned to this sample from one of the health agencies (eg. PHE samples will be prefixed with H20). This is necessary for linking samples to private patient metadata later. | <ul></ul>
<b><code >sample_type_collected</code></b></br>string, <i>enum</i> |  | <ul><li><code>dry swab</code></li><li><code>swab</code></li><li><code>sputum</code></li><li><code>BAL</code></li><li><code>aspirate</code></li></ul>
<b><code >sample_type_received</code></b></br>string, <i>enum</i> |  | <ul><li><code>primary</code></li><li><code>extract</code></li><li><code>culture</code></li><li><code>lysate</code></li></ul>
<b><code >sender_sample_id</code></b></br>string | If you are permitted, provide the identifier that was sent by your laboratory to SGSS here. | <ul></ul>
<b><code >source_age</code></b></br>integer |  | <ul></ul>
<b><code >source_sex</code></b></br>string, <i>enum</i> |  | <ul><li><code>F</code></li><li><code>M</code></li><li><code>Other</code></li></ul>
<b><code >swab_site</code></b></br>string, <i>enum</i> | Required if sample_type_collected is swab | <ul><li><code>nose</code></li><li><code>throat</code></li><li><code>nose-throat</code></li><li><code>endotracheal</code></li><li><code>rectal</code></li></ul>

### Metadata

```shell--ocarina
--metadata str value x
```

<blockquote class="lang-specific plaintext--uploader">
<p>The uploader supports the following column name to (key, value) mapping</p>
</blockquote>

```plaintext--uploader
...
```

Additonal metadata can be provided:
The following keys and values are reserved:


# Kittens

## Get All Kittens

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get()
```

```shell--ocarina
ocarina get kitten \
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint retrieves all kittens.

### HTTP Request

`GET http://example.com/api/kittens`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
include_cats | false | If set to true, the result will also include cats.
available | true | If set to false, the result will include kittens that have already been adopted.

<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Kitten


```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get(2)
```

```shell
curl "http://example.com/api/kittens/2" \
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "name": "Max",
  "breed": "unknown",
  "fluffiness": 5,
  "cuteness": 10
}
```

This endpoint retrieves a specific kitten.

<aside class="warning">Inside HTML code blocks like this one, you can't use Markdown, so use <code>&lt;code&gt;</code> blocks to denote code.</aside>

### HTTP Request

`GET http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to retrieve

## Delete a Specific Kitten


```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.delete(2)
```

```shell
curl "http://example.com/api/kittens/2" \
  -X DELETE \
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "deleted" : ":("
}
```

This endpoint deletes a specific kitten.

### HTTP Request

`DELETE http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to delete

