---
layout: post
title: Set up Google Ads conversion tracking
comments: true
category: Web-analytics
tags: gtm
---

## Set up Google Ads conversion tracking

We can use Tag Manager to deploy the Ads tracking code on website.

To create an Ads Conversion Tracking tag in Tag Manager, we'll first need to get the "Conversion ID" and the "Conversion Label" from the existiong Ads account. In Ads click "Tools", then click "Conversion".

Then edit settings of conversion which we need. Make note of the values for the "google_conversion_id" and the "google_conversion_label" variables.

<img src="/assets/img/2020-08-10-tags-for-marketing/1.png">

We'll need to include these in Tag Manager. Now let's create the Conversion Tracking tag.

In Tag Manager click "Tags" -> "New" -> "Google Ads". Select type "Ads Conversion Tracking". Configure it with "google_conversion_id" and the "google_conversion_label". Set up "Conversion Value" with ```{{tripValue}}```. Currency code - ```USD```.

Then in "Fire On" block select "All Pages" and test it in Preview Mode.



