---
title: News asset schema
id: 28741a802181af916c91e46f7a611ade46540f15ed56a94182d5ea25f3494cc3
author: Abhi Kumbara
version: 1.0.0
category: Conventions
status: Draft
created: 04/24/2020
---

## News asset JSON schema

```json
{
	"$schema": "https://conventions.0xcert.org/xcert-schema.json",
	"description": "News article asset digital schema.",
	"properties": {
		"$evidence": {
			"description": "A path to the evidence JSON with data needed to verify the asset.",
			"type": "string",
		},
		"$schema": {
			"description": "A path to JSON Schema definition file.",
			"type": "string",
		},
		"title": {
			"description": "A short natural-language name for the asset, as defined by https://iptc.org/std/ninjs/ninjs-schema_1.2.json",
			"type": "string",
		},
		"byline": {
			"description": "The name(s) of the creator(s) of the content of the asset, as defined by https://iptc.org/std/ninjs/ninjs-schema_1.2.json",
			"type": "string",
		},
		"headline": {
			"description": "A brief introduction to the content of the asset, as defined by https://iptc.org/std/ninjs/ninjs-schema_1.2.json",
			"type": "string",
		},
		"versioncreated": {
			"description": "The date and time when this version of the asset was created, as defined by https://iptc.org/std/ninjs/ninjs-schema_1.2.json",
			"type": "string",
			"format": "date-time",
		},
		"uri": {
			"description": "A valid URI pointing to a resource representing the asset to which this digital asset represents.",
			"type": "string",
		},
		"located": {
			"description": "The name of the location from which the content of the asset originates, as defined by https://iptc.org/std/ninjs/ninjs-schema_1.2.json",
			"type": "string",
		},
		"body_text": {
			"description": "The textual content of the asset, as defined by https://iptc.org/std/ninjs/ninjs-schema_1.2.json",
			"type": "string",
		}
	},
	"required": ["$schema","title","byline","headline","versioncreated","located"],
	"title": "News article asset",
	"type": "object"
}
```
	
