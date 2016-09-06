import yara
import os, sys
import json
import re 

RULESET_PATH = '/path/to/ruleset/folder/'

def compile_rulesets():
	rules = os.listdir(RULESET_PATH)
	compiled = []
	if 'rulesets.json' in rules:
		os.system('rm ' + RULESET_PATH + 'rulesets.json')
	filtered = [x for x in rules if not re.match('\.yar', x)]

	try:
		for item in filtered:
			# ruleset.yar > compile ruleset.yar > split . 
			print 'Compiling ' + str(item) + ' ... '
			yara.compile(RULESET_PATH + item).save(RULESET_PATH + item.split('.')[0])
			compiled.append({
				'name': item.split('.')[0],
				'enabled': True
				})
		json.dump(compiled, open('rulesets.json', 'w+'))

	except Exception, e:
		raise e
		return 1
	return 0


def main():
	if sys.argv[1] == 'compile':
		compile_rulesets()

if __name__ == '__main__':
	main()
