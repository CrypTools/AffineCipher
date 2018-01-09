String.prototype.decrypt = function(key, a, b) {
	const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
	const keyArray = key.split("-")
	for (let i in keyArray) {
		keyArray[i] = parseInt(keyArray[i])
	}
	let array = []
	for (let i of this) {
		array.push(alphabet.indexOf(i))
	}
	let output = "";
	for (var i = 0; i < array.length; i++) {
		const image = alphabet[(keyArray[i] * 26 + array[i] - b) / a]
		output += image
	}
	return output;
}
module.exports = (text, key, a, b) => text.decrypt(key, a, b)
