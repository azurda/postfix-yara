#!/usr/bin/python

import sys
import email
import yara
import os
import json

RULESET_PATH = '/home/usr/rulesets.json'
COMPILED_RULESET_PATH = '/path/to/rulesets/folder/'

CORES = 1

EX_TEMP_FAIL = 75
EX_UNAVAILABLE = 69
SUCCESS = 0

detections = []


def process_payload(payload, ruleset):
  ruleset_name = ruleset
  ruleset = yara.load(COMPILED_RULESET_PATH  + ruleset)
  if ruleset.match(data=str(payload)):
    detections.append(ruleset_name)

def main():
  ruleset_list = json.load(open(RULESET_PATH + 'rulesets.json', 'rb'))
  mail = email.message_from_file(sys.stdin)
  for part in mail.walk():
    for ruleset in ruleset_list:
      process_payload(part.get_payload(decode=True), ruleset['name'])
    if len(detections) > 0:
      return EX_TEMP_FAIL
  return SUCCESS

if __name__ == '__main__':
  main()

