---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell--ocarina: ocarina
  - plaintext--uploader: uploader
  - json--raw: json
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

## Malleable All-seeing Journal Of Research Artifacts

Majora is a Django-based wet-and-dry information management system. Majora is being rapidly developed as part of the COVID-19 Genomics UK Consortium (COG-UK) response to the outbreak of SARS-CoV-2.

Majora is a system that stores metadata on biological samples, sequencing runs, bioinformatics pipelines and files. These different items are referred to generally, as "artifacts". Majora is composed of three main parts:

* a database that defines "models" that represent artifacts such as samples and files,
* a web interface that allows access to basic metadata shared about artifacts,
* an "API" that provides an interface for other tools and programs to view and edit information about artifacts

This documentation attempts to cover all bases by showing all the fields for each of the artifacts and processes that can be added, updated and retrieved from Majora.
Although intended primarily for users who wish to write a computer program to use the API or users of the [Ocarina command line tool](https://github.com/SamStudio8/ocarina/), it should be useful for users of the CGPS metadata uploader.
Users of the uploader will likely also want to refer to the documentation for the [metadata uploader](https://metadata.docs.cog-uk.io/).

You may be interested to know that this API documentation page was created with [Slate](https://github.com/slatedocs/slate).

## Important notes

* Submitting a request for an artifact that already exists will allow you to change some properties of that object. The messages response will let you know if this is not the case.
* Sending a request to update an artifact that already exists is an overwriting operation. If you submit blank fields, those fields will be irreversibly deleted from the model.
* If metadata is missing, send a blank field or do not submit the field at all. Do not submit 'unknown' or 'null' or any other text that attempts to explain that the field is missing.


# Authentication

* [Authentication with the CGPS Uploader](https://metadata.docs.cog-uk.io/bulk-upload-1)
* [Authentication with Ocarina (API key)](https://github.com/SamStudio8/ocarina#configuration)
* [Authentication with Ocarina (OAuth)](https://docs.covid19.climb.ac.uk/oauth-app)

# Biosamples
## Add one or more biosamples to Majora

<code>/artifact/biosample/add/</code>


### Attributes

```json--raw
{
    "biosamples": {
        "adm1": "UK-ENG",
        "adm2": "Birmingham",
        "adm2_private": "B20",
        "admitted_date": null,
        "admitted_hospital_name": null,
        "admitted_hospital_trust_or_board": null,
        "admitted_with_covid_diagnosis": null,
        "anonymised_care_home_code": null,
        "biosample_source_id": "ABC12345",
        "central_sample_id": "BIRM-12345",
        "collecting_org": "Hypothetical University of Hooting",
        "collection_date": "2020-06-03",
        "collection_pillar": "2",
        "employing_hospital_name": null,
        "employing_hospital_trust_or_board": null,
        "is_care_home_resident": null,
        "is_care_home_worker": null,
        "is_hcw": null,
        "is_hospital_patient": null,
        "is_icu_patient": null,
        "is_surveillance": "Y",
        "metadata": {
            "epi": {
                "epi_cluster": "CLUSTER8"
            },
            "investigation": {
                "investigation_cluster": "Ward 0",
                "investigation_name": "West Midlands HCW",
                "investigation_site": "QEHB"
            }
        },
        "metrics": {
            "ct": {
                "records": {
                    "ct_value": "25",
                    "test_kit": "INHOUSE",
                    "test_platform": "INHOUSE",
                    "test_target": "ORF8"
                }
            }
        },
        "received_date": "2020-06-04",
        "root_sample_id": "PHA12345",
        "sample_type_collected": "swab",
        "sample_type_received": "primary",
        "sender_sample_id": "LAB12345",
        "source_age": "29",
        "source_sex": "F",
        "swab_site": "nose-throat"
    },
    "token": "6e06392f-e030-4cf9-911a-8dc9f2d4e714",
    "username": "majora-sam"
}
```
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
	--received-date 2020-06-04 \
	--adm2 Birmingham \
	--source-age 29 \
	--source-sex F \
	--adm2-private B20 \
	--biosample-source-id ABC12345 \
	--collecting-org 'Hypothetical University of Hooting' \
	--collection-pillar 2 \
	--root-sample-id PHA12345 \
	--sample-type-collected swab \
	--sample-type-received primary \
	--sender-sample-id LAB12345 \
	--swab-site nose-throat 
```
<blockquote class="lang-specific shell--ocarina"><p>Attributes currently unsupported by Ocarina: <code style='word-break: normal'>admitted_date</code>, <code style='word-break: normal'>admitted_hospital_name</code>, <code style='word-break: normal'>admitted_hospital_trust_or_board</code>, <code style='word-break: normal'>admitted_with_covid_diagnosis</code>, <code style='word-break: normal'>anonymised_care_home_code</code>, <code style='word-break: normal'>employing_hospital_name</code>, <code style='word-break: normal'>employing_hospital_trust_or_board</code>, <code style='word-break: normal'>is_care_home_resident</code>, <code style='word-break: normal'>is_care_home_worker</code>, <code style='word-break: normal'>is_hcw</code>, <code style='word-break: normal'>is_hospital_patient</code>, <code style='word-break: normal'>is_icu_patient</code></p></blockquote>
<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>Documentation for this function can be found on the CGPS uploader website linked below:</br><a href="https://metadata.docs.cog-uk.io/bulk-upload-1/bulk-upload">https://metadata.docs.cog-uk.io/bulk-upload-1/bulk-upload</a></p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>There may be some differences between this specification and the uploader, particularly for providing Metrics and Metadata. See the Metadata and Metrics sections below for column names that are compatible with the API spec.</p></blockquote>

Name | Description | Options
---- | ----------- | -------
<b><code style='color:#fff; background-color:#dc3545'>adm1</code></b></br>string, <i>required</i>, <i>enum</i> | Code of UK home nation of the patient from which the sample was collected | <ul><li><code>UK-ENG</code></li><li><code>UK-SCT</code></li><li><code>UK-WLS</code></li><li><code>UK-NIR</code></li></ul>
<b><code style='color:#fff; background-color:#dc3545'>central_sample_id</code></b></br>string, <i>required</i> | The centrally shared ID that you will use to refer to this sample inside the consortium. | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>collection_date</code></b></br>string, <i>required</i> | Provide where possible. When collection_date cannot be provided, you must provide received_date instead. | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>is_surveillance</code></b></br>string, <i>required</i>, <i>enum</i> | Whether this sample was collected under the COGUK surveillance protocol. | <ul><li><code>Y</code></li><li><code>N</code></li></ul>
<b><code style='color:#000; background-color:#ffc107'>received_date</code></b></br>string, <i>possibly required</i> | Date sample was first received by any lab. This date should be as close to possible to collection_date. This date must be provided if collection_date is missing. | <ul></ul>
<b><code style='color:#fff; background-color:#17a2b8'>adm2</code></b></br>string, <i>recommended</i> | The city or county that the patient lives in (avoid abbreviations or short hand) | <ul></ul>
<b><code style='color:#fff; background-color:#17a2b8'>source_age</code></b></br>integer, <i>recommended</i> | Ages should be whole numbers. Neonatals should be entered as 0. | <ul></ul>
<b><code style='color:#fff; background-color:#17a2b8'>source_sex</code></b></br>string, <i>recommended</i>, <i>enum</i> |  | <ul><li><code>F</code></li><li><code>M</code></li><li><code>Other</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>adm2_private</code></b></br>string | The outer postcode for the patient's home address (first half of the postcode only) | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>admitted_date</code></b></br>string | If is_hospital_patient, the date (YYYY-MM-DD) that the patient was admitted to hospital | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>admitted_hospital_name</code></b></br>string | If is_hospital_patient, provide the name of the hospital. If you do not know the name, use HOSPITAL | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>admitted_hospital_trust_or_board</code></b></br>string | If is_hospital_patient, provide the name of the trust or board that administers the hospital the patient was admitted to. | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>admitted_with_covid_diagnosis</code></b></br>string, <i>enum</i> | If is_hospital_patient, whether the patient was admitted with a COVID diagnosis | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>anonymised_care_home_code</code></b></br>string | A code to represent a particular care home, the mapping of this code to the care home should be kept securely by your organisation. You must take care to select a code that can not link the identity of the care home. | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>biosample_source_id</code></b></br>string | A unique identifier of patient or environmental sample. If you have multiple samples from the same patient, enter the FIRST central_sample_id assigned to one of their samples here.</br><aside class='warning' style='padding: 1em'>Do not provide personally identifying information here. Never use an NHS number.</aside> | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>collecting_org</code></b></br>string | The site (eg. hospital or surgery) that this sample was originally collected by. | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>collection_pillar</code></b></br>integer, <i>enum</i> | The pillar under which this sample was collected (e.g. 1, 2). This is likely 1, but leave blank if unsure. | <ul><li><code>1</code></li><li><code>2</code></li><li><code>103</code></li><li><code>34613</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>employing_hospital_name</code></b></br>string | If is_hcw, provide the name of the employing hospital. If you do not know the name, use HOSPITAL | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>employing_hospital_trust_or_board</code></b></br>string | If is_hcw, provide the name of the employing trust or board. | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>is_care_home_resident</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>is_care_home_worker</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>is_hcw</code></b></br>string, <i>enum</i> | Whether the sample was collected from a healthcare worker. This includes hospital-associated workers. | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>is_hospital_patient</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>is_icu_patient</code></b></br>string, <i>enum</i> |  | <ul><li><code>Y</code></li><li><code>N</code></li><li><code>(blank)</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>root_sample_id</code></b></br>string | Identifier assigned to this sample from one of the health agencies (eg. PHE samples will be prefixed with H20). This is necessary for linking samples to private patient metadata later. | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>sample_type_collected</code></b></br>string, <i>enum</i> |  | <ul><li><code>dry swab</code></li><li><code>swab</code></li><li><code>sputum</code></li><li><code>BAL</code></li><li><code>aspirate</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>sample_type_received</code></b></br>string, <i>enum</i> |  | <ul><li><code>primary</code></li><li><code>extract</code></li><li><code>culture</code></li><li><code>lysate</code></li></ul>
<b><code style='color:#fff; background-color:#6c757d'>sender_sample_id</code></b></br>string | If you are permitted, provide the identifier that was sent by your laboratory to SGSS here. | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>swab_site</code></b></br>string, <i>enum</i> | Required if sample_type_collected is swab | <ul><li><code>nose</code></li><li><code>throat</code></li><li><code>nose-throat</code></li><li><code>endotracheal</code></li><li><code>rectal</code></li></ul>


### Metrics
<blockquote class="lang-specific shell--ocarina"><p>To provide metrics with Ocarina:</p></blockquote>
```shell--ocarina
ocarina put biosample \
	...
	--metric ct.# ct_value 25 \
	--metric ct.# test_kit INHOUSE \
	--metric ct.# test_platform INHOUSE \
	--metric ct.# test_target ORF8 
```
<blockquote class="lang-specific shell--ocarina"><p>If a particular metric supports storing multiple records, you can provide them by incrementing a numerical suffix after the metric's namespace: <i>e.g.</i> <code>--metric name.1 key value</code> ... <code>--metric name.N key value.</code></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>Some metrics can be provided via the uploader using these column names:</p>
<ul><li><code>ct ct_value</code> ▶ <code>ct_#_ct_value (limit 2)</code></li>
<li><code>ct test_kit</code> ▶ <code>ct_#_test_kit (limit 2)</code></li>
<li><code>ct test_platform</code> ▶ <code>ct_#_test_platform (limit 2)</code></li>
<li><code>ct test_target</code> ▶ <code>ct_#_test_target (limit 2)</code></li></ul>
</blockquote>
Some artifacts in Majora can be annotated with additional Metric objects.
Metric objects group together specific information that allows for additional description of an artifact, but does not belong in the artifact itself.
Each metric has its own namespace, containing a fixed set of keys. Some or all of the keys may need a value to validate the Metric.
This endpoint allows you to submit the following Metrics:

Namespace | Name | Description | Options
--- | ---- | ----------- | -------
<b><code>ct</code></b> | <b><code>ct_value</code></b> | Cycle threshold value. Cannot be negative. Code an inconclusive or negative test as 0. | <ul></ul>
<b><code>ct</code></b> | <b><code>test_kit</code></b> |  | <ul><li><code>ALTONA</code></li><li><code>ABBOTT</code></li><li><code>AUSDIAGNOSTICS</code></li><li><code>BOSPHORE</code></li><li><code>ROCHE</code></li><li><code>INHOUSE</code></li><li><code>SEEGENE</code></li><li><code>VIASURE</code></li><li><code>BD</code></li><li><code>XPERT</code></li><li><code>QIASTAT</code></li><li><code>ALINITY</code></li><li><code>AMPLIDIAG</code></li><li><code>TAQPATH_HT</code></li><li><code>(blank)</code></li></ul>
<b><code>ct</code></b> | <b><code>test_platform</code></b> |  | <ul><li><code>ALTOSTAR_AM16</code></li><li><code>ABBOTT_M2000</code></li><li><code>ABBOTT_ALINITY</code></li><li><code>APPLIED_BIO_7500</code></li><li><code>ROCHE_COBAS</code></li><li><code>ROCHE_FLOW</code></li><li><code>ROCHE_LIGHTCYCLER</code></li><li><code>ELITE_INGENIUS</code></li><li><code>CEPHEID_XPERT</code></li><li><code>QIASTAT_DX</code></li><li><code>AUSDIAGNOSTICS</code></li><li><code>INHOUSE</code></li><li><code>ALTONA</code></li><li><code>PANTHER</code></li><li><code>SEEGENE_NIMBUS</code></li><li><code>QIAGEN_ROTORGENE</code></li><li><code>BD_MAX</code></li><li><code>AMPLIDIAG_EASY</code></li><li><code>THERMO_AMPLITUDE</code></li><li><code>(blank)</code></li></ul>
<b><code>ct</code></b> | <b><code>test_target</code></b> |  | <ul><li><code>E</code></li><li><code>N</code></li><li><code>S</code></li><li><code>RDRP</code></li><li><code>ORF1AB</code></li><li><code>ORF8</code></li><li><code>RDRP+N</code></li><li><code>(blank)</code></li></ul>


### Metadata

<blockquote class="lang-specific shell--ocarina"><p>To provide metadata with Ocarina:</p></blockquote>
```shell--ocarina
ocarina put biosample \
	...
	-m epi cluster CLUSTER8 \
	-m investigation cluster 'Ward 0' \
	-m investigation name 'West Midlands HCW' \
	-m investigation site QEHB 
```
<blockquote class="lang-specific plaintext--uploader"><p>Some metadata can be provided via the uploader using these column names:</p>
<ul><li><code>epi cluster</code> ▶ <code>epi_cluster</code></li>
<li><code>investigation cluster</code> ▶ <code>investigation_cluster</code></li>
<li><code>investigation name</code> ▶ <code>investigation_name</code></li>
<li><code>investigation site</code> ▶ <code>investigation_site</code></li></ul>
</blockquote>
Any artifact in Majora can be 'tagged' with arbitrary key-value metadata.
Unlike Metrics, there is no fixed terminology or validation on the keys or their values. Like Metrics, to aid organisation, metadata keys are grouped into namespaces.
This endpoint has 'reserved' metadata keys that should only be used to provide meaningful information:

Namespace | Name | Description | Options
--- | ---- | ----------- | -------
<b><code>epi</code></b> | <b><code>epi_cluster</code></b> | A local identifier for a known case cluster | <ul></ul>
<b><code>investigation</code></b> | <b><code>investigation_cluster</code></b> | An optional identifier for a cluster within an investigation | <ul></ul>
<b><code>investigation</code></b> | <b><code>investigation_name</code></b> | A named investigation (eg. a surveillance or directed case group) | <ul></ul>
<b><code>investigation</code></b> | <b><code>investigation_site</code></b> | An optional site name or code to differentiate between sites if the investigation covers more than one site. | <ul></ul>


# Library
## Add a sequencing library to Majora

<code>/artifact/library/add/</code>


### Attributes
<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>
```json--raw
{
    "biosamples": {
        "barcode": "02",
        "central_sample_id": "BIRM-12345",
        "library_primers": "ARTIC v3",
        "library_protocol": "ARTIC v3 (LoCost)",
        "library_selection": "PCR",
        "library_source": "VIRAL_RNA",
        "library_strategy": "AMPLICON",
        "metadata": {
            "artic": {
                "artic_primers": "3",
                "artic_protocol": "v3 (LoCost)"
            }
        },
        "sequencing_org_received_date": "2021-01-14"
    },
    "library_layout_config": "PAIRED",
    "library_layout_insert_length": 100,
    "library_layout_read_length": 300,
    "library_name": "HOOT-LIBRARY-20200322",
    "library_seq_kit": "Illumina MiSeq v3",
    "library_seq_protocol": "MiSeq 150 Cycle",
    "metadata": {},
    "token": "6e06392f-e030-4cf9-911a-8dc9f2d4e714",
    "username": "majora-sam"
}
```
<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>
```shell--ocarina
ocarina put library \
	--biosample BIRM-12345 VIRAL_RNA PCR AMPLICON 'ARTIC v3 (LoCost)' 'ARTIC v3' \
	--library-layout-config PAIRED \
	--library-name HOOT-LIBRARY-20200322 \
	--library-seq-kit 'Illumina MiSeq v3' \
	--library-seq-protocol 'MiSeq 150 Cycle' 
```
<blockquote class="lang-specific shell--ocarina"><p>Full Ocarina command example:</p></blockquote>
```shell--ocarina
ocarina put library \
	--biosample BIRM-12345 VIRAL_RNA PCR AMPLICON 'ARTIC v3 (LoCost)' 'ARTIC v3' \
	--library-layout-config PAIRED \
	--library-name HOOT-LIBRARY-20200322 \
	--library-seq-kit 'Illumina MiSeq v3' \
	--library-seq-protocol 'MiSeq 150 Cycle' \
	--library-layout-insert-length 100 \
	--library-layout-read-length 300 \
	--sequencing-org-received-date 2021-01-14 
```
<blockquote class="lang-specific shell--ocarina"><p>Attributes merged into positional arguments by Ocarina:<ul>
<li><code>biosample</code> ▶ <code>central_sample_id</code> <code>library_source</code> <code>library_selection</code> <code>library_strategy</code> <code>library_protocol</code> <code>library_primers</code></li>
</ul></blockquote>
<blockquote class="lang-specific shell--ocarina"><p>Attributes currently unsupported by Ocarina: <code style='word-break: normal'>barcode</code></p></blockquote>
<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>Documentation for this function can be found on the CGPS uploader website linked below:</br><a href="https://metadata.docs.cog-uk.io/bulk-upload-1/samples-and-sequencing">https://metadata.docs.cog-uk.io/bulk-upload-1/samples-and-sequencing</a></p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>There may be some differences between this specification and the uploader, particularly for providing Metrics and Metadata. See the Metadata and Metrics sections below for column names that are compatible with the API spec.</p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>Some attributes are named differently on the CGPS uploader:</p>
<ul><li><code>library_primers</code> ▶ <code>artic_primers</code></li>
<li><code>library_protocol</code> ▶ <code>artic_protocol</code></li></ul>
</blockquote>

Name | Description | Options
---- | ----------- | -------
<b><code style='color:#fff; background-color:#dc3545'>central_sample_id</code></b></br>string, <i>required</i> |  | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_layout_config</code></b></br>string, <i>required</i>, <i>enum</i> |  | <ul><li><code>SINGLE</code></li><li><code>PAIRED</code></li></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_name</code></b></br>string, <i>required</i> | A unique, somewhat memorable name for your library. | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_selection</code></b></br>string, <i>required</i>, <i>enum</i> |  | <ul><li><code>RANDOM</code></li><li><code>PCR</code></li><li><code>RANDOM_PCR</code></li><li><code>OTHER</code></li></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_seq_kit</code></b></br>string, <i>required</i> |  | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_seq_protocol</code></b></br>string, <i>required</i> |  | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_source</code></b></br>string, <i>required</i>, <i>enum</i> |  | <ul><li><code>GENOMIC</code></li><li><code>TRANSCRIPTOMIC</code></li><li><code>METAGENOMIC</code></li><li><code>METATRANSCRIPTOMIC</code></li><li><code>VIRAL_RNA</code></li><li><code>OTHER</code></li></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_strategy</code></b></br>string, <i>required</i>, <i>enum</i> |  | <ul><li><code>WGA</code></li><li><code>WGS</code></li><li><code>AMPLICON</code></li><li><code>TARGETED_CAPTURE</code></li><li><code>OTHER</code></li></ul>
<b><code style='color:#fff; background-color:#17a2b8'>library_primers</code></b></br>string, <i>recommended</i> |  | <ul></ul>
<b><code style='color:#fff; background-color:#17a2b8'>library_protocol</code></b></br>string, <i>recommended</i> |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>barcode</code></b></br>string |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>library_layout_insert_length</code></b></br>integer |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>library_layout_read_length</code></b></br>integer |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>sequencing_org_received_date</code></b></br>string | Date sample was received by the organisation which sequenced it. This date is used for tracking sample turnaround time. | <ul></ul>


### Metadata

<blockquote class="lang-specific shell--ocarina"><p>To provide metadata with Ocarina:</p></blockquote>
```shell--ocarina
ocarina put library \
	...
	-m artic primers 3 \
	-m artic protocol 'v3 (LoCost)' 
```
<blockquote class="lang-specific plaintext--uploader"><p>Some metadata can be provided via the uploader using these column names:</p>
<ul><li><code>artic primers</code> ▶ <code>artic_primers</code></li>
<li><code>artic protocol</code> ▶ <code>artic_protocol</code></li></ul>
</blockquote>
Any artifact in Majora can be 'tagged' with arbitrary key-value metadata.
Unlike Metrics, there is no fixed terminology or validation on the keys or their values. Like Metrics, to aid organisation, metadata keys are grouped into namespaces.
This endpoint has 'reserved' metadata keys that should only be used to provide meaningful information:

Namespace | Name | Description | Options
--- | ---- | ----------- | -------
<b><code>artic</code></b> | <b><code>artic_primers</code></b> | The version number of the ARTIC primer set (if used) to prepare this library | <ul></ul>
<b><code>artic</code></b> | <b><code>artic_protocol</code></b> | The version number of the ARTIC protocol (if used) to prepare this library | <ul></ul>


# Sequencing
## Add a sequencing run to Majora

<code>/process/sequencing/add/</code>


### Attributes
<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>
```json--raw
{
    "library_name": "HOOT-LIBRARY-20200322",
    "runs": {
        "bioinfo_pipe_name": "ARTIC Pipeline (iVar)",
        "bioinfo_pipe_version": "1.3.0",
        "end_time": "YYYY-MM-DD HH:MM",
        "flowcell_id": "ABCDEF",
        "flowcell_type": "v3",
        "instrument_make": "ILLUMINA",
        "instrument_model": "MiSeq",
        "run_name": "YYMMDD_AB000000_1234_ABCDEFGHI0",
        "start_time": "YYYY-MM-DD HH:MM"
    },
    "token": "6e06392f-e030-4cf9-911a-8dc9f2d4e714",
    "username": "majora-sam"
}
```
<blockquote class="lang-specific shell--ocarina"><p>Minimal Ocarina command with mandatory parameters:</p></blockquote>
```shell--ocarina
ocarina put sequencing \
	--instrument-make ILLUMINA \
	--instrument-model MiSeq \
	--library-name HOOT-LIBRARY-20200322 \
	--run-name YYMMDD_AB000000_1234_ABCDEFGHI0 
```
<blockquote class="lang-specific shell--ocarina"><p>Full Ocarina command example:</p></blockquote>
```shell--ocarina
ocarina put sequencing \
	--instrument-make ILLUMINA \
	--instrument-model MiSeq \
	--library-name HOOT-LIBRARY-20200322 \
	--run-name YYMMDD_AB000000_1234_ABCDEFGHI0 \
	--bioinfo-pipe-name 'ARTIC Pipeline (iVar)' \
	--bioinfo-pipe-version 1.3.0 \
	--end-time 'YYYY-MM-DD HH:MM' \
	--flowcell-id ABCDEF \
	--flowcell-type v3 \
	--start-time 'YYYY-MM-DD HH:MM' 
```
<blockquote class="lang-specific python"><p>Function not currently implemented in Ocarina Python API</p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>Documentation for this function can be found on the CGPS uploader website linked below:</br><a href="https://metadata.docs.cog-uk.io/bulk-upload-1/samples-and-sequencing">https://metadata.docs.cog-uk.io/bulk-upload-1/samples-and-sequencing</a></p></blockquote>
<blockquote class="lang-specific plaintext--uploader"><p>There may be some differences between this specification and the uploader, particularly for providing Metrics and Metadata. See the Metadata and Metrics sections below for column names that are compatible with the API spec.</p></blockquote>

Name | Description | Options
---- | ----------- | -------
<b><code style='color:#fff; background-color:#dc3545'>instrument_make</code></b></br>string, <i>required</i>, <i>enum</i> |  | <ul><li><code>ILLUMINA</code></li><li><code>OXFORD_NANOPORE</code></li><li><code>PACIFIC_BIOSCIENCES</code></li><li><code>ION_TORRENT</code></li></ul>
<b><code style='color:#fff; background-color:#dc3545'>instrument_model</code></b></br>string, <i>required</i> |  | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>library_name</code></b></br>string, <i>required</i> | The name of the library as submitted to add_library | <ul></ul>
<b><code style='color:#fff; background-color:#dc3545'>run_name</code></b></br>string, <i>required</i> | A unique name that corresponds to your run. Ideally, use the name generated by your sequencing instrument. | <ul></ul>
<b><code style='color:#fff; background-color:#17a2b8'>bioinfo_pipe_name</code></b></br>string, <i>recommended</i> | The name of the bioinformatics pipeline used for downstream analysis of this run | <ul></ul>
<b><code style='color:#fff; background-color:#17a2b8'>bioinfo_pipe_version</code></b></br>string, <i>recommended</i> | The version number of the bioinformatics pipeline used for downstream analysis of this run | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>end_time</code></b></br>string |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>flowcell_id</code></b></br>string |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>flowcell_type</code></b></br>None |  | <ul></ul>
<b><code style='color:#fff; background-color:#6c757d'>start_time</code></b></br>string |  | <ul></ul>

