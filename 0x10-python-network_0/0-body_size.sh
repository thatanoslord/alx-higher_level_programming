#!/bin/bash
# Gets the HTTP's byte size response header for a given URL.
curl -s "$1" | wc -c
