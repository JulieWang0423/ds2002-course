#!/bin/bash

set -e

# Generate 100 universally unique identifiers and save to guids.list
for i in {1..100}
do
  /usr/bin/uuidgen
done > guids.list
