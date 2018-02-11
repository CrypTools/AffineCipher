/***********************************

Use: "ATTACK".encrypt(a: 3, b: 6)
=> ["gllgmk", [0, 2, 2, 0, 0, 1]]
	 "GLLGMK".decrypt(coefs: [0, 2, 2, 0, 0, 1], a: 3, b: 6)
=> "attack"
***********************************/
import Foundation

extension String {
    func encrypt(a: Float, b: Float) -> Array<Any> {
        let alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, ".components(separatedBy: ",")
        let str = self.lowercased()
        var out = "";
        var coefs = Array<Int>();
        for i in str {
            out += alphabet[Int(floor(Float(alphabet.index(of: String(i))!) * a + b)) % 26]
            let div = floor(Double(Int(Float(alphabet.index(of: String(i))!) * a + b) / 26))
            coefs.append(Int(div))
        }
        return [out, coefs];
    }
    func decrypt(coefs: Array<Int>, a: Float, b: Float) -> String {
        let alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, ".components(separatedBy: ",")
        let str = self.lowercased()
        var out = "";
        for i in 0...str.count - 1 {
            let coef = Float(coefs[i])
            let l = Float(alphabet.index(of: String(Array(str)[i]))!)
            out += alphabet[Int((coef * Float(26) + l - b) / a) % 26]
        }
        return out
    }
}
