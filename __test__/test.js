// Test made using EyeJS - https://eye.js.org

const path = require('path').normalize(__testDir + "/../JS/")

const encrypt = require(path + "encrypt.js")
const decrypt = require(path + "decrypt.js")


eye.test("Encryption", "node",
	$ => $(encrypt("attack", 3, 6)).Equal([ 'gllgmk', '0-2-2-0-0-1' ])
)
eye.test("Decryption", "node",
	$ => $(decrypt("gllgmk", "0-2-2-0-0-1", 3, 6)).Equal("attack"),
	$ => $(decrypt(encrypt("attack", 3, 6)[0], encrypt("attack", 3, 6)[1], 3, 6)).Equal("attack")
)
