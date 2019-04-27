# `jail-scraper`

Data scraper for the county jails of Georgia, currently capable of querying the
inmate registries of 16 different county jails, anonymizing the data, and
archiving them as dated JSON files.

The first name, last name, and date of birth of each inmate is replaced with
a unique cryptographic hash of that information, to allow researchers to study
re-incarceration on an individual basis without breaching the privacy of the
inmates. Home addresses are removed entirely.
