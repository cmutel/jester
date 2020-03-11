# Jester

Import data from the [olca-schema](https://github.com/GreenDelta/olca-schema) JSON-LD format into HESTIA and the [HESTIA JSON-LD schema](https://gitlab.com/hestia-earth/schema).

**Note:** This is prototype code, do not use in production!

We are interested in importing data to fulfill a limited number of use cases in HESTIA - therefore, we don't need to support all olca-schema features or metadata. In particular, imported data will fulfill two functions:

1. Provide data on background activities outside the scope of HESTIA, but useful in calculating complete life cycle assessments
2. Provide supplementary data on specific farm or other agricultural systems.

TODO: Do we need to treat these differently? Is there any data in e.g. Agribalyse or LCACommons where we wouldn't prefer to get the raw data in the first place?

