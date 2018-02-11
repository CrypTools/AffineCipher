String.prototype.encrypt = function(a, b) {
	const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('')
	let array = [];
	for (let i of this) {
		array.push(alphabet.indexOf(i.toLowerCase()))
	}
	let output = "";
	let cle = [];
	let divtem = "";
	for (let i of array) {
		const image = alphabet[(i * a + b) % 26]
		output += image
		const div = Math.floor((i * a + b) / 26).toString()
		cle.push(div)
	}
	return [output, cle.join("-")]
}
module.exports = (text, a, b) => text.encrypt(a, b)
